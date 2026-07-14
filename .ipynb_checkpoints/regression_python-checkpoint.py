#!/usr/bin/env python
# coding: utf-8

# this notebook demonstrates a simple linear regression analysis using [Python/R] to model salary based on years of experience

# In[1]:


pip install pandas


# In[3]:


pip install matplotlib


# In[4]:


## importing required libraries
import pandas as pd
import matplotlib.pyplot as plt


# In[5]:


df = pd.read_csv('regression_data.csv')


# In[6]:


df.head()


# In[9]:


plt.scatter(df['YearsExperience'], df['Salary'])
plt.xlabel('Years of Experience')
plt.ylabel('Salary')


# In[ ]:




