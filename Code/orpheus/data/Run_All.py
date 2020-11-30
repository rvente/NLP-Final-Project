# Copyright (C) 2020 Ralph "Blake" Vente and Anthony Chen
#
# orpheus is free software: you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
from DataFuncs import CountDocs, Prune, GetSample

#This has not been run on a PC with less than 49GB ram. Usage is >36GB. Maybe go to DataFuncs.py and decrease all chunksizes
#Timed run, default settings:

#count how many docs each author has
authorcount = CountDocs('yelp_academic_dataset_review.json')

#get list of authors with more than 30 reviews
pruned = Prune(authorcount,30)

#generate excel file with 1000 authors and 30 docs each, randomly chosen. Authors must have more than 30 docs each
GetSample('yelp_academic_dataset_review.json', pruned, 1000, 30)
