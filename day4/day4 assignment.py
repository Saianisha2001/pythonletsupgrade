#!/usr/bin/env python
# coding: utf-8

# In[12]:


count=0
for num in range(100,500):  
    sum = 0  
    temp = num  
    while temp > 0:  
        digit = temp % 10  
        sum += digit ** 3  
        temp //= 10  
        if num == sum:
            count=count+1
    if(count==1):
                
        print(num)
        break
                


# In[ ]:





# In[ ]:




