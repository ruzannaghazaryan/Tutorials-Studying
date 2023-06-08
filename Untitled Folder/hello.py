# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 21:45:14 2023

@author: Dell
"""

# Demo file for Spyder Tutorial
# Hans Fangohr, University of Southampton, UK

def solution(n):
    str_n = str(n)
    part1, part2 = str_n[:len(str_n)//2], str_n[len(str_n)//2:]
    if (sum([int(i) for i in part1]) == sum([int(j) for j in part2])):
        return True
    return False
        
number = 1230
print(solution(number))

print(number)
