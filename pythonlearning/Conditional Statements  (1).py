#!/usr/bin/env python
# coding: utf-8

# # Basic Questions

# # if statement

# ## 1.Check if a number is positive

# In[1]:


num = input()
if num >= 0:
    print("The Entered Number is Positive")


# In[1]:


#Direct value
num = 7
if num >= 0:
    print("The Entered Number is Positive")


# In[16]:


#Direct value
num = -5
if num >= 0:
    print("The Entered Number is Positive")


# In[2]:


#User_defined Value
num = int(input())
if num >= 0:
    print("The Entered Number is Positive")


# In[17]:


if True:
    print("The Entered Number is Positive")


# In[18]:


if False:
    print("The Entered Number is Positive")


# ## 2.Check if a number is greater than 10

# In[19]:


num = int(input())
if num > 10:
    print("Number is Greater than 10")


# In[20]:


num = int(input())
if num > 10:
    print("Number is Greater than 10")


# ## 3.Check if a string contains the letter 'a'

# In[2]:


string = input("enter a string which have a letter")
if "a" in string:
    print("string contain a")



# In[6]:


string = "siddi"
if "a" in string:
    print("string contain a")


# ## 4.Check if age is eligible for voting (≥18)

# In[7]:


age = int(input())
if age>=18:
    print("age is eligible for voting")


# ## 5.check if a list is empty

# In[12]:


list = ()
if len(list) == 0:
    print("list is empty")


# # if-else Statement

# In[ ]:





# ## 1.Check if a number is even or odd

# In[17]:


num = int(input())
if num%2==0:
    print("number is even")
else :
    print("number is odd")


# In[18]:


num = int(input())
if num%2==0:
    print("number is even")
else :
    print("number is odd")


# ## 2.Check if a number is positive or negative

# In[20]:


num = int(input())
if num>0:
    print("number is postive")
else :
    print("number is negative")


# In[21]:


num = int(input())
if num>0:
    print("number is postive")
else :
    print("number is negative")


# ## 3.Check if length of string is greater than 5

# In[24]:


num = input()
if len(num)>5:
    print("length of string is greater than")
else :
    print("length of string is not greater than")


# In[26]:


num = input()
if len(num)>5:
    print("length of string is greater than")
else :
    print("length of string is not greater than")


# ## 4.Check if a number is divisible by 8

# In[ ]:


num = int(input())
if num%8==0:
    print("number is divisible by 8")
else :
    print("number is not divisible by 8")


# # if–elif–else Ladder

# ## 1.Grade calculation

# In[4]:


marks = int(input())
if marks>80:
    print("grade A")
elif marks>60:
    print("grade b")
elif marks>40:
    print("grade c")
elif marks<=38:
    print("fail")


# In[9]:


marks = int(input())
if marks>80:
    print("grade A")
elif marks>60:
    print("grade b")
elif marks>40:
    print("grade c")
else :
    print("fail")


# In[6]:


marks = int(input())
if marks>80:
    print("grade A")
elif marks>60:
    print("grade b")
elif marks>40:
    print("grade c")
elif marks<=38:
    print("fail")


# In[7]:


marks = int(input())
if marks>80:
    print("grade A")
elif marks>60:
    print("grade b")
elif marks>40:
    print("grade c")
elif marks<=38:
    print("fail")


# ## 2.Identify the type of triangle

# In[19]:


a = int(input())
b = int(input())
c = int(input())
if a == b == c:
    print("equaleted triangke")
elif a==b!=c:
    print("isolated triangle")
elif a!=b!=c:
    print("scalene triangle")
else:
    print("false input")


# In[21]:


a = int(input())
b = int(input())
c = int(input())
if a == b == c:
    print("equaleted triangke")
elif a==b!=c:
    print("isolated triangle")
elif a!=b!=c:
    print("scalene triangle")
else:
    print("false input")


# In[22]:


a = int(input())
b = int(input())
c = int(input())
if a == b == c:
    print("equaleted triangke")
elif a==b!=c:
    print("isolated triangle")
elif a!=b!=c:
    print("scalene triangle")
else:
    print("false input")


# In[23]:


a = int(input())
b = int(input())
c = int(input())
if a == b == c:
    print("equaleted triangke")
elif a==b!=c:
    print("isolated triangle")
elif a!=b!=c:
    print("scalene triangle")
else:
    print("false input")


# ## 3.Check age group

# In[25]:


a = int(input())
if a<12:
    print("child")
elif a<18 :
    print("teen")
elif a<30:
    print("adult")
else:
    print("senior citizen")


# In[27]:


a = int(input())
if a<12:
    print("child")
elif a<18 :
    print("teen")
elif a<30:
    print("adult")
else:
    print("senior citizen")


# In[28]:


a = int(input())
if a<12:
    print("child")
elif a<18 :
    print("teen")
elif a<30:
    print("adult")
else:
    print("senior citizen")


# In[29]:


a = int(input())
if a<12:
    print("child")
elif a<18 :
    print("teen")
elif a<30:
    print("adult")
else:
    print("senior citizen")


# # Intermediate Questions

# # Question:
# At an amusement park, a person can ride the roller coaster only if they are at least 12 years old.
# 
# If they are under 18 but above 12, they must also have parental permission. 
# 
# Otherwise, only 18+ can ride freely.
# 
# Write a program using nested if-else to decide.

# In[46]:


age = int(input())
if age>12:
    if (age>12) or age <18:
        permission = input("enter the perission")
        if permission == "yes":
            print("have parental ride or you can ride")
        else:
            print("you cant'ride")
    else:
        print("can ride freely")
else :
    print("you cant ride")


# In[47]:


age = int(input())
if age>12:
    if (age>12) or age <18:
        permission = input("enter the perission")
        if permission == "yes":
            print("have parental ride or you can ride")
        else:
            print("you cant'ride")
    else:
        print("can ride freely")
else :
    print("you cant ride")


# In[3]:


age = int(input())
if age>12:
    if (age>12) or age <18:
        permission = input("enter the perission")
        if permission == "yes":
            print("have parental ride or you can ride")
        else:
            print("you cant'ride")
    else:
        print("can ride freely")
else :
    print("you cant ride")


# In[14]:


age = int(input())
if age<12:
    print("you cant ride")
elif age>18:
    print("you can ride freely")
elif (age>12) or age <18:
        permission = input("enter the perission")
        if permission == "yes":
            print("have parental ride or you can ride")
        else:
            print("you cant'ride")


# In[12]:


age = int(input())
if age<12:
    print("you cant ride")
elif age>18:
    print("you can ride freely")
elif (age>12) or age <18:
        permission = input("enter the perission")
        if permission == "yes":
            print("have parental ride or you can ride")
        else:
            print("you cant'ride")


# In[15]:


age = int(input())
if age<12:
    print("you cant ride")
elif age>18:
    print("you can ride freely")
elif (age>12) or age <18:
        permission = input("enter the perission")
        if permission == "yes":
            print("have parental ride or you can ride")
        else:
            print("you cant'ride")


# # Roller Coaster Ride Eligibility

# In[ ]:





# # Movie Ticket Pricing

# # Job Application Filter

# # Advanced Questions

# In[ ]:




