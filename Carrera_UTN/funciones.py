import json
import pygame
import os
from colores import *
from rectangulos import *



def funcion_leer_json_array(ubicacion_archivo:str) -> list:
    """_summary_

    Args:
        ubicacion_archivo (str): _description_

    Returns:
        (list):  lista del archivo json
    """
    retorno = False
    try:
        with open(ubicacion_archivo, 'r',encoding='utf-8') as archivo:
            datos = json.load(archivo)
            retorno = datos
    except Exception as ex:
        print(ex)
    return retorno
    


lista_data = funcion_leer_json_array("Carrera_UTN\data_preguntas.json")


def crear_json(nombre_archivo:str,data:list):
    """creo un archivo json 

    Args:
        nombre_archivo (str): el nombre que quiero que tenga el archivo
        data (list): lo que quiero que tenga
    """
    with open(nombre_archivo,"w") as file:
        json.dump(data,file,indent=4)

def si_(lista):
    if type(lista) == list:
        return True
    else:
        return False

def ordenamiento_ascendente_descendente(lista:list, clave:str,ordenamiento:bool):
    """recorre la lista y oredena segun parametro ingesado,
    puede ser de forma ascendente o descendente 

    Args:
        lista (list): lista de los personajes
        clave (str): puede ser cualquier key de los diccionarios    
        ordenamiento (bool): se ingresa FALSE si es ascendete y TRUE si es descendente

    Returns:
        _type_: una nueva lista con las condiciones
    """
    if si_(lista) == True:
        return sorted(lista, key = lambda x: x[clave],reverse= ordenamiento) 
    else:
        return False

def crear_lista_con_puntajes(dicccionario:dict,list_con_datos:list):
    dict_con_datos = {}

    nombre = dicccionario["ingreso"]
    puntaje = dicccionario["score"]

    dict_con_datos["nombre"] = nombre
    dict_con_datos["score"] = puntaje

    list_con_datos.append(dict_con_datos)
    return list_con_datos

def crear_lista_con_strings(lista:list):
    nueva_lista = []
    for diccionarios in lista:
        cadena = f"Nombre:  {diccionarios["nombre"]} Puntos: {diccionarios["score"]}"
        nueva_lista.append(cadena)
    return nueva_lista

def crear_cuadro_con_texto(ventana:pygame.Surface,texto:str,color,x:int,y:int,width:int,height:int):
    pygame.draw.rect(ventana,color,(x,y,width,height))
    rectangulo = crear_rectangulo(x, y, width, height)
    ventana.blit(texto,(x+(rectangulo.width-texto.get_width())/2, y+(rectangulo.height-texto.get_height())/2))
    return rectangulo



def render_texto(texto,color,fuente):
    texto_renderizado = fuente.render(str(texto),True,color)
    return texto_renderizado


def lectura_posicion(pos_click:list,rect:pygame.Rect):
    lectura_boton = False
    try:
        if ((pos_click[0] > (rect.x) and pos_click[0] < (rect.x+rect.width)) and
            (pos_click[1] > rect.y and pos_click[1] < (rect.y+rect.height))):
            lectura_boton = True
    except Exception as ex:
        print(ex)
    return lectura_boton

def update(pos_click:list,rect_terminar:pygame.Rect,
    rect_a:pygame.Rect,rect_b:pygame.Rect,rect_c:pygame.Rect,lista_largo:list,dic:dict):
    boton_terminar = lectura_posicion(pos_click,rect_terminar)
    boton_a = lectura_posicion(pos_click,rect_a)
    boton_b = lectura_posicion(pos_click,rect_b)
    boton_c =  lectura_posicion(pos_click,rect_c)

    mover_personaje_con_validacion(dic,boton_a,boton_b,boton_c)
    movimineto_de_lista(boton_a,boton_b,boton_c,boton_terminar,lista_largo,dic)

def update_2(pos_click:list,rect_volver:pygame.Rect,diccionario:dict):
    boton_volver = lectura_posicion(pos_click,rect_volver)

    cambio_escenario(boton_volver,diccionario)

def mover_personaje_con_validacion(dic,boton_a,boton_b,boton_c):
    validacion_respuesta(dic,lista_dato_a,lista_respuesta,boton_a)
    validacion_respuesta(dic,lista_dato_b,lista_respuesta,boton_b)
    validacion_respuesta(dic,lista_dato_c,lista_respuesta,boton_c)

    mover_personaje(rec_personaje,dic)



def movimineto_de_lista(boton_a,boton_b, boton_c,
    boton_terminar,lista_largo,diccionario:dict):
    if boton_terminar:
        diccionario["estado_juego"] = 2
        
    elif (boton_a or boton_b or boton_c):
        diccionario["contador"] += 1

    if (diccionario["contador"] > (len(lista_largo)-1)):
        diccionario["contador"] = 0
        diccionario["estado_juego"] = 2

def cambio_escenario(boton_volver,diccionario:dict): #escenario 2
    if boton_volver:
        estado_juego(diccionario)


#rev
def crear_tabla_de_puntuacion(diccionario_juego,lista,nombre_archivo):
    if diccionario_juego["estado_juego"] == 2:
        lista_con_datos = (crear_lista_con_puntajes(diccionario_juego,lista))
        if os.path.exists(nombre_archivo):
            lista = funcion_leer_json_array(nombre_archivo)
            #algo mas
        else:
            crear_json(nombre_archivo,lista_con_datos)
    return lista_con_datos

def crear_cuadros_de_texto_para_tabla(ventana:pygame.Surface,
    color,x:int,y:int,width:int,height:int,lista_de_tabla:list):
    for string in lista_de_tabla:
        y += 100
        texto = render_texto(string,ROJO,myfont)
        crear_cuadro_con_texto(ventana,texto,color,x,y,width,height)

def estado_juego(diccionario:dict): #reinicio
    if diccionario["estado_juego"] == 1 or diccionario["estado_juego"] == 2: #si pierde vuelve a 0
        diccionario["score"] = "000"
        diccionario["contador"] = 0
        diccionario["ingreso"] = ""
        diccionario["estado_juego"] = 0
        diccionario["bandera_nivel_personaje"] = True
        rec_personaje.x = x_rec_personaje_inicio
        rec_personaje.y = y_rec_personaje_inicio


def validacion_respuesta(diccionario,lista_opcion,lista_respuesta,lectura_boton:bool)-> int:
    if lectura_boton:
        if lista_opcion[diccionario["contador"]] == lista_respuesta[diccionario["contador"]]:
            diccionario["score"] = int(diccionario["score"]) + 10
            diccionario["respuesta_movimiento_correcta"] = True
        else:
            diccionario["respuesta_movimiento_incorrecta"] = True



def buscar_claves(lista:list,clave:str):
    lista_titulos = []
    for e_lista in lista:
        lista_titulos.append(e_lista[clave])
    return lista_titulos



#rev
def animar_moviento(pantalla,lista_animaciones,rectangulo_principal):
    contador_ani = 0
    largo = len(lista_animaciones)
    if contador_ani >= largo:
        contador_ani = 0
    pantalla.blit(lista_animaciones[contador_ani], rectangulo_principal)
    contador_ani += 1


def mover_personaje(personaje:pygame.Rect,dic):
    if dic["bandera_nivel_personaje"]:
        if dic["respuesta_movimiento_correcta"]:
            personaje.x += 200
        elif dic["respuesta_movimiento_incorrecta"]:
            personaje.x -= 100
    else:
        if dic["respuesta_movimiento_correcta"]:
            personaje.x -= 200 
        elif dic["respuesta_movimiento_incorrecta"]:
            personaje.x += 100

    if personaje.colliderect(rec_6):
        personaje.x += 100
    if personaje.colliderect(rec_12):
        personaje.x += 100
    if personaje.x > pared_derecha.x and dic["bandera_nivel_personaje"] == True:
        dic["bandera_nivel_personaje"] = False
        personaje.y = 300
        personaje.x = 900
    
    if personaje.x > pared_derecha.x and dic["bandera_nivel_personaje"] == False:
        dic["bandera_nivel_personaje"] = True
        personaje.y = 200
        personaje.x = 900

    if personaje.x < pared_izquierda.x and dic["bandera_nivel_personaje"] == False:
        dic["estado_juego"] = 2

    dic["respuesta_movimiento_correcta"] = False
    dic["respuesta_movimiento_incorrecta"] = False

#rev
def tiempo(event,timer_segundos,dic,segundos,fin_tiempo):
    if event.type == timer_segundos:
        if fin_tiempo == False:
            segundos = int(segundos)-1
            if segundos == 0:
                dic["contador"] += 1
                fin_tiempo = True

def crar_rectangulos(SCREEN:pygame.Surface,texto:str,diccionario:dict,myfont):
    if diccionario["estado_juego"] == 1:
        texto_pregunta = render_texto("PREGUNTA",GRIS_OSCURO,myfont)
        texto_reiniciar = render_texto("REINICIAR",GRIS_OSCURO,myfont)

        rectangulo_pregunta = crear_cuadro_con_texto(SCREEN,texto_pregunta,AMARILLO,x_preguntas,y_preguntas,width_preguntas,height_preguntas)
        rectangulo_reiniciar = crear_cuadro_con_texto(SCREEN,texto_reiniciar,AMARILLO,350,350,180,100)

        #cambios
        pregunta_en_lista = render_texto(lista_preguntas[diccionario["contador"]],ROJO,myfont)
        crear_cuadro_con_texto(SCREEN,pregunta_en_lista,AZUL,350,180,100,30)

        dato_a = render_texto(lista_dato_a[diccionario["contador"]],ROJO,myfont)
        rectangulo_a = crear_cuadro_con_texto(SCREEN,dato_a,AZUL,x_cuadro_res,y_cuadro_res,width_res,height_res)

        dato_b = render_texto(lista_dato_b[diccionario["contador"]],ROJO,myfont)
        rectangulo_b = crear_cuadro_con_texto(SCREEN,dato_b,AZUL,x_cuadro_res+250,y_cuadro_res,width_res,height_res)

        dato_c = render_texto(lista_dato_c[diccionario["contador"]],ROJO,myfont)
        rectangulo_c = crear_cuadro_con_texto(SCREEN,dato_c,AZUL,x_cuadro_res+510,y_cuadro_res,width_res,height_res)

        tema_pregunta = render_texto(lista_tema[diccionario["contador"]],ROJO,myfont)
        rectangulo_tema_pregunta = crear_cuadro_con_texto(SCREEN,tema_pregunta,AZUL,100,380,100,30)

        #Score
        score_render = render_texto(score,GRIS_OSCURO,myfont)
        crear_cuadro_con_texto(SCREEN,score_render,AZUL,620,90,100,30)

        int_score_render = myfont.render(str(diccionario["score"]),True,GRIS_OSCURO)
        crear_cuadro_con_texto(SCREEN,int_score_render,AZUL,620,120,100,30)

        #Tiempo


    elif diccionario["estado_juego"] == 0:
        texto = render_texto(diccionario["ingreso"],ROJO,myfont)
        crear_cuadro_con_texto(SCREEN,texto,AMARILLO,300,240-80,200,80)


lista_preguntas = buscar_claves(lista_data,"pregunta")
lista_dato_a = buscar_claves(lista_data,"a")
lista_dato_b = buscar_claves(lista_data,"b")
lista_dato_c = buscar_claves(lista_data,"c")
lista_tema = buscar_claves(lista_data,"tema")
lista_respuesta = buscar_claves(lista_data,"correcta")
