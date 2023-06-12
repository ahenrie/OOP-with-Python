from dessert import Order, Candy, Cookie, IceCream, Sundae
from payable import Payable
from receipt import make_receipt

def main():
  class DessertShop:
    def prompt(self):
      print("1: Candy\n2: Cookie\n3: Ice Cream\n4: Sundae")

    def user_prompt_payment(self):
      valid_types = {"1": "CASH", "2": "CARD", "3": "PHONE"}
      payment_prompt = '\n'.join(['\n',
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

    def new_order(self):
      while True:
        new_order = input("Would you like to place another order? (y/n): ")
        if new_order.lower() == "y":
          self.place_order()
        else:
          break

    def place_order(self):
      order = Order()
      done = False
      prompt = '\n'.join([
               '\n',
                '1: Candy',
                '2: Cookie',
                '3: Ice Cream',
                '4: Sundae',
                '\nWhat would you like to add to the order? (1-4, Enter for done): '
            ])

      payment_prompt = '\n'.join([
                      '\n',
                      '1: Cash',
                      '2: Card',
                      '3: Phone',
                      '\nEnter payment method: '
            ])

      while not done:
        choice = input(prompt)
        match choice:
          case '':
            payment_type = self.user_prompt_payment()
            order.set_pay_type(payment_type)
            done = True
          case '1':
            item = self.user_prompt_candy()
            order.add(item)
            print(f'{item.name} has been added to your order.')
          case '2':
            item = self.user_prompt_cookie()
            order.add(item)
            print(f'{item.name} has been added to your order.')
          case '3':
            item = self.user_prompt_icecream()
            order.add(item)
            print(f'{item.name} has been added to your order.')
          case '4':
            item = self.user_prompt_sundae()
            order.add(item)
            print(f'{item.name} has been added to your order.')
          case _:
            print('Invalid response: Please enter a choice from the menu (1-4) or Enter')
      print()

      data = []
      data.append(["Name", "Packaging", "Quantity", "Unit Price", "Cost", "Tax"])
      order.sort()
      for item in order:
        string = item.__str__()
        values = string.split(",")
        data.append(values[0:6])

      # check for sundaes
      if len(values) > 6:
        data.append([values[6], "", "", "", values[7], ""])

      data.append(["Order Subtotals", "", "", "", f"${order.order_cost():.2f}", f"${order.order_tax():.2f}"])
      data.append(["Order Total", "", "", "", f"${order.order_cost() + order.order_tax():.2f}", ""])
      data.append(["Total Items in the order", "", str(len(order))])
      data.append(["Paid with", "", str(order.get_pay_type())])

      make_receipt(data)

  shop = DessertShop()
  shop.new_order()

main()
