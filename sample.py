#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 23:35:39 2019

@author: dharmit
"""
import pandas as pd

# to avoid the warning messages
pd.options.mode.chained_assignment = None

# read the dataset into a pandas dataframe
df_female = pd.read_csv('creatinine-female-flattened.csv')
df_male = pd.read_csv('creatinine-male-flattened.csv')

total_rows = len(df_male)
print("total rows:",total_rows)
df_female_sampled = df_female.sample(n=total_rows, random_state=1)
print(df_female_sampled)

df_female_sampled.to_csv('creatinine-female-flattened-sampled.csv')

