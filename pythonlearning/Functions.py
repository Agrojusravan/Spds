#!/usr/bin/env python
# coding: utf-8

# ## create a function to perform addition operation

# In[1]:


def add (a,b):
    res=a+b
    return(res)


# In[2]:


add(4,5)


# In[3]:


add(5,6)


# #  wap to print to check even or odd

# In[5]:


num = int(input())
if  num%2==0:
    print("even")
else:
    print("odd")


# In[10]:


def even_odd(num):
    if  num%2==0:
        print("even")
    else:
        print("odd") 


# In[11]:


even_odd(25)


# In[12]:


even_odd(2)


# # wap to print to check postive or negative

# In[14]:


def postive_negative(num):
    if  num>0:
        print("postive")
    else:
        print("negative") 


# In[15]:


postive_negative(2)


# In[16]:


postive_negative(-1)


# In[17]:


postive_negative(0)


# # wap to print to check age

# In[22]:


def criteria(num):
    if  num<10:
        print("kid")
    elif num<18:
        print("teen")
    elif num<50:
        print("adult")
    else :
        print("senior citizen")


# In[23]:


criteria(10)


# In[24]:


criteria(9)


# In[25]:


criteria(18)


# In[26]:


criteria(50)


# # wap to create a calculator

# In[28]:


def calculator(a,b):
    add = a+b
    sub = a-b
    mul = a*b
    div = a/b
    return(add,sub,mul,div)


# In[46]:


calculator(a=2,b=5)


# In[45]:


calculator(a=5,b=2)


# In[47]:


calculator(2)


# In[48]:


calculator(2,5,6)


# In[52]:


calculator(a=2,5)


# In[55]:


calculator(3,b=6)


# In[40]:


calculator(2,5)


# In[41]:


calculator(a=2,b=5)


# In[42]:


calculator(b=2,a=5)


# In[31]:


def add(a,b):
    return(sum(a,b))


# In[35]:


import math


# In[37]:


math.pow(2,3)


# In[38]:


str1 = "sravan"


# In[39]:


str1.upper()


# In[43]:


calculator(2)


# In[44]:


calculator(2,5,6)


# In[56]:


calculator(2,5,6)


# # default argument

# In[57]:


def add(a,b,c=5):
    return(a+b+c)


# In[59]:


add(3,4,6)


# In[60]:


add(3,4)


# In[61]:


add(1)


# In[1]:


calculator(a=2,5)


# # 2 Arbitrary arguments

# In[19]:


def add(*n):
    return(n)


# In[20]:


add(1,2,3)


# In[4]:


def add(*n):
    return(sum(n))


# In[5]:


add(1,2,3)


# In[6]:


add(3)


# In[7]:


add(3,5)


# In[10]:


def add(**n):
    return(n)


# In[14]:


add(a=1,b=2)


# In[15]:


def add(**n):
    return(sum(n))


# In[16]:


add(a=1,b=2)


# # Recursive function 

# ## wap to print factorial of a number

# In[24]:


def factorial(num):
    if (num==0 or num==1):
        return(1)
    else:
        return(num*factorial(num-1))


# In[28]:


factorial(4)


# In[30]:


factorial(5)


# # wap to recursive function to print the first n terms of the fibonacci function

# In[4]:


def fibonacci(num):
    if num <= 0:
        return ("invalid number")
    elif num == 1:
        return 0
    elif num == 2:
        return 1
    else:
        return fibonacci(num-1)+fibonacci(num-2)


# In[7]:


fibonacci(4)


# In[5]:


num = int(input())
for i in range(1,num+1):
    print(fibonacci(i))


# In[7]:


num = int(input())
for i in range(1,num+1):
    print(fibonacci(i),end=",")


# # lambda function

# # wap using lambda function check even or odd

# In[10]:


result = lambda num :"even" if num%2==0  else  "odd"
print(result(6))


# In[11]:


num = int(input())
result = lambda num :"even" if num%2==0  else  "odd"
print(result(num))


# # 2 create a lambda function to calculate the maximum of two numbers with out using max()

# In[12]:


a = int(input("enter the first number"))
b = int(input("enter the second number"))
result = lambda a,b : "first number is greater" if a>b else "second number is greater"
print(result(a,b))


# # filter()

# # 1 use filter to get all squares of a even numbers from a list

# In[13]:


# using for loop
l1 = [1,2,3,4,5,6,7,8,9]
for i in l1:
    if i%2==0:
        print(i**2)


# In[18]:


# using filter
l1 = [1,2,3,4,5,6,7,8,9]
even = filter(lambda i: i %2==0,l1)
square = [i**2 for i in even]
square


# In[20]:


l1 = [1,2,3,4,5,6,7,8,9]
even = filter(lambda i: i %2==0,l1)
for i in even:
    print(i**2)


# # 2 use filter to select only palindromes from a list of words
# example = "madam","racecar","hello"->madam, racecar

# In[21]:


a = "sravan"
rev = a[::-1]


# In[22]:


rev


# In[24]:


if a == rev:
    print("equale")
else:
    print("not equale")


# In[25]:


l2=["madam","hello","racecar"]


# In[28]:


rev =list(filter(lambda i : i ==i[::-1],l2))


# In[29]:


rev


# # map()

# # 1 use map to get cube of each number in a list

# In[30]:


# usinf for loop


# In[31]:


l1=[1,2,3,4,5,6,7,8,9]
for i in l1:
    print(i**3)


# In[34]:


list(map(lambda i:i**3,l1))


# # 2 use map to add two list wise

# In[35]:


l1 = [1,2,3]
l2 = [4,5,6]
list(map(lambda x,y:x+y,l1,l2))


# # reduce

# In[37]:


pip install functools


# In[1]:


from functools import reduce


# # use reduce to find the dum of all number in list

# In[2]:


l1 = [1,2,3,4,5,6]
res = reduce(lambda x,y:x+y,l1)
res


# # use reduce to concatenate a lsit of string into single string
# "python","is","fun"--"python is fun"

# In[5]:


l2 = ["python","is","fun"]
res = reduce(lambda x,y:x+" "+y,l2)
res


# In[ ]:




