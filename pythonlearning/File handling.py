#!/usr/bin/env python
# coding: utf-8

# In[1]:


open("C:\Users\agroj\OneDrive\Documents\Desktop\NEW.txt")


# In[7]:


file = open(r"C:\Users\agroj\OneDrive\Documents\Desktop\NEW.txt")


# In[8]:


file


# In[9]:


file.read()


# In[10]:


file.readable()


# In[11]:


file.readline()


# In[12]:


file.tell()


# In[14]:


file.seek(10)


# In[15]:


file.readline()


# In[16]:


file.readline()


# In[17]:


file.seek(0)
file.readline()


# In[18]:


file.seek(10)
file.readline()


# ## creating a file using write mode

# In[52]:


f=open(r"C:\Users\agroj\OneDrive\Documents\Desktop\Sample.txt","w")


# In[53]:


f


# In[54]:


f.writable()


# In[55]:


f.write("I AM SRAVAN")


# In[56]:


f.close()


# In[57]:


f.writelines(["iam sravan""good boy""living in hyd"])


# In[58]:


f=open(r"C:\Users\agroj\OneDrive\Documents\Desktop\Sample.txt","w")


# In[59]:


f.writelines(["iam sravan","good boy","living in hyd"])


# In[60]:


file.close()


# In[78]:


f1=open(r"C:\Users\agroj\OneDrive\Documents\Desktop\sravan.txt","w")


# In[79]:


f1


# In[80]:


f1.writable()


# In[81]:


f1.write("iam good boy")


# In[82]:


f1.close()


# In[83]:


f1=open(r"C:\Users\agroj\OneDrive\Documents\Desktop\sravan.txt","w")


# In[84]:


f1.writable()


# In[85]:


f1.writelines(["iam good boy\n","sravan\n","hyd"])


# In[86]:


f1.close()


# # appending the content in existing file

# In[93]:


t = open(r"C:\Users\agroj\OneDrive\Documents\Desktop\sravan.txt","a")


# In[94]:


t


# In[95]:


t.write("\ni love books")


# In[96]:


t.close()


# In[100]:


t = open(r"C:\Users\agroj\OneDrive\Documents\Desktop\sravan.txt","r+")


# In[101]:


t.read()


# In[102]:


t.write("jai sri ram")


# In[103]:


t.close()


# In[106]:


t = open(r"C:\Users\agroj\OneDrive\Documents\Desktop\sravan.txt","r+")


# In[107]:


t.writelines(["sravan","sai"])


# In[109]:


t.close()


# In[1]:


t = open(r"C:\Users\agroj\OneDrive\Documents\Desktop\sravan.txt","r+")


# In[2]:


t.readable()


# In[3]:


t.read()


# In[4]:


t.write("kirshna")


# In[5]:


t.close()


# In[6]:


t = open(r"C:\Users\agroj\OneDrive\Documents\Desktop\sravan.txt","r+")


# In[7]:


t.read()


# In[8]:


t = open(r"C:\Users\agroj\OneDrive\Documents\Desktop\sravan.txt","r+")


# In[10]:


t.write("srvan")


# In[11]:


t.seek(0)
t.read()


# In[12]:


t.close()


# # create a file using create mode

# In[16]:


a = open(r"C:\Users\agroj\OneDrive\Documents\Desktop\sai.txt","x")


# In[15]:


a


# # context method

# In[23]:


a = open(r"C:\Users\agroj\OneDrive\Documents\Desktop\s.txt", "x")


# In[27]:


with open(r"C:\Users\agroj\OneDrive\Documents\Desktop\s.txt", "w") as a:
    a.write("sravan")


# In[28]:


a.close()


# In[ ]:




