# -*- coding: utf-8 -*-
"""
Created on Fri May 25 07:03:32 2018

@author: CB1118
"""
import pandas as pd
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

df = pd.read_csv("chicago2.csv")
pd.set_option('display.width',200)
total_rows = df.shape[0]
print(total_rows)

def show_raw_data(df, increment, total_rows):

    st_row = 0
    end_row = st_row + increment
    continue_ = "Z"
    view_raw = input("Would you like to see a few rows of raw data? (Y/N): ")
    if view_raw.upper() == "Y":
        x = input("\nFor readability it is preferable to use a wide viewing window.  Press <Enter> to continue...")
        while continue_.upper() != "X":
            
            if st_row == 0:
                valid_answers = ["N","X"]
                show_data_msg = "At start of File.  Enter (N)ext for next set of rows or e(X)it to quit "
            elif st_row + increment > total_rows-1:
                valid_answers = ["P","X"]
                show_data_msg = "EOF reached.  Enter (P)revious for previous rows or e(X)it to quit "
            else:
                valid_answers = ["N","P","X"]
                show_data_msg = "Enter (N)ext for next set of rows, (P)revious for previous rows or e(X)it to quit " 

            print(df[st_row:end_row])

            #make sure continue_ is not a valid answwer to avoid endless loop
            continue_ = "Z"
            
            while continue_.upper() not in valid_answers:
                continue_ = input(show_data_msg)

            if continue_.upper() == "N":
                st_row += increment
                if end_row + increment > total_rows -1:
                    end_row = total_rows 
                else:
                    end_row = st_row + increment
            if continue_.upper() == "P" and st_row > 0:
                st_row -= increment
                end_row = st_row + increment
                
show_raw_data(df, 12, total_rows)
