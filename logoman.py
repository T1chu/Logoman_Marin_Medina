import pygame
import sys
import random
import time
from logos import *

pygame.init()

TAMAÑO_PANTALLA = (1200, 700)
pantalla = pygame.display.set_mode(TAMAÑO_PANTALLA)
pygame.display.set_caption("Logoman")

# Definir colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
GRIS = (128, 136, 142)

# Cargar imagen de fondo
fondo = pygame.image.load("fondoymusica/paisaje-nevado-en-el-bosque-arte-digital_3840x2160_xtrafondos.com.jpg").convert()
fondo = pygame.transform.scale(fondo, TAMAÑO_PANTALLA)

# Cargar sonido de fondo
pygame.mixer.music.load("fondoymusica/Y2meta.app - Martin Garrix - Animals (Official Lyrics Video) (128 kbps).mp3")
pygame.mixer.music.set_volume(0.1)  # Volumen inicial
pygame.mixer.music.play(-1)  # Reproducir en bucle

# Cargar icono del juego
icono = pygame.image.load("logos_correctos/icono_izquierda.png")
pygame.display.set_icon(icono)

# Fuente para el texto
fuente = pygame.font.Font(None, 36)

# Variables del juego
vidas = 5
monedas = 0
rounds = 0
tiempos_respuestas = []
comodines = {"Next": 1, "Half": 1, "Reload": 1}
ya_usados = []  # Lista para llevar el seguimiento de los logos
promedio_tiempo = 0
record_monedas = 0  # Variable para almacenar el record de monedas

# Variables para el control de volumen
volumen_encendido = True
icono_volumen_on = pygame.image.load("fondoymusica/volumenon.png")
icono_volumen_on = pygame.transform.scale(icono_volumen_on, (50,50))
icono_volumen_off = pygame.image.load("fondoymusica/images.png")
icono_volumen_off = pygame.transform.scale(icono_volumen_off, (50,50))
icono_volumen_actual = icono_volumen_on  # Inicialmente encendido

def mostrar_mensaje(texto, posicion):
    texto_superficie = fuente.render(texto, True, NEGRO)
    pantalla.blit(texto_superficie, posicion)

def seleccionar_logo_y_opciones(ya_usados):
    disponibles = [logo for logo in logos_correctos if logo["nombre"] not in ya_usados]
    if not disponibles:
        return None, None  # No hay más logos
    logo_correcto = random.choice(disponibles)
    opciones = random.sample(logo_correcto["incorrectas"], 3)
    opciones.append(logo_correcto["imagen"])
    random.shuffle(opciones)
    ya_usados.append(logo_correcto["nombre"])
    return logo_correcto, opciones

def mostrar_vidas(vidas):
    for i in range(vidas):
        pygame.draw.circle(pantalla, ROJO, (30 + i * 30, 30), 10)

def usar_half(opciones, logo_correcto):
    incorrectas = [op for op in opciones if op != logo_correcto["imagen"]]
    opciones_mostradas = [logo_correcto["imagen"], random.choice(incorrectas)]
    random.shuffle(opciones_mostradas)
    return opciones_mostradas

def pantalla_inicial():
    pantalla.blit(fondo, (0, 0))  # Dibujar fondo de pantalla

    mostrar_mensaje("Bienvenido a Logoman", (450, 90))

    boton_jugar = pygame.Rect(500, 200, 180, 50)
    boton_promedio = pygame.Rect(500, 300, 250, 50)
    boton_coins = pygame.Rect(500, 400, 200, 50)
    boton_record = pygame.Rect(500, 500, 250, 50)
    boton_volumen = pygame.Rect(30, 50, 200, 60)  
    
    pygame.draw.rect(pantalla, GRIS, boton_jugar)
    pygame.draw.rect(pantalla, GRIS, boton_promedio)
    pygame.draw.rect(pantalla, GRIS, boton_coins)
    pygame.draw.rect(pantalla, GRIS, boton_record)
    pygame.draw.rect(pantalla, BLANCO, boton_volumen)  # Dibujar botón de volumen

    mostrar_mensaje("Jugar", (550, 215))
    mostrar_mensaje("Promedio de tiempo", (510, 315))
    mostrar_mensaje("Coins", (570, 415))
    mostrar_mensaje("Record de monedas", (510, 515))

    # Dibujar ícono de volumen actual
    pantalla.blit(icono_volumen_actual, (150, 50))
    
    # Mostrar estado del volumen
    texto_volumen = "Music on" if volumen_encendido else "Music off"
    if texto_volumen == "Music on":
        mostrar_mensaje(texto_volumen, (30, 70))
    else:
        mostrar_mensaje(texto_volumen, (30, 70))

    pygame.display.flip()
    return boton_jugar, boton_promedio, boton_coins, boton_record, boton_volumen

def cambiar_volumen():
    global volumen_encendido, icono_volumen_actual
    volumen_encendido = not volumen_encendido
    if volumen_encendido:
        pygame.mixer.music.set_volume(0.1)  # Volver a encender el volumen
        icono_volumen_actual = icono_volumen_on
    else:
        pygame.mixer.music.set_volume(0.0)  # Apagar el volumen
        icono_volumen_actual = icono_volumen_off

def jugar():
    global vidas, monedas, rounds, tiempos_respuestas, comodines, ya_usados, promedio_tiempo, record_monedas

    vidas = 5
    monedas = 0
    rounds = 0
    tiempos_respuestas = []
    comodines = {"Next": 1, "Half": 1, "Reload": 1}
    ya_usados = []

    ejecutando = True
    tiempo_inicio_partida = time.time()  # Iniciar tiempo de la partida

    while ejecutando and rounds < 15:
        logo_correcto, opciones = seleccionar_logo_y_opciones(ya_usados)
        if logo_correcto is None:  # No hay más logos
            break
        nombre_empresa = logo_correcto["nombre"]
        tiempo_inicio_ronda = time.time()  # Iniciar tiempo de la ronda
        opciones_mostradas = opciones 
        siguiente_ronda = False
        
        while not siguiente_ronda and ejecutando:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    ejecutando = False
                    pygame.quit()
                    sys.exit()
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    x, y = evento.pos
                    if botones_opciones[0].collidepoint(x, y) and opciones_mostradas[0] == logo_correcto["imagen"]:
                        monedas += 20
                        siguiente_ronda = True
                    elif botones_opciones[1].collidepoint(x, y) and opciones_mostradas[1] == logo_correcto["imagen"]:
                        monedas += 20
                        siguiente_ronda = True
                    elif botones_opciones[2].collidepoint(x, y) and opciones_mostradas[2] == logo_correcto["imagen"]:
                        monedas += 20
                        siguiente_ronda = True
                    elif botones_opciones[3].collidepoint(x, y) and opciones_mostradas[3] == logo_correcto["imagen"]:
                        monedas += 20
                        siguiente_ronda = True
                    elif botones_opciones[0].collidepoint(x, y) or botones_opciones[1].collidepoint(x, y) or botones_opciones[2].collidepoint(x, y) or botones_opciones[3].collidepoint(x, y):
                        monedas -= 10
                        vidas -= 1
                        # No cambiar de ronda ni actualizar opciones, solo continuar en la misma
                    elif boton_next.collidepoint(x, y) and comodines["Next"] > 0:
                        comodines["Next"] -= 1
                        monedas += 20
                        siguiente_ronda = True
                    elif boton_half.collidepoint(x, y) and comodines["Half"] > 0:
                        comodines["Half"] -= 1
                        opciones_mostradas = usar_half(opciones, logo_correcto)
                    elif boton_reload.collidepoint(x, y) and comodines["Reload"] > 0:
                        comodines["Reload"] -= 1
                        logo_correcto, opciones = seleccionar_logo_y_opciones(ya_usados)
                        if logo_correcto is None:  
                            break
                        nombre_empresa = logo_correcto["nombre"]
                        opciones_mostradas = opciones
                        tiempo_inicio_ronda = time.time() 

            tiempo_transcurrido_ronda = time.time() - tiempo_inicio_ronda
            if tiempo_transcurrido_ronda > 15:  
                vidas -= 1
                # No cambiar de ronda ni actualizar opciones, solo continuar en la misma

            if vidas <= 0:
                siguiente_ronda = True  # Forzar salida de la ronda si se quedan sin vidas

            if not ejecutando or rounds >= 15 or vidas <= 0:
                break

            pantalla.blit(fondo, (0, 0))  
            mostrar_mensaje(f"¿Cuál es el logo de {nombre_empresa}?", (400, 100))
            
            botones_opciones = []
            for i, opcion in enumerate(opciones_mostradas):
                separacion = 250
                boton_opcion = pygame.Rect(i * separacion + 100, 200, 150, 150)
                botones_opciones.append(boton_opcion)
                pantalla.blit(opcion, boton_opcion)

            mostrar_vidas(vidas)

            boton_half = pygame.Rect(200, 550, 150, 50)
            boton_next = pygame.Rect(400, 550, 150, 50)
            boton_reload = pygame.Rect(600, 550, 150, 50)

            pygame.draw.rect(pantalla, ROJO, boton_next)
            pygame.draw.rect(pantalla, ROJO, boton_half)
            pygame.draw.rect(pantalla, ROJO, boton_reload)

            mostrar_mensaje("Next", (440, 565))
            mostrar_mensaje("Half", (230, 565))
            mostrar_mensaje("Reload", (630, 565))

            pygame.display.update()

        if siguiente_ronda:
            rounds += 1
            tiempo_respuesta = time.time() - tiempo_inicio_ronda
            tiempos_respuestas.append(tiempo_respuesta)

    if tiempos_respuestas:
        promedio_tiempo = sum(tiempos_respuestas) / len(tiempos_respuestas)
    else:
        promedio_tiempo = 0

    global record_monedas
    if monedas > record_monedas:
        record_monedas = monedas

    pantalla.blit(fondo, (0, 0))  # Dibujar fondo de pantalla
    mostrar_mensaje("Juego terminado", (300, 250))
    mostrar_mensaje(f"Promedio de tiempo de respuesta: {promedio_tiempo:.2f} segundos", (200, 300))
    mostrar_mensaje(f"Total de monedas obtenidas: {monedas}", (200, 350))
    pygame.display.update()
    time.sleep(5)


def mostrar_promedio():
    pantalla.blit(fondo, (0, 0))  # Dibujar fondo de pantalla
    mostrar_mensaje(f"Promedio de tiempo de respuesta: {promedio_tiempo:.2f} segundos", (400, 300))
    pygame.display.update()
    time.sleep(3)

def mostrar_coins():
    pantalla.blit(fondo, (0, 0))  # Dibujar fondo de pantalla
    mostrar_mensaje(f"Total de monedas obtenidas: {monedas}", (400, 300))
    pygame.display.update()
    time.sleep(3)

def mostrar_record():
    pantalla.blit(fondo, (0, 0))  # Dibujar fondo de pantalla
    mostrar_mensaje(f"Record de monedas: {record_monedas}", (400, 300))
    pygame.display.update()
    time.sleep(3)

ejecutando = True
boton_jugar, boton_promedio, boton_coins, boton_record, boton_volumen = pantalla_inicial()

while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            x, y = evento.pos
            if boton_jugar.collidepoint(x, y):
                jugar()
                boton_jugar, boton_promedio, boton_coins, boton_record, boton_volumen = pantalla_inicial()
            elif boton_promedio.collidepoint(x, y):
                mostrar_promedio()
                boton_jugar, boton_promedio, boton_coins, boton_record, boton_volumen = pantalla_inicial()
            elif boton_coins.collidepoint(x, y):
                mostrar_coins()
                boton_jugar, boton_promedio, boton_coins, boton_record, boton_volumen = pantalla_inicial()
            elif boton_record.collidepoint(x, y):
                mostrar_record()
                boton_jugar, boton_promedio, boton_coins, boton_record, boton_volumen = pantalla_inicial()
            elif boton_volumen.collidepoint(x, y):
                cambiar_volumen()
                pantalla_inicial()

pygame.quit()
sys.exit()

