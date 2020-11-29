# Copyright (C) 2020 Ralph "Blake Vente
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
from code import InteractiveConsole
from pprint import pprint, pformat

import tensorflow as tf
print(tf.__version__)
tf.gfile = tf.io.gfile


class PathExtractor():
    def __init__(self, min_len=2, max_len=5):
        self.nlp = spacy.load('en')
        self.nlp.add_pipe(BeneparComponent('benepar_en'))

    def peek(self, printable):
      #print(printable)
      return printable

    def extract_doc_tree(self, document) -> 'Spacy.Doc':
        doc = self.nlp(document)
        return doc

    def extract_unipath(self, document) -> 'List[List[Tuple[str]]]':
        doc = self.nlp(document)
        
        # visit each node of the tree, yielding results of calling fn on the span
        def parse(span, fn) -> 'Tuple[str]':
            children = list(span._.children)
            for child in children:
                yield from parse(child, fn)
            yield fn(span)

        by_sentence = []
        for sent in doc.sents:
            v = list(parse(sent,
                  # leaf nodes have no labels?? extract them from the string.
                  lambda x: x._.labels or (x._.parse_string.partition(" ")[0][1:], )))
            by_sentence.append(v)
        # reduce surrounding tuples so we have List[str]
        return by_sentence


if __name__ == '__main__':
    path = PathExtractor()
    r = path.extract_unipath("The time for action is now. It's never too late.")

    try:
        pprint(r)
    except Exception as e:
        print(e)
