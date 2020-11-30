import numpy as np
import pandas as pd
[]
from sacred import Experiment, Ingredient
from sacred.observers import FileStorageObserver

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score, confusion_matrix, f1_score
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC

ex = Experiment('100a_50d_l0')
# ex.observers.append(FileStorageObserver('logs'))

@ex.config
def cfg():
    dataset = {
        'name': '100 author 50 docs each pos_tags',
        'filename': './data/100A50D_POS.pkl',
        'min_doc_freq': 0.005,
    }
    name = 'support vector classifier'


@ex.capture(prefix='dataset')
def load_data(filename, min_doc_freq):
    df = pd.read_pickle(filename)

    vectorizer = TfidfVectorizer(min_df=min_doc_freq)
    experimental_feature = df['pos_tags'].to_list()
    authors = df['user_id'].to_list()
    vectors = vectorizer.fit_transform(experimental_feature)
    print(df.head(), df.shape, sep="\n")
    X_train, X_test, y_train, y_test = train_test_split(
        vectors, authors, test_size=0.3, random_state=42)
    print(X_train.shape)
    return X_train, X_test, y_train, y_test


@ex.command
def svc(_log, name):
    X_train, X_test, y_train, y_test = load_data()
    svm = LinearSVC()
    svm.fit(X_train, y_train)
    y_pred = svm.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    confusion = confusion_matrix(y_test, y_pred)
    f1 = f1_score(y_test, y_pred, average="weighted")
    ex.log_scalar("test.accuracy", accuracy)
    ex.log_scalar("test.confusion", str(confusion))
    ex.log_scalar("test.f1_score", f1)
    _log.info(f"{name}")
    _log.info(f"acc={accuracy}, f1={f1}")
    return accuracy
