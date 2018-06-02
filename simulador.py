# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
#Definimos un robot con una pose de 3 grados de libertad: x,y,theta con posición y orientación inicial (0,0,0)
num_robot = 30#Número de robots
uder = 1
uizq = 1
radio = 0.005
L = 0.1
dim = 300 #define las dimensiones del mapa. Suponemos un recinto cuadrado

#Definimos los genes aleatorios de cada robot así como la posición aleatoria inicial
#Funciones configuración robot
def gen(num_robot):
    genes = np.random.random_sample((num_robot,3,10))
    return genes
genes = gen(num_robot) #Creación código genético del robot

def g_pose_i(num_robot,dim):
  robot=np.array((dim-1)*np.random.random_sample((num_robot,3)))#el rango está parametrizado y normalizado a las posiciones de los vectores
  for i in range(num_robot):
      for j in range(3):
          robot[i][j] = int(robot[i][j])
  return robot

robot = g_pose_i(num_robot,dim)#Inicialización 30 robots

def ini(robot,dim,num_robot):#♠creación ycondiciones iniciales del mapa
    mapa = num_robot*np.ones((dim,dim,3))
        
    for j in (124,174):#eje y, vertical
    #Definimos zona de comida
        for k in (24,74):#eje x, horizontal
            mapa[k][j][1] = 0#comida 
            mapa[k][j][2] = 1#rojo
    #Definimos zona de veneno
        for l in (224,274):#eje x, horizontal
            mapa[l][j][1] = 1#veneno 
            mapa[l][j][2] = 1#rojo 
    #situamos los robots        
    for i in range(num_robot):#i va moviéndose por las id de los robots
        xtemp = int(robot[i][0])#las posiciones x e y coinciden con las posiciones de los vectores
        ytemp = int(robot[i][1])
        #asignamos las posiciones iniciales de los robots tras crear el mapa
        mapa[xtemp][ytemp][0] = i
        
    return mapa

mapa = ini(robot,dim,num_robot)


def act_map(mapa,o_robot,num_robot):#esta función actualizará el mapa tras los movimientos
    """
    Notación: mapa es un array (id_robot,gnd_col,air_col)
    
    **gnd_col: color suelo  0 --> comida
                            1 --> veneno
    **air_col: color aire   0 --> azul
                            1 --> rojo
    """
    for i in range(num_robot):#i va moviéndose por las id de los robots
        xtemp = int(o_robot[i][0])#las posiciones x e y coinciden con las posiciones de los vectores
        ytemp = int(o_robot[i][1])
        #asignamos las posiciones iniciales de los robots tras crear el mapa
        mapa[xtemp][ytemp][0] = i
    return mapa
def sensors(robot, neurons): 
    #el protocolo consiste en recorrer el mapa buscando los robots
    #cuando se encuentre un robot se leen los sensores y se reinicia la posición
    #dejando el color del aire, que se borrará al final
    
    for i in range(dim):#eje x, horizontal
        for j in range(dim):#eje y, vertical
            if(mapa[i][j][0] != 30):
#               neurons[mapa[i][j][0]][] 
    return 0
#Definimos la función de movimiento:

def movimiento(uizq,uder,robot,radio,L,num_robot):
    v = (uizq+uder)/2
    w = (2*(uizq+uder))/L
    for n in range(num_robot):       
        robot[n][0] = robot[n][0]+v*(np.cos(robot[n][2])*0.05)
        robot[n][1] = robot[n][1]+v*(np.sin(robot[n][2])*0.05)
        robot[n][2] = robot[n][2]+w*radio
    return robot

print(mapa[24][174])