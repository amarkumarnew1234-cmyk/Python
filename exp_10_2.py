'''2.  Create numpy array of (3,3) dimension. Now find sum of all rows & columns 
individually. Also find 2nd maximum element in the array. '''
import numpy as np
arr=np.array([[10,20,30],[40,50,60],[70,80,90]])
row_sum=np.sum(arr, axis=1)
col_sum=np.sum(arr, axis=0)
print("Row Sum:", row_sum)
print("Column Sum:", col_sum)
second_max=np.partition(arr.flatten(), -2)[-2]
print("Second Maximum Element:", second_max)

