#!/usr/bin/env python
# coding: utf-8

# ### 1 string Representation

# #### using simgle task

# In[1]:


'I am sravan'


# In[2]:


'it is my bag'


# In[3]:


'it's my bag'


# #### using double Quote

# In[4]:


"it's my bag"


# #### multiline string Quote

# In[6]:


''' i
am 
sravan '''


# In[8]:


"""""i
am 
sravan """""


# ### escape characters

# In[11]:


''' i
am 
sravan '''


# In[9]:


'it's my bag'


# ## 1 \'

# In[10]:


'it\'s my bag'


# In[2]:


print('it\'s my bag')


# ## 2 \n

# In[12]:


"i\n am \nsravan"


# In[13]:


print("i\n am \nsravan")


# ## 3 \t

# In[14]:


print("i\tam\tsravan")


# ## 4 \v

# In[5]:


print("i\va\vsravan")


# ## 5 \b

# In[6]:


print("i \bam \bsravan")


# ## 6 adding a slash

# In[18]:


print("C:\Users\agroj\Downloads\Complete Operators.html")


# In[19]:


print("C:\\Users\\agroj\\Downloads\\Complete Operators.html")


# ## 7 using raw string

# In[20]:


print(r"C:\Users\agroj\Downloads\Complete Operators.html")


# In[21]:


r"C:\Users\agroj\Downloads\Complete Operators.html"


# ### Differents way to print

# In[4]:


name = "manoj"
age = 24


# In[5]:


type(name)


# In[6]:


type(age)


# ### joining two or more statement in single printstatement

# ## using + symbol

# In[7]:


print("my name is" + name + "my age is " + age)


# In[11]:


name = "sravan"
age = 22
print("my name is "  + name + " , my age is " , age)


# ### using formate method

# In[23]:


name = "sravan"
age = 24


# In[50]:


print("my Name is {} my Age is {}".formate(name,age))


# ## using f string

# In[19]:


name = "sravan"
age = 22
print("my name is :",name)
print("my name is :",age)


# In[19]:


name = "sravan"
age = 24


# In[20]:


print(f"my name is {name} and my age is {age}")


# In[21]:


name = "sravan"
age = 24


# In[20]:


print("my name is {name} my age is {age}")


# In[ ]:





# ### indexing 

# #### forward indexing

# In[29]:


name = "INNOMATICS RESEARCH LABS"


# In[30]:


name[10]


# In[31]:


name[11]


# In[32]:


name[26]


# #### backward indexing

# In[33]:


name[-20]


# In[34]:


name[-36]


# ### slicing

# In[35]:


name = "manoj"


# In[36]:


name[::]


# In[37]:


name[::-1]


# In[38]:


len(name)


# In[ ]:





# # task

# In[2]:


name = "INNOMATICS RESEARCH LABS"


# In[3]:


len(name)


# In[4]:


print("first element",name[0])


# In[5]:


print("middle element",name[12])


# In[6]:


print("middle element",name[23])


# In[7]:


print("middle element",name[-1])


# ##### middle element

# In[10]:


name = "INNOMATICS RESEARCH LABS"


# In[12]:


middle  = len(name)//2


# In[14]:


name[middle]


# ### slicing conti

# In[31]:


name = "INNOMATICS RESEARCH LABS"


# In[32]:


name[::2]


# In[33]:


name[::1]


# In[34]:


name


# In[35]:


name[::-1]


# In[36]:


name[::-3]


# In[39]:


name[0:7:2]


# In[40]:


name[5:21:5]


# In[41]:


name[21: :4]


# In[42]:


name[-1:-4:-2]


# In[43]:


name[-14:-24:-5]


# In[44]:


name[-4:-21:-10]


# In[45]:


name[-4:-1:1]


# In[46]:


name[-6:-1:5]


# In[47]:


name[24:17:-2]


# In[48]:


name[16:17:1]


# #### string operation

# ### multiply

# In[51]:


name = "karam"


# In[52]:


name*3


# In[ ]:





# ### add/conact

# In[53]:


surname = "shah"


# In[54]:


name+surname


# In[57]:


name+" "+surname


# In[63]:


name+"\t"+surname


# ### length

# In[56]:


len(name)


# In[62]:


print(name+"\t "+surname) #using escape


# ### string methods

# In[2]:


print("\u00df")


# In[17]:


name = "InNoMATICS REsEßACH LaBS"


# In[18]:


name


# ### case conversion operations 

# In[19]:


name = "InNoMATICS REsEAaCH LaBS"


# In[20]:


name.lower()


