#En este ejemplo se carga una imagen y se dezplaza (Dejando un rastro )
from skimage import io
from pipelines import *

A=io.imread('barbara.jpg')

plt.imshow(pipeline1(A))
plt.show()

A=io.imread('barbara.jpg')
plt.imshow(pipeline2(A))
plt.show()
