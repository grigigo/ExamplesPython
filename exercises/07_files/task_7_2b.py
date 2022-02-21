# -*- coding: utf-8 -*-
"""
Задание 7.2b

Переделать скрипт из задания 7.2a: вместо вывода на стандартный поток вывода,
скрипт должен записать полученные строки в файл

Имена файлов нужно передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore
и строки, которые начинаются на '!'.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ignore = ["duplex", "alias", "configuration"]

name_read = 'config_sw1.txt'
name_write = 'config_write.txt'
file_r = open(name_read)
file_w = open(name_write, 'w')

for elem in file_r:
    flag = True
    if elem.count('!'):
        flag = False
    for ign in ignore:
        if ign in elem:
            flag = False
    if flag:
        file_w.write(elem)

file_r.close()
file_w.close()
