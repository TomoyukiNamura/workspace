
import numpy as np
import pandas as pd


def create_neurons(pict):
    names = [(x,y) for x in range(5) for y in range(5)]
    neurons = pd.Series([-1]*len(names), index=names, name='Activation')
    for y, line in enumerate(pict):
        for x in range(len(line)):
            if line[x] != ' ':
                neurons[(x,y)] = 1
            else:
                neurons[(x,y)] = -1
    return neurons

def show(neurons):
    for y in range(5):
        for x in range(5):
            if neurons[(x, y)] == 1:
                print('#',end='')
            else:
                print(' ',end='')
        print('')

def learn_character(neurons, links):
    pairs = [(f,t) for f in links.index for t in links.columns if f != t]
    for (f,t) in pairs:
        if neurons[f] == neurons[t]:
            links.ix[f, t] += 1
        else:
            links.ix[f, t] -= 1


def run_hopfield(neurons, links):
    for index, value in links.iterrows():
        a = (value * neurons).sum()
        if a >= 0:
            neurons[index] = 1
        else:
            neurons[index] = -1


d = create_neurons([
    '#### ',
    '#   #',
    '#   #',
    '#   #',
    '#### '
    ])
j = create_neurons([
    '#####',
    '   # ',
    '   # ',
    '#  # ',
    ' ##  '
    ])
c = create_neurons([
    ' ####',
    '#    ',
    '#    ',
    '#    ',
    ' ####'
    ])
m = create_neurons([
    '#   #',
    '## ##',
    '# # #',
    '#   #',
    '#   #'
    ])

show(d)
print(d)
print('')
show(j)
print('')
show(c)
print('')
show(m)
print('')

names = [(x,y) for x in range(5) for y in range(5)]
links = pd.DataFrame(np.zeros(shape=(25, 25)), index=names, columns=names)
links.index.name = 'input'
links.columns.name = 'output'


print(d)
print(links)
learn_character(d, links)
print(links)
learn_character(j, links)
print(links)
learn_character(c, links)
print(links)
learn_character(m, links)
print(links)
learn_character(m, links)
print(links)

#print(links)

input_chr = create_neurons([
    '#### ',
    '    #',
    '    #',
    '#  # ',
    ' ##  '])


#print(links)
print(input_chr)
show(input_chr)
run_hopfield(input_chr, links)
show(input_chr)

