#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as P
import numpy as N


# In[2]:


arr1 = N.array((1,2,N.nan,4,5))
x = P.DataFrame(arr1)
x


# In[3]:


arr2 = N.array((1,2,3,4,5))
y = P.DataFrame(arr2)
y


# In[4]:


from sklearn.linear_model import LinearRegression


# In[5]:


lr = LinearRegression()


# In[6]:


lr.fit(x,y)


# In[ ]:


from sklearn.tree import DecisionTreeRegressor


# In[ ]:


dtr = DecisionTreeRegressor()


# In[ ]:


dtr.fit(x,y)


# # NON vis method

# In[11]:


df = P.read_csv(r"C:\Users\agroj\Downloads\4777664-Pandas_Datasets\Datasets\Data Cleaning\SampleWeatherData.csv")


# In[12]:


df


# In[13]:


df.info() # hoe to get


# In[14]:


df["Time"]=df["Time"].astype("datetime64[ns]") # how to convert
df


# In[15]:


df.isnull()  # if there is missing vvalue -= True


# In[16]:


df.isnull().sum()


# # Visulization method

# In[17]:


pip install missingno


# In[18]:


import missingno 


# In[19]:


missingno.bar(df)


# In[20]:


missingno.bar(df,figsize=(5,3))


# In[21]:


missingno.matrix(df)


# In[22]:


missingno.heatmap(df,figsize=(5,2))


# In[23]:


df


# In[25]:


df.fillna({"Temperature":19.0})


# In[26]:


df.fillna({"Temperature":19.0,"Humidity":52.5})


# In[27]:


df


# In[28]:


df.fillna({"Temperature":19.0,"Humidity":52.5},inplace=True)


# In[29]:


df


# In[31]:


df["Time"].fillna(method="bfill")


# In[33]:


df["Time"].fillna(method="ffill")


# In[34]:


df["Time"].bfill()


# In[36]:


df["Time"].ffill(inplace=True)


# In[37]:


df


# # Stastical value

# In[38]:


df1 = P.read_csv(r"C:\Users\agroj\Downloads\4777664-Pandas_Datasets\Datasets\Data Cleaning\emp_salary.csv")


# In[39]:


df1


# In[44]:


df1.drop(columns = "Unnamed: 0",inplace=True)


# In[45]:


df1


# In[46]:


df1.info()


# In[49]:


df1["Age"].plot(kind="kde",figsize = (3,3))


# In[52]:


x=df1["Age"].mean()
x


# In[55]:


df1["Age"].fillna(x,inplace=True)


# In[56]:


df1


# In[58]:


y=df1["Salary"].mean()
y


# In[59]:


df1["Age"].fillna(y,inplace=True)


# In[60]:


df1


# In[67]:


df1["Salary"].plot(kind="Kde",figsize = (3,3)) 
#kernal density based estimation


# In[66]:


df1["Salary"].plot(kind="kde",figsize = (3,3))


# In[69]:


a = df1["Salary"].median()
a


# In[74]:


df1["Salary"].fillna(a,inplace=True)


# In[75]:


df1


# In[82]:


b = df1["Gender"].mode()
b


# In[86]:


c = df1["Gender"].mode()[0]
c


# In[87]:


df1["Gender"].fillna(c)


# # groupby

# In[89]:


mm = P.read_csv(r"C:\Users\agroj\Downloads\4777664-Pandas_Datasets\Datasets\Data Cleaning\marks_missing.csv")
mm


# In[90]:


mm["Marks"].mean()


# In[93]:


mm.groupby("Grade")["Marks"].transform(lambda x : x.mean())


# In[94]:


mm


# In[108]:


mm["Marks"]=mm.groupby("Grade")["Marks"].transform(lambda x : x.mean())


# In[109]:


mm


# In[113]:


x = N.array([1,2,3,4,5,6,7])
y = N.array([1,2,9,N.nan,25,N.nan,49])
z = P.DataFrame((x,y))
z = z.T
z


# In[114]:


z.interpolate()


# In[115]:


z.interpolate(method="polynomial",order=2)


# # Identifing the Outliers

# ## 1.Domain Knowledge

# In[116]:


df = P.DataFrame({"marks":[-2,4,6,8,10,12,14,16,18,200]})


# In[117]:


df


# In[118]:


df["marks"]>20


# In[119]:


df["marks"]<0


# In[124]:


df[(df["marks"]>20) | (df["marks"]<0)]


# # Statstical way

# ## IQR method

# In[143]:


value = P.read_csv(r"C:\Users\agroj\Downloads\4777664-Pandas_Datasets\Datasets\Data Cleaning\BoxPlot_IQR_Data.csv")
value


# In[ ]:





# In[161]:


def outlier_det_IQR(df,col_name):
    q1 = df[col_name].quantile(0.25)
    q3 = df[col_name].quantile(0.75)
    iqr = q3 - q1
    lb = q1 - (1.5*iqr)
    ub = q3 - (1.5*iqr)
    return df[(df[col_name]<lb),(df[col_name]>ub)]


# In[162]:


outlier_det_IQR(value,"Values")


# In[ ]:





# In[153]:


def outlier_det_IQR(df,col_name):
    q1 = df[col_name].quantile(0.25)
    q3 = df[col_name].quantile(0.75)
    iqr = q3 - q1
    lb = q1 - (1.5*iqr)
    ub = q3 - (1.5*iqr)
    return df[(df[col_name]<lb)|(df[col_name]>ub)]


# In[154]:


outlier_det_IQR(value,"Values")


# In[155]:


def out_det_z(df,col_name):
    mean = df[col_name].mean()
    std = df[col_name].std(ddof=0)
    z = (df[col_name]-mean)/std
    return df[(z<-3)|(z>3)]


# In[156]:


out_det_z(value,"Values")


# In[157]:


def out_det_z(df,col_name):
    mean = df[col_name].mean()
    std = df[col_name].std(ddof=0)
    z = (df[col_name]-mean)/std
    return z


# In[158]:


out_det_z(value,"Values").mean()


# In[159]:


out_det_z(value,"Values").std(ddof=0)


# In[163]:


value["Values"].plot(kind="box",figsize=(5,3))


# In[165]:


df = P.read_csv(r"C:\Users\agroj\Downloads\4777664-Pandas_Datasets\Datasets\Data Cleaning\multivariate_ouliers (2).csv")
df


# In[166]:


df.drop(columns = ["Unnamed: 0"],inplace=True)


# In[167]:


df


# In[169]:


df.plot(x="Exp",y="Salary",kind="scatter",figsize=(3,3))


# # ml models

# In[4]:


ot = P.read_csv(r"C:\Users\agroj\Downloads\4777664-Pandas_Datasets\Datasets\Data Cleaning\multivariate_ouliers.csv")
ot


# In[5]:


ot.drop(columns=["Unnamed: 0"],inplace=True)


# In[6]:


ot


# # 1 KNN algorithm

# In[7]:


pip install pyod


# In[8]:


from pyod.models.knn import KNN


# In[9]:


knn_obj = KNN(n_neighbors=1)


# In[10]:


knn_obj.fit_predict(ot)


# In[11]:


import matplotlib.pyplot as M
import seaborn as S


# In[12]:


M.figure(figsize=(5,4))
S.scatterplot(ot,x="Exp",y="Salary")


# In[13]:


from sklearn.ensemble  import IsolationForest


# In[23]:


if_obj = IsolationForest(contamination=0.1)


# In[24]:


if_obj.fit_predict(ot)


# In[25]:


M.figure(figsize=(4,3))
S.scatterplot(ot,x="Exp",y="Salary",hue=if_obj.fit_predict(ot),palette="tab10")


# # local Outlier Factor

# In[26]:


from sklearn.neighbors import LocalOutlierFactor


# In[30]:


lof_obj = LocalOutlierFactor(contamination=0.1)


# In[31]:


lof_obj.fit_predict(ot)


# In[32]:


M.figure(figsize=(4,3))
S.scatterplot(ot,x="Exp",y="Salary",hue=lof_obj.fit_predict(ot),palette="tab10")


# # Duplicates

# In[2]:


dup = P.read_csv(r"C:\Users\agroj\Downloads\4777664-Pandas_Datasets\Datasets\Data Cleaning\dup.csv")
dup


# In[4]:


dup.duplicated()


# In[5]:


dup.duplicated().sum()


# In[6]:


dup[dup.duplicated()]


# In[7]:


dup[dup.duplicated()].index


# In[9]:


dup.drop_duplicates(inplace=True)


# In[10]:


dup


# In[20]:


dup_col = P.read_csv(r"C:\Users\agroj\Downloads\4777664-Pandas_Datasets\Datasets\Data Cleaning\dup_col.csv")


# In[21]:


dup_col


# In[22]:


dup_col.drop(columns=["Unnamed: 0"],inplace=True)


# In[23]:


dup_col


# In[25]:


dct = dup_col.T
dct


# In[34]:


dct.duplicated()


# In[28]:


dct.duplicated().sum()


# In[29]:


dct.drop_duplicates(inplace=True)


# In[30]:


dct


# In[31]:


dct.T


# In[32]:


dup_col = dct.T


# In[33]:


dup_col


# # Inconsistent data

# In[35]:


inco = P.read_csv(r"C:\Users\agroj\Downloads\4777664-Pandas_Datasets\Datasets\Data Cleaning\incons.csv")


# In[36]:


inco


# In[38]:


inco.drop(columns=["Unnamed: 0"],inplace=True)


# In[39]:


inco


# In[41]:


inco[(inco["Age"]<0) | (inco["Age"]>100)]


# In[42]:


inco.loc[((inco["Age"]<0) | (inco["Age"]>100)),"Age"]


# In[43]:


inco.loc[((inco["Age"]<0) | (inco["Age"]>100)),"Age"] = N.nan


# In[44]:


inco


# In[48]:


inco["Gender"].unique()


# In[47]:


def x(value):
    if value=="M" or value=="male":
        print("Male")
    else :
        print("Female")


# In[50]:


inco["Gender"].apply(x)


# In[51]:


inco


# In[52]:


inco["Gender"]=inco["Gender"].apply(x)
inco


# # note - if there is NaN take elif and keep as it is

# # noicy

# In[53]:


incc = P.read_csv(r"C:\Users\agroj\Downloads\4777664-Pandas_Datasets\Datasets\Data Cleaning\Inncosistent.csv")
incc


# In[59]:


incc["Age"]=incc["Age"].str.replace(r"[^0-9]","",regex=True)


# In[60]:


incc


# In[64]:


incc["Salary"]=incc["Salary"].str.replace(r"[^0-9]","",regex=True)


# In[65]:


incc


# In[ ]:




