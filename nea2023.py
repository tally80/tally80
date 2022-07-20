#import additional libraries
import time, sys, datetime, calendar
#splash screen to the program
print('''.::: SHOP IN PARKWOOD VALE :::.
    SIP Card Management System
    
    please wait...''')
time.sleep(2)

#lists to store data
customers = []
stores = []
transactions = []


#Try to load the customers list from the file. If it fails at all, then it will use the blank list.
try:
  f = open("customers.txt", "r")
  customers = eval(f.readline())
  f.close()
except:
  pass

#Try to load the stores list from the file. If it fails at all, then it will use the blank list.
try:
  f = open("stores.txt", "r")
  stores = eval(f.readline())
  f.close()
except:
  pass

#Try to load the transactions list from the file. If it fails at all, then it will use the blank list.
try:
  f = open("transactions.txt", "r")
  transactions = eval(f.readline())
  f.close()
except:
  pass

#list of days to help with input
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]


#Subroutine for adding a new customer
def newCustomer():
    customerName = input("Please enter the customer's first and last name: ").title()
    startDate = input("Please enter the start date (dd/mm/yyyy): ")
    validFrom = datetime.datetime.strptime(startDate,"%d/%m/%Y").date()
    while (len(startDate)) != 10:
        print("Error! Please enter the date in the valid format.")
        startDate = input("Please enter the start date (dd/mm/yyyy): ")
        validFrom = datetime.datetime.strptime(startDate,"%d/%m/%Y").date()
    validUntil = validFrom + datetime.timedelta(days=365)
    cardNumber = input("Enter the new SIP card number, e.g. SIP12345: ")
    cardList = []
    for row in customers:
        cardList.append(row[1])
    while cardNumber in cardList:
        print("ERROR! Card number already in use.")
        cardNumber = input("Enter the new SIP card number, e.g. SIP12345: ")
        
    row = [customerName, cardNumber, validFrom, validUntil]
    customers.append(row)
    
    print("New customer added successfully.")
    time.sleep(1)



#subroutine for adding a new store
def newStore():
    
    storeName = input("Please Enter the name of your store: ").title()
    while (storeName == ""):
        print("ERROR! Cannot be blank!")
        storeName = input("Please Enter the name of your store: ").title()
    
    discountDay = input("Please enter the day you wish to offer 10% discount on purchases: ").title()
    while(discountDay == ""):
        print("ERROR! Cannot be blank!")
        discountDay = input("Please enter the day you wish to offer 10% discount on purchases: ").title()
    
    delivery = input("Will you be offering free deliveries to SIP members? Yes / No: ").title()
    while (delivery == "" and delivery != "Yes" and delivery != "No"):
        print("ERROR! invalid input! Please Enter either Yes or No.")
        delivery = input("Will you be offering free deliveries to SIP members? Yes / No: ").title()
        
    products = input("Enter the product you will offer a 2 for 1 deal on: ").title()
    while (products == ""):
        print("ERROR! Cannot be blank!")
        products = input("Enter the product you will offer a 2 for 1 deal on: ").title()
           
    row = [storeName, discountDay, delivery, products]
    stores.append(row)
    
    print("New store added successfuly.")
    time.sleep(1)



#subroutine for adding a new transaction
def newTransaction():
    name = input("Enter the name of the store: ").title()
    storeList = []
    for row in stores:
        storeList.append(row[0])
    while name.title() not in storeList:
        print("ERROR. Cannot find store name.")
        name = input("Enter the name of the store: ").title()
    
    for row in stores:
        if name == row[0] and row[2] == "Yes":
            delivery = 0.0
            print("Customer recieves free delivery.")
            time.sleep(1)
        elif name == row[0] and row[2] == "No":
            delivery = 2.00
            print("Delivery is charged at £2.00")
            time.sleep(1)
    
    date = datetime.date.today()
    
    day = calendar.day_name[date.weekday()]
    for row in stores:
        if name == row[0] and day == row[1]:
            discount = 0.1
            discountUsed = "Yes"
            print("The customer is entitled to 10% discount on this transaction.")
        elif name == row[0] and day != row[1]:
            discount = 0.0
            discountUsed = "No"
            print("The customer is NOT entitled to any discount on this transaction today.") 
    
    
    sipCode = input("Enter the customer's SIP card number, e.g SIP12345: ").upper()
    sipList = []
    for row in customers:
        sipList.append(row[1])
    while sipCode.upper() not in sipList:
        print("ERROR! SIP Code does not exit.")
        sipCode = input("Enter the customer's SIP card number, e.g SIP12345: ").upper()
    print("Checking if the card is valid...")
    time.sleep(1)
    for row in customers:
        if sipCode == row[1]:
            expDate = row[3]
            if expDate < datetime.date.today():
                print("Sorry! This card expired on ", expDate)
                print("Returning to the main menu...")
                time.sleep(1)
            elif expDate >= datetime.date.today():
                print("This SIP card is valid!")
            else:
                print("Error. Returning to main menu...")
                time.sleep(1)

    products = input("Enter any 2 for 1 products bought: ").title()
    productList = []
    for row in stores:
        productList.append(row[3])
    while products not in productList:
        print("That is not a valid 2 for 1 product.")
        print("Valid 2 for 1 products are:")
        for row in products:
            print("\t",row)
        print()
        products = input("Enter any 2 for 1 products bought: ").title()


    cost = float(input("Enter the total cost of the transaction: £"))
    while cost == "":
        print("ERROR! Cannot be blank")
        cost = float(input("Enter the total cost of the transaction: £"))
        
    subTotal = round(cost + delivery, 2)
    discountValue = round(subTotal * discount,2)
    total = round(subTotal - discountValue, 2)
    print("The total for this transaction, inc delivery and any discount is: £" + str(total))

    row = [name, date, day, discountUsed, sipCode, products, delivery, total, discountValue]
    transactions.append(row)

    print("New transaction successfully added.")
    time.sleep(1)


#subroutine for printing a monthly report
def printReport():
    name = input("Enter the name of the store: ").title()
    storeList = []
    for row in stores:
        storeList.append(row[0])
    if name.title() not in storeList:
        print("ERROR. Cannot find store name.")
        name = input("Enter the name of the store: ").title()
    
    reportStart = input("Enter start date of report to print (dd/mm/yyy): ")
    startDate = datetime.datetime.strptime(reportStart,"%d/%m/%Y").date()
    reportEnd = input("Enter end date of report to print (dd/mm/yyy): ")
    endDate = datetime.datetime.strptime(reportEnd,"%d/%m/%Y").date()

    for row in transactions:
        if (row[1] >= startDate  and row[1] <= endDate):
            rName = str(row[0])
            rDate = str(row[1].strftime("%d,%m,%Y"))
            rDay = str(row[2])
            rDiscount = str(row[3])
            rSip = str(row[4])
            rProduct = str(row[5])
            rTotal = str(row[7])
            rDiscTotal = str(row[8])
            report = [rName, rDate, rDay, rDiscount, rSip, rProduct, rTotal, rDiscTotal]
            print("::::: REPORT :::::")
            print("Store Name |  Sale Date  |  Day  |  Discount Used?  |  SIP  |  2 for 1 Product  |  Amount Spent  |  Discount Amount")
            for row in report:
                print(report[row])
                time.sleep(3)
        else:
            print("No transactions can be found in this date range")
            startAgain = input("Do you want to search again? Y/N: ").upper()
            if startAgain == "Y":
                print()
                printReport()
            elif startAgain == "N":
                return
            time.sleep(1)
    


#subroutine to exit the program
def exit():
    sys.exit()

#main menu. The while loop is so that the user will always return to the main menu.
while (True):
    print(''':::::::::::::::::::::::::::::::
.::: SHOP IN PARKWOOD VALE :::.

    Please enter a number for one of the following options:

    1. Record a new customer
    2. Record a new store
    3. Record a transaction
    4. Print a report
    5. Exit''')
    menu = input("> ")
    
    if menu == "1":
        newCustomer()
    elif menu == "2":
        newStore()
    elif menu == "3":
        newTransaction()
    elif menu == "4":
        printReport()
    elif menu == "5":
        exit()
    else:
        print("ERROR! Please enter a valid option.")
    
    time.sleep(1)
  
    f = open("customers.txt", "w")
    f.write(str(customers))
    f.close()
    
    f = open("stores.txt", "w")
    f.write(str(stores))
    f.close()

    f = open("transactions.txt", "w")
    f.write(str(transactions))
    f.close()
