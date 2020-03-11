# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 12:22:24 2020

@author: 
"""
import pandas as pd
import numpy as np

collatz_series = []
int_series = []
global data

def collatz_sequence(x):
    num_seq = [x]
    if x < 1:
       return []
    while x > 1:
       if x % 2 == 0:
         x = x / 2
       else:
         x = 3 * x + 1
    # Added line
       num_seq.append(int(x))    
    return num_seq

def collatz_training_data():

    
    randnums= np.random.randint(1,100000,10000)
    for i in randnums : 
        int_series.append(i)
        collatz_series.append(collatz_sequence(i))
    collatz_dict = dict(zip(int_series,collatz_series))
    
    
    df = pd.DataFrame.from_dict(collatz_dict, orient='index')
    df.transpose()
    print(df)
    #df.to_csv(r'training_set.csv', index = True)

collatz_training_data()

