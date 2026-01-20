#!/usr/bin/env python
# coding: utf-8

# ## TERNARY STATMENTS
# 

# ## PASS

# In[2]:


age=19
if age>18:
    print("adult")


# In[3]:


age=19
if age>18:


# In[5]:


age=19
if age>18:
    pass


# ### break

# ## using for loop

# In[7]:


for i in range(0,10):
    print(i)


# In[10]:


for i in range(0,10):
    if i == 3:
        break
    print(i)


# ## continue

# In[11]:


for i in range(0,10):
    if i == 3:
        continue
    print(i)


# # WHILE LOOP

# ## WAP TO PRINT 1 TO 10 NUMBERS
# 

# ##  USING FOR LOOP

# In[13]:


for i in range(1,11):
    print(i)


# ## using while loop

# In[1]:


# it goes infinte loop so we dont use this num = 1
while num>0:
    print(num)


# In[2]:


num = 1
while num<11:
    print(num)
    num +=1


# In[5]:


num = 1
while num<11:
    if num==5:
        break
    print(num)
    num +=1


# ## wap to print sum fist 10 natural numbers

# In[1]:


sum_= 0
num = 1
while num<11:
    sum_=sum_+num
    print(sum_)
    num +=1


# ## print even nuber 1 to 20

# In[3]:


num = 2
while num<21:
    print(num)
    num +=2


# # wap to print reverse a number

# In[6]:


num = int(input())
rev = 0
while num > 0:
    digit=num%10
    rev = (rev*10)+digit
    num=num//10
rev


# In[ ]:




