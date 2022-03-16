# -*- coding: utf-8 -*-
"""
Задание 12.1

Создать функцию ping_ip_addresses, которая проверяет пингуются ли IP-адреса.

Функция ожидает как аргумент список IP-адресов.

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для проверки доступности IP-адреса, используйте команду ping (запуск ping через subprocess).
IP-адрес считается доступным, если выполнение команды ping отработало с кодом 0 (returncode).
Нюансы: на Windows returncode может быть равен 0 не только, когда ping был успешен,
но для задания нужно проверять именно код. Это сделано для упрощения тестов.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

import subprocess

ips = ['192.168.3.1', '100.100.200.50', '192.168.54.3', '127.0.0.1', '8.8.8.8']


def ping_ip_addresses(ip_list):
    available = []
    unavailable = []

    for elem in ip_list:
        answer = subprocess.run(['ping', '-c', '3', '-n', elem], stdout=subprocess.DEVNULL)
        if answer.returncode == 0:
            available.append(elem)
        else:
            unavailable.append(elem)

    return tuple(available), tuple(unavailable)


result = ping_ip_addresses(ips)
print(f'Доступны: {result[0]}\nНедоступны: {result[1]}')
