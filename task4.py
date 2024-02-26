import csv

"""в данной счасти кода я импортирую стандартную библиотеку csv и считываю файл с помощью DictReader он превращает txt файл в словарь"""
with open('space.txt', encoding='utf-8') as f:
    arr = list(csv.DictReader(f, delimiter='*'))

"""создаю отдельную функцию для генерации паролей"""


def generate_password(elem):
    tri_last_planet = elem['planet'][-3:]
    dve_centr_corabl = elem['ShipName'][1:3][::-1]
    tri_first_planet = elem['planet'][:3][::-1]
    password = tri_last_planet + dve_centr_corabl + tri_first_planet
    return password


"""создаю новый столбец в словаре под названием password"""
for i in arr:
    i['password'] = generate_password(i)

"""сохраняю полученный файл"""
with open('space_uniq_password.csv', 'w', newline='', encoding='utf-8') as f:
    w = csv.writer(f)
    w.writerow(['ShipName', 'planet', 'coord_place', 'direction', 'password'])
    w.writerow(arr)
