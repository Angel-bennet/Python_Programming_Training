class BankAccount:
    #Constructor-will execute only once
    def __init__(self,balance,name):
        self.name=name
        self.__balance=balance   #private-__
    #getters
    def get_balance(self):
        return self.__balance
    #setters
    def set_balance(self,amount):
        if amount>0:
            self.__balance+=amount
        else:
            print("invalid balance amount")
acc=BankAccount(500,'Angel')
print(acc.get_balance())
acc.set_balance(500)
print("Total after setting balance",acc.get_balance())