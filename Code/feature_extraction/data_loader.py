# Copyright (C) 2020 Ralph "Blake Vente
#
# orpheus is free software: you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
#
# This program will convert a parse tree into a collections.Counter() of the
# directed nested n-grams of the constituency parse tree.

from collections import Counter

import numpy as np
import pandas as pd
from icecream import ic
from scipy import stats
from sklearn import tree
from sklearn.ensemble import AdaBoostClassifier, RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score
from sklearn.model_selection import KFold, train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import LinearSVC
from sklearn.utils import shuffle

DATA_DIR_NAME = 'data/'
DATA_FILE_NAME = "50Authors30DocsEach.csv"


def experiment(N_TRIALS, N_SPLITS, classifier, X, y):
    score_distribution = list()
    for _ in range(N_TRIALS):
        kf = KFold(n_splits=N_SPLITS, shuffle=True)
        for train_index, test_index in kf.split(X, y):
            X_train, X_test = X.iloc[train_index], X.iloc[test_index]
            y_train, y_test = y.iloc[train_index], y.iloc[test_index]

            classifier.fit(X_train, y_train)
            accuracy = classifier.score(X_test, y_test)
            score_distribution.append(accuracy)

    return score_distribution


if __name__ == "__main__":
    df = pd.read_csv(DATA_DIR_NAME+DATA_FILE_NAME)
    ic(set(df))
    assert(set(df) >= {'user_id', 'review_contents'})
    vectorizer = TfidfVectorizer()
    authors = df['user_id'].to_list()
    reviews = df['review_contents'].to_list()
    vectors = vectorizer.fit_transform(reviews)
    ic(vectors[:10].toarray())
    # help(vectors)

    print(vectors.shape)
    X_train, X_test, y_train, y_test = train_test_split(
        vectors, authors, test_size=0.3, random_state=42)
    svm = LinearSVC()
    svm.fit(X_train, y_train)
    predictions = svm.predict(X_test)
    print('svm', accuracy_score(y_test, predictions))

    X_train = X_train.toarray()
    X_test = X_test.toarray()
    nb = GaussianNB()
    nb.fit(X_train, y_train)
    predictions = nb.predict(X_test)
    print('NB', accuracy_score(y_test, predictions))

    print(df.head())
