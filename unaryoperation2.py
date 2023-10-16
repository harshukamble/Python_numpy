import numpy as np
print("----------------------------Unary Operation---------------------------")
print("----------------------------One d-------------------------------------")
arry=np.array([[1,2,3]])
print("max element of array",arry.max())
print("min element of array",arry.min())
print("sum of element",arry.sum())
print("cummultative sum of element",arry.cumsum())
print("----------------------------two d-------------------------------------")
arr2=np.array([[1,2,3],
               [4,5,6],
               [7,8,9],
               [10,11,12]])
print("max of an arry2",arr2.max())
print("min of array 2",arr2.min())
print("row-wise max element",arr2.max(axis=1))
print("column-wise max element",arr2.max(axis=0))
print()
print("cumutatitve sum element \n",arr2.cumsum(axis=1))
print("----------------------------Three d-------------------------------------")
arr2=np.array([[[1,2,3],
               [4,5,6],
               [7,8,9],
               [10,11,12]],
               [[11,12,33],
               [4,55,66],
               [7,8,9],
               [10,111,12]]])
print("max of an arry2 \n",arr2.max())
print("min of array 2 \n",arr2.min())
print("row-wise max element \n",arr2.max(axis=2))
print("column-wise max element \n",arr2.max(axis=1))
print()
print("cumutatitve sum element \n",arr2.cumsum(axis=2))