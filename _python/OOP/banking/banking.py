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
        print(f"Balance: ${balance}")
        return self

    def yield_interest(self):
        if(self.balance > 0):
            self.balance = self.balance + (self.balance * self.int_rate)
        return self


acct1 = BankAccount()
acct2 = BankAccount()

acct1.deposit(100).deposit(20).deposit(30).withdraw(10).yield_interest().display_account_info()
acct2.deposit(100).deposit(20).withdraw(30).withdraw(5).withdraw(38).withdraw(20).yield_interest().display_account_info()

# monty.make_deposit(50).transfer_money(guido, 800).make_deposit(1000).display_user_balance()
# guido.make_deposit(100).make_deposit(200).make_withdrawal(1000).display_user_balance()