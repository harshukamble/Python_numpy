import numpy as np
arr=np.array([[21,22,23],
              [11,22,33],
              [21,22,33],])
#column wise sorting
print(np.sort(arr,axis=0))
#row wise sorting
print(np.sort(arr,axis=1))
#sorting in 1d
print(np.sort(arr,axis=None))
print("************************Car Details*************************************")
dtypes=[("name","S10"),('price',float),("number",int)]
values=[("opel",1111111.55,121212),("landrover",2542111.55,8547212),("marrzo",11000.85,56912),("swift",1111111.78,23412457),]
arr3=np.array(values,dtype=dtypes)
print(arr3)
#sort the array by order
print(np.sort(arr3,order='name'))
print(np.sort(arr3,order=['price',"number"]))
