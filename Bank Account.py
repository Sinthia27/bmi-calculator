class Bank_Account:
  def __init__(self, first_name, last_name, account_id, account_type, pin, balance):
    self.first_name = first_name
    self.last_name = last_name
    self.account_id = account_id
    self.account_type = account_type
    self.pin = pin
    self.balance = balance

  def deposit(self, amount):
    self.balance += amount
    return self.balance

  def withdraw(self, amount):
    self.balance -= amount
    return self.balance



  def display_balance(self):
      print(f"Your account balance is £{self.balance}")


toji = Bank_Account("Toji", "Fushiguro", 129489238, "Debit", 221202, 500.00)

toji.deposit(96)

toji.withdraw(25)

toji.display_balance()
