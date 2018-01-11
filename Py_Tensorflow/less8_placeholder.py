#coding=utf-8
import tensorflow as tf 

v1 = tf.placeholder(tf.float32)
v2 = tf.placeholder(tf.float32)

out_v = tf.multiply(v1,v2)

with tf.Session() as sess:
	print(sess.run(out_v,feed_dict={v1:[2.],v2:[3.]}))