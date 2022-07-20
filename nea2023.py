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


#Load data from a text file into the global list. If file does not exist, it will make a new .txt file.
try:
  f = open("customers.txt", "r")
  customers = eval(f.readline())
  f.close()
#This will mean if the Try code cannot execute, then it will bypass it and continue to next snippet.
except:
  pass

#Load data from a text file into the global list. If file does not exist, it will make a new .txt file.
try:
  f = open("stores.txt", "r")
  stores = eval(f.readline())
  f.close()
#This will mean if the Try code cannot execute, then it will bypass it and continue to next snippet.
except:
  pass

#Load data from a text file into the global list. If file does not exist, it will make a new .txt file.
try:
  f = open("transactions.txt", "r")
  transactions = eval(f.readline())
  f.close()
#This will mean if the Try code cannot execute, then it will bypass it and continue to next snippet.
except:
  pass

#list of days to help with input
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]


#Subroutine for adding a new customer
def newCustomer():
    #Get data from user through inputs. .title() will force the first letter of each word to capitalise.
    customerName = input("Please enter the customer's first and last name: ").title()
    startDate = input("Please enter the start date (dd/mm/yyyy): ")
    #This converts the input data to datetime format.
    validFrom = datetime.datetime.strptime(startDate,"%d/%m/%Y").date()
    #this is to validate the date intered is 10 characters inc slashes. if not it loops back to the input again.
    while (len(startDate)) != 10:
        print("Error! Please enter the date in the valid format.")
        startDate = input("Please enter the start date (dd/mm/yyyy): ")
        validFrom = datetime.datetime.strptime(startDate,"%d/%m/%Y").date()
    #this takes the start date and adds 365 days to it to create the expiry date automatically.
    validUntil = validFrom + datetime.timedelta(days=365)
    cardNumber = input("Enter the new SIP card number, e.g. SIP12345: ")
    #This creates a new list of all the SIP card numbers in the customer list ready to be searched to check the new number is unique.
    cardList = []
    for row in customers:
        cardList.append(row[1])
    #this iterates the list and if the number is present, returns an error message and loops back to input.
    while cardNumber in cardList:
        print("ERROR! Card number already in use.")
        cardNumber = input("Enter the new SIP card number, e.g. SIP12345: ")
    
    #The variables needed are added to a new list that is then appended to the customer list.
    row = [customerName, cardNumber, validFrom, validUntil]
    customers.append(row)
    
    print("New customer added successfully.")
    time.sleep(1)



#subroutine for adding a new store
def newStore():
    #Get data from user through inputs. .title() will force the first letter of each word to capitalise.
    storeName = input("Please Enter the name of your store: ").title()
    #Validation to ensure user does not leave the field blank. Displays an error message and then loops back to input.
    while (storeName == ""):
        print("ERROR! Cannot be blank!")
        storeName = input("Please Enter the name of your store: ").title()
    
    discountDay = input("Please enter the day you wish to offer 10% discount on purchases: ").title()
    #Validation to ensure user does not leave the field blank. Displays an error message and then loops back to input.
    while(discountDay == ""):
        print("ERROR! Cannot be blank!")
        discountDay = input("Please enter the day you wish to offer 10% discount on purchases: ").title()
    
    delivery = input("Will you be offering free deliveries to SIP members? Yes / No: ").title()
    #Validation to ensure user enters "Yes" or "No". Message then loops back to input.
    while (delivery == "" and delivery != "Yes" and delivery != "No"):
        print("ERROR! invalid input! Please Enter either Yes or No.")
        delivery = input("Will you be offering free deliveries to SIP members? Yes / No: ").title()
        
    products = input("Enter the product you will offer a 2 for 1 deal on: ").title()
    #Validation to ensure user does not leave the field blank. Displays an error message and then loops back to input.
    while (products == ""):
        print("ERROR! Cannot be blank!")
        products = input("Enter the product you will offer a 2 for 1 deal on: ").title()
    
    #Variables required are added to a new list which is then appended to the stores list.
    row = [storeName, discountDay, delivery, products]
    stores.append(row)
    
    print("New store added successfuly.")
    time.sleep(1)



#subroutine for adding a new transaction
def newTransaction():
    #Get data from user through inputs. .title() will force the first letter of each word to capitalise.
    name = input("Enter the name of the store: ").title()
    #Adds the store names in store list to a new list to be searched to find if store name entered by user already exists.
    storeList = []
    for row in stores:
        storeList.append(row[0])
    #If the store name is not in the list, then an error message is displayed and loops back to input.
    while name.title() not in storeList:
        print("ERROR. Cannot find store name.")
        name = input("Enter the name of the store: ").title()
    
    #This iteration takes the store name and searches the relevant index to see if they offer free delivery.
    for row in stores:
        #if they offer free delivery, then delivery costs 0.0.
        if name == row[0] and row[2] == "Yes":
            delivery = 0.0
            print("Customer recieves free delivery.")
            time.sleep(1)
        #if they do not offer free delivery, then delivery costs 2.00
        elif name == row[0] and row[2] == "No":
            delivery = 2.00
            print("Delivery is charged at £2.00")
            time.sleep(1)
    
    #fetches today's date.
    date = datetime.date.today()
    #Uses the date and returns the name of the weekday. E.g. Monday.
    day = calendar.day_name[date.weekday()]
    #this creates
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
