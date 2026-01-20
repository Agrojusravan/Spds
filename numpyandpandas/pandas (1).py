#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as P


# # creating a series

# ## 1.Using list

# In[2]:


l1 = list((11,12,13,14,15))
print(l1)
print(type(l1))

print("-----------")
ser_list = P.Series(l1)
print(ser_list)
print(type(ser_list))


# ## 2 Using a Tuple

# In[3]:


tup1 = tuple([11,12,13,14,15])
print(tup1)
print(type(tup1))

print("-----------")
ser_tuple = P.Series(l1)
print(ser_tuple)
print(type(ser_tuple))


# ## 3 using a numpy array

# In[4]:


import numpy as N


# In[5]:


arr1 = N.array(N.arange(31,36))
print(arr1)
print(type(arr1))

print("-----------")
ser_numpyarray = P.Series(l1)
print(ser_numpyarray)
print(type(ser_numpyarray))


# # Assigning Custom index Values

# In[6]:


l2 = list((41,42,43,44))
print(l2)
print(type(l2))
ser_l2=P.Series(l2,index=["a","b","c","d"])
print(ser_l2)
print(type(ser_l2))


# # changing no of bits used to store elements

# In[7]:


l2 = list((41,42,43,44))
print(l2)
print(type(l2))
ser_l2=P.Series(l2,dtype="int8")
print(ser_l2)
print(type(ser_l2))


# # Adding name to the series

# In[8]:


l2 = list((41,42,43,44))
print(l2)
print(type(l2))
ser_l2=P.Series(l2,name="this is series store tha sewquence from 41 to 45")
print(ser_l2)
print(type(ser_l2))


# # use index , use dtype , use name 

# In[9]:


l2 = list((41,42,43,44))
print(l2)
print(type(l2))
ser_l2=P.Series(l2,index=["a","b","c","d"],dtype="int8",name="this is series store tha sewquence from 41 to 45")
print(ser_l2)
print(type(ser_l2))


# In[10]:


a=P.Series(l2,copy=True)  # copy it does not effect original value


# In[11]:


a[0]=5
a


# In[12]:


a


# In[13]:


l2


# In[14]:


a=P.Series(l2,copy=False)
a[0]=5
a


# In[15]:


l2


# In[16]:


a = N.array([11,12,13,14,15])
df = P.Series(a,copy = False)
print(df)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# # Data frame

# In[17]:


data = {"NAME":["karan","arjun","yash","shanshank","tajesh","raj","kush","leela","shibaram","shiva"],
       "AGE":[21,22,23,24,25,26,27,28,29,30],
       "CITY":["pune","chennai","surat","hyderabd","mumbai","delhi","punjab","amrit","shimla","goa"]}


# In[18]:


data


# In[19]:


dataframe_dictionary=P.DataFrame(data)

dataframe_dictionary
# In[20]:


dataframe_dictionary


# In[21]:


list_=[["science",19],["maths",18],["history",17],["geo",16]]
dataframe_list=P.DataFrame(list_)
dataframe_list


# In[22]:


list_=[["science",19],["maths",18],["history",17],["geo",16]]
dataframe_list=P.DataFrame(list_,columns=["subject","marks"])
dataframe_list


# In[23]:


list_=[["science",19],["maths",18],["history",17],["geo",16]]
dataframe_list=P.DataFrame(list_,columns=["subject","marks"],index=["a","b","c","d"])
dataframe_list


# # Attributes

# In[24]:


data = {"NAME":["karan","arjun","yash","shanshank","tajesh","raj","kush","leela","shibaram","shiva"],
       "AGE":[21,22,23,24,25,26,27,28,29,30],
       "CITY":["pune","chennai","surat","hyderabd","mumbai","delhi","punjab","amrit","shimla","goa"]}
df=P.DataFrame(data)
df


# In[25]:


df.shape


# In[26]:


df.shape[0]


# In[27]:


df.shape[1]


# In[28]:


df.dtypes


# In[29]:


df.columns


# In[30]:


df.describe


# In[31]:


df.describe()


# In[32]:


df.describe(percentiles=[.1,0.99])


# In[33]:


df.describe(include="all")


# In[34]:


df.describe(exclude="int")


# In[35]:


df.info()


# In[36]:


df.head(2)


# In[37]:


df.head()


# In[38]:


df.tail()


# In[39]:


df.tail(2)


# ## Statistacal Measures

# In[40]:


marks = N.array([50,60,55,61,70,75,80,85,90,95])
hr_study = N.array([2,3,4,2,5,3,6,4,7,8])


# In[41]:


hr_study


# In[42]:


marks


# ## creating a data frame tha calculate

# In[43]:


df = P.DataFrame((marks,hr_study),index=["marks","hr_study"])


# In[44]:


df


# In[45]:


df.mean()


# In[46]:


df.mean(axis=1)


# In[47]:


dft = df.T


# In[48]:


dft.mean()


# In[49]:


df.mean(axis=1)


# In[50]:


dft.mean()


# In[51]:


dft.median()


# In[52]:


dft.mode()


# In[53]:


dft.var()


# In[54]:


dft.var(ddof=0)


# In[55]:


dft.std(ddof=0)


# In[56]:


dft.cov()


# In[57]:


dft.skew()


# In[58]:


dft.median()


# In[59]:


dft.mean()


# In[60]:


dft.corr()


# # FILE HANDLING

# In[61]:


df = P.read_csv(r"C:\Users\agroj\Downloads\4777664-Pandas_Datasets\Datasets\adult_csv.csv")


# In[62]:


df


# In[63]:


df.info()


# In[64]:


df.mean(numeric_only=True)


# In[65]:


a=df["capitalloss"]


# In[66]:


a.mean()


# In[67]:


df = P.read_csv(r"C:\Users\agroj\Downloads\4777664-Pandas_Datasets\Datasets\adult_csv.csv",usecols=["age","education","sex"])


# In[68]:


df


# In[69]:


df = P.read_csv(r"C:\Users\agroj\Downloads\4777664-Pandas_Datasets\Datasets\adult_csv.csv",nrows=10)


# In[70]:


df


# # Header issue

# In[71]:


sam = P.read_csv(r"C:\Users\agroj\Downloads\4777664-Pandas_Datasets\Datasets\sample.csv")


# In[72]:


sam


# In[73]:


sam_h =P.read_csv(r"C:\Users\agroj\Downloads\4777664-Pandas_Datasets\Datasets\sample.csv",header=1)


# In[74]:


sam_h


# # Readin encoded files

# In[75]:


diwali = P.read_csv(r"C:\Users\agroj\Downloads\4777664-Pandas_Datasets\Datasets\Diwali Sales Data.csv")


# In[ ]:


import chardet


# In[ ]:


with open(r"C:\Users\agroj\Downloads\4777664-Pandas_Datasets\Datasets\Diwali Sales Data.csv","rb") as file :
    print(chardet.detect(file.read()))


# In[ ]:


diwali = P.read_csv(r"C:\Users\agroj\Downloads\4777664-Pandas_Datasets\Datasets\Diwali Sales Data.csv",encoding="ISO-8859-1")


# In[ ]:


diwali


# In[ ]:


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


# In[ ]:


len(encoding_technique)


# In[ ]:


for i in encoding_technique:
    try:
        P.read_csv(r"C:\Users\agroj\Downloads\4777664-Pandas_Datasets\Datasets\Diwali Sales Data.csv",encoding=i)
        print(i)
    except:
        pass


# In[ ]:


for i in encoding_technique:
    try:
        P.read_csv(r"C:\Users\agroj\Downloads\4777664-Pandas_Datasets\Datasets\Diwali Sales Data.csv",encoding=i)
        print(i)
    except:
        print("hii")


# In[ ]:


diwali = P.read_csv(r"C:\Users\agroj\Downloads\4777664-Pandas_Datasets\Datasets\Diwali Sales Data.csv",encoding="GBK")


# In[ ]:


diwali


# In[ ]:


P.read_csv(r"C:\Users\agroj\Downloads\4777664-Pandas_Datasets\Datasets\ENcoding\Sample_Data.tsv")


# In[ ]:


a = P.read_csv(r"C:\Users\agroj\Downloads\4777664-Pandas_Datasets\Datasets\ENcoding\Sample_Data.tsv",sep="\t")


# In[ ]:


P.read_csv(r"C:\Users\agroj\Downloads\4777664-Pandas_Datasets\Datasets\ENcoding\Sample_Data.tsv",delimiter="\t")


# In[ ]:


a.to_csv(r"C:\Users\agroj\OneDrive\Documents\Desktop\Cleandeddata")


# In[ ]:


P.read_csv(r"C:\Users\agroj\OneDrive\Documents\Desktop\Cleandeddata")


# In[ ]:


P.read_csv(r"C:\Users\agroj\Downloads\4777664-Pandas_Datasets\Datasets\reduced_household_power_consumption.txt")


# In[ ]:


P.read_csv(r"C:\Users\agroj\Downloads\4777664-Pandas_Datasets\Datasets\reduced_household_power_consumption.txt",sep=";")


# # openimg excel gile

# In[76]:


pip install xlrd


# In[77]:


P.read_excel(r"C:\Users\agroj\Downloads\4777664-Pandas_Datasets\Datasets\Sample - Superstore.xls")


# In[78]:


P.read_excel(r"C:\Users\agroj\Downloads\4777664-Pandas_Datasets\Datasets\Sample - Superstore.xls",sheet_name=2)


# In[79]:


P.read_json(r"C:\Users\agroj\Downloads\4777664-Pandas_Datasets\Datasets\iris.json")


# In[80]:


P.read_clipboard()


# In[ ]:


P.read_html("https://www.indiatoday.in/sports/ipl/points-table")


# # Slicing and indexing 

# ## `Accessing the entire record

# ## using loc[row_label,column_label]->labelled basesd indexing

# In[ ]:


df = P.DataFrame({"Name":["karan","Arjun","Yash","Raj"],
                 "Age":[21,24,28,29],
                 "city":["pune","satara","beed","sangali"]},index = ["g","h","i","j"])
df


# In[ ]:


df.loc["g",:]


# In[ ]:


df.loc["g","Name","Age"]


# In[ ]:


df.loc["g",["Name","Age"]]


# In[ ]:


df.loc["g","Name":"Age"]


# # using ilac

# In[ ]:


df.iloc[0,0]


# In[ ]:


df


# In[ ]:


df.iat[2,2]


# # practical

# In[83]:


loan = P.read_csv(r"C:\Users\agroj\Downloads\clean_loandata.csv")
loan


# In[84]:


loan.info()


# In[85]:


loan[loan["Gender"]=="Male"]


# In[86]:


# Q1. What is the average annual income of Male applicants?
loan.loc[loan["Gender"]=="Male","Annual_Income"].mean()


# In[87]:


# Q2. What is the average annual income of Female applicants?
loan.loc[loan["Gender"]=="Female","Annual_Income"].mean()


# In[88]:


# Q3. What is the maximum loan amount among applicants younger than 30 years?
loan.loc[loan["Age"]<30,"Loan_Amount"].max()


# In[89]:


loan.head(1)


# In[90]:


# Q4. How many applicants have annual income greater than 500,000?
sum(loan["Annual_Income"]>500000)


# In[91]:


len(loan[loan["Annual_Income"]>500000])


# In[92]:


(loan[loan["Annual_Income"]>500000]).count()


# In[93]:


# Q5. Find the minimum loan amount sanctioned to an applicant from the Urban area.
loan.loc[loan["Property_Area"]=="Urban","Loan_Amount"].min()


# In[94]:


# Q6. What is the average loan amount of Married applicants?
loan.loc[loan["Married"]=="Yes","Loan_Amount"].mean()


# In[95]:


# Q7. What is the variance of loan amount among Graduate applicants?
loan.loc[loan["Education"]=="Graduate","Loan_Amount"].var()


# In[96]:


# Q8. Find the maximum loan amount of Female applicants who are Unmarried and live in Semiurban area.
loan.loc[(loan["Gender"]=="Female")&(loan["Married"]=="No")&(loan["Property_Area"]=="Semiurban"),"Loan_Amount"].max()


# In[97]:


# Q9. What is the average loan term for Self-Employed applicants?
loan.loc[loan["Employment_Type"]=="Self-Employed","Loan_Term_Months"].mean()


# In[98]:


# Q10. Count how many applicants have a loan term of 360 months.


# In[99]:


sum(loan["Loan_Term_Months"]==360)


# In[100]:


#Q.11 Among Graduate females , what is the average annual income?
loan.loc[(loan["Gender"]=="Female")&(loan["Education"]=="Graduate"),"Annual_Income"].mean()


# In[101]:


#Q. 12 find the maximum loam amount of applicant with 2 or more dependents.
loan.loc[loan["Dependents"]>=2,"Loan_Amount"].max()


# In[102]:


#Q 13 how many applicates are not graduate but have an income above 8000000
loan.loc[(loan["Education"]=="Not Graduate")&(loan["Annual_Income"]>800000)]


# In[103]:


sum(loan.loc[(loan["Education"]=="Not Graduate")&(loan["Annual_Income"]>800000)])


