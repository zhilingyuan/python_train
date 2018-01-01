import tensorflow as tf
import numpy as np
import pdb
sess=tf.Session()
a = tf.constant(np.random.rand(5, 5, 2))
b = tf.constant(np.random.rand(5, 2, 10))
c = tf.matmul(a,b)#a*b #还是要阅读文档 试不出来
#第一维度一定要相同
#在第一维度后的进行二维matmul（5，2）*（2，5）
#所以在高维也是一样
print('  '+str(sess.run(c)))
pdb.set_trace()
#print('     '+str(sess.run(b)))
#print('  '+str(sess.run(a)))
sess.close()

