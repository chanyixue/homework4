# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 08:40:23 2024

@author: Student
"""

import random


answer = random.randint(1, 100)

while True:
    guess = int(input("猜1到100之間的數字: "))
    
    if guess == answer:
        print("恭喜！你猜對了！")
        break
    elif guess < answer:
        print("猜的數字太低了，再試一次。")
    else:
        print("猜的數字太高了，再試一次。")
