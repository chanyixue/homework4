# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 08:31:53 2024

@author: Student
"""


my_tuple = (1, 2, 3)


my_list = list(my_tuple)
my_list.extend([4, 5])


new_tuple = tuple(my_list)

print("新的tuple為", new_tuple)
