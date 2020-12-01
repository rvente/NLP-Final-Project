# Copyright (C) 2020 Ralph "Blake" Vente and Anthony Chen
#
# orpheus is free software: you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
#
# This program will take a df of user_id, review_contents and add another column
# containing the parse tree features as a Doc
#
# TODO: Future Work: this is 'trivially multi-threadable' using Python's Dask

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

from tqdm import tqdm
import spacy
from benepar.spacy_plugin import BeneparComponent
tqdm.pandas()


DATA_DIR_NAME = 'data/'
# DATA_FILE_NAME = "50A30D.csv"
# DATA_FILE_NAME = "100A50D.csv"
DATA_FILE_NAME = "100A50D.xlsx"
COL_LABELS = ["user_id", "review_contents"]

class PathExtractor():
    def __init__(self):
        self.nlp = spacy.load('en')
        self.nlp.add_pipe(BeneparComponent('benepar_en'))

    def extract_doc_tree(self, document: 'String') -> 'Doc':
        doc = self.nlp(document)
        return doc

if __name__ == "__main__":
    # read file with two cols, "user_id" and "review_contents"
    df = pd.read_excel(DATA_DIR_NAME+DATA_FILE_NAME, names=COL_LABELS)

    extractor = PathExtractor()

    df = df.head(10)
    df = df.astype('string')
    df['documents'] = df['review_contents'].progress_map(extractor.extract_doc_tree)

    try:
        # df.to_hdf("100A50D_with_doc.h5", key='df')
        # df.to_pickle("100A50D_with_doc.pkl")
        df.to_pickle("Sample_with_doc.pkl")
    except Exception as e:
        print(e)

    assert(set(df) >= set(COL_LABELS))
