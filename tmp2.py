import numpy as np

u = np.random.normal(0, 1, (2,))
v = np.random.normal(0, 1, (2,))
print('u:', u)
print('v:', v)

print(u - v)
print((u - v) ** 2)
print(np.sum(u - v) ** 2)
