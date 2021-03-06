#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File Name: nn_softmax_regression_gluon.py
# Description: http://zh.d2l.ai/chapter_deep-learning-basics/softmax-regression-gluon.html
# Create Time: 2020-10-02 20:30
# Author: lorne

import d2lzh as d2l
from mxnet import gluon, init
from mxnet.gluon import loss as gloss, nn

batch_size = 256
train_iter, test_iter = d2l.load_data_fashion_mnist(batch_size)

net = nn.Sequential()
net.add(nn.Dense(10))
net.initialize(init.Normal(sigma=0.01))

loss = gloss.SoftmaxCrossEntropyLoss()

trainer = gluon.Trainer(net.collect_params(), 'sgd', {'learning_rate': 0.1})


num_epochs = 5
d2l.train_ch3(net, train_iter, test_iter, loss, num_epochs, batch_size, None,
              None, trainer)
