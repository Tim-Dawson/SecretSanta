import random
from prettytable import PrettyTable

x = PrettyTable()

x.field_names = ['Giver', 'Receiver']


person = ['Jo', 'Jason', 'Laura', 'Nick', 'Jenny', 'Lynne', 'Ivor', 'Tim', 'Michelle']
couples = [['Tim', 'Michelle'], ['Lynne', 'Ivor'], ['Jo', 'Jason'], ['Nick', 'Jenny']]

received = []


def is_couple(a, b):
    couple = False
    for pair in couples:
        if a in pair and b in pair:
            print(a + " " + b + " COUPLE")
            couple = True
    return couple

for family_member in person:
    give_to = random.choice(person)

    while family_member == give_to or is_couple(family_member, give_to) or give_to in received:
        give_to = random.choice(person)

    x.add_row([family_member, give_to])
    received.append(give_to)


print(x)
