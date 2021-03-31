#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pylab as plt


# In[2]:


import sys
get_ipython().system('{sys.executable} -m pip install git+https://github.com/mattbellis/h5hep.git')


# In[3]:


import h5hep


# In[4]:


get_ipython().system('{sys.executable} -m pip install git+https://github.com/mattbellis/particle_physics_simplified.git')


# In[5]:


import pps_tools as pps


# In[6]:


get_ipython().system('{sys.executable} -m pip install plotly')


# In[7]:


import pps_tools as pps


# In[9]:


#Downloading Data


# In[10]:


pps.download_from_drive('dimuons_1000_collisions.hdf5')


# INTERFACING WITH THE DATA

# In[13]:


infile = 'data/dimuons_1000_collisions.hdf5'

collisions = pps.get_collisions(infile,experiment='CMS',verbose=False)
print(len(collisions), " collisions")  # This line is optional, and simply tells you how many events are in the file.


# In[14]:


#Collisions
second_collision = collisions[1]   # the second event
print("First event: ",second_collision)
all_muons = second_collision['muons']    # all of the jets in the first event
print("All muons: ",all_muons)
first_muon = all_muons[0]    # the first jet in the first event
print("First muon: ",first_muon)   
muon_energy = first_muon['e']      # the energy of the first photon
print("First muon's energy: ",muon_energy)


# In[16]:


energies = []

for collision in collisions:          # loops over all the events in the file
  muons = collision['muons']      # gets the list of all muons in the event
  
  for muon in muons:           # loops over each muon in the current event
    e = muon['e']                # gets the energy of the muon
    
    energies.append(e)             # puts the energy in a list


# In[17]:


plt.hist(energies,bins=50,range=(0,100));


# In[18]:


infile = 'data/dimuons_1000_collisions.hdf5' 

alldata = pps.get_all_data(infile,verbose=False)
nentries = pps.get_number_of_entries(alldata)

print("# entries: ",nentries)   # This optional line tells you how many events are in the file


# In[19]:


for entry in range(nentries):      # This range will loop over ALL of the events
    collision = pps.get_collision(alldata,entry_number=entry,experiment='CMS')

for entry in range(0,int(nentries/2)):     # This range will loop over the first half of the events
    collision = pps.get_collision(alldata,entry_number=entry,experiment='CMS')
    
for entry in range(int(nentries/2),nentries):      # This range will loop over the second half of the events
    collision = pps.get_collision(alldata,entry_number=entry,experiment='CMS')


# In[20]:


energies = []

for event in range(0,int(nentries/3)):        # Loops over first 3rd of all events
  
  collision = pps.get_collision(alldata,entry_number=event,experiment='CMS')    # organizes the data so you can interface with it
  muons = collision['muons']         # gets the list of all photons in the current event
  
  for muon in muons:                 # loops over all photons in the event
    e = muon['e']                      # gets the energy of the photon
    
    energies.append(e)                   # adds the energy to a list


# In[21]:


plt.hist(energies,bins=50,range=(0,100));


# In[ ]:




