import pygame
from constantes import *
from funciones import *
from imagenes import *
from rectangulos import *



#dimensiones de la pantalla
SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Carrera de mente")

#timer_segundo = pygame.USEREVENT #puedo agregarle +1 +2 #es un evento
#pygame.time.set_timer(timer_segundo,1000) #1000 = 1seg

#TIPOGRAFIA


segundos = "5"
fin_tiempo = False
timer_segundos = pygame.USEREVENT
pygame.time.set_timer(timer_segundos,1000)



flag_run = True
while flag_run: #solo cambiamos el diccionario
    lista_eventos = pygame.event.get()
    for event in lista_eventos:
        if event.type == pygame.QUIT:
            flag_run = False

        if dic_mutable["estado_juego"] == 1:
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos_click = list(event.pos)
                print(pos_click)

                update(pos_click,
                rectangulo_terminar,rectangulo_a,rectangulo_b,rectangulo_c,lista_dato_a,dic_mutable)
            if event.type == pygame.USEREVENT:
                tiempo(event,timer_segundos,dic_mutable,segundos,fin_tiempo)
        elif dic_mutable["estado_juego"] == 0:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    dic_mutable["ingreso"] = dic_mutable["ingreso"][:-1]
                elif event.key == pygame.K_RETURN:
                    dic_mutable["estado_juego"] = 1
                else:
                    dic_mutable["ingreso"] += event.unicode
        elif dic_mutable["estado_juego"] == 2:
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos_click_2 = list(event.pos)
                print(pos_click_2)
                update_2(pos_click_2,rectangulo_volver,dic_mutable)

    SCREEN.fill(AZUL)

    if dic_mutable["estado_juego"] == 1:
        animar_moviento(SCREEN,imagen_cuadro_azul,rec_1)
        animar_moviento(SCREEN,imagen_cuadro_azul,rec_2)
        animar_moviento(SCREEN,imagen_cuadro_azul,rec_3)
        animar_moviento(SCREEN,imagen_cuadro_azul,rec_4)
        animar_moviento(SCREEN,imagen_cuadro_azul,rec_5)
        animar_moviento(SCREEN,imagen_cuadro_verde,rec_6)
        animar_moviento(SCREEN,imagen_cuadro_azul,rec_7)
        animar_moviento(SCREEN,imagen_cuadro_azul,rec_8)
        animar_moviento(SCREEN,imagen_cuadro_azul,rec_16)
        animar_moviento(SCREEN,imagen_cuadro_azul,rec_15)
        animar_moviento(SCREEN,imagen_cuadro_azul,rec_14)
        animar_moviento(SCREEN,imagen_cuadro_azul,rec_13)
        animar_moviento(SCREEN,imagen_cuadro_verde,rec_12)
        animar_moviento(SCREEN,imagen_cuadro_azul,rec_11)
        animar_moviento(SCREEN,imagen_cuadro_azul,rec_10)
        animar_moviento(SCREEN,imagen_cuadro_azul,rec_9)
        animar_moviento(SCREEN,imagen_personaje,rec_personaje)

        #texto_pregunta = render_texto("PREGUNTA",GRIS_OSCURO,myfont)
        texto_terminar = render_texto("TERMINAR",GRIS_OSCURO,myfont)

        #rectangulo_pregunta = crear_cuadro_con_texto(SCREEN,texto_pregunta,AMARILLO,x_preguntas,y_preguntas,width_preguntas,height_preguntas)
        rectangulo_terminar = crear_cuadro_con_texto(SCREEN,texto_terminar,AMARILLO,500,550,180,100)

        #cambios
        pregunta_en_lista = render_texto(lista_preguntas[dic_mutable["contador"]],ROJO,myfont)
        crear_cuadro_con_texto(SCREEN,pregunta_en_lista,AZUL,450,50,100,30)

        dato_a = render_texto(lista_dato_a[dic_mutable["contador"]],ROJO,myfont)
        rectangulo_a = crear_cuadro_con_texto(SCREEN,dato_a,AZUL,x_cuadro_res,y_cuadro_res,width_res,height_res)

        dato_b = render_texto(lista_dato_b[dic_mutable["contador"]],ROJO,myfont)
        rectangulo_b = crear_cuadro_con_texto(SCREEN,dato_b,AZUL,x_cuadro_res+250,y_cuadro_res,width_res,height_res)

        dato_c = render_texto(lista_dato_c[dic_mutable["contador"]],ROJO,myfont)
        rectangulo_c = crear_cuadro_con_texto(SCREEN,dato_c,AZUL,x_cuadro_res+510,y_cuadro_res,width_res,height_res)

        tema_pregunta = render_texto(lista_tema[dic_mutable["contador"]],ROJO,myfont)
        rectangulo_tema_pregunta = crear_cuadro_con_texto(SCREEN,tema_pregunta,AZUL,100,580,100,30)

        #Score
        score_render = render_texto(score,GRIS_OSCURO,myfontGrande)
        crear_cuadro_con_texto(SCREEN,score_render,GRIS,840,500,50,30)

        int_score_render = myfontGrande.render(str(dic_mutable["score"]),True,GRIS_OSCURO)
        crear_cuadro_con_texto(SCREEN,int_score_render,AZUL,920,500,50,30)

        #Tiempo
        tiempo_render = myfont.render(str(segundos),True,ROJO)
        crear_cuadro_con_texto(SCREEN,tiempo_render,AZUL,720,0,50,30)


    elif dic_mutable["estado_juego"] == 0:
        texto = render_texto(dic_mutable["ingreso"],ROJO,myfont)
        crear_cuadro_con_texto(SCREEN,texto,AMARILLO,300,240-80,200,80)

    elif dic_mutable["estado_juego"] == 2:
        texto = render_texto("VOLVER",ROJO,myfont)
        rectangulo_volver =crear_cuadro_con_texto(SCREEN,texto,AMARILLO,600,550,180,100)

        lista_puntajes_nombres = crear_tabla_de_puntuacion(dic_mutable,crear_lista_con_puntajes(dic_mutable,lista_datos_personaje),"puntajes")
        
        lista_nueva =crear_lista_con_strings(lista_puntajes_nombres)

        crear_cuadros_de_texto_para_tabla(SCREEN,AZUL,200,100,50,100,lista_nueva)
    pygame.display.update()

pygame.quit()
