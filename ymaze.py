#!/usr/bin/env python3
# coding: utf-8

# In[ ]:


import csv
import sys

# In[ ]:


filename = 'ymaze.csv'
filename = 'becia.csv'
filename = sys.argv[1]

# In[229]:


def is_data_valid(data):
    return len(set(data)) == 3

def get_triads(data):
    return [data[i:i+3] for i,e in enumerate(data) if i < (len(data)-2)]

def get_alternations(data):
    return [t for t in get_triads(data) if len(set(t)) == 3]


# In[230]:


with open(filename) as f:
    data = list([row for row in csv.DictReader(f)])

header = list(data[0].keys())


# In[231]:


data


# In[232]:


for i,record in enumerate(data):
    if ''.join(data[i].values()) == '': continue
    entries = data[i]['entries']
    triads = get_triads(entries)
    alternations = get_alternations(entries)
    data[i].update({'entries_valid':is_data_valid(entries)})
    data[i].update({'alternations':'-'.join(alternations)})
    data[i].update({'no_entries':len(entries)})
    data[i].update({'no_triad':len(triads)})
    data[i].update({'no_alt':len(alternations)})
    data[i].update({'perc_alt_per_triad':(len(alternations)/len(triads))*100})
    data[i].update({'perc_alt_per_entr':(len(alternations)/len(entries))*100})


# In[233]:


data


# In[234]:


outname = filename + '.out.csv'


# In[235]:


with open(outname, 'w', newline='') as f:
    wr = csv.DictWriter(f,data[0].keys())
    wr.writeheader()
    wr.writerows(data)


# In[ ]:




