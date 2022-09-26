from re import I
import numpy as np
import scipy as sc
import matplotlib.pyplot as plt

# FUNCION DEL COSTE DE ERROR
# th = [x, y]
func = lambda th: np.sin(1 / 2 * th[0] **2 - 1/4 * th[1] ** 2 + 3) * np.cos(2 * th[0] + 1 - np.e ** th[1])

res = 100 

# Returns num evenly spaced samples, calculated over the interval [start, stop].
# numpy.linspace(start, stop, num=50)
_X = np.linspace(-2, 2, res)
_Y = np.linspace(-2, 2, res)

# Return a new array of given shape and type, filled with zeros.
_Z = np.zeros((res, res))

"""
>>> for count, value in enumerate(values):
...     print(count, value)
...
0 a
1 b
2 c
"""

for ix, x in enumerate(_X):
    for iy, y in enumerate(_Y):
        _Z[iy, ix] = func([x,y])

# contourf([X, Y,] Z, [levels], **kwargs)
# contour and contourf draw contour lines and filled contours
plt.contourf(_X, _Y, _Z, 100)
plt.colorbar()

# Random values in a given shape.
# valores del 0 - 1 por eso hace lo del * 4 - 2 para q esten entre [-2, 2]
Theta = np.random.rand(2) * 4 - 2
_T = np.copy(Theta)

# incremento
h = 0.001

#learning right ? 
lr = 0.001

# punto de inicio
plt.plot(Theta[0], Theta[1], "o", c="white")


grad = np.zeros(2)

for _ in range(10000): 
    # 10000 veces 2 iteraciones ya q Theta vector x2
    for it, th in enumerate(Theta):
        # hacemos copia Theta para no modificar la variable del punto inicial...
        _T = np.copy(Theta)

        # valor menos incremento... menos pq es decreciente? 
        _T[it] = _T[it] - h
        # derivada valor_modificado - valor_anterior
        deriv = (func(_T) - func(Theta)) / h
        # vector gradientes: derivadas parciales
        grad[it] = deriv

    # REPETIR HASTA CONVERGENCIA --> queremos q la pendiente de la funcion de coste sea proxima a nula --> minimo local --> minimo error
    # a := ratio de aprendizaje = "cuanto afecta el gradiente a la actualizacion de nuestros parametros en cada iteracion"
    # 0 := 0 - a * Vf 
    Theta = Theta - lr * grad
    #print(func(Theta))

    if(_ % 100 == 0): 
        plt.plot(Theta[0], Theta[1], ".", c="red")

plt.plot(Theta[0], Theta[1], "o", c="green")

plt.show()