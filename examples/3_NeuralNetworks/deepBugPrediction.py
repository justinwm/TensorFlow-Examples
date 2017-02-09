#Author: Justin Civi

from __future__ import print_function

import tensorflow as tf
from tensorflow.python.ops import rnn, rnn_cell

batch_size = 2

# Import MNIST data
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("/tmp/data/", one_hot=True)
batch_x, batch_y = mnist.train.next_batch(28)
print(batch_x[0])




