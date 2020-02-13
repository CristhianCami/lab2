from sys import stdin
import math


def suma(r,t):
    k = (r[0] + t[0], r[1] + t[1])
    return k

def resta(r,t):
    k = (r[0] - t[0], r[1] - t[1])
    return k

def multiplicacion(r,t):
    k = (r[0]*t[0] - r[1]*t[1],r[0]*t[1] + r[1]*t[0])
    return k

def division(r,t):
    k = ((r[0]*t[0] + r[1]*t[1])/(t[0]**2+t[1]**2),(r[1]*t[0] - r[0]*t[1])/(t[0]**2+t[1]**2))
    return k

def modulo(r):
    k = (r[0]**2 + r[1]**2)**(1/2)
    return k

def conjugado(r):
    k = (r[0], -1*r[1])
    return k

def cartesianasAPolares(r):
    l = (r[0]**2 + r[1]**2)**(1/2)
    s = math.atan(r[1]/r[0])
    return (l,s*(180/math.pi))

def polaresACartesianas(e):
    h = e[0]
    c = e[1]*(math.pi/180)
    return (h*math.cos(c),h*math.sin(c))

def fase(c):
    return math.atan2(c[1],c[0])

def adicionVectores(a,b):
    r = []
    for i in range(len(a)):
        r.append(suma(a[i],b[i]))
    return r

def inversaVectores(l):
    k = []
    for i in range(len(l)):
        k.append(multiplicacion(l[i],(-1,0)))
    return k

def multiplicacionEscalar(a,b):
    s = []
    for i in range(len(b)):
        s.append(multiplicacion((a,0),b[i]))
    return s

def adicionMatriz(a,b):
    c = []
    for i in range(len(a)):
        c.append([])
        for j in range(len(a[0])):
            c[i].append(suma(a[i][j],b[i][j]))
    return c

def inversaAditivoMatriz(e):
    p = []
    for i in range(len(e)):
        p.append(inversaVectores(e[i]))
    return p

def multiplicacionEscalarMatriz(a,b):
    e = []
    for i in range(len(b)):
        e.append([])
        for j in range(len(b[i])):
            e[i].append(multiplicacion((a,0),b[i][j]))
    return e

def transpuesta(e):
    c = []
    for i in range(len(e[0])):
        c.append([])
        for j in range(len(e)):
            c[i].append(e[j][i])
    return c
        
def norma(e):
    h = 0
    for i in range(len(e)):
        h += e[i]**2
    rta = h**(0.5)
    return rta

def conjugada(v):
    k= []
    for j in v:
        k.append(conjugado(j))
    return k

def distancia(c,e):
    h = 0
    for i in range(len(c)):
        h += (c[i]-e[i])**2
    rta = h**(0.5)
    return rta

def matrizPorMatriz(a,b):
    e = []
    for i in range(len(a[0])):
        e.append([])
        for j in range(len(b[0])):
            c = (0,0)
            for k in range(len(a)):
                c = suma(multiplicacion(a[i][k],b[j][k]),c)
            e[i].append(c)
    return e

def adjunta(e):
    return conjugada(transpuesta(e))

def isUnitaria(a):
    b = []
    if matrizPorMatriz(a,b):
        return 0

def tensorVector(a,b):
    e = []
    for i in range(len(a)):
        for j in range(len(b)):
            e.append(multiplicacion(a[i],b[j]))
    return e

def tensorMatriz(c,e):
    k = []
    for i in range(len(c)):
        for j in range(len(e)):
            k.append(tensorVector(c[i],e[j]))
    return k


        



