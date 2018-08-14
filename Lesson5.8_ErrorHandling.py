# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 19:12:12 2018

@author: CB1118
"""

def create_groups(items, n):
    try:
        size = len(items) // n  # this line could cause a ZeroDivisionError exception
    except ZeroDivisionError:
        print("WARNING: Returning empty list. Please use a nonzero number.")
        return[]
    else:
        groups = []
        for i in range(0, len(items), size):
            groups.append(items[i:i + size])
        return groups
    finally:
        # print the number of groups and return groups    
        print("{} groups returned.".format(n))

print("Creating 6 groups...")
for group in create_groups(range(32), 6):
    print(list(group))

print("\nCreating 0 groups...")
for group in create_groups(range(32), 0):
    print(list(group))