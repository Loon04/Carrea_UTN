import pygame
from colores import *

x_rect_imagen = 150
y_rect_imagen = 200

x_rec_personaje_inicio = 100
y_rec_personaje_inicio = 200


def crear_rectangulo(x:int,y:int,width:int,height:int):
    rectangulo = pygame.Rect(x,y,width,height)
    return rectangulo

rec_1 =  crear_rectangulo(x_rect_imagen,y_rect_imagen,100,80)

rec_2 = crear_rectangulo(x_rect_imagen+105,y_rect_imagen,100,80)

rec_3 = crear_rectangulo(x_rect_imagen+210,y_rect_imagen,100,80)

rec_4 = crear_rectangulo(x_rect_imagen+310,y_rect_imagen,100,80)

rec_5 = crear_rectangulo(x_rect_imagen+410,y_rect_imagen,100,80)

rec_6 = crear_rectangulo(x_rect_imagen+510,y_rect_imagen,100,80)

rec_7 = crear_rectangulo(x_rect_imagen+610,y_rect_imagen,100,80)

rec_8 = crear_rectangulo(x_rect_imagen+710,y_rect_imagen,100,80)

rec_9 =  crear_rectangulo(x_rect_imagen,y_rect_imagen+110,100,80)

rec_10 = crear_rectangulo(x_rect_imagen+100,y_rect_imagen+110,100,80)

rec_11 = crear_rectangulo(x_rect_imagen+210,y_rect_imagen+110,100,80)

rec_12 = crear_rectangulo(x_rect_imagen+310,y_rect_imagen+110,100,80)

rec_13 = crear_rectangulo(x_rect_imagen+410,y_rect_imagen+110,100,80)

rec_14 = crear_rectangulo(x_rect_imagen+510,y_rect_imagen+110,100,80)

rec_15 = crear_rectangulo(x_rect_imagen+610,y_rect_imagen+110,100,80)

rec_16 = crear_rectangulo(x_rect_imagen+710,y_rect_imagen+110,100,80)

rec_personaje = crear_rectangulo(x_rec_personaje_inicio,y_rec_personaje_inicio,30,50)

pared_derecha = crear_rectangulo(950,300,1,500)

pared_izquierda = crear_rectangulo(155,200,1,300)