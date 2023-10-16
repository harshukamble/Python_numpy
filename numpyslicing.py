import numpy as np
arry1=np.array([[1,2,3,4,5,6,7,8],
               [11,22,33,44,55,66,77,88]])
print("--------------------indexing---------------------------")
print(arry1[1,3])
arry2=np.array([[[1,2,3,4,5],
                 [11,22,33,44,55]],
                 [[1,1,1,1,1],
                  [221,2,2,2,2]]])
print(arry2.ndim)
print(arry2[1,1,0])
print(arry2)
print(arry1)
condition=arry1>5
print(arry1[condition])
print("--------------------Slicing---------------------------")
print(arry1[:2,::2])

