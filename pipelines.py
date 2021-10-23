from filters import *
import matplotlib.pyplot as plt

def pipeline1(A):
    A = preprocessFilter(A)
    A = averageFilter(A)
    A = laplacianFilter(A)
    return A

def pipeline2(A):
    A = preprocessFilter(A)
    A = averageFilter(A)
    A = traslationFilter(A)
    A = laplacianFilter(A)
    return A
