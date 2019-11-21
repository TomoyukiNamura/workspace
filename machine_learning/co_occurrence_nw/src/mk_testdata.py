#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
from probgraph import BaseGraph, ProbGraph

nodes = ["A", "B", "C", "D", "E"]

edge_mat = np.array([
    [0, 1, 1, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]])

conditional_prob = [
    np.array([
            [0.5, 0.5]]),
    np.array([
            [0.9, 0.1],
            [0.1, 0.9]]),
    np.array([
            [0.9, 0.1],
            [0.1, 0.9]]),
    np.array([
            [0.95, 0.05],
            [0.1, 0.9],
            [0.1, 0.9],
            [0.05, 0.95]]),
    np.array([
            [0.9, 0.1],
            [0.1, 0.9]])]


# グラフ定義
pg = ProbGraph(nodes, edge_mat, conditional_prob)

#グラフ表示
pg.plot_graph()

# サンプル取得
sample_data = pg.gen_samples(1000)
sample_data2 = pg.gen_samples(1000)

# 共起グラフ作成


data = np.concatenate([sample_data, sample_data2], axis=1)



n_nodes = data.shape[1]
edge_mat = np.zeros([n_nodes,n_nodes])

for i in range(data.shape[0]):
    tmp_data = data[[i],:]
    edge_mat += np.dot(tmp_data.T,tmp_data)

edge_mat -= np.diag(np.diag(edge_mat))


edge_mat

#edge_mat /= data.shape[0]

print(edge_mat)

