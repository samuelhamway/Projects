# -*- coding: utf-8 -*-
"""
Call script as follows: python3 extract_to_tsv.py -o <out_file> <json_file> <num_posts_to_output>

"""
import csv
import json     ## imports
import sys
import random

if int(sys.argv[4]) < sum(1 for line in open(sys.argv[3])):
    lines = random.sample(range(0, 99), int(sys.argv[4]))  ## take random sample if less than total
else:
    lines = list(range(0, 100))
    
in_file = open(sys.argv[3])     

with open(sys.argv[2], 'wt', encoding='utf-8') as out_file:  
    
    tsv_writer = csv.writer(out_file, delimiter='\t',lineterminator = '\n')   
    tsv_writer.writerow(['Name', 'title', 'coding']) ## create tsv file for output

    for position, line in enumerate(in_file):
        
        if position in lines:
            
            post = json.loads(line)
            
            name = post['data']['author_fullname'] ## add data to each line
            title = post['data']['title']
            line = [name,title,'']
            
            tsv_writer.writerow(line)
            
out_file.close()
        
