# -*- coding: utf-8 -*-
"""
@author: samh4
"""

#%% IMPORTS

import sys
import json
import math
import os

#%% COMPUTE TF-IDF

output_dict = {}
tfidf_dict = {}
ponies = []

path = sys.argv[2]

with open(os.path.join(os.path.dirname(__file__), path), 'r') as in_file:
      
    pony_counts = json.load(in_file)
    num_ponies = 0
    
    for count in pony_counts:
        num_ponies = num_ponies + 1  ## count characters
    
    for pony in pony_counts:
        
        ponies.append(pony)    ## append to list of characters
        word_scores = {}
        
        for word in pony_counts[pony]:
            
            tf = pony_counts[pony][word]  ## calculate tf
            pony_list = []
            
            for i in pony_counts:
                for j in pony_counts[i]:
                    if word == j:
                        pony_list.append(i)
                        break
                    
            num_ponies_use = len(pony_list)
            idf = math.log(num_ponies/num_ponies_use) ## calculate idf
            tfidf = tf * idf ## compute tf-idf
            
            word_scores[word] = tfidf
        
        tfidf_dict[pony] = word_scores   ## dict of tf-idf

n = int(sys.argv[4])

#%% DICT OUTPUT TO COMMAND LINE

for key in ponies:
    output_dict[key] = sorted(tfidf_dict[key], key=tfidf_dict[key].get, reverse=True)[:n]

print(output_dict)

          
     