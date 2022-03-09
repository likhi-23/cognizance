import numpy as np
i = np.array([1 ,0, 0, 0 ,1, 0])
j = np.array([0 ,0, 1, 1 ,0 ,1])
array_len=len(i)
for p in range(array_len):
    if i[p] == j[p] :       
        result=0
    else :
        result=1
if result==0:
    
    print("Arrays are equal ")
else :
    
    print("Arrays are not equal ")
