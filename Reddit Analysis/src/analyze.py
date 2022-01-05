# -*- coding: utf-8 -*-
"""
@author: samh4
"""

#%% IMPORTS

import sys
import csv    
import json
import matplotlib.pyplot as plt

coded_file = sys.argv[2]    

#%% COMPUTING FEATURE COUNT

try:
    if sys.argv[3] == '-o':
        stdout = False             ## determine based on argument wheter stdout
        out_file = sys.argv[4]
except:
    stdout = True
   
tsv_file = open(coded_file)
read_tsv = csv.reader(tsv_file, delimiter="\t") ## read tsv file

c = 0
f = 0
r = 0           ## coding variables
o = 0

for row in read_tsv:
    
    if row[2] == 'c':
        c = c + 1
    elif row[2] == 'f':
        f = f + 1           ## add to coding variables to get total
    elif row[2] == 'r':
        r = r + 1
    elif row[2] == 'o':
        o = o + 1
        
output = {"course-related": c,
          "food-related": f,      ## output dict
          "residence-related": r,
          "other": o}

#%% VISUALIZE PIE CHART

pct_count = [0,0,0,0]
count = [c,f,r,o]
total = c+f+r+o
b = 0

while b < len(count):
    pct_count[b] = (count[b]*100)/total
    b+=1
    
y = pct_count
mylabels = output.keys()
myexplode = [0.1,0.1,0.1,0.1]

plt.pie(y, explode = myexplode, labels = mylabels, autopct='%1.1f%%',shadow = True,startangle=90)
fig = plt.gcf()
fig.set_size_inches(8.5,8.5) 
plt.show()

#%% VISUALIZE BAR GRAPH

plt.figure(figsize = (10, 5))
plt.ylim(0, (max(count)+10))
plt.bar(mylabels, count, color ='maroon', width = 0.66)
plt.xlabel("Coding Categories",fontsize=13)
plt.ylabel("No. of Posts",fontsize=13)
plt.title("Posts by Category",fontsize=15)
plt.show()

#%% OUTPUT

if stdout == True:      
    print(output)
else:
    with open(out_file, 'w') as outfile:  ## if not stout, create output JSON file
        json.dump(output, outfile)
   
