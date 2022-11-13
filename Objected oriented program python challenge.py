class Account:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance
    
    def __str__(self):
        return f"Account owner {self.owner} \nAccount balance ${self.balance}"
    
    def deposit(self,amount):
        #avail_balance = self.balance
        if amount:
            self.balance += amount
            return f"Deposit accepted"
        
    
    def withdraw(self,amount):
        #avail_balance = self.balance
        if not amount <= self.balance:
            return f"Funds unavilable!"
        else:
            self.balance -= amount
            return f"Withdrawl accepted"
            
acct1 = Account('Joe',100)

acct1.owner

print(acct1)

acct1.deposit(50)

acct1.withdraw(160)