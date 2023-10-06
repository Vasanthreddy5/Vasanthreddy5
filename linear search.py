from calendar import month
from datetime import datetime

now=datetime.now()
y,m=now.year,now.month

print(month(theyear=y,themonth=m))

#linear search
array=[3,6,4,1,8,9,7]
n=len(array)
x=8
def linearsearch(array,n,x):
    for i in range(0,n):
        if array[i]==x:
            return i
    return -1

result=linearsearch(array,n,x)
if result==-1:
    print("Element is not found in the array")
else:
    print(f'Element is found at index:{result}')