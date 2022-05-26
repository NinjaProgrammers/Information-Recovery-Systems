from math import sqrt
from numpy import dot

def angle(u, v):
    num = dot(u, v)
    if num == 0: return 0
    return num / (sqrt(dot(u, u)) * sqrt(dot(v, v)))