# In[104]:


len(loan.loc[(loan["Education"]=="Not Graduate")&(loan["Annual_Income"]>800000)])


# # Groupby

# In[108]:


# Q19. Find the average loan amount of Married Males vs. Married Females.
loan.loc[loan["Married"]=="Yes"].groupby("Gender")["Loan_Amount"].mean()


# In[114]:


# Q20. Find the number of dependents (on average) for Salaried vs. Self-Employed applicants.
loan.groupby("Employment_Type")["Dependents"].mean()


# In[116]:


# Q21. Find the average loan amount by Property Area (Urban, Rural, Semiurban).
loan.groupby("Property_Area")["Loan_Amount"].mean()


# In[119]:


# Q22. Group by Education and find the average loan term.
loan.groupby("Education")["Loan_Term_Months"].mean()


# In[121]:


# Q23. Group by Employment_Type and find the maximum income.
loan.groupby("Employment_Type").max()


# In[122]:


# Q24. Find the average loan amount for each combination of Gender and Married status.
loan.groupby("Gender","Married")["Loan_Amount"]


# In[124]:


loan.groupby(["Gender","Married"])["Loan_Amount"].mean()


# In[127]:


loan.groupby(["Married","Gender"])["Loan_Amount"].mean()


# # query()

# In[131]:


loan.query("Education=='Graduate'")


# # Data frame and Manipolation

# ## Adding A column

# In[2]:


df = P.DataFrame({"Name":["karan","arjun","yash","shashnak"],
                 "Age":[23,21,18,26]})
df


# In[3]:


df["city"]=["pune","satar","jalgaon","sangli"]
df


# ## adding a row

# In[4]:


df.loc[4]=["sravan",22,"hyderabad"]
df


# In[5]:


df.loc[len(df)]=["sai",24,"telangana"]
df


# In[6]:


a = 3
b = 4
a +=1
a


# ## Removing the column

# In[7]:


df


# In[8]:


df.drop("Age")


# In[9]:


df.drop(columns="Age")


# In[10]:


df


# In[11]:


df.drop(columns="Age",inplace=True)


# In[12]:


df


# In[13]:


df.drop(index=1)


# In[14]:


df


# In[15]:


df.drop(index=1,inplace=True)


# In[16]:


df


# In[17]:


df.reset_index()


# In[18]:


df.reset_index(drop=True)


# In[19]:


df.rename(columns={"city":"Place","Name":"surname"})


# In[20]:


df


# In[21]:


df = df.rename(columns={"city":"Place","Name":"surname"})
df


# In[44]:


df1 = P.DataFrame({"ID":[0,2,1,4,5],
                   "salary":[10000,16000,12000,13000,15000],
                   "dept":["police","teacher","doctor","driver","Trainer"]})
df2 = P.DataFrame({"EID":[5,2,7,4,9],
                   "saly":[10000,11000,12000,13000,14000],
                   "dep":["teacher","police","doctor","driver","Trainer"]})


# In[45]:


df1


# In[46]:


df2


# # Types of Merges /Joins
# * inner
# * outer
# * right-join
# * left-join

# In[47]:


df1.merge(df2) # innner join


# In[48]:


df1.merge(df2,on="EID",how="inner")


# In[49]:


df1.merge(df2,left_on="ID",right_on="EID") # innner join


# In[50]:


df1.merge(df2,left_on="salary",right_on="saly") # innner join


# In[51]:


df1.merge(right=df2,how="outer",left_on="ID",right_on="EID") # Outer


# In[52]:


df1.merge(df2,how="left",left_on="ID",right_on="EID")    #left


# In[54]:


df1.merge(df2,how="right",left_on="ID",right_on="EID") # right


# # useful function 1 sort()

# In[56]:


df1 = P.DataFrame({"EmpId":[101,102,103,104,105],
                    "Exp":[4,5,6,5,6],
                    "Salary":[40000,50000,50000,30000,70000]}) 
df1


# In[57]:


df1.sort_values(by=["Salary"])


# In[62]:


df1.sort_values(by=["Salary","EmpId"])


# In[63]:


df1.sort_values(by=["EmpId","Salary"])


# # map and apply

# In[2]:


loan = P.read_csv(r"C:\Users\agroj\Downloads\4777664-Pandas_Datasets\Datasets\loandata.csv")
loan


# In[3]:


loan["Gender"].map({"Male":1,"Female":0})


# In[4]:


loan


# In[5]:


