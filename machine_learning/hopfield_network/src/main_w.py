import numpy as np
import pandas as pd
from hfnet import HNWords


# make training data
#train = ['Red Apple', 'Yellow Banana', 'Yellow Apple']
train = ['Red Apple', 'Yellow Banana']

# init hopfield_net
hopfield_net = HNWords(4)

# show links
print(hopfield_net.links)

# train
for index in range(len(train)):
    hopfield_net.fit(train[index])

# show links
print(hopfield_net.links)

# test
pict_pred = hopfield_net.recall('Red',5)
print(pict_pred)
