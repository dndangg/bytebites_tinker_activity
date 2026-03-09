"""
ByteBites Scenario: Real-world usage demonstration
This script shows a realistic workflow of customers browsing, ordering, and checking out.
"""

from models import FoodItem, Menu, Order, Customer

print("=" * 70)
print("BYTEBITES SCENARIO: Customer Order Workflow")
print("=" * 70)

# ================== SETUP: Build the Menu ==================
print("\n[SETUP] Creating ByteBites Menu")
print("-" * 70)

# Create food items
burger = FoodItem("Spicy Burger", 12.99, "Entrees", 4.8)
classic_burger = FoodItem("Classic Burger", 10.49, "Entrees", 4.7)
fries = FoodItem("Crispy Fries", 4.99, "Sides", 4.6)
soda = FoodItem("Large Soda", 2.50, "Drinks", 4.5)
iced_tea = FoodItem("Iced Tea", 3.00, "Drinks", 4.4)
chocolate_cake = FoodItem("Chocolate Cake", 7.99, "Desserts", 4.9)
ice_cream = FoodItem("Vanilla Ice Cream", 5.99, "Desserts", 4.8)

# Build menu
menu = Menu()
for item in [burger, classic_burger, fries, soda, iced_tea, chocolate_cake, ice_cream]:
    menu.add_item(item)

print(f"✓ Added 7 items to menu")
print(f"  Total items: {len(menu.items)}")

# ================== CUSTOMER 1: Alice ==================
print("\n[CUSTOMER 1] Alice's Order")
print("-" * 70)

# Customer 1 browses the menu
alice = Customer("Alice")
print(f"✓ Customer created: {alice.name}")
print(f"  Verified user: {alice.verify_user()} (no purchases yet)")

# Alice filters for entrees
print(f"\nAlice filters menu for 'Entrees':")
entrees = menu.filter_by_category("Entrees")
print(f"  Available entrees: {len(entrees)}")
for item in entrees:
    print(f"    - {item.name}: ${item.price} (⭐{item.popularity_rating})")

# Alice creates an order
print(f"\nAlice creates order:")
alice_order = Order()
alice_order.add_item(burger)
alice_order.add_item(soda)
alice_order.add_item(chocolate_cake)
print(f"  Items added: {len(alice_order.items)}")
for item in alice_order.items:
    print(f"    - {item.name}: ${item.price}")

# Alice's total
alice_total = alice_order.compute_total()
print(f"  Order total: ${alice_total:.2f}")

# Alice completes purchase
alice.add_order(alice_order)
print(f"✓ Order saved to purchase history")
print(f"  Verified user: {alice.verify_user()} (now verified after purchase!)")

# ================== CUSTOMER 2: Bob ==================
print("\n[CUSTOMER 2] Bob's Order")
print("-" * 70)

bob = Customer("Bob")
print(f"✓ Customer created: {bob.name}")
print(f"  Verified user: {bob.verify_user()} (new customer)")

# Bob browses drinks
print(f"\nBob filters menu for 'Drinks':")
drinks = menu.filter_by_category("Drinks")
print(f"  Available drinks: {len(drinks)}")
for item in drinks:
    print(f"    - {item.name}: ${item.price} (⭐{item.popularity_rating})")

# Bob also wants desserts
print(f"\nBob filters menu for 'Desserts':")
desserts = menu.filter_by_category("Desserts")
print(f"  Available desserts: {len(desserts)}")
for item in desserts:
    print(f"    - {item.name}: ${item.price} (⭐{item.popularity_rating})")

# Bob creates a large order
print(f"\nBob creates order:")
bob_order = Order()
bob_order.add_item(classic_burger)
bob_order.add_item(fries)
bob_order.add_item(iced_tea)
bob_order.add_item(ice_cream)
print(f"  Items added: {len(bob_order.items)}")
for item in bob_order.items:
    print(f"    - {item.name}: ${item.price}")

bob_total = bob_order.compute_total()
print(f"  Order total: ${bob_total:.2f}")

# Bob checks out
bob.add_order(bob_order)
print(f"✓ Order saved to purchase history")
print(f"  Verified user: {bob.verify_user()} (now verified!)")

# ================== CUSTOMER 3: Charlie (Empty Order) ==================
print("\n[CUSTOMER 3] Charlie's Order (Edge Case)")
print("-" * 70)

charlie = Customer("Charlie")
print(f"✓ Customer created: {charlie.name}")

# Charlie creates an empty order
charlie_order = Order()
print(f"\nCharlie creates order with no items")
print(f"  Items in order: {len(charlie_order.items)}")
charlie_empty_total = charlie_order.compute_total()
print(f"  Order total: ${charlie_empty_total:.2f} (empty order)")

print(f"  Verified user: {charlie.verify_user()} (no purchase)")

# Charlie never buys anything
print(f"  → Charlie remains unverified")

# ================== CUSTOMER 4: Diana (Multiple Orders) ==================
print("\n[CUSTOMER 4] Diana's Multiple Orders")
print("-" * 70)

diana = Customer("Diana")
print(f"✓ Customer created: {diana.name}")

# Diana's first order
print(f"\nDiana's first order:")
diana_order_1 = Order()
diana_order_1.add_item(burger)
diana_order_1.add_item(soda)
diana_total_1 = diana_order_1.compute_total()
print(f"  Items: {[item.name for item in diana_order_1.items]}")
print(f"  Total: ${diana_total_1:.2f}")
diana.add_order(diana_order_1)

# Diana's second order
print(f"\nDiana's second order (later that day):")
diana_order_2 = Order()
diana_order_2.add_item(classic_burger)
diana_order_2.add_item(fries)
diana_order_2.add_item(iced_tea)
diana_total_2 = diana_order_2.compute_total()
print(f"  Items: {[item.name for item in diana_order_2.items]}")
print(f"  Total: ${diana_total_2:.2f}")
diana.add_order(diana_order_2)

print(f"✓ Diana has {len(diana.purchase_history)} orders in purchase history")
print(f"  Verified user: {diana.verify_user()} (multiple purchases!)")

# ================== MENU ANALYSIS ==================
print("\n[ANALYSIS] Menu Category Breakdown")
print("-" * 70)

categories = ["Entrees", "Sides", "Drinks", "Desserts"]
for category in categories:
    items_in_category = menu.filter_by_category(category)
    print(f"  {category}: {len(items_in_category)} item(s)")

# Check for non-existent category
print(f"\nSearching for 'Appetizers' (doesn't exist):")
appetizers = menu.filter_by_category("Appetizers")
print(f"  Found: {len(appetizers)} items (empty result handled correctly)")

# ================== SUMMARY ==================
print("\n" + "=" * 70)
print("SCENARIO COMPLETE")
print("=" * 70)
print(f"\nCustomer Summary:")
print(f"  Alice:    Verified={alice.verify_user()},  Orders={len(alice.purchase_history)}")
print(f"  Bob:      Verified={bob.verify_user()},  Orders={len(bob.purchase_history)}")
print(f"  Charlie:  Verified={charlie.verify_user()}, Orders={len(charlie.purchase_history)}")
print(f"  Diana:    Verified={diana.verify_user()},  Orders={len(diana.purchase_history)}")

print(f"\n✓ All scenarios completed successfully!")
print("=" * 70)
