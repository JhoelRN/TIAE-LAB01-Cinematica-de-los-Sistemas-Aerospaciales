import numpy as np
import math as m
from numpy import matrix




def mensaje():
    print("Bienvenido XDs")

def mensajeObj(nombre):
    cadena = "Bienvenido "+nombre
    return cadena


#TIAE LABORATORIO 01

#PRINCIPAL ROTATIONS

#Preg05 (Matriz   R'x,phi'  )
def Rx(phi):
    return np.matrix([[1,0,0],
                 [0, m.cos (phi), -m.sin(phi)],
                 [0, m.sin(phi), m.cos(phi)]])

#Preg06 (Matriz   R'y,theta'  )
def Ry(theta):
    return np.matrix([[m.cos(theta) , 0, m.sin(theta)],
                   [0,             1,             0],
                   [-m.sin(theta), 0, m.cos(theta)]])

#Preg07 (Matriz   R'z,psi'  )
def Rz(psi):
    return np.matrix([[m.cos(psi),  -m.sin(psi),   0],
                 [m.sin(psi),    m.cos (psi),   0],
                 [0,                 0,         1]])

#preg08 (Body a NED)
def J11(phi,theta,psi):
    R1 = Rx(phi)
    R2 = Ry(theta)
    R3 = Rz(psi)
    return R3*R2*R1 #R de body a NED

def J22(phi,theta,psi):
    return np.matrix([[1,m.sin(phi)*m.tan(theta),m.cos(phi)*m.tan(theta)],
                 [0, m.cos (phi), -m.sin(phi)],
                 [0, m.sin(phi)/m.cos(theta), m.cos(phi)/m.cos(theta)]])

'''
def J(J11,J22):
    return np.matrix([[J11,np.zeros_like(J11)],
                 [np.zeros_like(J11), J22]])
'''


#preg09 (NED a Body) (Jnb)
def J11rev(phi,theta,psi):
    R1 = Rx(phi)
    R2 = Ry(theta)
    R3 = Rz(psi)

    R = R3*R2*R1
    R_inv = np.linalg.inv(R) # es la inversa
    return R_inv #R de body a NED

def J22rev(phi,theta,psi):
    return np.matrix([[1,0,-m.sin(theta)],
                 [0, m.cos (phi), m.cos(theta)*m.sin(phi)],
                 [0, -m.sin(phi), m.cos(theta)*m.cos(phi)]])


#preg10 y #preg11 (ECEF a NED)
##la matriz Ren es:
def J11en(mu,l):
    return np.matrix([[-m.cos(l) , -m.sin(l), -m.cos(l)*m.cos(mu)],
                   [-m.sin(l)*m.sin(mu), m.cos(l),-m.sin(l)*m.cos(mu)],
                   [-m.cos(mu), 0, -m.sin(mu)]])

##la matriz Rne es:
def J11ne(mu,l):
    R = J11en(mu,l)
    R_inv = np.linalg.inv(R) # es la inversa
    return R_inv
