import numpy as np
arr1=np.array([[90,45,60],
               [30,22,33],
               [7,8,9]])
print(arr1)
print(arr1.max())
print(arr1.min())
arr2=np.array([[1,2,3],
               [11,22,33],
               [21,32,43],])

print(arr1+arr2)
print(arr1-arr2)
print(arr1.dot(arr2))
print("----------------------------------Introduction to NymPy’s ufuncs-------------------------------------------------")
print(np.sin(arr1))
print(np.pi)
print(np.pi/2)
print(np.sqrt(64))  
print(np.exp(2))
