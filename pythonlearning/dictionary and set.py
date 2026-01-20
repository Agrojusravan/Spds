#!/usr/bin/env python
# coding: utf-8

# # dictionary

# ## creating a dictionary

# ### using traditional method

# In[2]:


dict1 = {name : manoj ,age : 24 ,gender : male}
dict1


# In[3]:


dict1 = {"name" : "manoj" ,"age" : 24 ,"gender" : "male"}
dict1


# ### using in-built method

# In[6]:


dict2 = dict(name="sravan",age=25,gender="male")


# In[7]:


dict2


# ### creating nested dictionary 

# In[64]:


info={"name":"sravan","age":24,{"gender":"male"}}


# In[71]:


info={'name':'sravan','age':24,'marks':{'maths': 100,'social':99}}


# In[72]:


info


# In[74]:


info["marks"]


# In[75]:


info["marks"]["social"]


# ### using zip() method

# In[9]:


key = ["name","age","gender"]
value =["sravan",23,"male"]
dict3 = dict(zip(key,value))
dict3


# In[10]:


type(dict1)
type(dict2)
type(dict3)


# ## verifying the features

# In[11]:


dict1


# In[15]:


dict1['name']


# In[16]:


dict1['age']


# In[17]:


dict1['gender']


# # 1 dictionary are mutable

# In[18]:


dict1["name"]="sravan"


# In[19]:


dict1


# # 2 dictionary are ordered

# In[20]:


dict4={"age":23,"salary":200000}


# In[21]:


dict4


# # 3

# In[24]:


dict5 = {"name" : "manoj" ,"age" : 24 ,"gender" : "male","age" : 24 }
dict5


# In[25]:


dict2 = dict(name="sravan",age=25,gender="male",gender="male")


# In[26]:


dict7 = {"name" : "manoj" ,"age" : 24 ,"gender" : "male","age1" : 24 }
dict7


# In[27]:


dict8 = dict(name="sravan",age=25,gender="male",gender1="male")


# In[28]:


dict8


# ## dictionary support indexing 

# In[29]:


dict9 = dict(name="sravan",age=25,gender="male")
dict9


# In[31]:


dict9[9]


# In[33]:


dict9["age"]


# ## methods

# In[35]:


dict2 = {"name" : "manoj" ,"age" : 24 ,"gender" : "male"}
dict2


# In[20]:


dict2.clear()


# In[21]:


dict2


# In[36]:


dict2.copy()


# In[37]:


dict2.fromkeys('name',10)


# In[38]:


dict2.get("name")


# In[40]:


dict2.get("city","hyderabad")


# In[41]:


dict2


# In[42]:


dict2.items()


# In[44]:


dict2.keys()


# In[45]:


dict2.values()


# In[46]:


dict2.pop()


# In[48]:


dict2.pop("name")


# In[49]:


dict2


# In[50]:


dict2.popitem()


# In[51]:


dict2


# In[52]:


dict2.setdefault("name","sravan")


# In[53]:


dict2


# In[54]:


dict3


# In[56]:


dict2.update(dict3)


# In[57]:


dict2


# # sets

# ### using traditional methods

# In[58]:


set1 ={1,2,3,4,45}


# In[59]:


set1


# In[62]:


type(set1)


# ### using in-built method

# In[60]:


set2=set((6,7,8,9,10))


# In[61]:


set2


# In[63]:


type(set2)


# ### features

# ### sets are mutable

# ### sets dont have order
# 

# In[77]:


set1=set((6,7,8,19,10))
set1


# ### set does not duplicate values
# 

# In[79]:


set2=set((6,7,6,8,19,10,11,10,11))
set2


# # methods

# In[73]:


set1=set(("hyderabad","mumbai","vizag","chennai"))
set1


# In[31]:


set1.add("andhra")


# In[32]:


set1


# In[33]:


set2=set(("hyd","mum","viz","chennai"))
set2


# In[34]:


copy_set2=set2.copy()


# In[35]:


copy_set2


# In[36]:


set2.difference(set1)


# In[37]:


set1.difference(set2)


# In[38]:


set1


# In[40]:


set1.difference(set2)


# In[41]:


set1.discard("mumbai")


# In[42]:


set1


# In[43]:


set1


# In[44]:


set2


# In[45]:


set1.intersection(set2)


# In[46]:


set1.intersection_update(set2)


# In[48]:


set1


# In[49]:


set1


# In[50]:


set1=set(("hyderabad","mumbai","vizag","chennai"))
set1


# In[51]:


set2=set(("hyd","mum","viz","chennai"))
set2


# In[52]:


set1.isdisjoint(set2)


# In[54]:


set1.discard("chennai")


# In[56]:


set1


# In[57]:


set1.isdisjoint(set2)


# In[58]:


set1=set(("hyderabad","mumbai","vizag","chennai"))
set1


# In[59]:


set1.issubset(set2)


# In[68]:


set2=set(("hyderbad","mumbai","vizag","chennai"))
set2


# In[69]:


set2.issubset(set1)


# In[70]:


set1


# In[71]:


set2


# In[72]:


set2.issubset(set1)


# In[74]:


set2=set(("hydersetbad","mumbai","vizag","chennai"))
set2


# In[80]:


set1=set(("hyderbad","mumbai"))
set1


# In[81]:


set1.issubset(set2)


# In[82]:


set2.issubset(set1)


# In[83]:


set1.issuperset(set2)


# In[84]:


set2.issuperset(set1)


# In[85]:


set1


# In[86]:


set2


# In[87]:


set1.pop()


# In[95]:


set2.pop()


# In[92]:


set1.pop()


# In[96]:


set1


# In[97]:


set2


# In[98]:


set1


# In[99]:


set1=set(("hyderabad","mumbai","vizag","chennai"))
set1


# In[100]:


set2=set(("hyd","mum","viz","chennai"))
set2


# In[102]:


set1.remove("hyderabad")


# In[103]:


set1


# In[107]:


set2.remove("hyd","mum","viz")


# In[108]:


set2.remove("hyd")


# In[109]:


set2


# In[110]:


set2.remove("hyd")


# In[111]:


set1


# In[112]:


set2


# In[113]:


set1.symmetric_difference(set2)


# In[114]:


set1.symmetric_difference_update(set2)


# In[115]:


set1


# In[116]:


set1.union(set2)


# In[117]:


set1.update(set2)


# In[118]:


set1


# In[119]:


set1


# In[120]:


set2


# In[121]:


set3 = frozenset((1,2,3,4))


# In[122]:


set3


# In[ ]:


type()

