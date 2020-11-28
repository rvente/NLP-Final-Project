import numpy as np
import pandas as pd
from sacred import Ingredient

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
auth100docs50 = Ingredient('dataset')


@auth100docs50.config
def cfg():
    filename = './data/100A50D.xlsx'
    col_labels = ["user_id", "review_contents"]


@auth100docs50.capture
def load_data(filename, col_labels):
    df = pd.read_excel(filename, names=col_labels)
    vectorizer = TfidfVectorizer()
    reviews = df['review_contents'].to_list()
    authors = df['user_id'].to_list()
    vectors = vectorizer.fit_transform(reviews)
    print(df.head())
    X_train, X_test, y_train, y_test = train_test_split(
        vectors, authors, test_size=0.3, random_state=42)
    return X_train, X_test, y_train, y_test
