# -*- coding: utf-8 -*-
"""
Created on Fri Jan 16 10:34:51 2015

@author: efourrier

Purpose: This module provide some examples of beautiful python code and
some recipes.

"""

#########################################################
# Zen of Python  
#########################################################

# type in the interactive console 
import this 

#########################################################
# import packages 
#########################################################

from itertools import izip
from collections import defaultdict
from functools import partial



def unzip(tuples):
    return zip(*tuples)


# one line if else condition 
r =None 
n =1   
r = n if r is None else r

def make_complex(x, y):
    return {'x': x, 'y': y}
    



#########################################################
# List,tuples, and loops  
#########################################################

# Variables
colors = ['red', 'green', 'blue', 'yellow']
names = ['raymond', 'rachel', 'matthew']

# Creating four None 
four_nones = [None] * 4

# Creating four lists 
four_lists = [[] for _ in xrange(4)]


# Unpacking 
for i, color in enumerate(colors):
    print i, '--->',color
   
# More advanced unpacking 

# swap 
a,b = 1,2
a,b = b,a
lup = [1234,10000,'vacation']
loan_id,amount,purpose = lup
amount

for (loan_id,amount,purpose) in [lup,[1235,5000,'home_improvment']]:
    print amount,purpose
    
# instead of zip use izip 
for name, color in izip(names, colors):
    print name, '--->', color


# Instead of using break use iter
blocks = []
for block in iter(partial(f.read, 32), ''):
    blocks.append(block)
    
    
#########################################################
# Dictionnaries 
#########################################################
    
d = {'matthew': 'blue', 'rachel': 'green', 'raymond': 'red'}



d = {'matthew': 'blue', 'rachel': 'green', 'raymond': 'red'}



for k in d :
    print k 
    
# if you are mutating the dictionary use d.keys() that is creating a copy 
for k in d.keys():
    del d[k]
    

d.items() # is a list of tuples 
d.iteritems() # is a generator 

# more computer efficient than d.items()
for k, v in d.iteritems():
    print k, '--->', v

# Constructing a dictionnary from 2 lists 
names = ['raymond', 'rachel', 'matthew']
colors = ['red', 'green', 'blue']

d = dict(izip(names, colors))


def beautiful_histo(l):
    d = {}
    for e in l:
        d[e] = d.get(e,0) +1
    return d

beautiful_histo(['red', 'green', 'red', 'blue', 'green', 'red'])     


# Dictionnary grouping 
names = ['raymond', 'rachel', 'matthew', 'roger',
         'betty', 'melissa', 'judith', 'charlie']
# i want name group by len 

# Same as setdefault
dd = defaultdict(list)

for name in names :
    key = len(name)
    dd[key].append(name)
    
print dd
# updating multiple state values 
x,y = 1,1

def fibonacci(n):
    x, y = 0, 1
    for i in xrange(n):
        print x
        x, y = y, x + y
        
# open files 
with open('data.txt') as f:
    data = f.read()
# do something with data

# with automaticely close the file 

# quick benchmark ipython execute one by one 
%timeit sum([i*i for i in range(100000)])
%timeit sum(i*i for i in range(100000))
%timeit sum(i*i for i in xrange(100000))

#########################################################
# Some tricks to know  
#########################################################

import sys
sys.path
# if you want to add a path 

#sys.path.append

# testing a module
#if __name__ == "__main__" :
    
# String formatting 
pwd = 'bouh'
uid = 'odbc'
print "%s is not a good password for %s" % (pwd, uid)

dir(list) # compute all the methods of a object 

# list comprehension 
# [mapping−expression for element in source−list if filter−expression]


