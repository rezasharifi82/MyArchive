#In The Name Of God
from collections import deque
from itertools import permutations
prefer=[[4,5,7,6],[6,4,7,5],[6,5,7,4],[5,4,6,7],
        [2,1,3,0],[1,0,2,3],[1,3,0,2],[2,0,3,1]]
# prefer=[[2,3],[3,2],
#         [1,0],[0,1]]

        # 2 1 3 0

a=[0,1,2,3]                             
b=[4,5,6,7] 
def per(a:list, b:list):
    c=deque(b)
    # d=deque(b)
    f=list(permutations(b))
    # a for men
    # b for women
    gamma=[]
    for i in f:
        z=[(x,y) for x,y in enumerate(i)]
        gamma.append(z)

    return gamma

def stable(a:list,prefer:list,z):
    alo=[]
    c=0
    # women=prefer[:4]
    # men=prefer[4:]
    for ins,i in enumerate(a):
        for j in a[ins+1:]:
            if((prefer[i[0]].index(j[1])<prefer[i[0]].index(i[1])) and 
            (prefer[j[1]].index(i[0])<prefer[j[1]].index(j[0]))):
                print("{} - First: \n 1: {} , 2: {} \n ----------".format(z,i,j))
                return False
            if((prefer[j[0]].index(j[1])>prefer[j[0]].index(i[1])) and 
            (prefer[i[1]].index(i[0])>prefer[i[1]].index(j[0]))):
                print("{} - Second: \n 1:{} , 2:{} \n ----------".format(z,i,j))
                return False
    # print(c)
    return True
    


f=per(a,b)
# print(*f,end="\n")
c=0
d=0
d=0

for i in f:
    # print(i)
    d+=1
    if(stable(i,prefer,d) ==True):
        c+=1
print(c)
# print(len(set(f)))

    