loan["Gender"]=loan["Gender"].map({"Male":1,"Female":0})


# In[6]:


loan


# In[7]:


def cat_to_num(n):
    if n == "Yes":
        return 1
    else :
        return 0


# In[8]:


loan["Married"]


# In[9]:


loan["Married"]=loan["Married"].map(cat_to_num)


# In[10]:


loan


# In[11]:


loan["Education"].apply({"Graduate":1,"Not Graduate":0})


# In[ ]:


def education(n):
    if n == "Graduate":
        return 1
    else :
        return 0


# In[ ]:


loan["Education"].apply(education)


# In[ ]:


loan["Education"]=loan["Education"].apply(education)


# In[ ]:


loan


# In[ ]:


P.concat((df1,df2))


# In[ ]:


P.concat((df1,df2),axis=1)


# # Time Series Analysis

# In[13]:


df = P.DataFrame()


# In[14]:


df["Time"]=[21]


# In[15]:


df


# In[16]:


P.date_range("2/01/2026","10/01/2026")


# In[17]:


P.date_range("2-01-2026","10-01-2026")


# In[19]:


P.date_range("01-01-2026","01-31-2026")


# In[22]:


P.date_range("01-01-2026","01-31-2026",periods=10)


# In[24]:


P.date_range("01-01-2026","01-31-2026",freq="Y")


# In[25]:


df


# In[33]:


df = P.DataFrame()


# In[34]:


df["date_time"] = ['2026-01-01', '2026-01-02', '2026-01-03', '2026-01-04',
               '2026-01-05', '2026-01-06', '2026-01-07', '2026-01-08',
               '2026-01-09', '2026-01-10', '2026-01-11', '2026-01-12',
               '2026-01-13', '2026-01-14', '2026-01-15', '2026-01-16',
               '2026-01-17', '2026-01-18', '2026-01-19', '2026-01-20',
               '2026-01-21', '2026-01-22', '2026-01-23', '2026-01-24',
               '2026-01-25', '2026-01-26', '2026-01-27', '2026-01-28',
               '2026-01-29', '2026-01-30', '2026-01-31']
df


# In[35]:


df.info()


# In[40]:


df["date_time"].astype('datetime64[ns]')


# In[41]:


df.info()


# In[44]:


a = P.read_csv(r"C:\Users\agroj\Downloads\4777664-Pandas_Datasets\Datasets\Time series Data\time_series.csv")
a


# In[45]:


a.info()


# In[48]:


a["datetime"]=a["Datetime"].astype('datetime64[ns]')


# In[49]:


a.info()


# In[62]:


a['Year']=a['Datetime'].dt.year


# In[65]:


a['Datetime']=P.to_datetime(a['Datetime'])


# In[67]:


a['Year']=a['Datetime'].dt.year
a


# In[68]:


a['Month']=a['Datetime'].dt.month


# In[69]:


a


# In[70]:


a["Datetime"].dt.day


# In[73]:


a['Month_name']=a['Datetime'].dt.month_name()
a


# In[77]:


a['Day_name']=a["Datetime"].dt.day_name()
a


# In[79]:


a = P.read_csv(r"C:\Users\agroj\Downloads\4777664-Pandas_Datasets\Datasets\Time series Data\time_series.csv",parse_dates=["Datetime"])


# In[80]:


a


# In[81]:


a.info()


# # Sample

# In[83]:


loan = P.read_csv(r"C:\Users\agroj\Downloads\4777664-Pandas_Datasets\Datasets\loandata (2).csv")
loan


# In[84]:


loan.sample(10)


# In[85]:


loan.sample(frac=0.1)


# # cross table

# In[88]:


loan["Gender"].value_counts()


# In[89]:


loan["Married"].value_counts()


# In[95]:


P.crosstab(index=[loan["Gender"],loan["Education"]],columns=[loan["Married"]])


# In[96]:


P.crosstab(index=[loan["Gender"],loan["Education"]],columns=[loan["Property_Area"]])


# # pivot table

# In[98]:


P.pivot_table(data = loan,index=["Gender","Education"],columns=["Married"],values=["ApplicantIncome"],aggfunc=["mean","median"])


# In[99]:


P.pivot_table(loan,index=["Gender"],columns=["Education"],values=["ApplicantIncome"],aggfunc=["mean","median"])


# In[100]:


P.crosstab(index=[loan["Gender"],loan["Education"],loan["Self_Employed"]],columns=[loan["Property_Area"],loan["Loan_Status"]])


# In[ ]:





