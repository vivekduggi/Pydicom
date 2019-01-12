
# coding: utf-8

# In[11]:


import matplotlib.pyplot as plt
import pydicom
from pydicom.data import get_testdata_files


# In[23]:


fn1 = pydicom.read_file("ttfm.dcm")


# # To Print dicom tags present in ttfm.dcm file

# In[25]:


print(fn1)


# In[26]:


fn2 = pydicom.read_file("bmode.dcm")


# # To Print dicom tags present in bmode.dcm file

# In[27]:


print(fn2)


# # output file in the format of text file as ttfm.txt

# In[28]:


fn1.save_as('ttfm.txt')


# # output file in the format of text file as bmode.txt
# 

# In[29]:


fn2.save_as('bmode.txt')

