# -*- coding: utf-8 -*-
"""scratchpad

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/notebooks/empty.ipynb
"""

#implement the bagging based ensemble model using cart(classification and regression trees)as base learners
import pandas
from sklearn.model_selection import train_test_split
from sklearn.ensemble import BaggingClassifier
from sklearn.tree import DecisionTreeClassifier
url="https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
names=['preg','plas','pres','skin','test','mass','pedi','age','class']
df=pandas.read_csv(url,names=names)
df.shape

from sklearn import model_selection  # Add this line to import model_selection
from re import S
array=df.values
X=array[:,0:8]
Y=array[:,8]
# Use model_selection.KFold
Kfold=model_selection.KFold(n_splits=10,random_state=7,shuffle=True) # Changed Shuffle to shuffle
cart=DecisionTreeClassifier()
num_trees=100
# Change 'base_estimator' to 'estimator'
model=BaggingClassifier(estimator=cart,n_estimators=num_trees,random_state=7)
# Use model_selection.cross_val_score
results=model_selection.cross_val_score(model,X,Y,cv=Kfold)
average_accuracy=sum(results)/len(results)
print("Average Accuracy is",average_accuracy)

from sklearn import model_selection  # Add this line to import model_selection
from sklearn.neighbors import KNeighborsClassifier #Import KNeighborsClassifier
from re import S
array=df.values
X=array[:,0:8]
Y=array[:,8]
# Use model_selection.KFold
Kfold=model_selection.KFold(n_splits=10,random_state=7,shuffle=True) # Changed Shuffle to shuffle
knn=KNeighborsClassifier() # Now KNeighborsClassifier is defined
num_trees=100
# Change 'base_estimator' to 'estimator'
#Since the previous cell used cart, continuing with the same to avoid confusion.
model=BaggingClassifier(estimator=cart,n_estimators=num_trees,random_state=7)
# Use model_selection.cross_val_score
results=model_selection.cross_val_score(model,X,Y,cv=Kfold)
average_accuracy=sum(results)/len(results)
print("Average Accuracy is",average_accuracy)

