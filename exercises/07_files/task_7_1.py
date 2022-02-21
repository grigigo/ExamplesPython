# -*- coding: utf-8 -*-
"""
Задание 7.1

Обработать строки из файла ospf.txt и вывести информацию по каждой строке в таком
виде на стандартный поток вывода:

Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

file = open('ospf.txt')

for elem in file:
    elem = elem.translate(elem.maketrans(',[]', '   ')).split()
    elem = elem[1:3] + elem[4:7]

    print(f'''
    Prefix                {elem[0]}
    AD/Metric             {elem[1]}
    Next-Hop              {elem[2]}
    Last update           {elem[3]}
    Outbound Interface    {elem[4]}''')

file.close()
