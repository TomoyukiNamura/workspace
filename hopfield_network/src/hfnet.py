import numpy as np
import pandas as pd
from copy import deepcopy


class HopfieldNetwork():
    def __init__(self, n_neurons):
        self.n_neurons = n_neurons
        self.links     = np.zeros(shape=(self.n_neurons, self.n_neurons))

    def _fit(self, neurons):
        update_mat = np.dot(neurons.reshape(self.n_neurons,1), neurons.reshape(1,self.n_neurons))
        self.links += (update_mat - np.diag(np.diag(update_mat)))

    def _recall(self, input_neurons, n_step):
        output_neurons = deepcopy(input_neurons)
        for t in range(n_step):
            for i in range(output_neurons.shape[0]):
                output_neurons[i] = 2 * (np.dot(self.links[i,:], output_neurons) >= 0) - 1
        return output_neurons


class HNPict(HopfieldNetwork):
    def __init__(self, n_neurons):
        super(HNPict, self).__init__(n_neurons)

    def _pict2neurons(self, pict):
        pict2 = deepcopy(pict)
        for i in range(len(pict)):
            pict2[i] = list(pict[i])
        np_pict = np.array(pict2)
        np_pict = np.reshape(np_pict, (np_pict.shape[0]*np_pict.shape[1],))
        neurons = 2 * (np_pict != ' ') - 1
        return neurons

    def _neurons2pict(self, neurons):
        np_pict = np.array(list(' ')*neurons.shape[0])
        np_pict[neurons==1] = '#'
        pict = list(np.reshape(np_pict, (5,5)))
        for i in range(len(pict)):
            pict[i] = ''.join(pict[i])
        return pict

    def fit(self, pict):
        self._fit(self._pict2neurons(pict))

    def recall(self, input_pict, n_step):
        input_neurons  = self._pict2neurons(input_pict)
        output_neurons = self._recall(input_neurons, n_step)
        return self._neurons2pict(output_neurons)

    def show_pict(self, pict):
        for index in range(len(pict)):
            print(pict[index])


class HNWords(HopfieldNetwork):
    def __init__(self, n_neurons):
        super(HNWords, self).__init__(n_neurons)

    def _words2neurons(self, words):
        neurons = np.array([-1]*self.n_neurons)
        if 'Apple' in words:  neurons[0] = 1
        if 'Banana' in words: neurons[1] = 1
        if 'Red' in words:    neurons[2] = 1
        if 'Yellow' in words: neurons[3] = 1
        return neurons

    def _neurons2words(self, neurons):
        words = ''
        if neurons[0] == 1: words += 'Apple '
        if neurons[1] == 1: words += 'Banana '
        if neurons[2] == 1: words += 'Red '
        if neurons[3] == 1: words += 'Yellow '
        return words

    def fit(self, words):
        self._fit(self._words2neurons(words))

    def recall(self, input_words, n_step):
        input_neurons  = self._words2neurons(input_words)
        output_neurons = self._recall(input_neurons, n_step)
        return self._neurons2words(output_neurons)


