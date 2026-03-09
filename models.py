# FoodItem class
# Represents individual menu items with their properties
# Attributes: name, price, category, popularity_rating
class FoodItem:
    def __init__(self, name: str, price: float, category: str, popularity_rating: float):
        """Initialize a food item with its properties."""
        self.name = name
        self.price = price
        self.category = category
        self.popularity_rating = popularity_rating


# Menu class
# Manages the full collection of available food items
# Provides filtering capabilities by category
# Attributes: items
# Methods: add_item(), filter_by_category()
class Menu:
    def __init__(self):
        """Initialize an empty menu."""
        self.items = []
    
    def add_item(self, item: FoodItem) -> None:
        """Add a food item to the menu."""
        self.items.append(item)
    
    def filter_by_category(self, category: str) -> list:
        """Return all items matching the specified category."""
        return [item for item in self.items if item.category == category]


# Order class
# Groups selected food items into a single transaction
# Computes and stores the total cost of the order
# Attributes: items
# Methods: add_item(), compute_total()
class Order:
    def __init__(self):
        """Initialize an empty order."""
        self.items = []
    
    def add_item(self, item: FoodItem) -> None:
        """Add a food item to the order."""
        self.items.append(item)
    
    def compute_total(self) -> float:
        """Calculate and return the total cost of all items in the order."""
        return sum(item.price for item in self.items)


# Customer class
# Manages customer information and tracks purchase history
# Attributes: name, purchase_history
# Methods: add_order(), verify_user()
class Customer:
    def __init__(self, name: str):
        """Initialize a customer with a name."""
        self.name = name
        self.purchase_history = []
    
    def add_order(self, order: Order) -> None:
        """Add an order to the customer's purchase history."""
        self.purchase_history.append(order)
    
    def verify_user(self) -> bool:
        """Verify the user has made at least one purchase."""
        return len(self.purchase_history) > 0
