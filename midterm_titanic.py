# -*- coding: utf-8 -*-
"""midterm_titanic.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1OKp_K7yPerIgnRxo8-5FBtQBIbWxXWOb
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from seaborn import load_dataset # this method will help us to #download the Titanic dataset
# %matplotlib inline # if you use jupyter notebook
plt.style.use('ggplot') # check for more with plt.style.available
data = load_dataset("titanic")

data.head(5)

data.isnull().sum()

"""# **1. #change the category dtype to str and lower and get back to category type**"""

#change the category dtype to str and lower and get back to category type
data['class']=data['class'].astype(str).str.lower().astype('category')
#df['class'] = df['class'].astype(str).str.lower().astype('category')

data.embarked.value_counts()

data.deck.value_counts()

"""# **Fill na data**"""

# Fill Nan data in Age
import numpy as np
np.random.seed(24)
#age_null = data.age.isna().sum()
data.loc[data['age'].isna(),'age'] = [i for i in np.random.randint(15,80,data.age.isna().sum())]
# Fill Nan data in Embarked from S,C,Q
data.loc[data.embarked.isna(),'embarked']= [i for i in np.random.choice(['S','C','Q'],data.embarked.isna().sum())]
# Fill Nan data in deck from S,C,Q
data.loc[data.deck.isna(),'deck']= [i for i in np.random.choice(['A','B','C','D','E','F','G'],data.deck.isna().sum())]

## df.loc[df['Favourite Sport'].isna(), 'Favourite Sport'] = [i for i in np.random.choice(['Volleyball', 'Football', 'Basketball', 'Cricket'], df['Favourite Sport'].isna().sum())]

#******************** NOT NECESSARY************************************************
#check whether survived column and alive column has the same value
i= 0
j = 0
for index,row in data.iterrows():
  if(row.survived == 1 and row.alive == 'yes'):
    i+=1
  elif(row.survived == 0 and row.alive == 'no'):
    j+=1
print(f'number of survived {i}')
print(f'number of not_survived {j}')
#******************** NOT NECESSARY************************************************

#******************** NOT NECESSARY************************************************
#max age of who == child is 15 and min is 0.43
data[data['class'] == 'Third'].age.min()
#******************** NOT NECESSARY************************************************

"""# **Select Only effective categories**"""

data.columns.tolist()
df = data[['survived', 'pclass', 'sex', 'age', 'fare', 'embarked', 'class', 'who', 'deck', 'alone']]
df

#train_test_split
from sklearn.model_selection import train_test_split
df_train,df_val = train_test_split(df, test_size = 0.2, random_state = 42)

df_train = df_train.reset_index(drop = True)
df_val = df_val.reset_index(drop = True)

y_train = df_train.survived.values
y_val = df_val.survived.values

del df_train['survived']
del df_val['survived']

"""# **Categorical Data to NUMERICAL Data **
Def Train and Predict
"""

from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction import DictVectorizer

def train (df_train, y_train):
  dicts = df_train.to_dict(orient = 'records')
  dv = DictVectorizer(sparse = False)
  X_train = dv.fit_transform(dicts)

  logisticmodel = LogisticRegression(max_iter=1000)
  logisticmodel.fit(X_train, y_train)
  return dv,logisticmodel

def predict (df_val, dv,logisticmodel):
  dicts = df_val.to_dict(orient = 'records')
  X= dv.transform(dicts)

  y_accuracy = logisticmodel.predict(X)
  y_pred = logisticmodel.predict_proba(X)[:,1]
  return y_pred, y_accuracy

dv, model = train(df_train,y_train)
y_pred, y_accuracy = predict(df_val ,dv,model)
y_pred, y_accuracy

from sklearn.metrics import roc_auc_score, accuracy_score
auc = roc_auc_score(y_val,y_pred)
accuracy = accuracy_score(y_val,y_accuracy)
auc,accuracy

import pickle
output_file = 'model_C = logisticmodel.bin'


f_out=open(output_file,'wb')
pickle.dump((dv,model),f_out)
f_out.close()

# instead of the upper code , use this
with open(output_file,'wb')as f_out:
  pickle.dump((dv,model),f_out)

print (f'the model is saved to {output_file}')