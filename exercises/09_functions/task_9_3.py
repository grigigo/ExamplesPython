# -*- coding: utf-8 -*-
"""
Задание 9.3

Создать функцию get_int_vlan_map, которая обрабатывает конфигурационный
файл коммутатора и возвращает кортеж из двух словарей:
* словарь портов в режиме access, где ключи номера портов,
  а значения access VLAN (числа):
{'FastEthernet0/12': 10,
 'FastEthernet0/14': 11,
 'FastEthernet0/16': 17}

* словарь портов в режиме trunk, где ключи номера портов,
  а значения список разрешенных VLAN (список чисел):
{'FastEthernet0/1': [10, 20],
 'FastEthernet0/2': [11, 30],
 'FastEthernet0/4': [17]}

У функции должен быть один параметр config_filename, который ожидает как аргумент
имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""


def get_int_vlan_map(config_filename):
    file = open(config_filename)
    result = {}
    for line in file:
        if 'FastEthernet' in line:
            interface = line.split()[1]
            line = file.readline().split()[-1]
            if line == 'access':
                vlan = file.readline().split()[-1]
                result[interface] = vlan
            if line == 'dot1q':
                result[interface] = file.readline().split()[-1].split(',')

    file.close()
    return result


config_filename = 'config_sw1.txt'
result = get_int_vlan_map(config_filename)
print(result)
