import sys
import numpy as np

print(sys.version)

a = 3
b = 3.123
c = [a, b]
d = []
for obj in [a, b, c, d]:
    print(obj, sys.getsizeof(obj))

print('Test Numpy')

a = np.array([])
b = np.array([1, 2, 3])
c = np.zeros(10**6)

for obj in [a, b, c]:
    print('sys:', sys.getsizeof(obj), 'np:', obj.nbytes)

a = np.zeros(5, dtype=np.int32)
b = np.zeros(5, dtype=np.float64)

for obj in [a, b]:
    print('obj.size is ',obj.size)
    print('obj.itemsize is ',obj.itemsize)
    print('nbytes         :', obj.nbytes)
    print('size x itemsize:', obj.size*obj.itemsize)

