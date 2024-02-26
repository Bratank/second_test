import csv
"""в данной счасти кода я импортирую стандартную библиотеку csv и считываю файл с помощью DictReader он превращает txt файл в словарь"""
with open('space.txt', encoding='utf-8') as f:
    arr = list(csv.DictReader(f, delimiter='*'))

name_ship = input()

"""получаю первое значение и создаю бесконечный цикл, за счет которого могу постоянно считывать значения ,которые вводит пользователь"""
while name_ship != 'stop':
    for i in arr:
        if name_ship == i['ShipName']:
            print(
                f'Корабль {i['ShipName']} был отправлен с планеты: {i['planet']} и его направление движения было: {i['direction']}')
            break
    else:
        print('error.. er.. ror..')
    name_ship = input()
