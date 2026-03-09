"""
Pytest test suite for ByteBites classes.
Focuses on: category filtering and total calculation behavior.
"""

import pytest
from models import FoodItem, Menu, Order, Customer


# ==================== FOODITEM TESTS ====================
class TestFoodItem:
    """Test FoodItem class initialization and attributes."""
    
    def test_fooditem_init(self):
        """Test FoodItem initialization with all attributes."""
        item = FoodItem("Spicy Burger", 12.99, "Entrees", 4.8)
        assert item.name == "Spicy Burger"
        assert item.price == 12.99
        assert item.category == "Entrees"
        assert item.popularity_rating == 4.8


# ==================== MENU - FILTERING TESTS ====================
class TestMenuFiltering:
    """Test Menu filtering behavior."""
    
    @pytest.fixture
    def sample_menu(self):
        """Create a menu with sample items for testing."""
        menu = Menu()
        menu.add_item(FoodItem("Spicy Burger", 12.99, "Entrees", 4.8))
        menu.add_item(FoodItem("Classic Burger", 10.49, "Entrees", 4.7))
        menu.add_item(FoodItem("Large Soda", 2.50, "Drinks", 4.5))
        menu.add_item(FoodItem("Iced Tea", 3.00, "Drinks", 4.4))
        menu.add_item(FoodItem("Chocolate Cake", 7.99, "Desserts", 4.9))
        menu.add_item(FoodItem("Vanilla Ice Cream", 5.99, "Desserts", 4.8))
        return menu
    
    def test_filter_multiple_items_same_category(self, sample_menu):
        """Test filtering category with multiple items."""
        drinks = sample_menu.filter_by_category("Drinks")
        assert len(drinks) == 2
        assert all(item.category == "Drinks" for item in drinks)
    
    def test_filter_no_match_empty_result(self, sample_menu):
        """Test filtering non-existent category returns empty list."""
        appetizers = sample_menu.filter_by_category("Appetizers")
        assert len(appetizers) == 0
    
    def test_filter_case_sensitive(self, sample_menu):
        """Test that filtering is case-sensitive."""
        lowercase = sample_menu.filter_by_category("drinks")
        assert len(lowercase) == 0
        
        correct_case = sample_menu.filter_by_category("Drinks")
        assert len(correct_case) == 2
    
    def test_filter_empty_menu(self):
        """Test filtering on an empty menu."""
        menu = Menu()
        result = menu.filter_by_category("Drinks")
        assert len(result) == 0


# ==================== ORDER - TOTAL CALCULATION TESTS ====================
class TestOrderTotalCalculation:
    """Test Order total calculation behavior."""
    
    def test_compute_total_single_item(self):
        """Test total with a single item."""
        order = Order()
        order.add_item(FoodItem("Burger", 12.99, "Entrees", 4.8))
        assert order.compute_total() == 12.99
    
    def test_compute_total_multiple_items(self):
        """Test total with multiple items."""
        order = Order()
        order.add_item(FoodItem("Burger", 12.99, "Entrees", 4.8))
        order.add_item(FoodItem("Soda", 2.50, "Drinks", 4.5))
        order.add_item(FoodItem("Fries", 4.99, "Sides", 4.6))
        
        expected = 12.99 + 2.50 + 4.99
        assert order.compute_total() == pytest.approx(expected, rel=1e-2)
    
    def test_compute_total_empty_order(self):
        """Test total for an empty order returns 0.0."""
        order = Order()
        assert order.compute_total() == 0.0
    
    def test_compute_total_duplicate_items(self):
        """Test total when same item is added multiple times."""
        order = Order()
        item = FoodItem("Ice Cream", 5.99, "Desserts", 4.8)
        order.add_item(item)
        order.add_item(item)
        
        assert order.compute_total() == pytest.approx(11.98, rel=1e-2)


