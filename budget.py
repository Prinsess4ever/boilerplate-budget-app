
class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.money = 0

    def deposit(self, money, msg=None):
        self.money += money
        self.ledger.append({'description': msg or '', 'amount': money})
        return True

    def withdraw(self, money, msg=None):
        if not self.check_funds(money):
            return False

        self.money -= money
        self.ledger.append({'description': msg or '', 'amount': -money})
        return True

    def check_funds(self, money):
        return money <= self.money

    def transfer(self, money, other_category):
        return (
            self.withdraw(money, "Transfer to " + other_category.name)
            and other_category.deposit(money, "Transfer from " + self.name)
        )

    def get_balance(self):
        return self.money

    def __str__(self):
        resultaat = self.name.center(30, '*') + '\n'

        for lijn in self.ledger:
            description = lijn["description"]
            amount = lijn["amount"]

            if len(description) > 23:
                description = description[:23]

            resultaat += f"{description:<23}{amount:>7.2f}\n"

        resultaat += "Total: " + str(self.money)
        return resultaat


def create_spend_chart(categories):
    alle_totalen = []
    for category in categories:
        totaal = 0
        for ledger_entry in category.ledger:
            if ledger_entry['amount'] < 0:
                totaal += ledger_entry['amount']
        alle_totalen.append(totaal)

    totaal = sum(alle_totalen)
    perc1 = [100 * (cat1 / totaal) for cat1 in alle_totalen]
    lijst = []
    for i in perc1:
        if i % 10 != 0:
            aantal = i % 10
            LGG = 10 - aantal
            if i == aantal:
                i = 0.0
            elif aantal > 5:
                i += LGG
            elif aantal == 5:
                i += 5
            else:
                i -= aantal
        lijst.append(i)

    lengtes = []
    resultaat = "Percentage spent by category" + '\n'
    for aantal in range(100, -1, -10):
        result = f"{str(aantal):>3}|"
        for percent in lijst:
            if aantal <= percent:
                result += " o "
            else:
                result += "   "


        resultaat += result + ' \n'

    resultaat += "    ----------" + '\n'
    names = [category.name for category in categories]
    lengthe = len(names[0])
    lenthe = len(names[1])
    lentgte = len(names[2])
    lengtes.append(lenthe)
    lengtes.append(lengthe)
    lengtes.append(lentgte)
    for i in range(len(lengtes)):
        names[i] += '    ' * max(lengtes)

    for getal in range(max(lengtes)):
        resultaat += "     " + names[0][getal] + "  " + names[1][getal] + "  " + names[2][getal] +  "  " + '\n'
        getal += 1

    return resultaat[:-2] + ' '



