class ATM:
    def __init__(self):
        self.account_number=""
        self.account_holder_name=""
        self.account_balance=0

    def create_account(self):
        self.account_number=int(input("Enter Account Number:"))
        self.account_holder_name=input("Enter Account holder name;")
        self.account_balance=float(input("Enter the current account balance:"))

    def deposit(self):
        amount=float(input("Enter the amount to be deposited:"))
        self.account_balance+=amount
        print(amount,"Deposited successfully...")

    def withdraw(self):
        amount=float(input("Enter the amount to withdraw:"))
        if amount<=self.account_balance:
            self.account_balance -= amount
            print(amount, "Deposited successfully...")
        else:
            print("Insufficient balance...")

    def balance_enquiry(self):
        print("Current Account balance:",self.account_balance)

    def mini_statement(self):
