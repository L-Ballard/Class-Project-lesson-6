# Program:      Lesson 4 Order Program
# Progammer:    Luke Ballard
# Date:         7/15/2024
# Purpose:      The purpse of this program is to add a looping order entry

# Variable
import locale
locale.setlocale(locale.LC_ALL, '')
cont = ""
order_total = 0
item_cnt = 0
flavor = ""
box_num = 0
choice = ""
box_price = 0
total_box = 0
total_price = 0
your_order = ''
#Price for box of cookie
Savannah_price = 3.50
ThinMint_price = 3.50
Tagalong_price = 5.00

def box_number():
        box_num = int(input("How many boxes would you like between 1 and 10? "))
        if box_num < 0 and box_num >10:
                print ("Error: Number of boxes can not be a negative number")
                print ("Please select a new number of boxes ")
        else:
                print("Thank you for selecting {} boxes of {}!".format(box_num, flavor))
                        
cont = input ("Would you like to order?: (y/n)")

while True:
        name = input ("Can I get a name for the order: ")
        if len(name) < 1 or len(name) > 20:
            print ("Name Error: please enter a name between 1 and 20 characters. Thank you!")
        else:
            break

while cont.lower () == "y":



#Menu
    print ("Here are all of our cookies!")
    print ("1. Savannah Cookie's {}".format(locale.currency(Savannah_price)))
    print ("2. Thin Mints Cookie's {}".format(locale.currency(ThinMint_price)))
    print ("3. Tagalong Cookie's {}".format(locale.currency(Tagalong_price)))

    
#Cookie Choice
    while True:
        choice = int(input ("Please select 1, 2, or 3 "))
        if (choice) <1 or choice >3:
                 print ("Error: you have slected out side the desired range. Please select 1, 2, or 3")
        elif (choice) == 1:
                print ("Savannah cookie's great choice!")
                flavor = "Savannah"
                box_number()
                break
        elif (choice) == 2:
                print ("Thin Mints cookie's great choice!")
                flavor = "Thin Mints"
                Box_number()
                break
        elif (choice) == 3:
                print ("Tagalong cookie's great choice!")
                flavor = "Tagalong"
                box_number()
                break
        else:
                break

#accumulator
    item_cnt += 1
    total_box = box_num + total_box
    total_price = box_price + total_price 
#detail output

    print ("Item    Name     Price   Qty    Total")
    print ("{}      {}     {}     {}     {}      ".format (item_cnt,
                                                  flavor,
                                                  locale.currency(box_price),
                                                  total_box,
                                                  locale.currency(total_price)))
 
    cont = ""
    while cont.lower() != "y" and cont.lower() != "n":    
        cont = input("Would you like to add another item?: (y/n)")

#output
your_order = ("""
Order for {}
The Total number of uniqe purches you made: {}
Your total number of boxes is: {}
Your total price come out to: {}

Thank you for your order
""".format (name, item_cnt, total_box,locale.currency(total_price)))

print (your_order)
#print("Debug end")
