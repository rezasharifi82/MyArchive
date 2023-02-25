#In The Name Of God
from collections import deque


span=[15,7,3,1]
span=deque(span)
def shell(a):
    v=span
    while(len(v)>0):
        k=v.popleft()
        for i in range(k,len(a)):
            t=a[i]
            j=i-k
            while(a[j]>t and j>=0):
                a[j+k]=a[j]
                j-=k
                
            a[j+k]=t

        print(a)





a=[61,81,16,50,2,18,91,81,44,70,22,27]
# b=[12,0,9,8,1,89,23,15,13,0,1,-1,-8,-888]
shell(a)
# shell(b)