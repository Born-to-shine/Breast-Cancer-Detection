# -*- coding: utf-8 -*-
"""breast_cancer_detection.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_YQq-_GKCxBelnc6SAiUqptgS6xDj-Go

# Breast Cancer Detection
### It detects whether the tumor is malignant or benign based on the matrix of features
##### Dataset - Breast_Cancer_Detection
"""

# Import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Import dataset
dataset = pd.read_csv('Breast_Cancer_Detection.csv')
x = dataset.iloc[:, 1:-1].values
y = dataset.iloc[:, -1].values

print(x)

print(y)

# Split dataset into training and test set
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state=0)

# Feature scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.fit_transform(x_test)

print(x_train)

print(x_test)

print(y_train)

print(y_test)

accuracy = []

# Import all libraries
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, accuracy_score

# Train Logistic Regression
def logistic_regression():
  classifier = LogisticRegression()
  classifier.fit(x_train, y_train)
  y_pred = classifier.predict(x_test)
  cm = confusion_matrix(y_test, y_pred)
  print('Confusion matrix:\n',cm)
  per = accuracy_score(y_test, y_pred)*100
  accuracy.append(per)
  print('Accuracy Score: ',per)

# Train k-Nearest Neighbor
def knn():
  classifier = KNeighborsClassifier(n_neighbors = 5)
  classifier.fit(x_train, y_train)
  y_pred = classifier.predict(x_test)
  cm = confusion_matrix(y_test, y_pred)
  print('Confusion matrix:\n',cm)
  per = accuracy_score(y_test, y_pred)*100
  accuracy.append(per)
  print('Accuracy Score: ',per)

# Train Support Vector Machine
def svm():
  classifier = SVC(kernel = 'linear', random_state = 0)
  classifier.fit(x_train, y_train)
  y_pred = classifier.predict(x_test)
  cm = confusion_matrix(y_test, y_pred)
  print('Confusion matrix:\n',cm)
  per = accuracy_score(y_test, y_pred)*100
  accuracy.append(per)
  print('Accuracy Score: ',per)

# Train kernel SVM
def kernel_svm():
  classifier = SVC(kernel = 'rbf', random_state = 0)
  classifier.fit(x_train, y_train)
  y_pred = classifier.predict(x_test)
  cm = confusion_matrix(y_test, y_pred)
  print('Confusion matrix:\n',cm)
  per = accuracy_score(y_test, y_pred)*100
  accuracy.append(per)
  print('Accuracy Score: ',per)

# Train Naive Bayes Classification
def naive_bayes():
  classifier = GaussianNB()
  classifier.fit(x_train, y_train)
  y_pred = classifier.predict(x_test)
  cm = confusion_matrix(y_test, y_pred)
  print('Confusion matrix:\n',cm)
  per = accuracy_score(y_test, y_pred)*100
  accuracy.append(per)
  print('Accuracy Score: ',per)

# Train Decision Tree Classification
def decision_tree():
  classifier = DecisionTreeClassifier(criterion='entropy', random_state = 0)
  classifier.fit(x_train, y_train)
  y_pred = classifier.predict(x_test)
  cm = confusion_matrix(y_test, y_pred)
  print('Confusion matrix:\n',cm)
  per = accuracy_score(y_test, y_pred)*100
  accuracy.append(per)
  print('Accuracy Score: ',per)

# Train Random Forest Classification
def random_forest():
  classifier = RandomForestClassifier(n_estimators=10, criterion='entropy', random_state = 0)
  classifier.fit(x_train, y_train)
  y_pred = classifier.predict(x_test)
  cm = confusion_matrix(y_test, y_pred)
  print('Confusion matrix:\n',cm)
  per = accuracy_score(y_test, y_pred)*100
  accuracy.append(per)
  print('Accuracy Score: ',per)

# Train dataset using different models in different functions
print('Logistic Regression:')
logistic_regression()
print('\n')
print('k-Nearest Neighbors:')
knn()
print('\n')
print('Support Vector Machine:')
svm()
print('\n')
print('Kernel SVM:')
kernel_svm()
print('\n')
print('Naive Bayes Classification:')
naive_bayes()
print('\n')
print('Decision Tree Classification:')
decision_tree()
print('\n')
print('Random Forest Classification:')
random_forest()

max = 0
for i in accuracy:
  if i>max :
    max = i

index = accuracy.index(max)
models = ['Logistic Regression', 'K-Nearest Neighbors', 'Support Vector Machine', 'Kernel SVM', 'Naive Bayes', 'Decision Tree', 'Random Forest']
print(models[index], 'is the best model for the detection of breast cancer.')