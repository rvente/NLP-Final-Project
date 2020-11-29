# Copyright (C) 2020 Ralph "Blake" Vente and Anthony Chen
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

from instance_parser import PathExtractor


DATA_DIR_NAME = 'data/'
# DATA_FILE_NAME = "50A30D.csv"
# DATA_FILE_NAME = "100A50D.csv"
DATA_FILE_NAME = "100A50D.xlsx"
COL_LABELS = ["user_id", "review_contents"]


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
    # read file with two cols, "user_id" and "review_contents"
    df = pd.read_excel(DATA_DIR_NAME+DATA_FILE_NAME, names=COL_LABELS)

    extractor = PathExtractor()

    # for row in dataframe, pathextractor(row['review_contents']) into new row['bin']
    df = df.head(10)
    df['documents'] = df['review_contents'].map(extractor.extract_doc_tree)

    try:
        # df.to_hdf("100A50D_with_doc.h5", key='df')
        df.to_pickle("")
    except Exception as e:
        print(e)

    assert(set(df) >= set(COL_LABELS))
