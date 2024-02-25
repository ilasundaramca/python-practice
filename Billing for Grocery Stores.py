#'Tamil Kadai' Grocery stores Billing application
price_list = {
'Rice' : 6.00,
'Dal' : 8.00,
'sugar' : 3.00,
'Salt' : 2.00,
'Snacks' : 1.00
}
#print(price_list)
#print(price_list["Salt"])

print("Tamil Kadai\n","தமிழ்க் கடை\n", "Date:2024-02-17")
#for item in price_list:
#   print(item)
#    print(item + "=$" + str(price_list[item]))

from datetime import datetime
#current_dateTime = datetime.now()
#print(current_dateTime)
print(datetime.now())

grand_total_list = []
all_line_items = []
products = True
while products:
    item = input ("Enter item Name: ")
    if item == "End":
      products = False
    else:
        quantity = int(input ("Enter Quantity: "))
# print(item + ":" + str(price_list[item]) + "x" + str (quantity) + "+" + (int(price_list[item]+int(quantity))))
        item_price = int(price_list[item]) * int(quantity)
        grand_total_list.append (item_price)

        line_item = item, ":", str(price_list[item]), "x", str(quantity), "=", str(item_price)
        all_line_items.append(line_item)
'''
#print (all_line_items)
for line in all_line_items:
    print (' '.join(line))
print ("Grand Total = ", str(sum(grand_total_list)))
'''



