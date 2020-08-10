#!/usr/bin/env python
# coding: utf-8

# In[13]:


import pandas as pd      


# In[14]:



column_names = ['user_id', 'item_id', 'rating', 'timestamp'] 
  


# In[15]:


path = 'https://media.geeksforgeeks.org/wp-content/uploads/file.tsv'
  


# In[16]:


df = pd.read_csv(path, sep='\t', names=column_names) 
  


# In[17]:



df.head()


# In[18]:



movie_titles = pd.read_csv('https://media.geeksforgeeks.org/wp-content/uploads/Movie_Id_Titles.csv') 


# In[19]:


movie_titles.head()


# In[20]:



data = pd.merge(df, movie_titles, on='item_id') 


# In[21]:


data.head() 


# In[22]:



data.groupby('title')['rating'].mean().sort_values(ascending=False).head() 


# In[23]:


data = pd.merge(df, movie_titles, on='item_id') 
data.head()


# In[24]:




data.groupby('title')['rating'].count().sort_values(ascending=False).head() 


# In[25]:



ratings = pd.DataFrame(data.groupby('title')['rating'].mean())  
  
ratings['num of ratings'] = pd.DataFrame(data.groupby('title')['rating'].count()) 
  
ratings.head() 


# In[ ]:





# In[ ]:




