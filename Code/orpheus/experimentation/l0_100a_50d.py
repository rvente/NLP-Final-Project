# Copyright (C) 2020 Ralph "Blake" Vente and Anthony Chen
#
# orpheus is free software: you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
#
# This program defines the experiments of this research project. Other files in this
# directory actually execute it.

import pandas as pd
from sacred import Experiment
from sacred.observers import FileStorageObserver

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score, confusion_matrix, f1_score
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import LinearSVC, SVC
# from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier, GradientBoostingClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.linear_model import LogisticRegression

ex = Experiment('orpheus')
ex.observers.append(FileStorageObserver('logs'))

# initial configuration: overridden by config_updates={...} invocation
@ex.config
def cfg():
    dataset = {
        'name': '100 author 50 docs each pos_tags',
        'filename': './data/100A50D__doc+pos.pkl',
        'min_doc_freq': 0.005,
        'feature_column': 'review_contents',
        'test_set_prop' : .03
    }
    naivebayes = {
        'name': 'MultinomialNB',
        'alpha': .01
    }
    name = 'support vector classifier'

# shared dataset component
@ex.capture(prefix='dataset')
def load_data(filename, min_doc_freq, feature_column, name, test_set_prop):
    df = pd.read_pickle(filename)

    vectorizer = TfidfVectorizer(
        min_df=min_doc_freq, analyzer='word', token_pattern=r'\S+', ngram_range=(1,3))
    experimental_feature = df[feature_column].to_list()
    authors = df['user_id'].to_list()
    vectors = vectorizer.fit_transform(experimental_feature)
    print(df[feature_column].head(), df.shape, sep="\n")
    X_train, X_test, y_train, y_test = train_test_split(
        vectors, authors, test_size=test_set_prop, random_state=42, stratify=authors)
    print(X_train.shape)
    return X_train, X_test, y_train, y_test



@ex.command
def log_stats(_log, clf, X_test, y_test, name, params={}):
    y_pred = clf.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    confusion = confusion_matrix(y_test, y_pred)
    f1 = f1_score(y_test, y_pred, average="weighted")
    ex.log_scalar("test.accuracy", accuracy)
    ex.log_scalar("test.confusion", str(confusion))
    ex.log_scalar("test.f1_score", f1)
    _log.info(f"{name}")
    _log.info(f"acc={accuracy}, f1={f1}")
    _log.info(params)
    return accuracy

@ex.command
def svc(_log, name):
    X_train, X_test, y_train, y_test = load_data()
    mx_iter = 10000
    params = {'max_iter' : mx_iter , 'verbose':0}
    clf = LinearSVC(**params)
    clf.fit(X_train, y_train)
    return log_stats(_log, clf, X_test, y_test, name, params)

@ex.command
def kernelsvc(_log, name):
    X_train, X_test, y_train, y_test = load_data()
    params = {'max_iter' : 1000 , 'verbose':0, 'kernel': 'rbf', 'C': 50.0}
    clf = SVC(**params)
    clf.fit(X_train, y_train)
    return log_stats(_log, clf, X_test, y_test, name, params)

@ex.command
@ex.capture(prefix='naivebayes')
def MultiNomNB(_log, name, alpha=.01):
    X_train, X_test, y_train, y_test = load_data()
    params = {'alpha': alpha}
    clf = MultinomialNB(**params)
    clf.fit(X_train, y_train)
    return log_stats(_log, clf, X_test, y_test, name, params)

@ex.command
def RandForest(_log, name):
    X_train, X_test, y_train, y_test = load_data()
    clf = RandomForestClassifier()
    clf.fit(X_train, y_train)
    return log_stats(_log, clf, X_test, y_test, name)

@ex.command
def AdaBoost(_log, name):
    X_train, X_test, y_train, y_test = load_data()
    clf = AdaBoostClassifier()
    clf.fit(X_train, y_train)
    return log_stats(_log, clf, X_test, y_test, name)

@ex.command
def MLP(_log, name):
    X_train, X_test, y_train, y_test = load_data()
    clf = MLPClassifier( hidden_layer_sizes=(50, 2), activation='tanh', learning_rate='adaptive', max_iter=500)
    clf.fit(X_train, y_train)
    return log_stats(_log, clf, X_test, y_test, name)


@ex.command
def LogReg(_log, name):
    X_train, X_test, y_train, y_test = load_data()
    clf = LogisticRegression()
    clf.fit(X_train, y_train)
    return log_stats(_log, clf, X_test, y_test, name)
