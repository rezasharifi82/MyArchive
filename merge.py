#In The Name Of God
from collections import deque

def merge_sort(a,first,last):
    if (first>=last):
        return 
    else:
        mid=(first+last)//2
        merge_sort(a,first,mid)
        merge_sort(a,mid+1,last)
        merge(a,first,mid,last)

def merge(a,first,mid,last):
    i=first
    j=mid+1
    t=[]
    while(i<=mid and j<=last):
        if(a[i]<=a[j]):
            t.append(a[i])
            i+=1
        else:
            t.append(a[j])
            j+=1
    while(i>mid and j<=last):
        t.append(a[j])
        j+=1
    while(j>last and i<=mid):
        t.append(a[i])
        i+=1

    # print(a)
    t=iter(t)
    for i in range(first,last+1):
        a[i]=next(t)



a=[-5,7,1,0,99,1,0,1,4,7,8,9,5,2,0,2,2,1,58,8,9]
# b=[12,0,9,8,1,89,23,15,13,0,1,-1,-8,-888]
merge_sort(a,0,len(a)-1)
# shell(b)
print(a)