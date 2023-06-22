'''
1ST PYTHON CLASS PROJECT
For this assignment, the auto store needs an application that will process mail order sales of repair parts. Parts are sold throughout Uganda. 
The application user will take information from customers by telephone and the application will compute the appropriate output information. 
Develop an interactive program in Python using dynamic functions. A separate order is processed for each part ordered. 
Customer information Customer Identification (Customer ID:), Name, and Town Code need be entered. 
There are two types of customers: Retail and Wholesale. 

If the customer is a retail customer, this is indicated by enter ‘ret’, while wholesale customers is ‘who’ Part ordered 
Partner number, description, price per part, quantity, oversize order status Shipping details (the output of the system)
Cost, sales tax, shipping and handling cost, total Application Use and Special Instructions Cost. 
This is simply the price times the quantity rounded to the nearest penny. All quantities are integer values.
Sales Tax. The application user enters customer and part ordered information. If  the firm is located within Kampala. 
Kampala retail customers (Town code = “KLA”) are charged a sales tax on purchases – the Kampala tax rate is 10%. 
Retail customers from Entebbe (Town code = “EBB”) and Mbarara (town code = “MBR”) are also taxed at a 5% tax rate. 
Retail customers from all other towns do not pay sales tax. Wholesale customers do not pay sales tax regardless of their town code.


Shipping Cost
The cost of shipping is based on the quantity of the shipment and the shipping method selected as indicated in the table given below. 
The distance for shipment does not matter. Shipping Charge	UPS	U.S PostalAir	Fed Ex Ground	Fed Ex Overnight
Charge per part	$7.00	$8.50	. $9.25	$12.00

Total. The Total is equal to the Cost + Sales Tax + Shipping & Handling. (write this to the txt file)
Use the following visual of the solution

This Assignment is individual.
Good Luck
By Ozzy

'''
####  Simple summary of whats required to do
##   input (Customer ID, Name, TownCode(KLA,EBB,MBR else No), Customer Type (retail'Ret', wholesale'who'), 
##   Order Parts (Partner Number description, price per part, quantity, Shipping Details())

##  Auto Print Output
##  print (Shipping Details(Cost, sales Tax, shipping  and handling costs, 
##  Cost(price * quantity')
##  Sales Tax (if KLA 10%, EBB and MBR 5% else 0%)
##  Shipping cost  (if UPS 7%, US Postal Air 8.5%, Fedx 9.25%, Fedx Overnight 12%)
##  Total =(cost + Sales Tax + Shipping) save to a txt file

########## START OF MY PROJECT DEVELOPMENT PROCESS ###############

