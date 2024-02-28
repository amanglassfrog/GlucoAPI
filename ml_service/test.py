import os
from sklearn.tree import DecisionTreeClassifier
from sklearn.feature_extraction.text import CountVectorizer
import tensorflow as tf
import pandas as pd
from tensorflow import lite
from ml_service.settings import BASE_DIR
#import joblib


file_path = os.path.join(BASE_DIR.parent, 'data_input.csv')

df = pd.read_csv(file_path)

print(df)

print(BASE_DIR.parent)