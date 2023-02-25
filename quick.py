#In The Name Of God
def split(a,first,last):

    pivot=a[first]
    i=first+1
    j=last
    while(i<=j):
        
        while(a[j]>pivot):
            j-=1
        while(i<j and a[i]<=pivot):
            i+=1
        if(i<j):
            a[i],a[j]=a[j],a[i]
        else:
            break
    
    pos=j
    a[first]=a[j]
    a[j]=pivot
    return pos

def quick(a:list,first,last):
    if(first<last):
        pos=split(a,first,last)
        quick(a,first,pos-1)
        quick(a,pos+1,last)


a=[23,15,7,14,28,18,7,5,29,19,12,7]

quick(a,0,len(a)-1)
print(a)