class Customer:
    def __init__(self):
        # declaring of customer variables in constructor
        print("####### ENTER CUSTOMER DETAILS BELOW #######")
        self.customerID = input("Enter Customer Number : ")
        self.customerNames = input("Enter Customer Names : " )
        self.customerCode = input("Enter Customer Region (KLA, EBB, MBR) : " )
        self.customerType = input("Enter Customer Type : " )
        print("---------------------------------------")

    # part_order_details method to recieve auto part details
    def part_order_details(self):
        # Autoparts Order details input
        print("#### ENTER CUSTOMER AUTOPART DETAILS ####")
        self.partNo = input("Enter Autopart Number : " )
        self.partDesc = input("Enter Autopart Description : " )
        self.partPrice = int(input("Enter Autopart Price : " ))
        self.partQty = int(input("Enter Autopart Quantity : " ))
        self.shippingType = input("Enter Shipping Type (UPS, AIR, FedExG, FedExO): " )
        print("---------------------------------------")

    # Total cost method calculating cost using autopart price and quantity   
    def total_cost(self): 
        totalCost = round(self.partPrice * self.partQty) #rounding my cost value after multiplying price and Qty
        return totalCost # returning totalcost variable from total_cost function
    
    # sales tax method definition
    def sales_tax(self):
        # Sales Tax (if KLA 10%, (EBB or MBR) 5% else 0%)
        if self.customerCode == 'KLA':
            sales_tax = (self.total_cost() * (10/100) )
            # sales_tax = ( (10/100) OR 10% )
        elif self.customerCode == 'EBB' or self.customerCode == 'MBR':
            sales_tax = (self.total_cost() * (5/100))
        else:
            sales_tax = (0)
        return sales_tax
        # (self.salesTax() * Customer.total_cost() )    

    # customer cost and sales method definition    
    def customer_total_cost_and_sales_tax(self):
        totalCost = self.total_cost()
        salesTax= self.sales_tax()
        customerTotalSales = (totalCost + salesTax)
        return customerTotalSales
    
    # Shipping costs
    def customer_shipping_costs(self):
        # Shipping cost  (if UPS $7, if (US PostalAir $8.5), elif (Fedx $9.25), elif (Fedx Overnight $12))
        # self.shippingType = input("Enter Shipping Type (UPS): " )
        customerQty = self.partQty
        if self.shippingType == 'UPS':
            shippingCharge = (customerQty * 7)
        elif self.shippingType == 'AIR':
            shippingCharge = (customerQty * 8.5)
        elif self.shippingType == 'FedExG':
            shippingCharge = (customerQty * 9.25)
        elif self.shippingType == 'FedExO':
            shippingCharge = (customerQty * 12)
        else:
            shippingCharge = (0)
        return shippingCharge

    # total cost for my customer
    def customer_over_all_cost(self):
        #  Total. The Total is equal to the Cost + Sales Tax + Shipping & Handling. (write this to the txt file)
        #  Total =(cost + Sales Tax + Shipping) save to a txt file   
        customercosts1 = self.customer_total_cost_and_sales_tax()
        # customercosts2 = self.customerShippingCosts()
        totalCustomerCosts = customercosts1 + self.customer_shipping_costs()
        return totalCustomerCosts


    # Total =(cost + Sales Tax + Shipping) save to a txt file C:/Users/dell/Desktop/
    def save_customer_cost_file(self):
            my_receipt =  open("C:/users/dell/Desktop/myreceipt.txt", 'w')
            my_receipt.write("#### KITEMAGGWA SHAFIC PYTHON ASSIGNMENT  ####")   
            my_receipt.write("#### CUSTOMER ORDER RECEIPT DETAILS  ####")   
            my_receipt.write("\n\nCUSTOMER NAMES :        " + str(self.customerNames) )   
            my_receipt.write("\nCUSTOMER AUTOPARTS COST : " + str(self.total_cost()) )   
            my_receipt.write("\nCUSTOMER SALES TAX :      " + str(self.customer_total_cost_and_sales_tax()) )   
            my_receipt.write("\nCUSTOMER SHIPPING COSTS : " + str(self.customer_shipping_costs()) )   
            my_receipt.write("\n------------------------------------" )   
            my_receipt.write("\nCUSTOMER TOTAL COSTS :    " + str(self.customer_over_all_cost()) )
            my_receipt.write("\n------------------------------------" )    

    def show_my_customers_details(self):
        print("####### SUMMARY OF CUSTOMER ORDER DETAILS #######")
        print("My Customer ID: ", self.customerID)  
        print("My Customer Name: ", self.customerNames)    
        print("My Customer Type: ", self.customerType)    
        print("Customer Autopart Number: ", self.partNo)    
        print("Customer Autopart Price: ", self.partPrice)    
        print("Customer Autopart Quantity: ", self.partQty)
        print("Shipping Type Selected: ", self.shippingType)
        print("Customer Sales tax : ", self.sales_tax())
        print("---------------------------------------")    
        print("Customer Total Sales Cost is : ", self.customer_total_cost_and_sales_tax())
        print("Customer Shipping costs :      ", self.customer_shipping_costs())
        print("---------------------------------------")    
        print("Customer Total Payout Costs :  ", self.customer_over_all_cost(),'/=')
        print("---------------------------------------")  
        print("---------------------------------------")  

def all_customer_full_data_details():
    
    for customer1 in range(2):
        customer1 = Customer()
        customer1.part_order_details()
        customer1.customer_over_all_cost()
        customer1.save_customer_cost_file()
        customer1.show_my_customers_details()      
        addAnotherCustomer = input("Enter Y to Add New Customer : " )
        if addAnotherCustomer != "Y":
            break
        else:
            print(customer1)  
# Calling the function to display all the detailssaved for a customer 
all_customer_full_data_details()


