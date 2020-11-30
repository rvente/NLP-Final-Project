# Copyright (C) 2020 Ralph "Blake" Vente and Anthony Chen
#
# orpheus is free software: you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
#
# This program loads pickles and adds a 'pos_tags' column derived from the
# 'spacy.Docs' in the dataframe. It takes about 0.05 seconds per review on one
# thread of a desktop Intel i5 4690K @ 3.5 GHz (a worst-case).


from instance_parser import (
    doc_visitor, span_to_pos,
    pos_nested_bigram_getter, l1_path_getter)
import pandas as pd
from tqdm import tqdm
tqdm.pandas()


# DATASET_BASENAME = 'data/small'
DATASET_BASENAME = 'data/100A50D'
# DATASET = 'data/100A50D_with_doc.pkl'
DATASET = f'{DATASET_BASENAME}_with_doc.pkl'
DATASET_OUTNAME = f'{DATASET_BASENAME}__doc+pos.pkl'

if __name__ == "__main__":
    try:
        print("read start")
        df = pd.read_pickle(DATASET)
        print("read done")

        def doc_to_pos(doc): return doc_visitor(doc, span_to_pos)

        def doc_to_pos_bigram(doc):
            return doc_visitor(doc, pos_nested_bigram_getter)

        def doc_to_l1_paths(doc):
            return doc_visitor(doc, l1_path_getter)

        # mutate to add pos_tag unigrams
        df['pos_tags'] = df['documents'].progress_apply(doc_to_pos)
        # mutate to add pos_tag unigrams
        df['nested_pos_bigrams'] = df['documents'].progress_apply(doc_to_pos_bigram)
        df['path_pos_bigrams'] = df['documents'].progress_apply(doc_to_l1_paths)
        df.drop(columns=['documents'], inplace=True)
        print(df)
        df.to_pickle(DATASET_OUTNAME)

    except Exception as e:
        print(e)
    pass
