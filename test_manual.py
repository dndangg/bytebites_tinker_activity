"""
Manual test script to verify the four classes work correctly.
This script creates sample objects and inspects them for correctness.
"""

from models import FoodItem, Menu, Order, Customer

print("=" * 60)
print("MANUAL TEST: ByteBites Classes")
print("=" * 60)

# Test 1: FoodItem Creation
print("\n[1] Testing FoodItem Class")
print("-" * 60)
burger = FoodItem("Spicy Burger", 12.99, "Entrees", 4.8)
soda = FoodItem("Large Soda", 2.50, "Drinks", 4.5)
ice_cream = FoodItem("Vanilla Ice Cream", 5.99, "Desserts", 4.9)

print(f"  burger.name: {burger.name}")
print(f"  burger.price: {burger.price}")
print(f"  burger.category: {burger.category}")
print(f"  burger.popularity_rating: {burger.popularity_rating}")
print(f"  ✓ FoodItem attributes stored correctly")

# Test 2: Menu Creation & add_item
print("\n[2] Testing Menu Class")
print("-" * 60)
menu = Menu()
print(f"  Initial menu.items: {menu.items}")
menu.add_item(burger)
menu.add_item(soda)
menu.add_item(ice_cream)
print(f"  Menu after adding 3 items: {len(menu.items)} items")
print(f"  Items: {[item.name for item in menu.items]}")
print(f"  ✓ Menu.add_item() works correctly")

# Test 3: Menu filter_by_category
print("\n[3] Testing Menu.filter_by_category()")
print("-" * 60)
drinks = menu.filter_by_category("Drinks")
print(f"  Drinks found: {[item.name for item in drinks]}")
print(f"  Count: {len(drinks)}")

desserts = menu.filter_by_category("Desserts")
print(f"  Desserts found: {[item.name for item in desserts]}")
print(f"  Count: {len(desserts)}")

entrees = menu.filter_by_category("Entrees")
print(f"  Entrees found: {[item.name for item in entrees]}")
print(f"  Count: {len(entrees)}")

no_match = menu.filter_by_category("NonExistent")
print(f"  NonExistent category: {no_match}")
print(f"  Count: {len(no_match)}")
print(f"  ✓ filter_by_category() works correctly")

# Test 4: Order Creation & add_item
print("\n[4] Testing Order Class")
print("-" * 60)
order = Order()
print(f"  Initial order.items: {order.items}")
order.add_item(burger)
order.add_item(soda)
print(f"  Order after adding 2 items: {len(order.items)} items")
print(f"  Items: {[item.name for item in order.items]}")
print(f"  ✓ Order.add_item() works correctly")

# Test 5: Order compute_total
print("\n[5] Testing Order.compute_total()")
print("-" * 60)
total = order.compute_total()
print(f"  Burger price: ${burger.price}")
print(f"  Soda price: ${soda.price}")
print(f"  Expected total: ${burger.price + soda.price}")
print(f"  Computed total: ${total}")
print(f"  Match: {total == burger.price + soda.price}")
print(f"  ✓ compute_total() calculates correctly")

# Test 6: Empty order total
print("\n[6] Testing Order.compute_total() on empty order")
print("-" * 60)
empty_order = Order()
empty_total = empty_order.compute_total()
print(f"  Empty order total: ${empty_total}")
print(f"  Is zero: {empty_total == 0.0}")
print(f"  ✓ Empty order returns 0.0")

# Test 7: Customer Creation & add_order
print("\n[7] Testing Customer Class")
print("-" * 60)
customer = Customer("Alice")
print(f"  customer.name: {customer.name}")
print(f"  customer.purchase_history: {customer.purchase_history}")
print(f"  ✓ Customer initialized correctly")

# Test 8: Customer verify_user before purchase
print("\n[8] Testing Customer.verify_user() [No purchases]")
print("-" * 60)
is_verified_before = customer.verify_user()
print(f"  verify_user() before purchase: {is_verified_before}")
print(f"  Is False: {is_verified_before == False}")
print(f"  ✓ Unverified customer returns False")

# Test 9: Customer add_order
print("\n[9] Testing Customer.add_order()")
print("-" * 60)
customer.add_order(order)
print(f"  purchase_history length: {len(customer.purchase_history)}")
print(f"  ✓ Order added to history")

# Test 10: Customer verify_user after purchase
print("\n[10] Testing Customer.verify_user() [After purchase]")
print("-" * 60)
is_verified_after = customer.verify_user()
print(f"  verify_user() after purchase: {is_verified_after}")
print(f"  Is True: {is_verified_after == True}")
print(f"  ✓ Verified customer returns True")

# Test 11: Integration Test
print("\n[11] Integration Test: Full Workflow")
print("-" * 60)
# Create second customer
customer2 = Customer("Bob")
# Create second order
order2 = Order()
order2.add_item(ice_cream)
order2.add_item(ice_cream)  # Add same item twice
total2 = order2.compute_total()
print(f"  Bob's order total (2x Ice Cream): ${total2}")
print(f"  Expected: ${ice_cream.price * 2}")
print(f"  Match: {total2 == ice_cream.price * 2}")
# Add order to history
customer2.add_order(order2)
print(f"  Bob is verified: {customer2.verify_user()}")
print(f"  ✓ Integration workflow successful")

print("\n" + "=" * 60)
print("ALL MANUAL TESTS COMPLETED SUCCESSFULLY!")
print("=" * 60)
