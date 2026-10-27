# MULTIPLE INHERITANCE
#
# ONLINE SHOPPING
#
# Customer:
#     name,mob,address,email
# Product:
#     prod_name,price,description
# Order(Customer,Product)
#     order_id,quantity,total price,order date

class Customer:
    def __init__(self):
        self.customer_name=""
        self.mob_no=""
        self.address=""
        self.email=""
    def customer_data(self):
        self.customer_name=input("Enter customer name:")
        self.mob_no=input("Enter mobile number:")
        self.address=input("Enter the address:")
        self.email=input("Enter email id:")
    def customer_info(self):
        print("\n=====CUSTOMER DETAILS=====")
        print("Customer name:",self.customer_name)
        print("Mobile number:",self.mob_no)
        print("Address:",self.address)
        print("Email ID:",self.email)

class Product:
    def __init__(self):
        self.product_name=""
        self.price=""
        self.description=""
    def product_data(self):
        self.product_name=input("Enter Product name:")
        self.price=input(input("Enter the price:"))
        self.description=input("Enter product description")
    def product_info(self):
        print("\n=====PRODUCT DETAILS=====")
        print("Product name:",self.product_name)
        print("Product price:",self.price)
        print("Product description:",self.description)

class Order(Customer,Product):
    def __init__(self):
        self.order_id=""
        self.quantity=""
        self.total=""
        self.price=""
        self.order_date=""
    def order_data(self):
        self.order_id=int(input("Enter order id:"))
        self.quantity=int(input("Enter the quantity:"))
        self.total=input("Enter the total:")
        self.price=int(input("Enter the price:"))
        self.order_date=input("Enter order date:")
    def order_info(self):
        print("\n=====ORDER DETAILS=====")
        print("Order_id:",self.order_id)
        print("Quantity:",self.quantity)
        print("Total:",self.total)
        print("Price:",self.price)
        print("Order date:",self.order_date)

obj=Order()
obj.customer_data()