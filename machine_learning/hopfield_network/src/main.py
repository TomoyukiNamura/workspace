import numpy as np
import pandas as pd
from hfnet import HNPict


# make picts
pict_d = [
    '#### ',
    '#   #',
    '#   #',
    '#   #',
    '#### '
    ]
pict_j = [
    '#####',
    '   # ',
    '   # ',
    '#  # ',
    ' ##  '
    ]
pict_c = [
    ' ####',
    '#    ',
    '#    ',
    '#    ',
    ' ####'
    ]
pict_m = [
    '#   #',
    '## ##',
    '# # #',
    '#   #',
    '#   #'
    ]
pict_test = [
    '#### ',
    '    #',
    '    #',
    '#  # ',
    ' ##  '
    ]

# make training data
train = [pict_c, pict_d, pict_m, pict_j, pict_m, pict_c, pict_d]

# init hopfield_net
hopfield_net = HNPict(25)

# show links
print(hopfield_net.links)

# train
for index in range(len(train)):
    hopfield_net.fit(train[index])

# show links
print(hopfield_net.links)

# test
pict_pred = hopfield_net.recall(pict_test,3)
hopfield_net.show_pict(pict_test)
hopfield_net.show_pict(pict_pred)
