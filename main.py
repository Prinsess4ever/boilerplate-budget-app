# This entrypoint file to be used in development. Start by reading README.md
import sys

import budget
from budget import create_spend_chart
from unittest import main

food = budget.Category("Food")




food.deposit(1000, "initial deposit")

food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")

clothing = budget.Category("Kleren")
food.transfer(25.55, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
print(food.get_balance())

print('''
----------------------------------------------------
        # *************Food*************
        # initial deposit        1000.00
        # groceries               -10.15
        # restaurant and more foo -15.89
        # Transfer to Clothing    -50.00
        # Total: 923.96
''')
sys.exit(678)
#auto = budget.Category("Auto")
#auto.deposit(1000, "initial deposit")
#auto.withdraw(15)
#
# print(food)
# print(clothing)
#
# print(create_spend_chart([food, clothing, auto]))

# Run unit tests automatically
main(module='test_module', exit=False)