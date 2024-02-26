import csv
from itertools import *


def login(person):
    return f'{person.split()[0]}_{person.split()[1][0]}{person.split()[2][0]}'


def password():
    passwords = set()
    for password in permutations('asdfQWEgjhkmFGHJKLnbvc0123456789', 10):
        password = ''.join(password)
        if any(letter in 'QWEFGHJKL' for letter in password) and \
                any(letter in '0123456789' for letter in password) and \
                any(letter in 'asdfgjhkmnbvc' for letter in password):
            passwords.add(password)
        if len(passwords) == 3000:
            return list(passwords)


passwords = password()
f = open('scientist.txt')
scientists = []
for person in f:
    scientists.append(person.split('#'))
scientists = scientists[1:]
for person in scientists:
    person.append(login(person[0]))
    person.append(passwords.pop())

with open('scientist_password.csv','w',encoding='utf8',newline='') as file:
    w = csv.writer(file)
    w.writerow(['ScientistName','preparation','date','components','login','password'])
    w.writerows(scientists)