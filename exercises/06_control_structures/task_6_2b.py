# -*- coding: utf-8 -*-
"""
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт: Если адрес был введен неправильно, запросить адрес снова.

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'
Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

while True:
    ip = input("Введите IP-адрес: ")

    if ip.count('.') != 3:
        print('Неправильный IP-адрес')
    else:
        ip = ip.split('.')
        for elem in ip:
            if not elem.isdigit() or int(elem) < 0 or int(elem) > 255:
                print('Неправильный IP-адрес')
                break
        else:
            ip = [int(elem) for elem in ip]
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
            break
