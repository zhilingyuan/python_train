import tensorflow as tf

x = tf.constant([1,2,3])
y = tf.constant([4,5,6])
z = tf.constant([7,8,9])

p = tf.stack([x,y,z])

sess = tf.Session()
print(sess.run(tf.shape(p)))
print(sess.run(p))
