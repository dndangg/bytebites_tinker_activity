# Customer class
# Manages customer information and tracks purchase history
# Attributes: name, purchase_history
# Methods: add_order(), verify_user()
class Customer:
    pass


# FoodItem class
# Represents individual menu items with their properties
# Attributes: name, price, category, popularity_rating
class FoodItem:
    pass


# Order class
# Groups selected food items into a single transaction
# Computes and stores the total cost of the order
# Attributes: items
# Methods: add_item(), compute_total()
class Order:
    pass


# Menu class
# Manages the full collection of available food items
# Provides filtering capabilities by category
# Attributes: items
# Methods: add_item(), filter_by_category()
class Menu:
    pass
