from dask import dataframe as dd
import dask.bag as db
import dask.bag as db
from dask import delayed
from sklearn.feature_extraction.text import TfidfVectorizer
import csv
import pandas as pd

with open('task5.txt', 'r') as f:
    data = [f.read()]

vectorizer = TfidfVectorizer()

#Transforming the text into a matrix of TF-IDF features
X = vectorizer.fit_transform(data)

#Converting the first row of the TF-IDF matrix into a DataFrame andconvert to DASK dataframe 
df = dd.from_pandas(pd.DataFrame(X[0].T.toarray(), index=vectorizer.get_feature_names_out(),
columns=["tfidf"]), npartitions=100)

#Sorting it by descending order of TF-IDF scores 
list = df.sort_values(by=["tfidf"],ascending=False)

#Compute the task and take n first value
result = list.compute(assume_missing=True).head(int(input()))

result.to_csv('result5.csv', sep='|')