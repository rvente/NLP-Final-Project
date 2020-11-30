# Copyright (C) 2020 Ralph "Blake" Vente and Anthony Chen
#
# orpheus is free software: you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
#
# This program loads pickles and adds a 'pos_tags' column.


import pandas as pd

from instance_parser import span_visitor, unigram_getter

DATASET = 'Sample_POS.pkl'
DATASET = 'data/Sample_POS.pkl'
CTR = 1

def doc_to_pos_string(doc: 'Spacy.Doc') -> 'str':
    """traverse, get unigrams, flatten into space separated pos_tags"""
    global CTR
    CTR += 1
    print(CTR/5000)
    return " ".join(" ".join(span_visitor(sent, unigram_getter)) for sent in doc.sents)


def pos_col_append(df: 'pd.DataFrame[documents]') -> 'MUTATES':
    """MUTATE df with POS column; MUTATION for efficiency"""
    df['pos_tags'] = df['documents'].apply(doc_to_pos_string)


if __name__ == "__main__":
    try:
        print("read start")
        df = pd.read_pickle(DATASET)
        print("read done")
        pos_col_append(df)
        df.drop(columns=['documents'], inplace=True)
        print(df)
        df.to_pickle("data/Sample_POS.pkl")

    except Exception as e:
        print(e)
    pass
