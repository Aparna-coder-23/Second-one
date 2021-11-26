#!/bin/python3

import math
import os
import random
import re
import sys


# Write your code here
class Movie:
    def __init__(self, name, num_tik, tot_cost):
        self.name = name
        self._numT = num_tik
        self._totC = tot_cost
        
    
    def __string__(self):
        pass
        
        
         

if __name__ == '__main__':
    name = input()
    n = int(input().strip())
    cost = int(input().strip())
    
    p1 = Movie(name,n,cost)
    print(p1)

