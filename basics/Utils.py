from math import sqrt

def dot(u, v):
    return sum([i * j for i, j in zip(u, v)])

def angle(u, v):
    return dot(u, v) / (sqrt(dot(u, u)) * sqrt(dot(v, v)))