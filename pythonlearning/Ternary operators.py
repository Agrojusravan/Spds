#!/usr/bin/env python
# coding: utf-8

# ## wap to check if the number is even or odd

# ## using if else statment

# In[4]:


num =int(input())
if num%2==0:
    print("even")
else :
    print("odd")


# ## using ternary staments
# 

# In[6]:


num =int(input())
print("the enter number is even") if num%2==0 else print("the enter number is odd")


# ## check the enter number is postyive or negative or zero

# ## using if else statment
# 

# In[11]:


num =int(input())
if num>0:
    print("+ve")
elif num<0:
    print("-ve")
else :
    print("zero")


# ## using ternary statments

# In[12]:


num =int(input())
print("the enter number is postive")if num>0 else print("the enter number is negative")if num<0 else print("zero")


# In[25]:


age = int(input())
print(f"the kid age is {age}")if age<10 else print(f"the teen age is {age}")if age<18 else print(f"the adult age is {age}")if age <50 else print(f"senior citizen age is {age}")  


# In[ ]:




