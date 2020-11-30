# Copyright (C) 2020 Ralph "Blake" Vente
#
# orpheus is free software: you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
#
# This program will parse sentences and return trees.


import unittest

import spacy
from benepar.spacy_plugin import BeneparComponent
import pandas as pd
from code import InteractiveConsole
from pprint import pprint, pformat


import tensorflow as tf
tf.gfile = tf.io.gfile


# TODO: ensure there are no references and remove this function
# def extract_unipath(doc: 'Spacy.Doc') -> 'List[List[Tuple[str]]]':

#     # visit each node of the tree, yielding results of calling fn on the span
#     def parse(span, fn) -> 'Tuple[str]':
#         children = list(span._.children)
#         for child in children:
#             yield from parse(child, fn)
#         yield fn(span)

#     by_sentence = []
#     for sent in doc.sents:
#         v = list(parse(sent, unigram_getter))
#         by_sentence.append(v)
#     # reduce surrounding tuples so we have List[str]
#     return by_sentence

def doc_to_pos_string(doc: 'Spacy.Doc') -> 'str':
    """traverse, get unigrams, flatten into space separated pos_tags"""

    return " ".join(" ".join(span_visitor(sent, unigram_getter)) for sent in doc.sents)


def span_visitor(span: 'Spacy.Span', fn: 'Callable') -> 'Tuple[str]':
    """ visit all nodes in tree, applying fn on every node"""
    children = list(span._.children)
    yield fn(span)
    for child in children:
        yield from span_visitor(child, fn)


def unigram_getter(x: 'Spacy.Span') -> 'str':
    """ ret POS from a span, if span leaf, take POS from base str"""
    # leaf nodes have no labels?? extract them from the string.
    return (x._.labels or (x._.parse_string.partition(" ")[0][1:], ))[0]


def span_to_pos(x: 'Spacy.Span') -> 'str':
    """ ret POS from a span, if span leaf, take POS from base str"""
    # leaf nodes have no labels?? extract them from the string.
    return (x._.labels or (x._.parse_string.partition(" ")[0][1:], ))[0]


def l1_path_getter(x: 'Spacy.Span') -> 'str str ... str':
    """ unigram getter but returns paths of length 1 as strings"""
    # leaf nodes have no labels?? extract them from the string.
    x_pos_tag = span_to_pos(x)
    x_children = x._.children
    return " ".join(x_pos_tag+"↓"+span_to_pos(child) for child in x_children)


if __name__ == '__main__':
    # for unit tests, we import a small mock dataset
    # pd.Dataframe['user_id','review_contents','documents']

    DATASET_BASENAME = 'data/small'
    DATASET = f'{DATASET_BASENAME}_with_doc.pkl'
    df = pd.read_pickle(DATASET)
    doc: 'Spacy.Doc' = df['documents'][0]
    s = list(span_visitor(list(doc.sents)[0], unigram_getter))
    print(s)
    t = list(span_visitor(list(doc.sents)[0], l1_path_getter))
    print(t)
