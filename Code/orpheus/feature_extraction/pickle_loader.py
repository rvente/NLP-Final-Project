# Copyright (C) 2020 Ralph "Blake" Vente and Anthony Chen
#
# orpheus is free software: you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
#
# This program will convert a parse tree into a collections.Counter() of the
# directed nested n-grams of the constituency parse tree.


import pandas as pd
from instance_parser import extract_unipath



if __name__ == "__main__":
    try:
        df = pd.read_pickle('small.pkl')

        doc0: 'Spacy.Doc' = df['documents'][0]
        print(doc0)
        parse = extract_unipath(doc0)
        print(parse)

    except Exception as e:
        print(e)
    pass