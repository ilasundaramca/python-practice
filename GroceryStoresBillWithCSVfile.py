#'Tamil Kadai' Grocery stores Billing application
import sys
input_file = open('pricelist.csv','r')
all_itmes = input_file.readlines()
price_list = {}
for item in all_itmes:
    #print(item)
    item_name = item.split(",")[0]
    item_price = item.split(",")[1]

    price_list[item_name] = item_price.strip()
#print(price_list)
#sys.exit()


print("Tamil Kadai\n","தமிழ்க் கடை\n")

from datetime import datetime
current_dateTime = datetime.now()
dt = current_dateTime.strftime("%Y-%m-%d-%H-%M-%S")
print(dt)

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



print_file = open('Inv_'+ dt +'.txt','w')

print_file.write("Welcome to tamil kadai\n")

#print_file.write("Tamil Kadai\n")

for item in all_line_items:
    print_file.write(str(' '.join(item)))

print_file.write("\n\nTotal = " + str(sum(grand_total_list)))
print_file.close()
