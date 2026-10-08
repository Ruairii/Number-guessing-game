#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 00:35:43 2026

@author: ruairi
"""


import random as rdm

print('Welcome matey')
print('you have 3, 5 or 7 attempts to guess the correct number')
difficulty = input('Easy, Medium or Hard, Choose:')

# Number interpritor for victory message 
Dict = {1: 'first',
        2: 'second',
        3: 'third',
        4: 'fourth',
        5: 'fifth',
        6: 'sixth',
        7: 'seventh',
        }
# difficulty setter
if difficulty == 'Easy':
    D = 7

if difficulty == 'Medium':
    D = 5

if difficulty == 'Hard':
    D = 3

# step tracker
N = 0

CN = rdm.randint(0,100)

print(CN)

for i in range(D):
    
    N += 1
    
    G = int(input('Answer? '))
    
    if G != CN:
        
        if G < CN:
            print('Higher')
        if G > CN:
            print('Lower')
      
    
    if G == CN:
        print('Correct You Win!')
        print(Dict[N],' guess')
            
        break
    
    
    if N == D:
        print('Hard luck, You lose!')
        break




    