# Copyright (C) 2020 Ralph "Blake" Vente and Anthony Chen
#
# orpheus is free software: you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
#
# This program loads pickles and adds a 'pos_tags' column derived from the
# 'Spacy.Docs' in the dataframe. It takes about 0.05 seconds per review on one
# thread of a desktop Intel i5 4690K @ 3.5 GHz (a worst-case).


from instance_parser import span_visitor, unigram_getter
import pandas as pd
from tqdm import tqdm
tqdm.pandas()


DATASET_BASENAME = 'data/small'
DATASET = f'{DATASET_BASENAME}_with_doc.pkl'
DATASET_OUTNAME = f'{DATASET_BASENAME}__doc+pos.pkl'
# DATASET = 'data/100A50D_with_doc.pkl'


def doc_to_pos_string(doc: 'Spacy.Doc') -> 'str':
    """traverse, get unigrams, flatten into space separated pos_tags"""

    return " ".join(" ".join(span_visitor(sent, unigram_getter)) for sent in doc.sents)


def pos_col_append(df: 'pd.DataFrame[documents]') -> 'MUTATES':
    """MUTATE df with POS column; MUTATION for efficiency"""
    df['pos_tags'] = df['documents'].progress_apply(doc_to_pos_string)


if __name__ == "__main__":
    try:
        print("read start")
        df = pd.read_pickle(DATASET)
        print("read done")
        pos_col_append(df)
        df.drop(columns=['documents'], inplace=True)
        print(df)
        df.to_pickle(DATASET_OUTNAME)

    except Exception as e:
        print(e)
    pass
