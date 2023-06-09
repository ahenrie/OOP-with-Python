from dessert import Order, Candy, Cookie, IceCream, Sundae
from payable import Payable

class DessertShop:
    def prompt(self):
      print("1: Candy\n2: Cookie\n3: Ice Cream\n4: Sundae")

    def user_prompt_payment(self):
      valid_types = {"1": "CASH", "2": "CARD", "3": "PHONE"}
      payment_prompt = '\n'.join([ '\n',
                    '1: Cash',
                    '2: Card',
                    '3: Phone',
                    '\nEnter payment method: '])
      while True:
        choice = input(payment_prompt)
        if choice in valid_types:
          return valid_types[choice]
        else:
          print("Invalid payment. Please try again.")

    def user_prompt_candy(self):
      name = input("Enter the name of the candy: ")
      weight = float(input("Enter the weight of the candy: "))
      price_per_pound = float(input("Enter the price per pound of the candy: "))
      return Candy(name, weight, price_per_pound)

    def user_prompt_cookie(self):
      type = input("Enter the type of cookie: ")
      quantity = int(input("Enter the quantity purchased: "))
      price_per_dozen = float(input("Enter the price per dozen of the cookie: "))
      return Cookie(type, quantity, price_per_dozen)

    def user_prompt_icecream(self):
      flavor = input("Enter the flavor of the ice cream: ")
      scoops = int(input("Enter the number of scoops: "))
      price_per_scoop = float(input("Enter the price per scoop of the ice cream: "))
      return IceCream(flavor, scoops, price_per_scoop)

    def user_prompt_sundae(self):
      flavor = input("Enter the flavor of the ice cream: ")
      scoops = int(input("Enter the number of scoops: "))
      price_per_scoop = float(input("Enter the price per scoop of the ice cream: "))
      topping = input("Enter the topping: ")
      price_for_topping = float(input("Enter the price for the topping: "))
      return Sundae(flavor, scoops, price_per_scoop, topping, price_for_topping)

def main():
    shop = DessertShop() 
    order = Order()
    done = False
    # build the prompt string once
    prompt = '\n'.join([ '\n',
              '1: Candy',
              '2: Cookie',            
              '3: Ice Cream',
              '4: Sundae',
              '\nWhat would you like to add to the order? (1-4, Enter for done): '
        ])

    payment_prompt = '\n'.join([ '\n',
                    '1: Cash',
                    '2: Card',
                    '3: Phone',
                    '\nEnter payment method: '])

    while (not done):
        choice = input(prompt)
        match choice:
                case '':
                  payment_type = shop.user_prompt_payment()
                  order.set_pay_type(payment_type)
                  done = True
                case '1':            
                  item = shop.user_prompt_candy()
                  order.add(item)
                  print(f'{item.name} has been added to your order.')
                case '2':            
                  item = shop.user_prompt_cookie()
                  order.add(item)
                  print(f'{item.name} has been added to your order.')
                case '3':            
                  item = shop.user_prompt_icecream()
                  order.add(item)
                  print(f'{item.name} has been added to your order.')
                case '4':            
                  item = shop.user_prompt_sundae()
                  order.add(item)
                  print(f'{item.name} has been added to your order.')
                case _:            
                  print('Invalid response: Please enter a choice from the menu (1-4) or Enter')
    print()

    print(order)
"""
    total_cost = 0
    total_tax = 0

    #Print title of receipt
    print("----------------------------------------------Receipt---------------------------")
    i = 1
    for item in order:
      print(item)
      cost = item.calculate_cost()
      tax = item.calculate_tax()
      total_tax += tax
      total_cost += cost
      i += 1
    #Separate with ------------------
    print("---------------------------------------------------------------------------------")
    print(f"Total items in the order: {i}")
    print(f"Order Subtotals:\t\t\t\t${total_cost:.2f}\t\t[Tax: ${total_tax:.2f}]")
    print(f"Order Total:\t\t\t\t\t\t\t      ${total_tax + total_cost:.2f}")
"""
main()
