#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


if __name__ == '__main__':
    a = tuple(map(int, input("Введите очки команд:\n").split()))
    if len(a) != 20:
        print("Неверный размер кортежа", file=sys.stderr)
        exit(1)

    k = 0
    for i in a:
        k = a.count(i)
        if k != 1:
            print("Очки повторяются", file=sys.stderr)
            exit(1)

    a = list(a)
    a.sort(reverse=True)
    a = tuple(a)

    n = int(input("Введите кол-во очков: "))
    p = a.index(n) + 1
    print(f"Команда заняла {p} место")
