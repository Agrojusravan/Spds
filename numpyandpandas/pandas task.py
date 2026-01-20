#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as P


# In[20]:


import chardet as C


# In[5]:


P.read_csv(r"C:\Users\agroj\Downloads\4777664-Pandas_Datasets\Datasets\ENcoding\Salary Data (3).csv")


# In[21]:


with open(r"C:\Users\agroj\Downloads\4777664-Pandas_Datasets\Datasets\ENcoding\sample_binary_file (2).bin","rb") as file:
    print(C.detect(file.read()))


# In[22]:


P.read_csv(r"C:\Users\agroj\Downloads\4777664-Pandas_Datasets\Datasets\ENcoding\sample_binary_file (2).bin",encoding='ascii')


# In[14]:


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


# In[15]:


for i in encoding_technique:
    try:
        pd.read_csv(r"C:\Users\agroj\Downloads\4777664-Pandas_Datasets\Datasets\ENcoding\sample_binary_file (2).bin",encoding=i)
        print(i)
    except:
        print('failed')


# In[26]:


P.read_csv(r"C:\Users\agroj\Downloads\4777664-Pandas_Datasets\Datasets\ENcoding\Sample_Data (2).tsv",sep="\t")


# In[28]:


P.read_csv(r"C:\Users\agroj\Downloads\4777664-Pandas_Datasets\Datasets\ENcoding\Sample_Data (3).tsv",sep="\t")


# In[29]:


P.read_csv(r"C:\Users\agroj\Downloads\4777664-Pandas_Datasets\Datasets\ENcoding\sample_data_1 (2).csv")


# In[31]:


P.read_csv(r"C:\Users\agroj\Downloads\4777664-Pandas_Datasets\Datasets\ENcoding\sample_data_1 (3).csv")


# In[30]:


P.read_csv(r"C:\Users\agroj\Downloads\4777664-Pandas_Datasets\Datasets\ENcoding\sample_data_ascii (2).csv")


# In[32]:


P.read_csv(r"C:\Users\agroj\Downloads\4777664-Pandas_Datasets\Datasets\ENcoding\sample_data_iso-8859-1 (2).csv")


# In[33]:


P.read_csv(r"C:\Users\agroj\Downloads\4777664-Pandas_Datasets\Datasets\ENcoding\sample_data_iso-8859-2 (2).csv")


# In[34]:


P.read_csv(r"C:\Users\agroj\Downloads\4777664-Pandas_Datasets\Datasets\ENcoding\sample_data_iso-8859-3 (2).csv")


# In[35]:


P.read_csv(r"C:\Users\agroj\Downloads\4777664-Pandas_Datasets\Datasets\ENcoding\sample_dataset_with_outliers (2).csv")


# In[36]:


P.read_csv(r"C:\Users\agroj\Downloads\4777664-Pandas_Datasets\Datasets\ENcoding\sample_text_dataset (2).csv")


# In[37]:


P.read_csv(r"C:\Users\agroj\Downloads\4777664-Pandas_Datasets\Datasets\ENcoding\SampleWeatherData (2).csv")


# In[38]:


P.read_csv(r"C:\Users\agroj\Downloads\4777664-Pandas_Datasets\Datasets\ENcoding\Salary Data (2).csv")


# In[ ]:




