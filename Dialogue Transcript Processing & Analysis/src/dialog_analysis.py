# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 15:35:11 2021

@author: samh4
"""

#%% IMPORTS
import pandas as pd
import sys             
import json

#%% ANALYSIS

filename = sys.argv[3]

data = pd.read_csv(filename,sep=',')

ocurrences = data['pony'].value_counts().nlargest(7).drop(labels=['Spike']) ## collect 7 largest speakers by occurrence, remove spike to get target 6

total = 0

ocur_dict = {}
perc_dict = {}

for index, value in ocurrences.items():
    total = total + value                  ## compute occurences (speaking count), add to dict
    ocur_dict[index] = value
    
for index, value in ocurrences.items():
    percent = 0
    percent = (value/total)             ## compute verbosity, add to dict
    perc_dict[index] = percent
    
final_dict = {
    "count": ocur_dict,          ## concetenate dictionaries
    "verbosity": perc_dict
    }

#%% OUTPUT

with open(sys.argv[2], 'w') as result: ## generate JSON file of verbosity and speaking count
    json.dump(final_dict, result)
    



    