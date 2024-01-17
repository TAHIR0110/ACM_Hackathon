#!/usr/bin/env python
# coding: utf-8
#pip install serpapi
#pip install google-search-results


# In[61]:

from serpapi import GoogleSearch
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.metrics import accuracy_score

df = pd.read_csv('dataset9000.csv')

for column in df.columns:
    if df[column].dtype == 'object':
        label_encoder = LabelEncoder()
        df[column + '_encoded'] = label_encoder.fit_transform(df[column])

df.drop(['Database Fundamentals', 'Computer Architecture',
         'Distributed Computing Systems', 'Cyber Security', 'Networking',
         'Software Development', 'Programming Skills', 'Project Management',
         'Computer Forensics Fundamentals', 'Technical Communication', 'AI ML',
         'Software Engineering', 'Business Analysis', 'Communication skills',
         'Data Science', 'Troubleshooting skills', 'Graphics Designing',
         'Role_encoded'], axis=1, inplace=True)

X = df.drop('Role', axis=1)
y = df['Role']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

knn_model = KNeighborsClassifier(n_neighbors=3)
knn_model.fit(X_train_scaled, y_train)

y_pred = knn_model.predict(X_test_scaled)


user_input = {}
for column in X.columns:
    user_input[column] = float(input(f"Enter {column}: "))

user_df = pd.DataFrame([user_input])

user_input_scaled = scaler.transform(user_df)

user_predictions_proba = knn_model.predict_proba(user_input_scaled)

top_3_classes = user_predictions_proba.argsort()[0, -3:][::-1]

label_encoder.inverse_transform(top_3_classes)



inp_job = top_3_classes[0]

params = {
  "api_key": "74667d45acf8d73e71f442fcea119219a9c88b09bb187292159a3fc88235289c",
  "engine": "google_jobs",
  "google_domain": "google.com",
  "q": str(inp_job)
}

search = GoogleSearch(params)
result = search.get_dict()


Job_ID = []
for job_result in result['jobs_results']:
    Job_ID.append((job_result['job_id'],job_result['company_name'],job_result['title']))
print('1---------------------------------------------------------------1')

for job_id in Job_ID:
    params = {
        "api_key": "74667d45acf8d73e71f442fcea119219a9c88b09bb187292159a3fc88235289c",
        "engine": "google_jobs_listing",
        "q": str(job_id[0])
  }
    search = GoogleSearch(params)
    results = search.get_dict()
    try:
      print('---------------------------------------------------------------')
      print(job_id[1])
      print(job_id[2])
      print(results['apply_options'])
    except:
       continue

