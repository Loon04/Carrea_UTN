import pygame

#cargamos una imagen
#imagen = [pygame.image.load("Carrera_de_mente\imagen_carrera_de_mente.png")]
#imagen = pygame.transform.scale(imagen,(180,180))

imagen_cuadro_verde = [pygame.image.load("Carrera_UTN\cuadrado_verde.png")]

imagen_cuadro_azul = [pygame.image.load("Carrera_UTN\cuadrado_azul.png")]

imagen_personaje = [pygame.image.load("Carrera_UTN\personaje.png")]

def reescalar_imagenes(lista_animaciones,ancho,alto):
    for i in range(len(lista_animaciones)):
        imagen = lista_animaciones[i]
        lista_animaciones[i] = pygame.transform.scale(imagen,(ancho,alto))

x_reescalada = 100
y_reescalada = 90

reescalar_imagenes(imagen_cuadro_azul,x_reescalada,y_reescalada)

reescalar_imagenes(imagen_cuadro_verde,100,80)

reescalar_imagenes(imagen_personaje,30,50)