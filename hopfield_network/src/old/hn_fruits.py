
import numpy as np
import pandas as pd

names = ['Apple','Banana','Red','Yellow']
neurons = pd.Series([-1]*len(names), index=names,name='Activation')

links = pd.DataFrame(np.zeros(shape=(len(neurons),len(neurons))), index=names, columns=names)
links.index.name = 'input'
links.columns.name = 'output'

print(links)

def learn_event(event, links):
    pairs = [(x,y) for x in links.index for y in links.columns if x!= y]
    for (x,y) in pairs:
        if (x in event) & (y in event):
            links.ix[x, y] += 1
        elif (x in event) & (not y in event):
            links.ix[x, y] -= 1
        elif (x not in event) & (y in event):
            links.ix[x, y] -= 1
        else:
            links.ix[x, y] += 1

def run_hopfield(neurons, links):
    for index, value in links.iterrows():
        a = (value * neurons).sum()
        if a >= 0:
            neurons[index] = 1
        else:
            neurons[index] = -1


learn_event(['Red', 'Apple'], links)
print(links)

learn_event(['Yellow', 'Banana'], links)
print(links)


neurons['Red'] = 1
print(neurons)

run_hopfield(neurons, links)
print(neurons)

learn_event(['Yellow', 'Apple'], links)
print(links)

neurons['Red'] = 1; neurons['Apple'] = -1
print(neurons)


run_hopfield(neurons, links)
print(neurons)

