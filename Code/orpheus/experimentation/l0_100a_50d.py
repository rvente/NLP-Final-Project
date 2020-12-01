# Copyright (C) 2020 Ralph "Blake" Vente and Anthony Chen
#
# orpheus is free software: you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
#
# This program defines the experiment of this research project. run_all.py
# actually executes it.

import pandas as pd
from sacred import Experiment
from sacred.observers import FileStorageObserver

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score, confusion_matrix, f1_score
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import LinearSVC

ex = Experiment('100a_50d_l0')
ex.observers.append(FileStorageObserver('logs'))


@ex.config
def cfg():
    dataset = {
        'name': '100 author 50 docs each pos_tags',
        'filename': './data/100A50D__doc+pos.pkl',
        'min_doc_freq': 0.005,
        'feature_column': 'review_contents'
    }
    name = 'support vector classifier'


@ex.capture(prefix='dataset')
def load_data(filename, min_doc_freq, feature_column, name):
    df = pd.read_pickle(filename)

    vectorizer = TfidfVectorizer(
        min_df=min_doc_freq, analyzer='word', token_pattern=r'\S+')
    experimental_feature = df[feature_column].to_list()
    authors = df['user_id'].to_list()
    vectors = vectorizer.fit_transform(experimental_feature)
    print(df[feature_column].head(), df.shape, sep="\n")
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


@ex.command
def MultiNomNB(_log, name):
    X_train, X_test, y_train, y_test = load_data()
    clf = MultinomialNB(alpha=.01)
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    confusion = confusion_matrix(y_test, y_pred)
    f1 = f1_score(y_test, y_pred, average="weighted")
    ex.log_scalar("test.accuracy", accuracy)
    ex.log_scalar("test.confusion", str(confusion))
    ex.log_scalar("test.f1_score", f1)
    _log.info(f"{name}")
    _log.info(f"acc={accuracy}, f1={f1}")
    return accuracy
