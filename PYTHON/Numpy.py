#!/usr/bin/env python
# coding: utf-8

# In[3]:


get_ipython().system('pip install numpy')


# In[2]:


import numpy as S # using library by import keyword


# In[5]:


S.__version__


# In[6]:


arr = S.array([1,2,3,4,5,6])
print(arr)
print(type(arr))


# # features of numpy

# ## 1.its fast

# In[7]:


list1 = list([1,2,3,4,5,6])
arr1 = S.array(list1)
print(arr1)
print(type(arr1))


# In[8]:


list2 = list((1,2.3,3,4,5,6))
arr2 = S.array(list2)
print(arr2)
print(type(arr2))


# In[9]:


list3 = list(("1",2,3,4,5,6))
arr3 = S.array(list3)
print(arr3)
print(type(arr3))
list4 = list((1,2.3,3,4,5,6))
arr4 = S.array(list4)
print(arr4)
print(type(arr4))
arr3.ndim


# In[10]:


list1


# In[11]:


for i in arr1:
    print(i*i)


# In[12]:


arr1 **2


# ## consume less memory

# In[13]:


import sys


# In[14]:


get_ipython().run_cell_magic('time', '', 'list1\n')


# In[15]:


sys.getsizeof(list1)


# In[16]:


sys.getsizeof(arr1)


# In[17]:


list1


# In[18]:


arr2 = S.array(list1,dtype="int8")


# In[19]:


sys.getsizeof(arr2)


# ## supports multiple modules

# In[20]:


import math


# In[21]:


math.pi


# In[22]:


S.pi


# In[23]:


##help("numpy")


# # creating differemt dim array

# # 0D

# In[24]:


d = S.array((2))
print(type(d))
print(d.ndim)


# # 1D

# In[25]:


d1 = S.array((2,1,2,3,))
print(type(d1))
print(d1.ndim)


# # 2D

# In[26]:


d2 = S.array(((2,1,2,3,),(4,5,6,7)))
print(type(d2))
print(d2.ndim)
print(d2)
d3 = S.array([[2,1,2,3,],[4,5,6,7]])
print(type(d3))
print(d3.ndim)
print(d3
     )


# # 3D

# In[27]:


d4 = S.array((((2,1,2,3,),(4,5,6,7))))
print(type(d4))
print(d4.ndim)
print(d4)
d5 = S.array([[[2,1,2,3,],[4,5,6,7]]])
print(type(d5))
print(d5.ndim)
print(d5)


# In[28]:


a = S.arange(1,20)
print(a)
print(type(a))


# In[29]:


b = S.linspace(1,20,3)
print(b)
print(type(b))


# In[30]:


c = S.zeros((2,5))


# In[31]:


c


# In[32]:


d = S.zeros((2,5))
d


# In[33]:


f = S.full((2,5),8)
f


# In[34]:


S.identity(5)


# In[35]:


S.eye(2,5)


# # Attributes of an array

# In[36]:


arr = S.array(S.arange(1,10))
arr


# In[37]:


S.shape(arr)


# In[38]:


S.size(arr)


# In[39]:


arr.itemsize


# In[40]:


arr.nbytes


# In[41]:


S.ndim(arr)


# # copy v/s view

# In[42]:


arr1d = S.array(S.arange(1,10))
arr


# In[43]:


arr1d_copy=arr1d.copy()
arr1d_copy


# In[44]:


arr1d_copy[4]=10


# In[45]:


arr1d_copy


# In[46]:


arr1d


# In[47]:


arr1d_view=arr1d.view()


# In[48]:


arr1d_view


# In[49]:


arr1d_view[-1]=10


# In[50]:


arr1d_view


# In[51]:


arr1d


# # flatten v/s ravel

# In[52]:


arr3d = S.array(S.arange(21,30),ndmin=3)
arr3d


# In[53]:


arr3d.ndim


# In[54]:


arr3d_flatten=arr3d.flatten()


# In[55]:


arr3d_flatten[1]=10


# In[56]:


arr3d_flatten


# In[57]:


arr3d


# In[58]:


arr3d_ravel=arr3d.ravel()


# In[59]:


arr3d_ravel[5]=10


# In[60]:


arr3d_ravel


# In[61]:


arr3d


# # Reshape and resoze

# In[62]:


arr5d = S.array(S.arange(1,10),ndmin=5)


# In[63]:


arr5d


# In[64]:


arr5d_reshape=S.reshape(arr5d,(3,3))
arr5d_reshape


# In[65]:


arr5d_reshape=S.reshape(arr5d,(9,1))
arr5d_reshape


# In[66]:


arr5d_reshape=S.reshape(arr5d,(1,9))
arr5d_reshape


# In[67]:


arr5d_reshape=S.reshape(arr5d,(3,4))
arr5d_reshape


# In[68]:


arr5d_reshape=S.reshape(arr5d,(3,3))
arr5d_reshape


# In[69]:


arr5d_reshape[0][2]=10


# In[70]:


arr5d_reshape


# In[71]:


arr5d


# In[72]:


arr5d_resize=S.resize(arr5d,(3,3))


# In[73]:


arr5d_resize


# In[74]:


arr5d_resize[0][2]=1


# In[75]:


arr5d_resize


# In[76]:


arr5d


# In[77]:


arr5d_resize=S.resize(arr5d,(6,3))
arr5d_resize


# # indexing and slicing

# In[78]:


arr1d = S.array(S.arange(1,20,3))
arr1d


# In[79]:


arr1d[3]


# In[80]:


arr1d[-3]


# In[81]:


arrd = S.array(S.arange(1,20,3))
arrd


# In[82]:


arrd[:5:-1]


# In[83]:


arrd[0:-1:1]


# In[84]:


arr2d = S.array(S.arange(1,10),ndmin=2)


# In[85]:


arr2d


# In[86]:


arr2d[0]


# In[87]:


arr2d[0][3]


# In[88]:


arr2d3r3c=S.array([[1,2,3],
                   [4,5,6],
                   [7,8,9]])


# In[89]:


arr2d3r3c


# In[90]:


arr2d3r3c[0][1]


# In[91]:


arr2d3r3c[0:3:2,0:3:2]


# In[92]:


arr2d3r3c[1::,1::]


# In[93]:


arr2d3r3c=S.array([[11,12,13],
                   [14,15,16],
                   [17,18,19]])


# #access the following element using indexing and slicing
# 1.13
# 2.19
# 3.15
# 4.11
# 5.17

# In[94]:


arr2d3r3c[0][2]


# In[95]:


arr2d3r3c[2][2]


# In[96]:


arr2d3r3c[1][1]


# In[97]:


arr2d3r3c[0][1]


# In[98]:


arr2d3r3c[2][0]


# In[99]:


print(arr2d3r3c[0:1:1,2:3:1])
print(arr2d3r3c[2:3:1,2:3:1])
print(arr2d3r3c[1:2:,1:2:])
print(arr2d3r3c[0:1:1,0:1:1])
print(arr2d3r3c[2:3:,0:1:])


# # 3d array

# In[100]:


arr3=S.array([[[11,12,13],
              [14,15,16],
              [17,18,19]],
             [[1,12,13],
              [14,15,16],
              [17,18,19]]])
arr3


# In[101]:


arr3[1]


# In[102]:


arr3[0][1:2,1:2]


# In[103]:


arr3[0][1][1]


# # fancy indexing

# In[104]:


arr2d3r3c=S.array([[11,12,13],
                   [14,15,16],
                   [17,18,19]])


# In[105]:


arr2d3r3c[[0,2],[2,0]]


# In[106]:


arr3=S.array([[[11,12,13],
              [14,15,16],
              [17,18,19]],
             [[1,12,13],
              [14,15,16],
              [17,18,19]]])


# In[107]:


arr3[0][[0,2],[2,0]]


# In[108]:


S.iinfo("int8")


# In[109]:


S.finfo("float16")


# In[110]:


-6.55040e+04


# In[111]:


6.55040e+04


# # array operations

# ## arthmetic operations[+,-,*,/,%,//,**]

# In[112]:


arr2d3r3c


# In[ ]:





# In[113]:


arr2d3r3c *5


# ## comparision operations

# In[115]:


arr2d3r3c[arr2d3r3c>15]


# # Array broadcasting

# ## 
