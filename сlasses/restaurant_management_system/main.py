from classes import Restaurant, Customer
if __name__ == '__main__':
    restaurant = Restaurant()
    restaurant.menu.add_dish('Spaghetti Bolognese', 12)
    restaurant.menu.add_dish('Caesar Salad', 8)
    restaurant.menu.add_dish('Margherita Pizza', 10)
    restaurant.menu.add_dish('Grilled Chicken Breast', 15)
    restaurant.menu.add_dish('Fish and Chips ', 13)
    restaurant._start_program()