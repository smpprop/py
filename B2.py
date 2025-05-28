class BankAccount:
    def __init__(self):
        self.bal = 0

    def deposit(self, amt):
        if amt < 0:
            print("Invalid amount")
        else:
            self.bal += amt
            print(f"{amt} rupees is deposited")

    def withdraw(self, amt):
        if amt < 0:
            print("Enter a valid amount")
        elif self.bal < amt:
            print("Insufficient funds")
        else:
            self.bal -= amt
            print(f"{amt} rupees withdrawn")

    def getbalance(self):
        return self.bal


class SavingsAccount(BankAccount):
    def __init__(self):
        super().__init__()
        self.rate = 0

    def updateRate(self, rate):
        if rate < 0:
            print("Enter a valid rate")
        else:
            self.rate = rate
            print("Interest rate accepted")

    def compute(self):
        int_amt = (self.bal * self.rate // 100)
        self.bal += int_amt
        print(f"The interest rate is {self.rate}% and interest amount added is {int_amt}")
        return int_amt


MyAccount = SavingsAccount()
while True:
    print("\n1. Deposit\n2. Withdraw\n3. Get Balance\n4. Set Interest Rate\n5. Calculate Interest\n6. Exit")
    
    try:
        ch = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input, please enter a number.")
        continue

    if ch == 1:
        amt = int(input("Enter amount to deposit: "))
        MyAccount.deposit(amt)

    elif ch == 2:
        amt = int(input("Enter amount to withdraw: "))
        MyAccount.withdraw(amt)

    elif ch == 3:
        amt = MyAccount.getbalance()
        print(f"Available balance is {amt}")

    elif ch == 4:
        rate = float(input("Enter Interest Rate: "))
        MyAccount.updateRate(rate)

    elif ch == 5:
        MyAccount.compute()

    elif ch == 6:
        print("Exiting...")
        break

    else:
        print("Wrong choice. Please try again.")
  