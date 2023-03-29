#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as ny
import pandas as pd


# In[2]:


country=pd.read_csv('C:/Users/Hassan/Downloads/country_codes.csv')


# In[3]:


country.head()


# In[4]:


pirates=pd.read_csv('C:/Users/Hassan/Downloads/pirate_attacks.csv')


# In[5]:


pirates.head()


# In[6]:


#1 Unique attacks


# In[7]:


uniquepirates=pirates.drop_duplicates(keep=False)


# In[8]:


uniquepirates.head()


# In[9]:


len(uniquepirates)


# In[10]:


len(pirates)


# In[11]:


duplicaterows=len(pirates)-len(uniquepirates)
duplicaterows


# In[12]:


#2 Five countries that are nearest to the highest number of attacks 


# In[13]:


import plotly.express as px
import pandas as pd

fig = px.scatter_geo(pirates,lat='latitude',lon='longitude')
fig.update_layout(title = 'Attacks', title_x=0.5)
fig.show()


# In[14]:


#2 5 countries nearest to highest number of attacks 


# In[15]:


multipleattacks=pirates[pirates[['nearest_country','vessel_name']].duplicated()==True]
multipleattacksout=multipleattacks[['vessel_name','nearest_country']]
print(multipleattacksout)


# In[16]:



multipleattacks["cum_distance"]=multipleattacks.groupby(['nearest_country'])['shore_distance'].cumsum(axis=0)
multipleattacks["no_attacks"]=multipleattacks.groupby(['nearest_country']).size()
list=multipleattacks.groupby(['nearest_country']).size()
print(list)


# In[17]:


multipleattacks.sort_values(by=['cum_distance',],ascending=True)
multipleattacks.head()
multipleattacks[multipleattacks['nearest_country'].isin(['IDN','NGA','MYS','BGD','IND'])]


# In[18]:


#3 Average distance of an attack to the coast 


# In[19]:


pirates.shore_distance.mean()


# In[20]:


#4 Countries that have been attacked multiple times


# In[21]:


len(multipleattacks)


# In[22]:


multipleattacksfilt=multipleattacksout[multipleattacksout['vessel_name']!='NA']


# In[23]:


print(multipleattacksfilt)


# In[24]:


country=country.rename(columns={'country':'nearest_country'})
combined=pd.merge(multipleattacks,country, on='nearest_country')


# In[25]:


outputcombined=combined[['vessel_name','country_name']]


# In[26]:


print(outputcombined)


# In[27]:


#5 distribution over time 


# In[41]:



pirates['date'] = pd.date_range('2000-1-1', periods=7511, freq='D')
mask = (pirates['date'] > '2000-6-1') & (pirates['date'] <= '2000-6-3')
print(pirates.loc[mask])


# In[40]:


pirates.loc[mask].plot(x='date',y='shore_distance')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




