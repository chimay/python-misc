#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__' :
    fibo = [0, 1]
    derniers = [0, 1]
    for entier in range(2,720) :
        fibo += [fibo[-1] + fibo[-2]]
        derniers += [fibo[-1] % 10]
    print(derniers[0:60])
    print(derniers[60:120])
    print(derniers[120:180])
    print(derniers[180:240])
    print(derniers[240:300])
    print(derniers[300:360])
    print(derniers[360:420])
    print(derniers[420:480])
    print(derniers[480:540])
    print(derniers[540:600])
    print(derniers[600:660])
    print(derniers[660:720])
