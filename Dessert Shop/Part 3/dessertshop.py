#############################################################
from receipt import make_receipt
from dessert import Order, Candy, Cookie, IceCream, Sundae

def format_money(amount):
    return "$" + "{:.2f}".format(amount)

def main():
    myOrder = Order()
    candy1 = Candy("Candy Corn", 1.5, .25)
    candy2 = Candy("Gummy Bears", .25, .35)
    cookie1 = Cookie("Chocolate Chip", 6, 3.99)
    icecream1 = IceCream("Pistachio", 2, .79)
    sumndae1 = Sundae("Vanilla", 3, .69, "Hot Fudge", 1.29)
    cookie2 = Cookie("Oatmeal Raisin", 2, 3.45)

    # Add each instance of the objects to the Order object
    myOrder.add(candy1)
    myOrder.add(candy2)
    myOrder.add(cookie1)
    myOrder.add(icecream1)
    myOrder.add(sumndae1)
    myOrder.add(cookie2)

    # List of lists
    data = []
    total_cost = 0
    total_tax = 0

    #first Rows
    data.append(["Name", "Item Cost", "Tax"])
    for item in myOrder:
        name = str(item)
        cost = item.calculate_cost()
        tax = item.calculate_tax()
        formatted_cost = format_money(cost)
        formatted_tax = format_money(tax)
        data.append([name, formatted_cost, formatted_tax])
        total_cost += cost
        total_tax += tax

    # Rows for totals
    data.append(["---------------------------------"])
    data.append(["Order Subtotals", format_money(total_cost), format_money(total_tax)])
    data.append(["Order Total", " ",format_money(total_cost + total_tax)])
    data.append(["Total items in the order", " ", str(len(myOrder))])

    make_receipt(data, "receipt.pdf")

main()
