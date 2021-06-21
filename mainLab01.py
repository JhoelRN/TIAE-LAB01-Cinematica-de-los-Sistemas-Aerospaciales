import matplotlib
import numpy as np
import math as m

from numpy import matrix

import ast #para convertir a float valores csv





import conversionesLab01 as fconv

'''
nom = input("Ingrese un nombre ")
cadenaReturn = fconv.mensajeObj(nom)
print(cadenaReturn) 
print(" ")
'''


# TIAE LAB01 - 2021A 
print(" ******************** LABORATORIO 01 ******************** ")

#preg05
print(" ")
print("-      Pregunta 05")
angulophi = m.pi/3
print("The test angle phi is : ", angulophi)
Rx = fconv.Rx(angulophi)
Rx_redond = np.round(Rx,decimals=2)
print("Rx ↓↓")
print(Rx_redond)

#preg06
print(" ")
print("-      Pregunta 06")
angulotheta = m.pi/4
print("The test angle theta is : ", angulotheta)
Ry = fconv.Ry(angulotheta)
Ry_redond = np.round(Ry,decimals=2)
print("Ry ↓↓")
print(Ry_redond)

#preg07
print(" ")
print("-      Pregunta 07")
angulopsi = m.pi/5
print("The test angle psi is : ", angulopsi)
Rz = fconv.Rz(angulopsi)
Rz_redond = np.round(Rz,decimals=2)
print("Rz ↓↓")
print(Rz_redond)

#preg08
print(" ")
print("-      Pregunta 08")

#Transformacion matriz R y T (linear angular)
#Matriz J : Body a NED

#euler angles
phi = m.pi/3
theta = m.pi/4
psi = m.pi/5


u = 2 # surge
v = 4 # sway
w = 3 # heave
v_b = np.matrix([[u],
                 [v],
                 [w]])

p = 4# roll
q = 7# pitch
r = 5# yaw
w_b = np.matrix([[p],
                 [q],
                 [r]])



J1 = fconv.J11(phi,theta,psi)
print("J1 ↓↓")
print(J1)
J2 = fconv.J22(phi,theta,psi)
print("J2 ↓↓")
print(J2)

'''
J = fconv.J(J1,J2)
print("J ↓↓")
print(J)
'''


p_dot = J1*v_b
Theta_dot = J2*w_b

print("p_dot ↓↓")
print(p_dot)
print("Theta_dot ↓↓")
print(Theta_dot)

'''
Theta = np.matrix([[phi],
                 [theta],
                 [psi]])

print(Theta)
'''

#preg09
print(" ")
print("-      Pregunta 09")  #NED TO BODY

J1rev = fconv.J11rev(phi,theta,psi)
print("J1rev ↓↓")
print(J1rev)
J2rev = fconv.J22rev(phi,theta,psi)
print("J2rev ↓↓")
print(J2rev)

v_ = J1rev*p_dot #con valores de preg08
w_ = J2rev*Theta_dot 

print("v_ ↓↓")
print(v_)
print("w_ ↓↓")
print(w_)


#preg10
print(" ")
print("-      Pregunta 10")  #ECEF TO BODY

## Primero se realiza conversion de ECEF y NED
## Segundo se realiza la conversion de NED y Body

##rev(2.82)

## Estándar decimal simple	-9.189967	-75.015152     
## otro ejm: (AQP: -16.39889, -71.535)
l = -9.19
mu = -75.02
print("the_test_latitud,l=",l)
print("the_test_longitud,u=",mu)

#ECEF POSITION
x_dot = 4
y_dot = 5
z_dot = 5
ecefPos = np.matrix([[x_dot],
                 [y_dot],
                 [z_dot]])

# 1. [ECEF y NED] # 2. [NED y BODY]
Ren_inv = fconv.J11ne(mu,l) #la inv
Rnb_inv = fconv.J11rev(phi,theta,psi) #la inv
v_be = Ren_inv*Rnb_inv*ecefPos
print("v_be ↓↓")
print(v_be)



#preg11
print(" ")
print("-      Pregunta 11")  #ECEF TO NED
p_dot_en = fconv.J11ne(mu,l) * p_dot
print("p_dot_en ↓↓")
print(p_dot_en)


#%%

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

## CUESTIONARIO
'''
tiempo_seg = []
yaw_deg = []
yawRate = []
u = []
v = []
w = []


with open('/media/jhoelrn/MiParticion/JHOEL/ARCHIVOS DE PROGRAMAS/PYTHON 2021/Lab01 Tecnologia de la Ingenieria Aeronautica y Espacial/CirculoHorario.csv','r',encoding="utf-8") as archivo:
    archivo.readline() #descartamos 1ra linea
    for line in archivo:
        tiempo_seg.append( ast.literal_eval(line.split(',')[0]) ) #Tiempo
        #yaw_deg.append( ast.literal_eval(line.split(',')[1]) ) #Yaw
        yawRate.append( ast.literal_eval(line.split(',')[4]) ) #Yaw Rate
        #u.append( ast.literal_eval(line.split(',')[5]) ) # u
        #v.append( ast.literal_eval(line.split(',')[6]) ) # v
        #w.append( ast.literal_eval(line.split(',')[7]) ) # w




#float(close[2]) #no

##pruebas (comprob) ///////////////////////
print(tiempo_seg)

print(tiempo_seg[0])
#print(yaw_deg[0])
print(yawRate[0])
#print(u[0])
#print(v[0])
#print(w[0])

#print(len(u))
#print(len(v))
#print(len(w))
##fin pruebas ///////////////////////

print(yawRate)


print(" ")
print(yawRate[0]+yawRate[1])
print(tiempo_seg[0]+tiempo_seg[1])
print(26+37)
plt.plot(tiempo_seg,yawRate)
plt.show()
'''

##lectura
data = pd.read_csv('/media/jhoelrn/MiParticion/JHOEL/ARCHIVOS DE PROGRAMAS/PYTHON 2021/Lab01 Tecnologia de la Ingenieria Aeronautica y Espacial/CirculoHorario.csv',header=0,delimiter=',')
tiempo_seg=data.iloc[:,0]
yawRate=data.iloc[:,4]
u_data = data.iloc[:,5]
v_data = data.iloc[:,6]
w_data = data.iloc[:,7]
n_dot = data.iloc[:,8]
e_dot = data.iloc[:,9]
d_dot = data.iloc[:,10]
latitud_data = data.iloc[:,13]
longitud_data = data.iloc[:,14]


##pruebas
print(data)
print(tiempo_seg)
print(yawRate)
print(len(tiempo_seg))
print(len(yawRate))
print(len(u_data))
print(len(v_data))
print(len(w_data))


#Grafica YawRate (EX.)
plt.plot(tiempo_seg,yawRate)
plt.ylabel('(rad/s)')
plt.xlabel('Tiempo (s)')
plt.title('Figura: Yaw Rate')
#plt.legend(loc=1)
plt.grid(True)
plt.show()


#01 Graficas  BODY frame  ############

plt.plot(tiempo_seg,u_data) #.1
plt.ylabel('Velocidad(m/s)')
plt.xlabel('Tiempo (s)')
plt.title('Figura: Velocidad lineal "u" fijado en cuerpo')
#plt.legend(loc=1)
plt.grid(True)
plt.show()

plt.plot(tiempo_seg,v_data) #.2
plt.ylabel('(rad/s)')
plt.xlabel('Tiempo (s)')
plt.title('Figura: Velocidad lineal "v" fijado en cuerpo')
#plt.legend(loc=1)
plt.grid(True)
plt.show()

plt.plot(tiempo_seg,w_data) #.3
plt.ylabel('(rad/s)')
plt.xlabel('Tiempo (s)')
plt.title('Figura: Velocidad lineal "w" fijado en cuerpo')
#plt.legend(loc=1)
plt.grid(True)
plt.show()




#02 Graficas  ECEF frame  ############
plt.plot(latitud_data,longitud_data,'ro') #.1
plt.ylabel('Latitud')
plt.xlabel('Longitud')
plt.title('Figura: Location ')
#plt.legend(loc=1)
plt.grid(True)
plt.show()


#03 Graficas  NED frame  ############
plt.plot(tiempo_seg,n_dot) #.1
plt.ylabel('Velocidad(m/s)')
plt.xlabel('Tiempo (s)')
plt.title('Figura: Velocidad NED "N" ')
#plt.legend(loc=1)
plt.grid(True)
plt.show()

plt.plot(tiempo_seg,e_dot) #.2
plt.ylabel('Velocidad(m/s)')
plt.xlabel('Tiempo (s)')
plt.title('Figura: Velocidad NED "E" ')
#plt.legend(loc=1)
plt.grid(True)
plt.show()

plt.plot(tiempo_seg,d_dot) #.3
plt.ylabel('Velocidad(m/s)')
plt.xlabel('Tiempo (s)')
plt.title('Figura: Velocidad NED "D" ')
#plt.legend(loc=1)
plt.grid(True)
plt.show()

# %%
