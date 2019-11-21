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
            [0.8, 0.2],
            [0.3, 0.7]]),
    np.array([
            [0.1, 0.9],
            [0.7, 0.3]]),
    np.array([
            [0.8, 0.2],
            [0.6, 0.4],
            [0.3, 0.7],
            [0.9, 0.1]]),
    np.array([
            [0.2, 0.8],
            [0.8, 0.2]])]


bg = BaseGraph(nodes, edge_mat)
bg.plot_graph()

# グラフ定義
pg = ProbGraph(nodes, edge_mat, conditional_prob)

#グラフ表示
pg.plot_graph()

# 
sample_data = pg.gen_samples(100)








