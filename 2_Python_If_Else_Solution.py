#!/bin/python

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(raw_input().strip())

if n%2 == 1:
    print("Weird")
elif 1<n<6:
    print("Not Weird")
elif 5<n<21:
    print("Weird")
elif 20<n<101:
    print("Not Weird")
else:
    print("hatali giris")

