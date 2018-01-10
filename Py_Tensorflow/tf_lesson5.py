#coding=utf-8

"""lesson 5 code
	例子2
"""


import tensorflow as tf 
import numpy as np 


 #create data
x_data = np.random.rand(100).astype(np.float32)
y_data = x_data*0.1 + 0.3

### create tensorflow structure start ###
# Weights 可能是个矩阵,大写容易辨别
# 从初始值不断到预测状态
Weights = tf.Variable(tf.random_uniform([1],-1.0,1.0))
biases = tf.Variable(tf.zeros([1]))

y = Weights*x_data + biases
# 预测值与真实值的差距
loss = tf.reduce_mean(tf.square(y-y_data))
optimizer = tf.train.GradientDescentOptimizer(0.5)
train = optimizer.minimize(loss)

 # 初始化,变量都生效,结构激活
init = tf.initialize_all_variables()
### create tensorflow structure end ###
# session类似于指针,
sess = tf.Session()
sess.run(init)

for step in range(201):
	# 真正训练
	sess.run(train)
	if step % 20 == 0:
		print (step,sess.run(Weights),sess.run(biases))