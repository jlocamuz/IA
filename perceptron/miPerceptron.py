import math
from turtle import color
import matplotlib.pyplot as plt

def sigmoid(x):
    sig = 1 / (1 + math.exp(-x))
    return sig

def perceptron(x1, x2, bias, w0, w1, w2):
    #print(w0, w1, w2)
    z = x1*w1 + x2* w2 +bias * w0
    return sigmoid(z)
    
def aprender(compuerta):


    lr = 0.1
    w0 = 0.9
    w1=0.66
    w2=-0.2
    epochs = 0
    x = 0
    colors = ['green', 'red', 'black', 'yellow']
    while True:
        for indice, i in enumerate(compuerta):
            # aca no se tienen q pisar las neuronas no? 
            ps = perceptron(i[0][0],i[0][1], 1, w0, w1, w2)
            error = abs(i[1] - ps)
            plt.plot(x,error,"o",color=colors[indice])
            x += 1
            #print('error', error)
            deltaw0 = error * lr * 1
            deltaw1 = error * lr * i[0][0]
            deltaw2 = error * lr * i[0][1]
            w0 = w0 + deltaw0
            w1 = w1 + deltaw1
            w2 = w2 + deltaw2
        
        if epochs > 10000: 
            print('no aprendio')
            break
        
        if error < 0.01:
            plt.show()
            print(f'aprendio en {epochs} epochs ')
            break

        epochs += 1
if __name__ == '__main__':
    compuerta_or = [((0, 0), 0), ((0, 1), 1), ((1, 0), 1), ((1,1), 1)]
    aprender(compuerta_or)
    #compuerta_and = [((0, 0), 0), ((0, 1), 0), ((1, 0), 0), ((1,1), 1)]
    #aprender(compuerta_and)
    #compuerta_xor = [((0, 0), 0), ((0, 1), 1), ((1, 0), 1), ((1,1),0)]
    #aprender(compuerta_xor)
    plt.show()