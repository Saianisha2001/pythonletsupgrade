#!/usr/bin/env python
# coding: utf-8

# In[1]:


List = [1,2,3,4] 
List.append(5) 
print(List)
List.insert(2,6)      
print(List)
print(sum(List)) 
print(len(List)) 
print(List.pop()) 


# In[7]:


squares = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
print(squares.get(3))
print(squares.items())
element=squares.pop(4)
print('deleted element=',element)
print(squares)
squares.update(name=36,age=49)
print(squares)
squares.setdefault('new')
print(squares)


# In[8]:


newset={1,2,6}
newset.add(3)
print(newset)
newset.update([2, 3, 4])
print(newset)
newset.discard(4)
print(newset)
newset.remove(6)
print(newset)
otherset={2,3,4,7,9}
print(newset.union(otherset))
print(newset.clear())


# In[11]:


tup1 = (1, 2, 3, 4, 5, 6, 7 )
print ("tup1[1:5]: ", tup1[1:5])
tup2 = (12, 34.56)
tup3=tup1+tup2
print('tup3=',tup3)
print('length=',len(tup3))
print (cmp(tup1, tup2))
print('minimum val=',min(tup1))
print('maximum val=',max(tup1))


# 

# In[14]:


s1='artificial'
s2='INTELLIGENCE'
print(s1.count('i'))
print(s1.islower())
print(s2.lower())
print(s1.endswith("al"))
s3='-->'
print(s3.join(s1))
print(s1.swapcase())


# In[ ]:




