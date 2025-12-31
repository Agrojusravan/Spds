#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as P


# # creating a series

# ## 1.Using list

# In[3]:


l1 = list((11,12,13,14,15))
print(l1)
print(type(l1))

print("-----------")
ser_list = P.Series(l1)
print(ser_list)
print(type(ser_list))


# ## 2 Using a Tuple

# In[4]:


tup1 = tuple([11,12,13,14,15])
print(tup1)
print(type(tup1))

print("-----------")
ser_tuple = P.Series(l1)
print(ser_tuple)
print(type(ser_tuple))


# ## 3 using a numpy array

# In[5]:


import numpy as N


# In[6]:


arr1 = N.array(N.arange(31,36))
print(arr1)
print(type(arr1))

print("-----------")
ser_numpyarray = P.Series(l1)
print(ser_numpyarray)
print(type(ser_numpyarray))


# # Assigning Custom index Values

# In[7]:


l2 = list((41,42,43,44))
print(l2)
print(type(l2))
ser_l2=P.Series(l2,index=["a","b","c","d"])
print(ser_l2)
print(type(ser_l2))


# # changing no of bits used to store elements

# In[8]:


l2 = list((41,42,43,44))
print(l2)
print(type(l2))
ser_l2=P.Series(l2,dtype="int8")
print(ser_l2)
print(type(ser_l2))


# # Adding name to the series

# In[9]:


l2 = list((41,42,43,44))
print(l2)
print(type(l2))
ser_l2=P.Series(l2,name="this is series store tha sewquence from 41 to 45")
print(ser_l2)
print(type(ser_l2))


# # use index , use dtype , use name 

# In[10]:


l2 = list((41,42,43,44))
print(l2)
print(type(l2))
ser_l2=P.Series(l2,index=["a","b","c","d"],dtype="int8",name="this is series store tha sewquence from 41 to 45")
print(ser_l2)
print(type(ser_l2))


# In[11]:


a=P.Series(l2,copy=True)  # copy it does not effect original value


# In[12]:


a[0]=5
a


# In[13]:


a


# In[14]:


l2


# In[15]:


a=P.Series(l2,copy=False)
a[0]=5
a


# In[16]:


l2


# In[17]:


a = N.array([11,12,13,14,15])
df = P.Series(a,copy = False)
print(df)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# # Data frame

# In[18]:


data = {"NAME":["karan","arjun","yash","shanshank","tajesh","raj","kush","leela","shibaram","shiva"],
       "AGE":[21,22,23,24,25,26,27,28,29,30],
       "CITY":["pune","chennai","surat","hyderabd","mumbai","delhi","punjab","amrit","shimla","goa"]}


# In[19]:


data


# In[20]:


dataframe_dictionary=P.DataFrame(data)

dataframe_dictionary
# In[21]:


dataframe_dictionary


# In[22]:


list_=[["science",19],["maths",18],["history",17],["geo",16]]
dataframe_list=P.DataFrame(list_)
dataframe_list


# In[23]:


list_=[["science",19],["maths",18],["history",17],["geo",16]]
dataframe_list=P.DataFrame(list_,columns=["subject","marks"])
dataframe_list


# In[24]:


list_=[["science",19],["maths",18],["history",17],["geo",16]]
dataframe_list=P.DataFrame(list_,columns=["subject","marks"],index=["a","b","c","d"])
dataframe_list


# # Attributes

# In[25]:


data = {"NAME":["karan","arjun","yash","shanshank","tajesh","raj","kush","leela","shibaram","shiva"],
       "AGE":[21,22,23,24,25,26,27,28,29,30],
       "CITY":["pune","chennai","surat","hyderabd","mumbai","delhi","punjab","amrit","shimla","goa"]}
df=P.DataFrame(data)
df


# In[26]:


df.shape


# In[27]:


df.shape[0]


# In[28]:


df.shape[1]


# In[29]:


df.dtypes


# In[30]:


df.columns


# In[31]:


df.describe


# In[32]:


df.describe()


# In[33]:


df.describe(percentiles=[.1,0.99])


# In[34]:


df.describe(include="all")


# In[35]:


df.describe(exclude="int")


# In[36]:


df.info()


# In[37]:


df.head(2)


# In[38]:


df.head()


# In[39]:


df.tail()


# In[40]:


df.tail(2)


# ## Statistacal Measures

# In[41]:


marks = N.array([50,60,55,61,70,75,80,85,90,95])
hr_study = N.array([2,3,4,2,5,3,6,4,7,8])


# In[42]:


hr_study


# In[43]:


marks


# ## creating a data frame tha calculate

# In[44]:


df = P.DataFrame((marks,hr_study),index=["marks","hr_study"])


# In[45]:


df


# In[46]:


df.mean()


# In[47]:


