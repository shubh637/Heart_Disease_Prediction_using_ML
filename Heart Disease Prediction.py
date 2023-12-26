#!/usr/bin/env python
# coding: utf-8

# In[1]:


#importing all the necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy as sc
import sklearn as sc
import seaborn as sns


# In[5]:


df=pd.read_csv("C:\\Users\\TUSHAR SAIN\\Downloads\\framingham.csv")
df.info()


# In[6]:


df.describe()


# In[7]:


df


# In[ ]:





# In[15]:


df["education"].fillna(df["education"].mean(),inplace=True)
df["cigsPerDay"].fillna(df["cigsPerDay"].mean(),inplace=True)
df["BPMeds"].fillna(df["BPMeds"].mean(),inplace=True)
df["totChol"].fillna(df["totChol"].mean(),inplace=True)
df["BMI"].fillna(df["BMI"].mean(),inplace=True)
df["heartRate"].fillna(df["heartRate"].mean(),inplace=True)
df["glucose"].fillna(df["glucose"].mean(),inplace=True)


# In[31]:


sns.heatmap(df[df.columns].corr())


# In[54]:


plt.figure(figsize=(30,30))
sns.heatmap(df[df.columns].corr(),vmax=0.75,annot=True)


# In[44]:


#histogrames
fig,axes=plt.subplots(2,8,figsize=(30,20))
df.hist(ax=axes,bins=30,grid=False)
plt.show()


# In[48]:


#boxplots
plt.figure(figsize=(30,20))
for i in enumerate(df.columns):
    plt.subplot(6,4,i[0]+1)
    sns.boxplot(x=i[1],data=df)
plt.tight_layout()    


# In[50]:


plt.figure(figsize=(30,20))
plt.boxplot(df)


# In[203]:


x=df.iloc[:,0:14]
y=df.iloc[:,-1]
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=0)


# In[204]:


from sklearn.preprocessing import StandardScaler
sd=StandardScaler()
x_train=sd.fit_transform(x_train)
x_test=sd.fit_transform(x_test)


# In[205]:


from sklearn.linear_model import LogisticRegression
from sklearn import metrics
classifier= LogisticRegression()
classifier.fit(x_train,y_train)
y_pred=classifier.predict(x_test)
print("the logistic regression accuracy:",metrics.accuracy_score(y_pred,y_test))


# In[206]:


from sklearn.metrics import confusion_matrix
cm=confusion_matrix(y_test,y_pred)
sns.heatmap(cm/np.sum(cm),fmt=".2%",annot=True)



# In[207]:


#classification report
from sklearn.metrics import classification_report
report=classification_report(y_test,y_pred)
print(report)


# In[208]:


#features of the dataset
new_data=df.iloc[:,0:14]
features=list(new_data.columns)
features


# In[209]:


#coefficient of the model
coefficient=classifier.coef_.ravel().tolist()
print(coefficient)


# In[210]:


#coefficient table
data={"features":features,"coefficient":coefficient}
df1=pd.DataFrame(data)
df1


# In[212]:


df1.plot(kind="bar",figsize=(20,10))
plt.xticks(np.arange(0,14),features)
plt.show()


# In[ ]:





# In[ ]:




