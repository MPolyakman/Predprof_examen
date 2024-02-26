f = open('scientist.txt')
scientists = []
for person in f:
    scientists.append(person.split('#'))
aloporinol = []
for person in scientists[1:]:
    if person[1] == 'Аллопуринол':
        aloporinol.append(person[2])
original = sorted(aloporinol)
thiefs = []
for person in scientists[1:]:
    if person[1] == 'Аллопуринол' and person[2] != aloporinol[0]:
        thiefs.append([person[2],person[0]])
for person in sorted(thiefs):
    print(f'Разработчиками Аллопуринола были такие люди:{person[1]} - {person[0]}')
for person in scientists:
    if person[1] == 'Аллопуринол' and person[2] == aloporinol[0]:
        print(f'Оригинальный рецепт принадлежит:{person[0]}')
newlist = []
for person in scientists:
    if person[0] in thiefs and person[1] == 'Аллопуринол':
        scientists.remove(person)
    else:
        day = [person[2]]
        day.extend(person)
        newlist.append(day)
newlist = sorted(newlist[1:])
for person in newlist:
    print(person[1:])
