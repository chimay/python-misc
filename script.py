#!/usr/bin/env python

import sys
import time

def table(nombre=1, max=10) :
    base = float(nombre)
    max = int(max)
    for num in range(1, max+1) :
        print(base*num)
        time.sleep(1)

table(*sys.argv[1:])
