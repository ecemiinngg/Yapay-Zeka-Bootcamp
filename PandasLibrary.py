#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd


# In[9]:


pd.__version__


# In[10]:


names = pd.Series(["eco","mary","shell","robin"]) 
#create series
print(names)


# In[7]:


type(names)


# In[12]:


names[0:2]


# In[15]:


names[names.str.startswith("s")] 


# In[16]:


points = pd.Series([60,70,80,90])


# In[20]:


points.mean()


# In[22]:


points.std()


# In[23]:


points.sum()


# In[26]:


production_quantity = pd.Series([100,200,300,400],index=["p1","p2","p3","p4"])
production_quantity


# In[33]:


import datetime
dates=pd.date_range("2024-01-01",periods=10,freq="D")
product_quantity= pd.Series([100,200,300,400,700,1000,1600,2500,3200,4000],index=dates)
product_quantity


# In[35]:


product_quantity.plot()


# In[39]:


teams = pd.Series(["Fenerbahçe","Besiktas","Galatasaray","Trabzon",
          "Fenerbahçe","Besiktas","Galatasaray","Trabzon",
          "Fenerbahçe","Besiktas",
          "Fenerbahçe"])
teams.value_counts()


# In[41]:


teams.value_counts().plot(kind="bar")


# In[43]:


df = pd.DataFrame( {"isim" : ["vision","wanda","steve"],
                   "puan":[80,70,90], "cinsiyet" : ["E","K","E"]})
df


# In[ ]:




