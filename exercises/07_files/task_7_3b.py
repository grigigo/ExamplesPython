# -*- coding: utf-8 -*-
"""
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Переделать скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Пример работы скрипта:

Enter VLAN number: 10
10       0a1b.1c80.7000      Gi0/4
10       01ab.c5d0.70d0      Gi0/8

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

name_r = 'CAM_table.txt'

vlan = int(input('Введите номер влана: '))

file_r = open(name_r)

for line in file_r:
    if not 'Vlan' in line:
        pass
    else:
        file_r.readline()
        break

table = []
for line in file_r:
    line = line.split()
    line.pop(2)
    line[0] = int(line[0])
    table.append(line)

table.sort()

for elem in table:
    if elem[0] == vlan:
        print(f'{elem[0]:<8}{elem[1]:<18}{elem[2]:<8}')

file_r.close()
