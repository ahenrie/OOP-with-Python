from receipt import make_receipt
from desserts import Order, Candy, Cookie, IceCream, Sundae

def format_money(amount):
    return "$" + "{:.2f}".format(amount)

class DessertShop:
    def prompt(self):
        print("1: Candy\n2: Cookie\n3: Ice Cream\n4: Sundae")

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
    '''
    order.add(Candy('Candy Corn', 1.5, 0.25))
    order.add(Candy('Gummy Bears', 0.25, 0.35))
    order.add(Cookie('Chocolate Chip', 6, 3.99))
    order.add(IceCream('Pistachio', 2, 0.79))
    order.add(Sundae('Vanilla', 3, 0.69, 'Hot Fudge', 1.29))
    order.add(Cookie('Oatmeal Raisin', 2, 3.45))
    '''
    done = False
    # build the prompt string once
    prompt = '\n'.join([ '\n',
              '1: Candy',
               '2: Cookie',            
              '3: Ice Cream',
              '4: Sundae',
              '\nWhat would you like to add to the order? (1-4, Enter for done): '
        ])

    while (not done):
        choice = input(prompt)
        match choice:
                case '':
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

    # Print the PDF receipt
    data = []
    total_cost = 0
    total_tax = 0

    data.append(["Name", "Item Cost", "Tax"])
    #logic to test for empty order
    for item in order:
        name = str(item)
        cost = item.calculate_cost()
        tax = item.calculate_tax()
        formatted_cost = format_money(cost)
        formatted_tax = format_money(tax)
        data.append([name, formatted_cost, formatted_tax])
        total_cost += cost
        total_tax += tax
         
    data.append(["---------------------------------"])
    data.append(["Order Subtotals", format_money(total_cost), format_money(total_tax)])
    data.append(["Order Total", " ", format_money(total_cost + total_tax)])
    data.append(["Total items in the order", " ", str(len(order))])
 
    make_receipt(data, "receipt.pdf")

main()
