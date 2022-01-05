# -*- coding: utf-8 -*-
"""
@author: samh4
"""
#%% IMPORTS

import networkx as nx
import sys
import os
import json


#%% CREATE NETWORK GRAPH FROM JSON

in_path = sys.argv[2]
G = nx.Graph()          ## collect input file, initialize graph, create empty output dict
output_dict = {}

with open(os.path.join(os.path.dirname(__file__), in_path), 'r') as in_file: ## open file
      
    network = json.load(in_file)   ## load json
      
    for pony in network:
        
        subject_id = pony
        
        for interaction in network[pony]:
            
            object_id = interaction
            weight_val = network[pony][interaction]  ## collect weight value
            
            if G.has_edge(subject_id, object_id):  ## break if edge exists
                break
            else:
                G.add_edge(subject_id, object_id, weight=weight_val)   ## add edge else, set weight and two objects

#%% COMPUTE STATS

temp_lst = []
for i in sorted(G.degree, key=lambda x: x[1], reverse=True)[0:3]:
    temp_lst.append(i[0])
output_dict['most_connected_by_num'] = temp_lst       ## sort most connected by num, add to dict

temp_lst = []
for i in sorted(G.degree(weight='weight'), key=lambda x: x[1], reverse=True)[0:3]:
    temp_lst.append(i[0])
output_dict['most_connected_by_weight'] = temp_lst    ## sort most connected by weight, add to dict

centrality_dict = nx.betweenness_centrality(G)
pooled_lst = []
for i in centrality_dict:
    pooling = [i,centrality_dict[i]]      ## create list of lists for betweenness centrality for sorting
    pooled_lst.append(pooling)

temp_lst = []
for i in sorted(pooled_lst, key=lambda x: x[1], reverse=True)[0:3]:
    temp_lst.append(i[0])
output_dict['most_central_by_betweenness'] = temp_lst  ## sort by betweenness, add to dict

#%% OUTPUT JSON

out_path = sys.argv[4]
with open(os.path.join(os.path.dirname(__file__), out_path), 'w') as result:
    json.dump(output_dict, result)  ## generate jsdon file of stats dict




