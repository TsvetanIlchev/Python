import datetime
import pytz

class Account:

    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, balance):
        self._name = name
        self._balance = balance
        self._transaction_list = []
        print("Account created for " + self._name)
        print("Account was opened at {0} local time with amount: {1}".format(Account._current_time(), balance))

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            self.show_balance()
            self._transaction_list.append((Account._current_time(), amount))

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            self._transaction_list.append((Account._current_time(), -amount))
        else:
            print("Amount must be greater than zero and no more then your account balance")
        self.show_balance()


    def show_balance(self):
        print("Balance is {}".format(self._balance))

    def show_transactions(self):
        for date, amount in self._transaction_list:
            if amount > 0:
                transaction_type = "deposited"
            else:
                transaction_type = "withdraw"
                amount *= -1
            print("{:6} {} on {} (local time was {})".format(amount, transaction_type, date, date.astimezone()))

if __name__ == '__main__':
    tim = Account("Tim", 0)
    tim.show_balance()

    tim.deposit(1000)
    # tim.show_balance()
    tim.withdraw(500)
    # tim.show_balance()

    tim.withdraw(2000)

    tim.show_transactions()

    steph = Account("Steph", 800)
    steph.deposit(100)
    steph.withdraw(200)
    steph.show_transactions()

