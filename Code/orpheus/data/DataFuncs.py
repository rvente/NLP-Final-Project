# Copyright (C) 2020 Ralph "Blake" Vente and Anthony Chen
#
# orpheus is free software: you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
import pandas as pd
import random

#cont how many docs an author has
def CountDocs(f):

    #dict of authors to doc count
    authors = {}

    reviews = pd.read_json(f, lines=True, chunksize = 1000000)

    for chunk in reviews:
        for u in chunk['user_id']:
            if u in authors:
                authors[u] += 1
            else:
                authors[u] = 0
        print('\ncounted authors in chunk:\n')
        print(chunk['user_id'])

    return authors

#returns list of authors who meet review_cutoff
def Prune(d, review_cut):
    #get authors with more than review_cut reviews
    a = []
    for key, value in d.items():
        if value >= review_cut:
            print(key, ' has more than ',review_cut, ' reviews')
            a.append(key)

    print('\nNumber of authors with more than ', review_cut, 'reviews: ', len(a))
    return a

#returns dataset, f is original dataset, list a is authors to choose from, sample size is number of authors, reviews_each is to choose how many reviews each author gets in dataset.
def GetSample(f, a, samplesize, reviews_each):
    reviews = pd.read_json(f, lines=True, chunksize = 1000000)

    #trim to samplesize
    while len(a) > (samplesize):
        r = random.choice(a)
        a.remove(r)
        print('Removed ramdom user to decrese samplesize: ', r)

    w = {}
    print('Making dict of authors and their texts')
    for chunk in reviews:
        for index, row in chunk.iterrows():
            if row['user_id'] in a:
                if row['user_id'] in w:
                    w[row['user_id']].append(row['text'])
                else:
                    w[row['user_id']] = [row['text']]
        print('\nProcessed Chunk:\n')
        print(chunk)
    print('\nCutting dataset down to size\n')

    final = []
    #trim to reviews_each
    for key, value in w.items():
        while len(value) > reviews_each:
            value.remove(random.choice(value))
            print('Removed text from user, too many reviews: ', key)
        for t in value:
            final.append([key,t])
    #converting to excel file
    #check slice for bad authors
    slice = []
    for key in w.keys():
        slice.append([key,w[key][0]])

    #converting to excel file
    slice_df = pd.DataFrame(slice)
    slice_df.to_excel('Slice.xlsx', index = False, header = False)

    print('Converting to Excel as Sample.xlsx')
    new_df = pd.DataFrame(final)
    new_df.to_excel('Sample.xlsx', index = False, header = False)
