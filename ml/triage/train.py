import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import pickle

df = pd.read_csv("data/triage.csv")

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df["symptoms"])
y = df["label"]

model = LogisticRegression()
model.fit(X, y)

pickle.dump((vectorizer, model), open("model.pkl", "wb"))

