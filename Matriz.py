import tensorflow as tf
# Declaramos las 2 matricez como constantes
matrizA = tf.constant([[1,2,-3],[4,0,2]])
matrizB = tf.constant([[3,1],[2,4],[-1,5]])

# Multiplicamos las matricez
product = tf.matmul(matrizA, matrizB)

# Ejecutamos la sesion con el metodo 1
sess = tf.Session()
result = sess.run(product)
print(result)
sess.close()

# Ejecutamos la sesion con el metodo 2
#with tf.Session() as sess:
#    result2 = sess.run(product)
#    print(result2)