# -*- coding: utf-8 -*-

import numpy as np
from numpy.random import binomial
import matplotlib.pyplot as plt
import networkx as nx


class BaseGraph(nx.Graph):
    def __init__(self, nodes, edge_mat):
        super().__init__()
        self.add_nodes_from(nodes)
        self.edge_mat = edge_mat
        self.add_edges_from(self._mat2edges(nodes, edge_mat))
        
    def _mat2edges(self, nodes, mat):
        edges = []
        for hi, hv  in enumerate(mat):
            for wi, wv in enumerate(hv):
                if(wv): edges.append((nodes[hi], nodes[wi]))
        return edges
    
    def plot_graph(self):
        pos = nx.spring_layout(self)
        nx.draw_networkx(self, pos, with_labels=True)
        plt.axis("off")
        plt.show()


class ProbGraph(BaseGraph):
    def __init__(self, nodes, edge_mat, conditional_prob):
        super().__init__(nodes, edge_mat)
        self.conditional_prob = conditional_prob

    def gen_one_sample(self):
        
        # サンプル初期化
        sample = np.zeros(len(self.nodes), dtype='int')
        
        # サンプル発生させるノードidの順番を取得
        node_ids = list(range(len(self.nodes)))
        
        # サンプル発生
        for node_id in node_ids:
            # 親ノードのサンプル取得
            parent_values = sample[self.edge_mat[:,node_id]==1]
            
            # 条件付き確率分布のid取得
            condprob_distid = np.dot(parent_values, 2 ** np.arange(parent_values.shape[0]))
            
            # 条件付き確率取得
            condprob = self.conditional_prob[node_id][condprob_distid, 1]
            
            # サンプル発生
            sample[node_id] = binomial(n=1, p=condprob)
            
        return sample
    
    def gen_samples(self, n):
        return np.array([self.gen_one_sample() for i in range(n)])
