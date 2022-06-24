#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Warning O:N! time complexity
#Seriously don't try this with large numbers of entities
import itertools
import time
seconds1 = time.time()
	

def xbasey(x, y):
    if x == 0:
        return '0'
    nums = []
    while x:
        x, r = divmod(x, y)
        nums.append(str(r))
    return ''.join(reversed(nums))
#letters start here
lst1a=["a", "b", "c", "d", "e"]
n=len(lst1a)
s = "".join(lst1a)  
nums = list(s)
lst2a = list(itertools.permutations(nums))
    
#ops start here
n-=1
lst1=["+", "-", "/", "*"]
lst2=[]
x=0

while x<(len(lst1)**n):
    temp=(xbasey(x, len(lst1)))
    while len(temp)<n:
        temp="0"+temp
    temp2=""
    for ch in temp:
        temp2+=(lst1[int(ch)])
    lst2.append(list(temp2))
    x+=1
#interweaving starts here    
lst3=[]
for i in range(len(lst2a)):
    templ=[]
    for e in range(len(lst2a[i])):
        templ.append(lst2a[i][e])
    templ2=templ.copy()
    for j in lst2:
        templ2=templ.copy()
        for k in range(n):
            templ2.insert(((k*2)+1), j[k])
        lst3.append(templ2)
    
#formating output starts here
outlst=[]    
for i in lst3:
    out="".join(i)
    outlst.append(out)
    print(out)
    
print(outlst)

seconds2 = time.time()
print("Seconds =", seconds2-seconds1)	


# In[ ]:




