#!/bin/python3

import math
import os
import random
import re
import sys

# The function accepts INTEGER n as parameter.

def fizzBuzz(n):

     for i in range(1,n+1):
        if i%3 ==0 and i%5 ==0:
            print("FizzBuzz")
        elif i%3 == 0 and  i%5 !=0:
            print("Fizz")
        elif i%5 == 0 and  i%3 != 0:
            print("Buzz")
        else:
            print(i)
n = int(input())
fizzBuzz(n)
