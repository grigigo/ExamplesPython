# -*- coding: utf-8 -*-
"""
Задание 9.3a

Сделать копию функции get_int_vlan_map из задания 9.3.

Дополнить функцию: добавить поддержку конфигурации, когда настройка access-порта
выглядит так:
    interface FastEthernet0/20
        switchport mode access
        duplex auto

То есть, порт находится в VLAN 1

В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
Пример словаря:
    {'FastEthernet0/12': 10,
     'FastEthernet0/14': 11,
     'FastEthernet0/20': 1 }

У функции должен быть один параметр config_filename, который ожидает
как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw2.txt

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""


def get_int_vlan_map(config_filename):
    file = open(config_filename)
    result = {}
    for line in file:
        if 'FastEthernet' in line:
            list = []
            interface = line.split()[-1]
            while not '!' in line:
                line = file.readline()[:-1]
                if not '!' in line:
                    list.append(line[1:])
            mode = 'access' if list[0].split()[-1] == 'access' else 'trunk'
            print(list)
            print(mode)
            if mode == 'access':    # access позволяет пропускать через себя 1 vlan
                if 'duplex auto' in list:
                    vlan = 1
                else:
                    vlan = int(list[1].split()[-1])
                result[interface] = vlan
            if mode == 'trunk':
                vlans = [int(x) for x in list[1].split()[-1].split(',')]
                if 'duplex auto' in list:
                    vlans.append(1)
                result[interface] = vlans

    file.close()
    return result


config_filename = 'config_sw2.txt'
result = get_int_vlan_map(config_filename)
print(result)