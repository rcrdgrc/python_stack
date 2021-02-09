from decimal import Decimal, ROUND_05UP, ROUND_HALF_UP

class BankAccount:
    def __init__(self, int_rate=.008, balance=0):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        return self

    def display_account_info(self):
        cents = Decimal('0.01')
        balance = Decimal(self.balance).quantize(cents, ROUND_HALF_UP)
        # print(f"Balance: ${balance}")
        return balance

    def yield_interest(self):
        if(self.balance > 0):
            self.balance = self.balance + (self.balance * self.int_rate)
        return self
      
class User:
    def __init__(self, name, email_address):  # now our method has 2 parameters!
        self.name = name			        # and we use the values passed in to set the name attribute
        self.email = email_address		    # and the email attribute
        self.account = BankAccount(int_rate=0.02, balance=0)
    # adding the deposit method
    def make_deposit(self, amount):  # takes an argument that is the amount of the deposit
        # the specific user's account increases by the amount of the value received
        self.account.deposit(amount)
        return self
    # make_withdrawal(self, amount) - have this method decrease the user's balance by the amount specified
    def make_withdrawal(self, amount): 
        self.account.withdraw(amount)
        return self
    # display_user_balance(self) - have this method print the user's name and account balance to the terminal
    # eg. "User: Guido van Rossum, Balance: $150c
    def display_user_balance(self): 
        print(f"User: {self.name}, {self.account.display_account_info()}")
        return self
    # BONUS: transfer_money(self, other_user, amount) - have this method decrease the 
    # user's balance by the amount and add that amount to other other_user's balance
    def transfer_money(self, other_user, amount): 
        self.account.withdraw(amount)
        other_user.account.deposit(amount)
        return self




guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")

monty.make_deposit(50).transfer_money(guido, 800).make_deposit(1000).display_user_balance()
guido.make_deposit(100).make_deposit(200).make_withdrawal(1000).display_user_balance()
# print(guido.name)  # output: Guido van Rossum
# print(guido.account_balance)	# output: 300
# print(monty.name)  # output: Monty Python
# print(monty.account_balance) # output: 50