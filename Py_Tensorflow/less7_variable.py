#coding=utf-8
import tensorflow as tf 
state1 = tf.Variable(0, name='connter1')
state2 = tf.Variable(1, name='connter2')
# print state1.name
# print state2.name

one = tf.constant(1)
new_value = tf.add(one,state2)
# print new_value
update = tf.assign(state2, new_value)

init = tf.initialize_all_variables()

with tf.Session() as sess:
	sess.run(init)
	# sess.run(update)
	print sess.run(state2)