"""The program will copy the restaurant system. But I do it in my way, and how I understand it."""
import time
from typing import List


class NumberOutOfRange(Exception):
    """Class for generating a specified error"""


class Menu:
    """This class represents menu in this system. It has a list of dishes,
    which I create when I run my program."""

    def __init__(self):
        self.dishes: List[MenuItem] = []

    def add_dish(self, dish_name: str, price: float) -> None:
        """Adding the dish into list of dishes"""
        dish = MenuItem(dish_name, price)
        self.dishes.append(dish)

    def display_menu(self) -> None:
        """Displaying the menu, which I made up, using the function above"""
        if not self.dishes:
            print('The menu is empty')
        else:
            # It seems to me, that using enumerate() function is much better here.
            print('\nMenu:')
            for index, dish in enumerate(self.dishes):
                print(f'{index + 1}. {dish.get_dish()}')


class MenuItem:
    """It is a small class, the main purpose of which is to return the dish."""

    def __init__(self, dish_name: str, price: float):
        self.dish_name = dish_name
        self.price = price

    def get_dish(self) -> str:
        return f'{self.dish_name} - {self.price}$'


class Order:
    """Class, which represents an order and takes the restaurant as an attribute and
    ordered dishes."""

    def __init__(self, restaurant: 'Restaurant'):
        self.restaurant = restaurant
        self.ordered_dishes: List[MenuItem] = []

    def user_order(self) -> None:
        """This function performs handles customer's order."""
        order = input('\nType an appropriate numbers to add the dish to the order, split by comma: ')
        numbers_in_order = order.split(',')
        # Using try except construction aiming to avoid program crashing due to mistakes
        try:
            for num_str in numbers_in_order:
                num = int(num_str)
                if num < 1 or num > len(self.restaurant.menu.dishes):
                    raise NumberOutOfRange
                self.ordered_dishes.append(self.restaurant.menu.dishes[num - 1])
            print('Your order: ')
            for dish in self.ordered_dishes:
                print(dish.get_dish())
        except ValueError:
            print('Please make the correct order')
            # The class, which I made up in the beginning of my program.
        except NumberOutOfRange:
            print('One ore more numbers out of range')

    def get_the_bill(self) -> None:
        """The function, which handles the customer's bill. Use here while loop, because
        I need to repeat the cycle every time when user wants something else to order.
        It makes sense for me"""
        while 1:
            bill: float = 0
            for dish in self.ordered_dishes:
                bill += dish.price
            answer = input(f'Your bill is: {bill}$. Maybe anything else? (Yes/No)')
            if answer.strip().lower() == 'yes':
                Order.user_order(self)
            elif answer.strip().lower() == 'no':
                break
        print('\nOk, I hope that everything was tasty for you. Please, pay the bill.')
        # Creating a customer, which has definite methods and properties, which overwritten below.
        customer: Customer = Customer()
        if customer.can_pay(bill_amount=bill):
            final_balance = customer.cash - bill
            print(f'Your balance now is {final_balance}$')
        else:
            # It is just a kind of joke:):)
            self.restaurant.waiter.waiter_is_angry()


class Waiter:
    """Class which represents a waiter in this system. It can be polite in
    the beginning and rude if the customer can't pay the bill. I think everything is clear here"""

    def __init__(self, restaurant: 'Restaurant'):
        self.name: str = 'Tuco'
        self.restaurant = restaurant

    def waiter_greeting(self) -> None:
        print(f'Hi! My name is {self.name}. I\'m a waiter in this restaurant. '
              f'Have you chosen what you want to order?')
        time.sleep(2)
        self.restaurant.menu.display_menu()

    def waiter_is_angry(self) -> None:
        print('Get out from here! Never back here again!!')


class Restaurant:
    """The class of the restaurant itself. Has a symbolic name and takes a menu as an attribute."""

    def __init__(self):
        self.name = 'Clode Mone'
        self.menu = Menu()
        self.waiter = Waiter(self)

    def _start_program(self) -> None:
        """Function, which runs the program, and everything starts from here."""
        greeting = input(f'\nGood afternoon! You are in the restaurant {self.name}. '
                         f'You can sit for the free table and '
                         'await for the waiter. \n -Sit(s) \n -Go out(q)\n')
        if greeting.lower().strip() == 's':
            print('Ok. The waiter will come soon!')
            print('...')
            time.sleep(4)
            # step by step, this function calls the help-functions written below.
            waiter = Waiter(self)
            waiter.waiter_greeting()
            order = Order(self)
            order.user_order()
            order.get_the_bill()
        elif greeting.lower().strip() == 'q':
            print('Good Bye!')
        else:
            print('Incorrect choice')


class Customer:
    """This class I have made for fun:) I wanted to see a furious waiter if the customer can't
     afford to pay for the  bill. I also use here property decorator to get and set the values
     of the custome's cash. But to be honest, setter is useless for this program.
     I created it just for practice."""

    def __init__(self):
        self._cash: float = 100

    @property
    def cash(self) -> float:
        return self._cash

    @cash.setter
    def cash(self, money: float) -> None:
        if money < 0:
            print('Invalid sum')
        else:
            self._cash = money

    def can_pay(self, bill_amount: float) -> bool:
        if bill_amount < self.cash:
            print(f'(You can afford to pay the bill in {bill_amount}$, '
                  f'since you have {self.cash}$)')
            return True
        else:
            print(f'(You can not afford to pay the bill in {bill_amount}$, since you '
                  f'have {self.cash}$)')
            return False
