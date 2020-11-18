#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import numpy as np


# In[1]:


#this code extracts all entries submitted for one particular track


# In[5]:


#here, write the file name
file_name='devfolio-submissions.csv'

data=pd.read_csv(file_name)

project_id=np.arange(0,len(data))
project_name=data['team'].values
project_link=data['project'].values
project_tracks=data['tracks'].values

data=[project_id,project_name,project_link,project_tracks]


def sort_track(track_name):
    sorted_sheet=[]
    remote_education_hack=[]
    for i in project_id:
        if project_tracks[i]==project_tracks[i]:
            if track_name in project_tracks[i]:
                sorted_sheet.append([i,project_name[i],project_link[i],project_tracks[i]])
        sorted_data=pd.DataFrame(sorted_sheet,columns=['ID','Team Name','Project Link','Track'])
        sorted_data.to_csv(str(track_name)+' [SORTED].csv')
    return sorted_data

#here, use the sort_track function for as many categories as we have.
#should save as a "sorted" .csv
sort_track('Best Use of CockroachDB')
sort_track('Best Use of Google Cloud')
sort_track('Best Domain Registered with Domain.com')
sort_track('Best Hardware Hack Sponsored by Digi-Key')


# In[ ]:




