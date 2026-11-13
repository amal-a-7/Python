

Skip to content
Using Gmail with screen readers
Conversations
Get started with Gmail
Customize your inbox
Change profile image
Import contacts and mail
Get Gmail for mobile
     
0% of 15 GB used
Terms · Privacy · Program Policies
Last account activity: 2 days ago
Details
bank.py

class Bank:
    def __init__(self):
        self.accno = int(input("Enter the account number: "))
        self.accname = input("Enter the account name: ")
        self.acctype = input("Enter the account type: ")
        self.balance = 0

    def deposit(self):
        amount = int(input("Enter the deposit amount: "))
        self.balance = self.balance + amount
        print("\nAmount Deposited:", amount)

    def withdraw(self):
        amount = int(input("Enter amount to be withdrawn: "))
        if self.balance >= amount:
            self.balance = self.balance - amount
            print("\nAmount withdrawn is:", amount)
        else:
            print("\nInsufficient Balance")
            print("Current balance is:", self.balance)

    def display(self):
        print("Net Available balance =", self.balance)


B_Aobj = Bank()

while True:
    print("\n1. Deposit \n2. Withdraw \n3. View Balance \n4. Exit")
    ch = int(input("Enter your choice: "))
    
    if ch == 1:
        B_Aobj.deposit()
        B_Aobj.display()
    elif ch == 2:
        B_Aobj.withdraw()
        B_Aobj.display()
    elif ch == 3:
        B_Aobj.display()
    else:
        exit(0)

Displaying bank.py.