df.mean(axis=1)


# In[48]:


dft = df.T


# In[49]:


dft.mean()


# In[50]:


df.mean(axis=1)


# In[51]:


dft.mean()


# In[52]:


dft.median()


# In[53]:


dft.mode()


# In[54]:


dft.var()


# In[55]:


dft.var(ddof=0)


# In[56]:


dft.std(ddof=0)


# In[57]:


dft.cov()


# In[58]:


dft.skew()


# In[59]:


dft.median()


# In[60]:


dft.mean()


# In[61]:


dft.corr()


# # FILE HANDLING

# In[62]:


df = P.read_csv(r"C:\Users\agroj\Downloads\4777664-Pandas_Datasets\Datasets\adult_csv.csv")


# In[63]:


df


# In[64]:


df.info()


# In[65]:


df.mean(numeric_only=True)


# In[66]:


a=df["capitalloss"]


# In[67]:


a.mean()


# In[68]:


df = P.read_csv(r"C:\Users\agroj\Downloads\4777664-Pandas_Datasets\Datasets\adult_csv.csv",usecols=["age","education","sex"])


# In[69]:


df


# In[70]:


df = P.read_csv(r"C:\Users\agroj\Downloads\4777664-Pandas_Datasets\Datasets\adult_csv.csv",nrows=10)


# In[71]:


df


# # Header issue

# In[72]:


sam = P.read_csv(r"C:\Users\agroj\Downloads\4777664-Pandas_Datasets\Datasets\sample.csv")


# In[73]:


sam


# In[74]:


sam_h =P.read_csv(r"C:\Users\agroj\Downloads\4777664-Pandas_Datasets\Datasets\sample.csv",header=1)


# In[75]:


sam_h


# # Readin encoded files

# In[76]:


diwali = P.read_csv(r"C:\Users\agroj\Downloads\4777664-Pandas_Datasets\Datasets\Diwali Sales Data.csv")


# In[77]:


import chardet


# In[79]:


with open(r"C:\Users\agroj\Downloads\4777664-Pandas_Datasets\Datasets\Diwali Sales Data.csv","rb") as file :
    print(chardet.detect(file.read()))


# In[81]:


diwali = P.read_csv(r"C:\Users\agroj\Downloads\4777664-Pandas_Datasets\Datasets\Diwali Sales Data.csv",encoding="ISO-8859-1")


# In[82]:


diwali


# In[83]:


encoding_technique = [
    "ASCII",
    "UTF-8",
    "UTF-16",
    "UTF-32",
    "ISO-8859-1",
    "Windows-1252",
    "UTF-7",
    "UTF-EBCDIC",
    "UTF-16LE",
    "UTF-16BE",
    "UTF-32LE",
    "UTF-32BE",
    "ISO-8859-2",
    "ISO-8859-3",
    "ISO-8859-4",
    "ISO-8859-5",
    "ISO-8859-6",
    "ISO-8859-7",
    "ISO-8859-8",
    "ISO-8859-9",
    "ISO-8859-10",
    "ISO-8859-11",
    "ISO-8859-13",
    "ISO-8859-14",
    "ISO-8859-15",
    "ISO-8859-16",
    "KOI8-R",
    "KOI8-U",
    "GB2312",
    "GBK",
    "Shift_JIS",
    "EUC-JP"
]


# In[84]:


len(encoding_technique)


# In[87]:


for i in encoding_technique:
    try:
        P.read_csv(r"C:\Users\agroj\Downloads\4777664-Pandas_Datasets\Datasets\Diwali Sales Data.csv",encoding=i)
        print(i)
    except:
        pass


# In[88]:


for i in encoding_technique:
    try:
        P.read_csv(r"C:\Users\agroj\Downloads\4777664-Pandas_Datasets\Datasets\Diwali Sales Data.csv",encoding=i)
        print(i)
    except:
        print("hii")


# In[89]:


diwali = P.read_csv(r"C:\Users\agroj\Downloads\4777664-Pandas_Datasets\Datasets\Diwali Sales Data.csv",encoding="GBK")


# In[90]:


diwali


# In[91]:


P.read_csv(r"C:\Users\agroj\Downloads\4777664-Pandas_Datasets\Datasets\ENcoding\Sample_Data.tsv")


# In[101]:


a = P.read_csv(r"C:\Users\agroj\Downloads\4777664-Pandas_Datasets\Datasets\ENcoding\Sample_Data.tsv",sep="\t")


# In[102]:


P.read_csv(r"C:\Users\agroj\Downloads\4777664-Pandas_Datasets\Datasets\ENcoding\Sample_Data.tsv",delimiter="\t")


# In[103]:


a.to_csv(r"C:\Users\agroj\OneDrive\Documents\Desktop\Cleandeddata")


# In[104]:


P.read_csv(r"C:\Users\agroj\OneDrive\Documents\Desktop\Cleandeddata")


# In[105]:


P.read_csv(r"C:\Users\agroj\Downloads\4777664-Pandas_Datasets\Datasets\reduced_household_power_consumption.txt")


# In[106]:


P.read_csv(r"C:\Users\agroj\Downloads\4777664-Pandas_Datasets\Datasets\reduced_household_power_consumption.txt",sep=";")


# # openimg excel gile

# In[111]:


pip install xlrd


# In[112]:


P.read_excel(r"C:\Users\agroj\Downloads\4777664-Pandas_Datasets\Datasets\Sample - Superstore.xls")


# In[116]:


P.read_excel(r"C:\Users\agroj\Downloads\4777664-Pandas_Datasets\Datasets\Sample - Superstore.xls",sheet_name=2)


# In[117]:


P.read_json(r"C:\Users\agroj\Downloads\4777664-Pandas_Datasets\Datasets\iris.json")


# In[120]:


P.read_clipboard()


# In[122]:


P.read_html("https://www.indiatoday.in/sports/ipl/points-table")


# # Slicing and indexing 

# ## `Accessing the entire record

# ## using loc[row_label,column_label]->labelled basesd indexing

# In[3]:


df = P.DataFrame({"Name":["karan","Arjun","Yash","Raj"],
                 "Age":[21,24,28,29],
                 "city":["pune","satara","beed","sangali"]},index = ["g","h","i","j"])
df


# In[8]:


df.loc["g",:]


# In[14]:


df.loc["g","Name","Age"]


# In[15]:


df.loc["g",["Name","Age"]]


# In[16]:


df.loc["g","Name":"Age"]


# # using ilac

# In[17]:


df.iloc[0,0]


# In[4]:


df


# In[5]:


df.iat[2,2]


# # practical

# In[12]:


loan = P.read_csv(r"C:\Users\agroj\Downloads\clean_loandata.csv")
loan


# In[13]:


loan.info()


# In[29]:


loan[loan["Gender"]=="Male"]


# In[31]:


# Q1. What is the average annual income of Male applicants?
loan.loc[loan["Gender"]=="Male","Annual_Income"].mean()


# In[35]:


# Q2. What is the average annual income of Female applicants?
loan.loc[loan["Gender"]=="Female","Annual_Income"].mean()


# In[37]:


# Q3. What is the maximum loan amount among applicants younger than 30 years?
loan.loc[loan["Age"]<30,"Loan_Amount"].max()


# In[38]:


loan.head(1)


# In[51]:


# Q4. How many applicants have annual income greater than 500,000?
sum(loan["Annual_Income"]>500000)


# In[52]:


len(loan[loan["Annual_Income"]>500000])


# In[53]:


(loan[loan["Annual_Income"]>500000]).count()


# In[44]:


# Q5. Find the minimum loan amount sanctioned to an applicant from the Urban area.
loan.loc[loan["Property_Area"]=="Urban","Loan_Amount"].min()


# In[55]:


# Q6. What is the average loan amount of Married applicants?
loan.loc[loan["Married"]=="Yes","Loan_Amount"].mean()


# In[56]:


# Q7. What is the variance of loan amount among Graduate applicants?
loan.loc[loan["Education"]=="Graduate","Loan_Amount"].var()


# In[71]:


# Q8. Find the maximum loan amount of Female applicants who are Unmarried and live in Semiurban area.
loan.loc[(loan["Gender"]=="Female")&(loan["Married"]=="No")&(loan["Property_Area"]=="Semiurban"),"Loan_Amount"].max()


# In[74]:


# Q9. What is the average loan term for Self-Employed applicants?
loan.loc[loan["Employment_Type"]=="Self-Employed","Loan_Term_Months"].mean()


# In[25]:


# Q10. Count how many applicants have a loan term of 360 months.


# In[75]:


sum(loan["Loan_Term_Months"]==360)


# In[82]:


#Q.11 Among Graduate females , what is the average annual income?
loan.loc[(loan["Gender"]=="Female")&(loan["Education"]=="Graduate"),"Annual_Income"].mean()


# In[83]:


#Q. 12 find the maximum loam amount of applicant with 2 or more dependents.
loan.loc[loan["Dependents"]>=2,"Loan_Amount"].max()


# In[90]:


#Q 13 how many applicates are not graduate but have an income above 8000000
loan.loc[(loan["Education"]=="Not Graduate")&(loan["Annual_Income"]>800000)]


# In[92]:


sum(loan.loc[(loan["Education"]=="Not Graduate")&(loan["Annual_Income"]>800000)])


# In[91]:


len(loan.loc[(loan["Education"]=="Not Graduate")&(loan["Annual_Income"]>800000)])


# In[ ]:




