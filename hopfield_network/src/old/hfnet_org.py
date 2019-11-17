import numpy as np
import pandas as pd


class HopfieldNetwork():
    def __init__(self):
        self._init_links()

    def _init_links(self):
        #names = [(x,y) for x in range(5) for y in range(5)]
        #self.links = pd.DataFrame(np.zeros(shape=(25, 25)), index=names, columns=names)
        self.links = np.zeros(shape=(25, 25))
        #self.links.index.name   = 'input'
        #self.links.columns.name = 'output'

    def _pict2neurons(self, pict):
        #names = [(x,y) for x in range(5) for y in range(5)]
        #neurons = pd.Series([-1]*len(names), index=names, name='Activation')
        #for y, line in enumerate(pict):
        #    for x in range(len(line)):
        #        if line[x] != ' ':
        #            neurons[(x,y)] = 1
        #        else:
        #            neurons[(x,y)] = -1

        for i in range(len(pict)):
            pict[i] = list(pict[i])
        np_pict = np.reshape(np.array(pict), (25,))
        neurons = 2 * (np_pict != ' ') - 1
        return neurons

    def _neurons2pict(self, neurons):
        pict = []
        for y in range(5):
            pict_part = ''
            for x in range(5):
                #if neurons[(x,y)] == 1:
                if neurons[x,y] == 1:
                    pict_part += '#'
                else:
                    pict_part += ' '
            pict.append(pict_part)
        return pict

    def learn_pict(self, pict):
        neurons = self._pict2neurons(pict)
        #pairs = [(f,t) for f in self.links.index for t in self.links.columns if f != t]
        pairs = [(f,t) for f in range(self.links.shape[0]) for t in range(self.links.shape[1]) if f != t]
        for (f,t) in pairs:
            if neurons[f] == neurons[t]:
                #self.links.ix[f, t] += 1
                self.links[f,t] += 1
            else:
                #self.links.ix[f, t] -= 1
                self.links[f,t] -= 1

    def run_hopfield(self, input_pict):
        input_neurons = self._pict2neurons(input_pict)
        #for index, value in self.links.iterrows():
        #    a = (value * neurons).sum()
        #    if a >= 0:
        #        neurons[index] = 1
        #    else:
        #        neurons[index] = -1
        output_neurons = 2 * (np.dot(self.links, input_neurons) >= 0) - 1
        output_pict = self._neurons2pict(output_neurons)
        return output_pict


    def show_pict(self, pict):
        for index in range(len(pict)):
            print(pict[index])
    

