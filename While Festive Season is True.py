#!/usr/bin/env python
# coding: utf-8

# In[4]:


number = 0

while number <= 20:
    print(number)
    number = number + 2


# In[11]:


number = 0

while number <= 20:
    print(number)
    if number == 10:
        break
    number = number + 2


# In[17]:


number = 0

while number <= 20:
    number = number + 2
    if number == 12:
        continue
    print(number)
else:
        print('No Longer < 20')


# In[18]:


#notice 'continue' made the command skip 12.


# In[ ]:




