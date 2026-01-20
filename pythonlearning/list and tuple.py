#!/usr/bin/env python
# coding: utf-8

# ## list

# #### `creating homogeneous list

# In[2]:


list1 = [1,2,3,4,5]
print(list1)
print("the type of given list is :" ,type(list1))


# ### creating a hetrogeneous list

# In[5]:


list2 = [1,2,3,4,5,"a","b","C",]
print(list2)
print("the type of given list is :" ,type(list2))


# ### using the in-built function
# 

# In[6]:


list3 = list(11,12,13,14,15)
print(list3)
print("the type of given list is :" ,type(list3))


# In[8]:


list3 = list((11,12,13,14,15))
print(list3)
print("the type of given list is :" ,type(list3))


# In[9]:


list3 = list([11,12,13,14,15])
print(list3)
print("the type of given list is :" ,type(list3))


# In[11]:


list4 = list((11,12,13,14,15,"a","b","c"))
print(list4)
print("the type of given list is :" ,type(list4))


# ### creating a nested list

# In[13]:


list5 = [11,12,13,[14,15,"a","b"],"c"]
print(list5)
print("the type of given list is :" ,type(list5))


# ### verifying for features

# # 1 list are mutable

# In[26]:


list8


# In[33]:


list8.append(10)


# In[34]:


list8


# # 2 list are ordered

# In[29]:


list7 = [1,2,5,6,7]
list7


# # 3 list can have duplicate values

# In[17]:


list8 = [1,2,5,6,7,5,6,7]
list8


# # 4 elements in the list can be accessed using index

# In[18]:


list8


# In[19]:


len(list8)


# In[21]:


list8[7]


# In[22]:


list8[5]


# # methods

# In[24]:


list8 = [1,2,5,6,7,5,6,7,0,"a",2,3]
list8


# In[30]:


list8.append(10)


# In[32]:


list8


# In[35]:


list8.append("z")


# In[37]:


list8


# In[39]:


list8.clear()


# In[20]:


list8


# In[4]:


list8 = [1,1,2,5,6,7,5,6,7,0,"a",2,3]
list8


# In[5]:


list8.copy()


# In[6]:


list8.count(1)


# In[7]:


list8.count("z")


# In[8]:


list8.extend((1,2,3))


# In[9]:


list8


# In[10]:


list8.index("a")


# In[11]:


list8.insert(6,"sravan")


# In[18]:


list8


# In[ ]:





# In[19]:


list8.insert(7,"sravan")


# In[14]:


list8[6]


# In[15]:


list8.pop()


# In[62]:


list8


# In[64]:


list8.remove("sravan")


# In[66]:


list8


# In[67]:


list8.remove(1)


# In[68]:


list8


# In[69]:


list8.reverse()


# In[70]:


list8


# In[72]:


list8.sort() # sort founction on;y works for homogeneus 


# In[73]:


list9=[2,3,2,3,2,32]


# In[74]:


list9.sort()


# In[75]:


list9


# In[79]:


list9.sort(reverse=True)


# In[77]:


list9


# In[81]:


list9_copy


# ## tuple

# In[82]:


tup1=(1,2,3)


# In[83]:


tup1


# In[87]:


tup2=tuple((1,2,2,5,6,8))


# ## 

# In[89]:


tup2


# In[92]:


tup2.count(2)


# In[97]:


tup2.index(5)


# In[2]:


purle = (200,200,150)
def darken(color):
    return color


# In[3]:


c


# In[ ]:




