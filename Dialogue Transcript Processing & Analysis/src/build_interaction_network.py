# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 00:13:41 2021

@author: samh4
"""

#%% IMPORTS

import pandas as pd
import networkx as nx
import sys
import os
import json

#%% DATA  CLEANING & SETUP

output_dict = {}              ## initialize empty dict for output

in_file_path = sys.argv[2]
with open(os.path.join(os.path.dirname(__file__), in_file_path), 'r') as in_file:
    df = pd.read_csv(in_file,sep=',')    ## load raw data to df

df["pony"] = df["pony"].str.lower()   ## lowercase speaker names
substrings = ["others", "ponies", "and","all"]
df.loc[df['pony'].str.contains('|'.join(substrings)), 'pony'] = 'pass' ## replace non singular speakers with "pass" assignment
freq_chars = df['pony'].value_counts()[:101].index.tolist() ## list of most frequent characters
G = nx.Graph()   ## initialize network graph

#%% NETWORK BUILD

for row in range(len(df.index)):
   
    try:
        df.loc[row+1,'pony']
    except:                  ## break if no next speaker
        break
    
    if (df.loc[row,'pony'] == 'pass') or (df.loc[row+1,'pony'] == 'pass') or (df.loc[row,'pony'] == df.loc[row+1,'pony']) or (df.loc[row,'title'] != df.loc[row+1,'title']):
        continue       ## continue to next iteration if dialogue series invalid (through pass assignment)
    else:
        
        frequent = False
        for char in freq_chars:            
            if df.loc[row,'pony'] == char:  ## check if characters is frequent, break if not
                frequent = True
                break
            
        if frequent == True:            
            make_connect = False
            for char in freq_chars:
                if df.loc[row+1,'pony'] == char:  ## make connect if next speaker is also frequent
                    make_connect = True
                    break
            
            if make_connect == True:
                
                subject_id = str(df.loc[row,'pony'])
                object_id = str(df.loc[row+1,'pony'])  ## create IDs
                
                if G.has_edge(subject_id, object_id): 
                    G[subject_id][object_id]['weight'] += 1 ## add weight if edge exists
                else:
                    G.add_edge(subject_id, object_id, weight=1)  ## create edge else


#%% CREATE NETWORK JSON

for n in G.nodes():

    char_dict = {}
    
    for key in G[n]:  ## iterate through nodes, add weights+edges to dictionary
        char_dict[key] = G[n][key]['weight']
        
    output_dict[n] = char_dict

out_path = sys.argv[4]
with open(os.path.join(os.path.dirname(__file__), out_path), 'w') as result:
    json.dump(output_dict, result)  ## output JSON file
    
    