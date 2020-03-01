#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 16:11:41 2019

@author: dharmit
"""

import matplotlib.pyplot as plt

import pandas as pd

# to avoid the warning messages
pd.options.mode.chained_assignment = None

# read the dataset into a pandas dataframe
df = pd.read_csv('creatinine-female.csv')

#print(df)

#df_female=df[:36]
#print(df_female)

df1 = pd.read_csv('creatinine-male.csv')

#print(df1)

#df_male=df1[:48]
#print(df_male)

#sum_no_of_males = df_male["# of male"].sum()
#sum_no_of_females = df_female["# of female"].sum()
                         
#df_female_scaled["# of female scaled"] = (df_female["# of female"])*sum_no_of_males/sum_no_of_females
#print(df_female_scaled)                              
#print(df_female_scaled.sum())                              

#pd.melt(df, id_vars='s_creat mg/dl', value_vars=[1])

#df.loc[df.index.repeat(df["# of female"])]
df['# of female'] = df['# of female'].fillna(0.0).astype(int)  
#test = pd.DataFrame({
#    'id' : df["s_creat"],
#    'times' : df["# of female"]
#    })                        
                        
#print(test)                          
#test1=test.loc[test.index.repeat(test.times)].reset_index(drop=True)
#print(test1)

test2=df.loc[df.index.repeat(df["# of female"])].reset_index(drop=True)
print(test2)

test2.to_csv('creatinine-female-flattened.csv')

df1['# of male'] = df1['# of male'].fillna(0.0).astype(int)
test3=df1.loc[df1.index.repeat(df1["# of male"])].reset_index(drop=True)
print(test3)

test3.to_csv('creatinine-male-flattened.csv')