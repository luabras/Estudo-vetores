import numpy as np
import matplotlib.pyplot as plt

def plotVectors(vecs, cols, alpha=1):
    """
    Plot set of vectors.

    Parameters
    ----------
    vecs : array-like
        Coordinates of the vectors to plot. Each vectors is in an array. For
        instance: [[1, 3], [2, 2]] can be used to plot 2 vectors.
    cols : array-like
        Colors of the vectors. For instance: ['red', 'blue'] will display the
        first vector in red and the second in blue.
    alpha : float
        Opacity of vectors

    Returns:

    fig : instance of matplotlib.figure.Figure
        The figure of the vectors
    """
    plt.figure()
    plt.axvline(x=0, color='#A9A9A9', zorder=0)
    plt.axhline(y=0, color='#A9A9A9', zorder=0)

    for i in range(len(vecs)):
        x = np.concatenate([[0,0],vecs[i]])
        plt.quiver([x[0]],
                   [x[1]],
                   [x[2]],
                   [x[3]],
                   angles='xy', scale_units='xy', scale=1, color=cols[i],
                  alpha=alpha)

#vetor unitario: vetor/modulo
def vetorUnitario(u):
    uUnit = u/np.linalg.norm(u)
    
    return uUnit

u = [1, 2]
v = [2, 1]

#convertendo as listas em vetores no numpy
u = np.array(u)
v = np.array(v)

#soma de vetores
print(u+v)

#criando outros vetores diretamente no numpy
u1 = np.array([2, 3])
v1 = np.array([4, -1])

#produto escalar de u1.v1 (x1.x2 + y1.y2)
print(u1.dot(v1))

#modulo: raiz quadrada do produto escalar de um vetor com ele mesmo
modU1 = np.linalg.norm(u1)
print(modU1)

modV1 = np.linalg.norm(v1)
print(modV1)

#atribuindo cores em hexadecimal a variaveis
laranja = '#FF9A13'
azul = '#1190FF'
corAleatoria = '#11FFFF'

#vetor resultante
r = u1+v1

#usando funcao do matplotlib para plotar vetores
plotVectors([u1, v1, r], [laranja, azul, corAleatoria])

plt.xlim(-5, 10)
plt.ylim(-5, 5)

plt.show()

#usando a funcao para calcular vetor unitario
vetU = vetorUnitario(u)
print(vetU)