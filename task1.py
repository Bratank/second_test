import csv
"""в данной счасти кода я импортирую стандартную библиотеку csv и считываю файл с помощью DictReader он превращает txt файл в словарь
"""
with open('space.txt', encoding='utf-8') as f:
    arr = list(csv.DictReader(f, delimiter='*'))

"""в центральной части кода я проверяю на наличие координат и если координаты отсутствуют задаю значения x и y за счет формул"""
for i in arr:
    if i['coord_place'] == '0 0':
        n = int(i['ShipName'].split('-')[1][0])
        m = int(i['ShipName'].split('-')[1][1])
        if n > 5:
            x = n + int(i['coord_place'].split(' ')[0])
        elif n <= 5:
            x = -(n + int(i['coord_place'].split(' ')[0])) * 4 + len(i['planet'])
        if m > 3:
            y = m + len(i['planet']) + int(i['coord_place'].split(' ')[1])
        if m <= 3:
            y = -(n + int(i['coord_place'].split(' ')[1])) * m
        i['coord_place'] = f'{x} {y}'
    if i['ShipName'][3] == 'V':
        print(f'{i['ShipName']} - ({x}, {y})')

"""после сохраняю полученный список в файл"""
with open('space_new.txt', 'w', newline='', encoding='utf-8') as f:
    w = csv.writer(f)
    w.writerow(['ShipName', 'planet', 'coord_place', 'direction'])
    w.writerow(arr)