# ==================== INTEGRATION TESTS ====================
class TestIntegration:
    """Integration tests combining multiple classes."""
    
    def test_menu_filter_then_order(self):
        """Test filtering menu and using result in order."""
        menu = Menu()
        burger = FoodItem("Spicy Burger", 12.99, "Entrees", 4.8)
        soda = FoodItem("Large Soda", 2.50, "Drinks", 4.5)
        menu.add_item(burger)
        menu.add_item(soda)
        
        entrees = menu.filter_by_category("Entrees")
        
        order = Order()
        order.add_item(entrees[0])
        assert order.compute_total() == 12.99
    
    def test_customer_order_total_workflow(self):
        """Test customer placing order and verification."""
        customer = Customer("Alice")
        assert customer.verify_user() == False
        
        order = Order()
        order.add_item(FoodItem("Burger", 12.99, "Entrees", 4.8))
        order.add_item(FoodItem("Soda", 2.50, "Drinks", 4.5))
        
        customer.add_order(order)
        assert customer.verify_user() == True
        assert order.compute_total() == pytest.approx(15.49, rel=1e-2)


# ==================== EDGE CASES ====================
class TestSystemRobustness:
    """Tests where the system could break (boundaries and edge cases)."""
    
    def test_filter_returns_nothing_for_partial_category_name(self):
        """System does not return items from similar categories (e.g., 'Drink' vs 'Drinks')."""
        menu = Menu()
        menu.add_item(FoodItem("Soda", 2.50, "Drinks", 4.5))
        
        wrong_category = menu.filter_by_category("Drink")  # singular, not plural
        assert len(wrong_category) == 0

    def test_multiple_orders_stay_independent(self):
        """Each order total is calculated independently; one order doesn't affect another."""
        order1 = Order()
        order1.add_item(FoodItem("Burger", 12.99, "Entrees", 4.8))
        
        order2 = Order()
        order2.add_item(FoodItem("Soda", 2.50, "Drinks", 4.5))
        
        # Creating order2 should not affect order1's total
        assert order1.compute_total() == 12.99
        assert order2.compute_total() == 2.50

    def test_filtering_does_not_modify_menu(self):
        """Filtering the menu doesn't remove or change items from the original menu."""
        menu = Menu()
        menu.add_item(FoodItem("Burger", 12.99, "Entrees", 4.8))
        
        menu.filter_by_category("Drinks")  # filter for something else
        
        assert len(menu.items) == 1
        assert menu.items[0].name == "Burger"

    def test_customer_starts_unverified_becomes_verified(self):
        """Customer goes from unverified to verified after exactly one purchase."""
        customer = Customer("Alice")
        assert customer.verify_user() == False
        
        order = Order()
        order.add_item(FoodItem("Burger", 12.99, "Entrees", 4.8))
        customer.add_order(order)
        
        assert customer.verify_user() == True

    def test_order_total_handles_mixed_price_magnitudes(self):
        """System correctly sums items with very different prices."""
        order = Order()
        order.add_item(FoodItem("Napkin", 0.01, "Supplies", 3.0))
        order.add_item(FoodItem("Steak", 49.99, "Entrees", 4.8))
        
        assert order.compute_total() == pytest.approx(50.00, rel=1e-2)


# ==================== BEHAVIORAL TESTS (HAPPY PATH) ====================
class TestCoreBusinessLogic:
    """Tests for the main workflows customers care about."""
    
    def test_customer_browsing_and_ordering_workflow(self):
        """Customer can browse a menu, find items by category, and create an order."""
        menu = Menu()
        menu.add_item(FoodItem("Spicy Burger", 12.99, "Entrees", 4.8))
        menu.add_item(FoodItem("Large Soda", 2.50, "Drinks", 4.5))
        menu.add_item(FoodItem("Vanilla Ice Cream", 5.99, "Desserts", 4.8))
        
        # Customer browses for entrees
        entrees = menu.filter_by_category("Entrees")
        assert len(entrees) == 1
        
        # Customer builds order from different categories
        order = Order()
        order.add_item(entrees[0])
        order.add_item(menu.filter_by_category("Drinks")[0])
        order.add_item(menu.filter_by_category("Desserts")[0])
        
        expected_total = 12.99 + 2.50 + 5.99
        assert order.compute_total() == pytest.approx(expected_total, rel=1e-2)

    def test_new_customer_becomes_verified_after_purchase(self):
        """New customer becomes verified user after making their first purchase."""
        customer = Customer("NewCustomer")
        assert customer.verify_user() == False
        
        order = Order()
        order.add_item(FoodItem("Item", 5.00, "Category", 4.0))
        customer.add_order(order)
        
        assert customer.verify_user() == True