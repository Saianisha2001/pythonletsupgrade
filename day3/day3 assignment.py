#!/usr/bin/env python
# coding: utf-8

# In[1]:


n=int(input("enter the altitude"))
if(n<=1000):
    print('Safe to Land')
elif(n>1000 and n<=5000):
    print('Bring down to 1000')
elif(n>5000):
    print('Turn around')


# In[12]:





for num in range(2, 201):
   # all prime numbers are greater than 1
   if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
           print(num)
        


# In[ ]:





# In[ ]:




