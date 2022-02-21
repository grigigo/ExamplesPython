# -*- coding: utf-8 -*-
"""
Задание 6.2

Запросить у пользователя ввод IP-адреса в формате 10.0.1.1
В зависимости от типа адреса (описаны ниже), вывести на стандартный поток вывода:
   'unicast' - если первый байт в диапазоне 1-223
   'multicast' - если первый байт в диапазоне 224-239
   'local broadcast' - если IP-адрес равен 255.255.255.255
   'unassigned' - если IP-адрес равен 0.0.0.0
   'unused' - во всех остальных случаях

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

ip = [int(num) for num in input("Введите IP-адрес: ").split('.')]

if ip[0] >= 1 and ip[0] <= 223:
    print('unicast')
elif ip[0] >= 224 and ip[0] <= 239:
    print('multicast')
elif ip.count(255) == 4:
    print('local broadcast')
elif ip.count(0) == 4:
    print('unassigned')
else:
    print('unused')
