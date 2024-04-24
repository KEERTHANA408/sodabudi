# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 21:52:58 2024
sodaaa
@author: keert
"""
import numpy as np
import matplotlib.pyplot as plt
import time

def bubblesort(array):
    n = len(array)-1
    while n >= 1:
        i = 0
        while i < n:
            if array[i] > array[i + 1]:
                array[i],array[i + 1] = array[i],array[i + 1]
                i += 1
        n -= 1
sorts = [
    
    {"name": "bubble sort", "sort": lambda arr: bubblesort(arr)}

]
elements = np.array([i * 1000 for i in range(1, 5)])

plt.xlabel('list length')
plt.ylabel('time complexitiy')

for sort in sorts:
    times = list ()
    start_all = time.time ()
    for i in range (1, 5):
        start = time.time ()
        a = np.random.randint(1000, size = i * 1000)
        sort["sort"](a)
        end = time.time()
        times.append(end - start)
        print(sort["name"], "sorted", i * 1000, "elements in", end - start, "s")
    end_all = time.time()
    print(sort["name"], "sorted elements in",end_all - start_all, "s")
plt.plot(elements, times, label = sort["name"])
plt.grid()
plt.lengend()
plt.show()

    
    
                
            
    
