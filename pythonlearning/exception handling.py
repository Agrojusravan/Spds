#!/usr/bin/env python
# coding: utf-8

# # program error

# In[4]:


name = "sravan'


# In[6]:


if name == 1:
print(name)


# # exception handling

# In[12]:


num1=int(input())
num2=int(input())
dev = num1/num2
print(dev)


# In[5]:


try:
    num1=int(input())
    num2=int(input())
    dev = num1/num2
    print(dev)
except ValueError:
    print("enetr only members")
else:
    print("there are no exceptiob")
finally:
    print("code executed")


# # raise our own error

# In[8]:


def age_check(age):
    if age < 18:
        raise ValueError
    print("age is valid")


# In[9]:


age_check(16)


# In[12]:


try:
    age_check(16)
except ValueError:
    print("age is less than 18")
else:
    print("there are no error")


# In[13]:


try:
    age = int(input())
    age_check(age)
except ValueError:
    print("age is less than 18")
else:
    print("there are no error")


# In[ ]:




