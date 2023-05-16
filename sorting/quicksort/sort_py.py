import random
import time
import copy
from numba import jit, njit
from numba.typed import List
import numpy as np

@njit
def bubblesort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


@njit
def merge(left, right):
    merged = List()
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    while i < len(left):
        merged.append(left[i])
        i += 1

    while j < len(right):
        merged.append(right[j])
        j += 1
    return merged

@njit
def mergesort(lis):
    if len(lis) <= 1:
        return lis
    left = mergesort(lis[:len(lis)//2])
    right = mergesort(lis[len(lis)//2:])
    return merge(left, right)

@njit
def quicksort(A, lo, hi):
    '''
    a basic python implementation of the quick sort algorithms
        Based on the English wikipedia quicksort page
        used partitioning: Hoare
  '''
    if lo >= 0 and hi >= 0 and lo < hi:
        p = partition(A, lo, hi)
        quicksort(A, lo, p)
        quicksort(A, p + 1, hi)


@jit(nopython=True)
def partition(A, lo, hi):
    pivot = A[(hi - lo) // 2 + lo]
    i = lo - 1
    j = hi + 1
    
    while True:
        i += 1
        while A[i] < pivot:
            i += 1
        
        j -= 1
        while A[j] > pivot:
            j -= 1
        
        if i >= j:
            return j
        
        A[i], A[j] = A[j], A[i]

l=50000
#l=10
A=List()
B=[]
C=List()
D=[]

for _ in range(l):
    r=random.random() 
    A.append(r)
    B.append(r)
    C.append(r)
    D.append(r)

n=np.array(B)
D=np.array(D)



start_time = time.time()
quicksort(A, 0, l-1)
print("--- %s seconds --- qsort njit" % (time.time() - start_time))

start_time = time.time()
mergesort(C)
print("--- %s seconds --- mergesort njit" % (time.time() - start_time))

start_time = time.time()
bubblesort(D)
print("--- %s seconds --- bubblesort njit" % (time.time() - start_time))


start_time = time.time()
list.sort(B)
print("--- %s seconds --- list.sort" % (time.time() - start_time))

start_time = time.time()
np.sort(n)
print("--- %s seconds --- np.sort" % (time.time() - start_time))