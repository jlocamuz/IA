import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
from probando2 import *

personas = manipular_imagenes('./imagenes', './modificadas/')

# y estos son los resultados que se obtienen, en el mismo orden 
# 0 - A - CLAUDIA // 1 - B - ROSARIO
target_data = np.array([[0],[1],[0],[1],[0],[1],[0],[1],[0],[1]], "float32")

# len(personas) = 10
# len(personas[0]) = 7681  
for indice, i in enumerate(personas):
    personas[indice] = i[:-1] 
# len(personas[0]) = 7680

# cargamos los 7860 valores de cada pixel
training_data = np.array(personas, "float32")

capa1 = tf.keras.layers.Dense(units=100, input_shape=[7680])  # 100 neuronas con una entrada x pixel de imagen 7680
capa2 = tf.keras.layers.Dense(units=1, input_shape=[100]) # 1 neurona con 100 entradas , capa anterior

modelo = tf.keras.Sequential()
modelo.add(capa1)
modelo.add(capa2)

modelo.compile(
    optimizer=tf.keras.optimizers.Adam(0.1),
    loss='mean_squared_error'
)

historial = modelo.fit(training_data, target_data, epochs=50, verbose=False)
plt.plot(historial.history['loss'])
plt.show()
