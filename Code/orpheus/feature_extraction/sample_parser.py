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

    def extract_unipath(self, document):
        doc = self.nlp(document)
        
        def parse(span, fn, appendable) -> 'List[str]':
            children = list(span._.children)
            for child in children:
                parse(child, fn, appendable)
            appendable.append( fn(span) )

        by_sentence = []
        for sent in doc.sents:
            v = []
            parse(sent,
                # leaf nodes have no labels?? extract them from the string.
                  lambda x: x._.labels or (x._.parse_string.partition(" ")[0][1:], ),
                  v) # parse mutates v
            by_sentence.append(v)
        # reduce surrounding tuples so we have List[str]
        return by_sentence


if __name__ == '__main__':
    # nlp = spacy.load('en')
    # nlp.add_pipe(BeneparComponent('benepar_en'))
    # doc = nlp('The time for action is now. Its never too late to do something.')
    # print(list(doc.sents))
    # sent = list(doc.sents)[0]
    # print(sent._.parse_string)
    # print(sent._.labels)

    # def parse(span, fn):
    #     children = list(span._.children)
    #     fn(span)
    #     if not children:
    #         return
    #     for child in children:
    #         parse(child, fn)

    # parse(sent, lambda x: print(x._.labels or (
    #     # leaf nodes have no labels?? extract them from the string.
    #     x._.parse_string.partition(" ")[0][1:], )))

    # InteractiveConsole(locals=dict(globals(), **locals())
    #                    ).interact(pformat(locals()), "Goodbye")
    path = PathExtractor()
    r = path.extract_unipath("The time for action is now. It's never too late.")

    try:
        pprint(r)
    except Exception as e:
        print(e)
