class BankAccount:
  def __init__(self, checking=0, savings=0):
    self._checking = checking
    self._savings = savings

  def get_checking(self):
    return self._checking
  
  def get_savings(self):
    return self._savings

  def set_checking(self, checking):
    self._checking = checking

  def set_savings(self, savings):
    self._savings = savings

my_account = BankAccount()
    
my_account.set_checking(523.48)
print(my_account.get_checking())

my_account.set_savings(386.15)
print(my_account.get_savings())
