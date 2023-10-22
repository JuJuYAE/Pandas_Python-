#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np 
from numpy.random import randn 
import jedi


# In[3]:


labels = ["a" , "b", "c"]
my_data = [10,20,30]
arr = np.array(my_data)
d = {"a" : 10 , "b" : 20, "c" : 30}


# In[4]:


pd.Series(data = my_data)


# In[5]:


pd.Series(data= my_data , index = labels)


# In[6]:


pd.Series(my_data,labels)


# In[7]:


pd.Series(arr, labels)


# In[8]:


pd.Series(d)


# In[9]:


pd.Series(arr)


# In[10]:


ser1 = pd.Series([1,2,3,4],["USA","GER","USSR", "JPN"])


# In[11]:


ser1


# In[12]:


ser2 = pd.Series([1,2,5,4],["USA","GER","ITA", "JPN"])


# In[13]:


ser2


# In[14]:


ser2["ITA"]


# In[15]:


ser3 = pd.Series(labels)


# In[16]:


ser3


# In[17]:


ser3[0]


# In[18]:


ser1


# In[19]:


ser2


# In[20]:


ser1+ser2


# In[21]:


np.random.seed(101)


# In[150]:


df = pd.DataFrame(randn(5,4), ["A","B","C","D","E"],["W","X","Y","Z"])


# In[23]:


df


# In[24]:


df[["W","Z"]]


# In[25]:


df["new"] = df["W"] + df["Y"]


# In[26]:


df


# In[27]:


df.drop("new",axis = 1)


# In[28]:


df


# In[29]:


df.drop("new",axis = 1, inplace = True )


# In[30]:


df


# In[31]:


df.drop("E")


# In[32]:


df.shape


# In[33]:


#Selecting Rows 


# In[34]:


df


# In[35]:


df.loc["A"]


# In[36]:


df.iloc[2]


# In[37]:


df.loc["B", "Y"]


# In[38]:


df.loc[["A","B"], ["X","Y"]]


# In[39]:


df > 0 


# In[40]:


df[df>0]


# In[41]:


df["W"]> 0 


# In[42]:


df[df["W"]>0]


# In[43]:


result_df = df[df["W"]>0]


# In[44]:


result_df


# In[45]:


result_df["X"]


# In[46]:


df


# In[47]:


df[["Y","X"]]


# In[48]:


df["W"] > 0 


# In[49]:


df[df["W"]>0][["W","Z"]]


# In[50]:


(df["W"]> 0) & (df["X"]<0)


# In[51]:


df.reset_index()


# In[52]:


newind = "CA NY WY OR CO".split()


# In[53]:


newind


# In[54]:


df["States"] = newind 


# In[55]:


df


# In[56]:


df.set_index("States")


# In[57]:


df


# In[58]:


# Index Levels
outside = ['G1','G1','G1','G2','G2','G2']
inside = [1,2,3,1,2,3]
hier_index = list(zip(outside,inside))
hier_index = pd.MultiIndex.from_tuples(hier_index)


# In[59]:


outside


# In[60]:


inside


# In[61]:


hier_index


# In[62]:


df = pd.DataFrame(randn(6,2),hier_index, "A B".split())


# In[63]:


df


# In[64]:


df.loc["G1"].loc[1]


# In[65]:


df.index.names


# In[66]:


df.index.names = "Groups Numbers".split()


# In[67]:


df


# In[68]:


df.loc["G2"]


# In[69]:


df.loc["G2"].loc[2]["B"]


# In[70]:


df.xs


# In[71]:


df.loc["G1"]


# In[72]:


df.xs(1,level = "Numbers")


# In[73]:


df.xs(1, level = "Numbers")


# In[74]:


d = {"A":[1,2,np.nan] , "B":[5,np.nan,np.nan] , "C":[1,2,3]}


# In[75]:


df = pd.DataFrame(d)


# In[76]:


df


# In[77]:


df.dropna(axis= 1)


# In[78]:


df.dropna()


# In[82]:


df.dropna(thresh=2)


# In[83]:


df.fillna(value = "Fill value")


# In[90]:


df["A"] = df["A"].fillna(value= df["A"].mean())


# In[91]:


df


# In[92]:


# Create dataframe
data = {'Company':['GOOG','GOOG','MSFT','MSFT','FB','FB'],
       'Person':['Sam','Charlie','Amy','Vanessa','Carl','Sarah'],
       'Sales':[200,120,340,124,243,350]}


# In[94]:


df = pd.DataFrame(data)


# In[95]:


df


# In[105]:


byComp = df.groupby("Company")


# In[101]:


byComp.mean()


# In[103]:


byComp.sum().loc["FB"]


# In[109]:


df.groupby("Company").min()


# In[113]:


df.groupby("Company").describe().transpose()["FB"]


# In[114]:


import pandas as pd
df = pd.DataFrame({'col1':[1,2,3,4],'col2':[444,555,666,444],'col3':['abc','def','ghi','xyz']})
df.head()


# In[115]:


df


# In[118]:


df["col2"].nunique()


# In[119]:


df["col2"].unique()


# In[121]:


df["col2"].value_counts()


# In[122]:


df


# In[125]:


df[(df["col1"]>2) & (df["col2"]==444)]


# In[130]:


def times2 (x) : 
    return x*2 


# In[131]:


df["col1"]


# In[129]:


df["col1"].apply(times2)


# In[133]:


df['col3'].apply(len)


# In[135]:


df['col2'].apply(lambda x : x*2)


# In[136]:


df


# In[138]:


df.drop("col1",axis = 1)


# In[139]:


df.columns


# In[140]:


df.index


# In[141]:


df


# In[143]:


df.sort_values(by = "col2")


# In[145]:


df.isnull()


# In[146]:


data = {'A':['foo','foo','foo','bar','bar','bar'],
     'B':['one','one','two','two','one','one'],
       'C':['x','y','x','y','x','y'],
       'D':[1,3,2,5,4,1]}

df = pd.DataFrame(data)


# In[147]:


df


# In[149]:


df.pivot_table(values = "D", index = ["A" , "B"], columns = ["C"])

