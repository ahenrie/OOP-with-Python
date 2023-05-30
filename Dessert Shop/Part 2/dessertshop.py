#############################################################
"""
I added a __str__ magical method to the Order class to clean 
up what I originally made. I do not know if I will get docked
points so I left what I originally wrote just in lines 32-34
"""
#############################################################

from dessert import Order, Candy, Cookie, IceCream, Sundae

def main():
   myOrder = Order()
   candy1 = Candy("Candy Corn", 1.5, .25)
   candy2 = Candy("Gummy Bears", .25, .35)
   cookie1 = Cookie("Chocolate Chip", 6, 3.99)
   icecream1 = IceCream("Pistachio", 2, .79)
   sumndae1 = Sundae("Vanilla", 3, .69, "Hot Fudge", 1.29)
   cookie2 = Cookie("Oatmeal Raisin", 2, 3.45)

   #add each intance of the objects to the Order object
   myOrder.add(candy1)
   myOrder.add(candy2)
   myOrder.add(cookie1)
   myOrder.add(icecream1)
   myOrder.add(sumndae1)
   myOrder.add(cookie2)

   #iterate through each item that is added and print
   for item in myOrder:
      print(item)

   #dislpay the total number of items in myOrder
   #total = str(myOrder.__len__())
   #print("Total number of items in order: " + total)
   print(myOrder)

main()
