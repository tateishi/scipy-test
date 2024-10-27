import numpy as np
from time import time

array = np.arange(1e6)
print(array.shape)
print(array.ndim)

list_array = array.tolist()

now = time()
y = [n * 5 for n in list_array]
print(f"elapsed {time()-now}")

now = time()
x = array * 5
print(f"elapsed {time()-now}")


x = np.array([1, 2, 3, 4])
print(x)
x = np.reshape(x, (len(x), 1))
print(x)

y = np.array([0, 1, 2, 1])
print(y)
y = np.reshape(y, (1, len(y)))
print(y)

print(x.shape)
print(y.shape)

outer = x * y
print(outer)
print(outer.shape)
