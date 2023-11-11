import numpy as np

arr = np.array([1, 2, 3])
drr = np.array([1, 2, 4])

sd=0.1*arr.dot(drr)
print(sd)