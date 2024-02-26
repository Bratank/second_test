import csv

"""функция в которой я сортирую данные по номерам корабля"""
def sort(arr):
    for i in range(1, len(arr)):
        space_shatl = arr[i]
        a = int(space_shatl['ShipName'].split('-')[1])
        j = i - 1

        while j >= 0 and int(arr[j]['ShipName'].split('-')[1]) > a:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = space_shatl
    return arr

"""в данной счасти кода я импортирую стандартную библиотеку csv и считываю файл с помощью DictReader он превращает txt файл в словарь"""
with open('space.txt', encoding='utf-8') as f:
    arr = list(csv.DictReader(f, delimiter='*'))
#применяю сортировку и вывожу первые 10 значений
arr = sort(arr)
for i in range(10):
    print(arr[i]['ShipName'])
