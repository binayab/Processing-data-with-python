#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Simple example of processing data with Python.
#Using pandas to create a dataframe, read from csv and json
#clean, analyze and use dataset to select specific columns or select row by value


# In[46]:


#Creating a Pandas DataFrame

import pandas as pd
#creating canned data
data = {'Week':pd.Series(['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'])
        ,'Snowfall':pd.Series(['3.5','0.1','1.00','0','4.6','1.0','0.2'])}

#Reading from a dataframe
dfcanned = pd.DataFrame(data)
print("Amount of Snowfall (in) each day of the week: \n",dfcanned)


# In[12]:


#Reading from a csv 

dfc = pd.read_csv(r'C:\Users\prati\Desktop\data.csv')
print("Reading from a csv File, The Monthly Rainfall and Temperature data:\n",dfc)


# In[24]:


#Reading from a json file

df = pd.read_json(r'C:\Users\prati\data.json')
print("Reading from a json file:\n",df)


# In[ ]:


#Next Cleaning the data:


# In[29]:


#Filling '0' in the missing values

dfzeros = df.fillna(0)
print("The data with zeroed values: \n")
print(dfzeros)


# In[28]:


#Removing rows that have invalid data 

dfclean = df.dropna()
print("The data with dropped values: \n")
print(dfclean)


# In[31]:


#Counting number of rows with NaNs

count = 0
for index, row in df.iterrows():
    if any(row.isnull()):
        count = count + 1
        
print("Total Number of rows with Nans: "+str(count))


# In[34]:


#Basic Data Analysis

print("Mean: ",dfclean.mean())
print("\nMedian: ",dfclean.median())
print("\nStandard Deviation: ",dfclean.std())


# In[ ]:


#Data Subset


# In[41]:


#Indexing to print the rainfall and mean for first three months

rainfall = dfclean['Rainfall'][0:3]
print("Rainfall\n",rainfall)
print("Mean Rainfall for first 3 months is: ",rainfall.mean())


# In[42]:


#Using Indexing to select multiple columns from the dataset
#Printing just temperature and rainfall

dftr = (dfclean[['Temperature','Rainfall']])
print(dftr)


# In[45]:


#loc function to selecting a specific row using a certain value

#Need to create a index as to use a loc function, we need to have a properly indexed framework
index = dfclean['Month']
dfIndexed = dfclean.set_index(index)
print("Selects a row by value \n", dfIndexed.loc['March'])


# In[ ]:




