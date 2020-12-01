# Copyright (C) 2020 Ralph "Blake" Vente
#
# orpheus is free software: you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
#
# This program stores utilities to convert tree representations to string
# representations.

from code import InteractiveConsole
from pprint import pformat, pprint
from typing import Callable, Generator, Tuple

import pandas as pd
import spacy
import tensorflow as tf
from benepar.spacy_plugin import BeneparComponent

tf.gfile = tf.io.gfile

# TODO: put these in a central location
SpaceDelimitedTokens = str
Span = spacy.tokens.Span
Doc = spacy.tokens.Doc


def doc_to_pos_string(doc: Doc) -> SpaceDelimitedTokens:
    """traverse, get unigrams, flatten into space separated pos_tags"""

    return " ".join(" ".join(span_visitor(sent, unigram_getter)) for sent in doc.sents)


def doc_visitor(doc: Doc, fn: Callable) -> SpaceDelimitedTokens:
    """apply fn(Span) across document flatten into space separated tokens"""

    return " ".join(" ".join(span_visitor(sent, fn)) for sent in doc.sents)


def span_visitor(span: Span, fn: Callable) -> 'Generator[Span, Callable, None]':
    """ visit all nodes in tree, applying fn on every node"""
    children = list(span._.children)
    yield fn(span)
    for child in children:
        yield from span_visitor(child, fn)


def unigram_getter(x: Span) -> str:
    """get POS unigrams aka POS single pos label"""
    return span_to_pos(x)


def span_to_pos(x: Span) -> str:
    """ ret POS from a span, if span leaf, take POS from base str"""
    # leaf nodes have no labels?? extract them from the string.
    return (x._.labels or (x._.parse_string.partition(" ")[0][1:], ))[0]


def pos_nested_bigram_getter(x: Span) -> SpaceDelimitedTokens:
    """returns all nested bigrams from x as space-separated tokens"""
    # leaf nodes have no labels?? extract them from the string.
    x_pos_tag = span_to_pos(x)
    x_children = x._.children
    return " ".join(f"{x_pos_tag}↓{span_to_pos(child)}" for child in x_children)


def l1_path_getter(x: Span) -> SpaceDelimitedTokens:
    """returns all POS paths of length 1 from node x as strings"""
    # leaf nodes have no labels?? extract them from the string.
    x_pos_tag = span_to_pos(x)
    x_par = x._.parent
    par_pos_tag = span_to_pos(x_par) if x_par is not None else "ROOT"
    upper_bigram = f"{x_pos_tag}↑{par_pos_tag}"
    return (pos_nested_bigram_getter(x) + " " + upper_bigram).strip()


def path_getter(x: Span, length: 'int') -> SpaceDelimitedTokens:
    """returns all POS paths of given from node x as strings"""
    x_pos_tag = span_to_pos(x)
    x_par = x._.parent
    par_pos_tag = span_to_pos(x_par) if x_par is not None else "ROOT"
    upper_bigram = f"{x_pos_tag}↑{par_pos_tag}"

    x_children = x._.children
    subsequent_nodes = [x_par] + x_children

    # return (pos_nested_bigram_getter(x) + " " + upper_bigram).strip()
    # return " ".join(f"{x_pos_tag}↓{span_to_pos(child)}" for child in x_children)
    return


if __name__ == '__main__':
    """ for unit tests, we import a small mock dataset of the form
    pd.Dataframe['user_id','review_contents','documents']
    where 'documents' is a 'Doc """

    DATASET_BASENAME = 'data/small'
    DATASET = f'{DATASET_BASENAME}_with_doc.pkl'
    df = pd.read_pickle(DATASET)
    doc: 'Doc' = df['documents'][0]
    for getter in [span_to_pos, l1_path_getter, pos_nested_bigram_getter]:
        print(getter)
        print(doc_visitor(doc, getter))
