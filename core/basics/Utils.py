from math import sqrt

from numpy import dot as npdot, transpose


def dot(u, v):
    return npdot(u, transpose(v))[0, 0]

def angle(u, v):
    num = dot(u, v)
    if num == 0: return 0
    return num / (sqrt(dot(u, u)) * sqrt(dot(v, v)))

def normalize(arr):
    mx = max(arr)
    for i in arr: i /= mx
    return arr