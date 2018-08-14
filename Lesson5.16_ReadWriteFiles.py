# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 19:37:41 2018

@author: CB1118
"""

def dump_file_content(f_name):
    with open(f_name,"r") as f:
        print(f.read())

dump_file_content("some_file.txt")

f = open("some_file.txt","a")
f.write("\nGood Bye!")
f.close()

dump_file_content("some_file.txt")

f = open("some_file.txt","w")
f.write("Everything is gone!")
f.close()

dump_file_content("some_file.txt")
