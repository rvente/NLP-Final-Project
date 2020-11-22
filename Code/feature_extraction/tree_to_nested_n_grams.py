# Copyright (C) 2020 Ralph "Blake Vente
#
# orpheus is free software: you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
#
# This program will convert a parse tree into a collections.Counter() of the
# directed nested n-grams of the constituency parse tree.


import unittest

import spacy
from benepar.spacy_plugin import BeneparComponent

import tensorflow as tf
print(tf.__version__)
tf.gfile = tf.io.gfile


class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)


class PathExtractor():
    def __init__(self, min_len=2, max_len=5):
        pass


if __name__ == '__main__':
    nlp = spacy.load('en')
    nlp.add_pipe(BeneparComponent('benepar_en'))
    doc = nlp('The time for action is now. Its never too late to do something.')
    sent = list(doc.sents)[0]
    print(sent._.parse_string)
    print(sent._.labels)
    print(list(sent._.children)[0])
    # unittest.main()
