#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 00:19:30 2019

@author: dharmit
"""

import pandas as pd

# to avoid the warning messages
pd.options.mode.chained_assignment = None

# read the dataset into a pandas dataframe
df_female_sampled = pd.read_csv('creatinine-female-flattened-sampled.csv')
df_male = pd.read_csv('creatinine-male-flattened.csv')

mean_female = df_female_sampled["s_creat"].mean()
mean_male = df_male["s_creat mg/dl"].mean()

print(mean_female)
print(mean_male)

mean_ratio = mean_male/mean_female
print(mean_ratio)

df_female_sampled.loc[:,"s_creat"] *= mean_ratio

print(df_female_sampled.head(10))

df_female_sampled.to_csv('creatinine-female-flattened-sampled-scaled.csv')