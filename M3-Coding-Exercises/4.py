# DO NOT ALTER THIS CODE
import sys
strings = [l.split(",") for l in sys.argv[1].split("*")]
accounts = [[int(n) for n in s] for s in strings]

class Bank:
  def __init__(self, name, customers, accounts):
    self.name = name
    self.customers = customers
    self.accounts = accounts
    
  def branch_total(self, accounts):
    total = 0
    for account in accounts:
      total += account
    return total

# Write your code here
class RegionalBank(Bank):
  def regional_total(self):
    total = 0
    for account in accounts:
      total += self.branch_total(account)
    return total
  
my_bank = RegionalBank("Bank of America", 9, accounts)
print(my_bank.regional_total())
