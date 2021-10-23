import numpy as np
from skimage import io
from scipy.signal import convolve2d
from skimage.util import img_as_ubyte
from skimage.transform import resize
from skimage.util import img_as_ubyte


def averageFilter(A):
    k=3;
    B=(1/k**2)*np.ones((k,k));
    for i in range(1,10):
        A=convolve2d(A,B,mode='same')
    return A

def laplacianFilter(A):
    B=np.array([[1, 1,1],
                [1,-8,1],
                [1, 1,1]]);
    C=convolve2d(A,B,mode='same');
    alpha=-0.5
    D=A+alpha*C
    return D

def traslationFilter(A):
    [m,n]=A.shape
    B=np.zeros((m,n), np.uint8)
    for i in range(round(min(m,n)/2)):
        deltax=i
        deltay=i
        for x in range(m):
            for y in range(n):
                x_t=x+deltax 
                y_t=y+deltay
                if x_t<m and  y_t<n:
                    B[x_t,y_t]=A[x,y]
    return B

def preprocessFilter(A):
    return img_as_ubyte(resize(A,(128,128)))[:,:,0]