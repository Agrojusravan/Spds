#!/usr/bin/env python
# coding: utf-8

# In[ ]:


a=1   #using arthematic operator
b=2
a=a+b
b=a-b
a=a-b
print(a)
print(b)


# In[2]:


a=1      #using bitwise operator
b=2
a=a^b
b=a^b
a=a^b
print(a)
print(b)


# In[ ]:


bin(5),bin(10)


# In[7]:


#count even or odd
count_even = 0
count_odd = 0
for i in range (1,11):
    if i%2==0:
        count_even+=1
        
    else:
        count_odd+=1
print(count_even)
print(count_odd)


# In[13]:


n = int(input())
sum = 0
for i in range (1,n):
    if n%i==0:
        sum+=i
if sum==n:
    print("perfect square")
else :
    print("not perfect sqaure")


# In[16]:


n = int(input())
sum = 0
for i in range(1,n+1):
    
    sum += i
sum


# In[20]:


def fact(n):
    if n==0 or n==1:
        return 1
    else :
        return n*fact(n-1)


# In[21]:


fact(5)


# In[ ]:




