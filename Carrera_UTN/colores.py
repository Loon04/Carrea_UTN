import pygame

NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)

# Colores adicionales
AMARILLO = (255, 255, 0)
NARANJA = (255, 165, 0)
ROSA = (255, 192, 203)
MORADO = (128, 0, 128)
CIAN = (0, 255, 255)

# Otros colores
GRIS = (128, 128, 128)
GRIS_CLARO = (200, 200, 200)
GRIS_OSCURO = (64, 64, 64)

x_preguntas = 350
y_preguntas = 50
width_preguntas = 180
height_preguntas = 100

x_cuadro_res = 220
y_cuadro_res = 480
width_res = 60
height_res = 30


score = "Score:"

pygame.init()

pygame.font.get_fonts()

myfont = pygame.font.SysFont("Calibri", 30)
myfontGrande = pygame.font.SysFont("Calibri", 40)