#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 23:24:45 2026

@author: ruairi
"""

import random as rdm

print('Welcome matey')
print('you have 3 attempts to guess the correct number')
difficulty = int(input('1.Easy, 2.Medium, 3.Hard, Choose:'))

CN = rdm.randint(0,10)

print(CN)

FG = int(input('First guess:'))

if FG == CN:
    print('Correct!')
    print('Woah, First try!')
else:
    if difficulty == 3:
        print('Game Over')
    else:
        if FG > CN:
            print('Lower')
        if FG < CN:
            print('Higher')
            SG = int(input('Second guess:'))
    
        if SG == CN:
            print('Correct!')
            print('Impressive!, Second guess')
        else:
            if difficulty == 2:
                print('Game Over')
            else:
                if SG > CN:
                    print('Lower')
                if SG < CN:
                        print('Higher')
                        TG = int(input('Third guess:'))

                if TG == CN:
                    print('Correct!')
                    print('Nice!, third times the charm')
                else:
                        print('Wrong')
                        print('YOU LOSE')
    
    
    