# In[21]:


name.upper()


# In[22]:


name.title()


# In[23]:


name.capitalize()


# In[24]:


name.casefold() #forcful coversion from anycase takes place


# In[25]:


name.swapcase()


# ### alignment method

# In[26]:


name


# In[27]:


name.ljust(34)


# In[28]:


name.ljust(34,"*")


# In[29]:


name.ljust(20)


# In[30]:


name.rjust(40,"*")


# In[31]:


name.center(39,"*")


# ### trimming method

# In[32]:


name


# In[37]:


name1 = "       InNoMATICS REsEAaCH LaBS        "


# In[34]:


name1.lstrip()


# In[35]:


name1.rstrip()


# In[36]:


name1.strip()


# ### check methods

# In[39]:


name = "InNoMATICS REsEßACH LaBS"


# In[40]:


name.isalpha()


# In[41]:


a = "sravan"


# In[42]:


a.isalpha()


# In[43]:


name.isalnum()


# In[45]:


b = "sra123"


# In[46]:


b.isalpha()


# In[53]:


b.isalnum()


# In[60]:


age = "24"


# In[62]:


age.isdigit()


# In[63]:


age.isnumeric()


# In[64]:


age.isdecimal()


# 

# In[67]:


example = "²³"


# In[68]:


example.isnumeric()


# In[69]:


example.isdecimal()


# In[70]:


example.isdecimal()


# In[71]:


text = "Ⅳ"


# In[72]:


text.isdigit()


# In[73]:


text.isdecimal()


# In[74]:


text.isnumeric()


# In[76]:


name = "INNO"


# In[77]:


name.isupper()


# In[78]:


name.islower()


# In[79]:


name = "INNo"


# In[80]:


name.islower()


# In[81]:


name.isupper()


# In[82]:


name = "inno"


# In[83]:


name.isupper()


# In[84]:


name.islower()


# In[85]:


text1 = "name1"
text2 = "2name"


# In[87]:


text1.isidentifier()


# In[88]:


text2.isidentifier()


# In[89]:


name


# In[90]:


name.startswith("IN")


# In[91]:


name.endswith("o")


# In[94]:


name.endswith("n")


# In[95]:


name.endswith("inno")


# In[96]:


name.endswith("in no")


# In[97]:


name.isupper()


# In[98]:


name.isascii()


# In[99]:


a = "‰"


# In[100]:


a.isascii()


# In[102]:


b = "DEL"


# In[103]:


b.isascii()


# In[104]:


c = "€"


# In[106]:


c.isascii() #beacuse ascii values is onlt takes upto 127


# In[107]:


c.isprintable()


# In[108]:


c.isspace()


# In[109]:


d = "in no"


# In[110]:


d.isspace()


# In[111]:


e =" "


# In[112]:


e.isspace()


# In[113]:


e.istitle()


# In[114]:


b


# In[115]:


b.istitle()


# In[116]:


f = "Inno"


# In[117]:


f.istitle()


# In[118]:


g = "This Is My Book"


# In[119]:


g.istitle()


# ### count and length

# In[122]:


name = "INNOMATICS"


# In[123]:


name.count("o")


# In[124]:


name.count("O")


# In[125]:


name.count("N")


# In[126]:


len(name)


# ### search and replace

# In[127]:


name


# In[128]:


name.find("A")


# In[130]:


name.rfind("A")


# In[131]:


name.find("Z")


# In[133]:


name.find("Z")


# In[134]:


name[2]


# In[135]:


name[22]


# In[136]:


name


# In[141]:


name.index("T")


# In[142]:


name.index("Z")


# In[144]:


name.rindex("T")


# In[146]:


name.rindex("S")


# In[147]:


name


# In[148]:


name.replace("N","n")


# In[150]:


name.replace("Z","x")


# ### split and join

# In[151]:


name


# In[152]:


name.split("N")


# In[153]:


name.split("A")


# In[154]:


name.partition("A")


# In[155]:


name.rpartition("I")


# In[156]:


name.partition("I")


# In[157]:


name.rpartition("I")


# In[159]:


" ".join(name.partition("I"))


# In[160]:


"*".join(name.partition("I"))


# In[161]:


"".join(name.partition("I"))


# ### ENCODE

# In[162]:


name.encode()


# In[163]:


en = "₹"


# In[164]:


en.encode()


# In[169]:


b = b'\xe2\x82\xb9'


# In[170]:


b.decode()


# In[171]:


name


# In[172]:


name.removeprefix("I")


# In[173]:


name.removesuffix("S")


# In[ ]:




