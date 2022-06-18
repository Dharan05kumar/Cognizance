import numpy as np
A=np.random.randint(0,2,6)
print("First array:")
print(A)
B=np.random.randint(0,2,6)
print("Second array:")
print(B)
array_equal=np.allclose(A, B)
print(array_equal)
