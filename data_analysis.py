#!/usr/bin/env python
# coding: utf-8

# In[30]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


import pandas as pd

df = pd.read_csv("C:\\Users\\\\Downloads\\archive\\training_data_with_weather_info_week_1.csv")


# In[46]:


df.shape


# In[47]:


df.dtypes


# In[45]:


df.isnull().values.any()


# In[4]:


#Have a look on data
df.head()


# In[8]:


#numberof unique value
df.nunique()


# In[17]:


df_india = df[df['Country/Region'] =='India'].nunique()


# In[21]:


df['Country/Region'] .value_counts()


# In[27]:


#using groupby on country and count ID 
df.groupby('Country/Region')['Id'].count().max()


# In[35]:


df['Country/Region'].value_counts()[:30].plot(kind='bar')


# In[36]:


df.describe()


# In[41]:


df_top_five_countries = df['Country/Region'].value_counts()[:5]

print(df_top_five_countries)
df_top_five_countries.plot(kind='pie')


# In[55]:


#cases in a country

df[:2000].groupby('Country/Region')['ConfirmedCases'].plot(kind='bar')

