import pygame
import sys
import random
import time
from logos import *

pygame.init()

TAMAÑO_PANTALLA = (1200, 700)
pantalla = pygame.display.set_mode(TAMAÑO_PANTALLA)
pygame.display.set_caption("Logoman")

BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
GRIS = (128, 136, 142)

fondo = pygame.image.load("fondoymusica\descarga.gif").convert()
fondo = pygame.transform.scale(fondo, TAMAÑO_PANTALLA)

fondo_explicacion = pygame.image.load("fondoymusica\images (3).jpg")
fondo_explicacion = pygame.transform.scale(fondo_explicacion, TAMAÑO_PANTALLA)

icono = pygame.image.load("logos_correctos/icono_izquierda.png")
pygame.display.set_icon(icono)

logo = pygame.image.load("logos_correctos/logo.png")
logo = pygame.transform.scale(logo, (320, 170))

audio_perder = pygame.mixer.music.load("fondoymusica\Y2meta.app - Ponele voluntad (128 kbps).mp3")
audio_perder = pygame.mixer.music.set_volume(0.1)


fuente = pygame.font.Font(None, 36)

pygame.mixer.music.load("fondoymusica/Y2meta.app - Martin Garrix - Animals (Official Lyrics Video) (128 kbps).mp3")
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1)

vidas = 5
monedas = 0
rounds = 0
tiempos_respuestas = []
comodines = {"Next": 1, "Half": 1, "Reload": 1}
ya_usados = []
promedio_tiempo = 0
record_monedas = 0

# Variables para el control de volumen
volumen_encendido = True
icono_volumen_on = pygame.image.load("fondoymusica/volumenon.png")
icono_volumen_on = pygame.transform.scale(icono_volumen_on, (50, 50))
icono_volumen_off = pygame.image.load("fondoymusica/volumenoff.png")
icono_volumen_off = pygame.transform.scale(icono_volumen_off, (50,50))
icono_volumen_actual = icono_volumen_on

def mostrar_mensaje(texto, posicion):
    texto_superficie = fuente.render(texto, True, NEGRO)
    pantalla.blit(texto_superficie, posicion)

def mostrar_mensaje_volumen(texto, posicion):
    texto_superficie = fuente.render(texto, True, NEGRO)
    pantalla.blit(texto_superficie, posicion)

def seleccionar_logo_y_opciones(ya_usados):
    disponibles = [logo for logo in logos_correctos if logo["nombre"] not in ya_usados]
    if not disponibles:
        return None, None
    logo_correcto = random.choice(disponibles)
    opciones = random.sample(logo_correcto["incorrectas"], 3)
    opciones.append(logo_correcto["imagen"])
    random.shuffle(opciones)
    ya_usados.append(logo_correcto["nombre"])
    diccionario_seleccionar_logo_y_opciones = [logo_correcto, opciones]
    return diccionario_seleccionar_logo_y_opciones

def mostrar_vidas(vidas):
    for i in range(vidas):
        pygame.draw.circle(pantalla, ROJO, (30 + i * 30, 30), 10)

def usar_half(opciones, logo_correcto):
    incorrectas = [op for op in opciones if op != logo_correcto["imagen"]]
    opciones_mostradas = [logo_correcto["imagen"], random.choice(incorrectas)]
    random.shuffle(opciones_mostradas)
    return opciones_mostradas
    
def determinar_nivel(record_monedas):
    if record_monedas >= 0 and record_monedas <= 50:
        apodo = "Novato"
    elif record_monedas > 50 and record_monedas <= 100:
        apodo ="Crack"
    elif record_monedas > 100 and record_monedas <= 150:
        apodo ="Experto"
    elif record_monedas > 150 and record_monedas <= 200:
        apodo ="Maestro"
    elif record_monedas > 200 and record_monedas <= 250:
        apodo ="Genio"
    elif record_monedas > 250 and record_monedas <= 299:
        apodo ="LA MAQUINA"
    elif record_monedas == 300:
        apodo = "DIOS"
    return apodo


def pantalla_inicial():
    pantalla.blit(fondo, (0, 0))

    pantalla.blit(logo, (470, 10))

    boton_jugar = pygame.Rect(500, 120, 250, 50)
    boton_promedio = pygame.Rect(500, 220, 250, 50)
    boton_coins = pygame.Rect(500, 320, 250, 50)
    boton_record = pygame.Rect(500, 420, 250, 50)
    boton_volumen = pygame.Rect(30, 50, 200, 60)
    boton_nivel = pygame.Rect(500, 520, 250, 50)
    boton_salir = pygame.Rect(500,620,250,50)

    pygame.draw.rect(pantalla, ROJO, boton_jugar, border_radius=10)
    pygame.draw.rect(pantalla, ROJO, boton_promedio, border_radius=10)
    pygame.draw.rect(pantalla, ROJO, boton_coins, border_radius=10)
    pygame.draw.rect(pantalla, ROJO, boton_record, border_radius=10)
    pygame.draw.rect(pantalla, BLANCO, boton_volumen, border_radius=10)
    pygame.draw.rect(pantalla, ROJO, boton_nivel, border_radius=10)
    pygame.draw.rect(pantalla,ROJO, boton_salir, border_radius=10)

    mostrar_mensaje("Jugar", (590, 135))
    mostrar_mensaje("Promedio de tiempo", (510, 230))
    mostrar_mensaje("Coins", (590, 330))
    mostrar_mensaje("Record de monedas", (510, 430))
    mostrar_mensaje("Nivel alcanzado", (540, 530))
    mostrar_mensaje("Salir", (590, 630))

    pantalla.blit(icono_volumen_actual, (150, 50))

    texto_volumen = "Music on" if volumen_encendido else "Music off"
    mostrar_mensaje_volumen(texto_volumen, (30, 70))

    diccionario = [boton_jugar, boton_promedio, boton_coins, boton_record, boton_volumen, boton_nivel, boton_salir]

    pygame.display.update()
    return diccionario

def cambiar_volumen():
    global volumen_encendido, icono_volumen_actual
    volumen_encendido = not volumen_encendido
    if volumen_encendido:
        pygame.mixer.music.set_volume(0.1)
        icono_volumen_actual = icono_volumen_on
    else:
        pygame.mixer.music.set_volume(0.0)
        icono_volumen_actual = icono_volumen_off

def mostrar_respuesta_correcta(logo_correcto):
    pantalla.blit(fondo, (0, 0))
    mostrar_mensaje("La respuesta correcta es:", (420, 100))
    pantalla.blit(logo_correcto["imagen"], (440, 200))
    pygame.display.update()
    time.sleep(2)

def explicacion():
    pantalla.blit(fondo_explicacion, (0, 0))
    texto_explicacion = [
        "EL JUEGO CONSISTE EN LO SIGUIENTE:",
        "En cuanto le des al botón 'Sí'",
        "Se te mostrarán 4 logos y arriba se te preguntará cuál es el correcto.",
        "En caso de acertar, pasarás a la siguiente ronda.",
        "De lo contrario, tendrás que elegir otro hasta acertar.",
        "El juego consiste en 15 rondas.",
        "Tienes 3 comodines:",
        "Half: deja 2 opciones",
        "Next: pasa de pregunta",
        "Reload: cambia la pregunta"
    ]
    y_offset = 100
    for linea in texto_explicacion:
        mostrar_mensaje(linea, (50, y_offset))
        y_offset += 40  # Ajusta la separación entre líneas según sea necesario

    boton_si = pygame.Rect(450, 550, 100, 50)
    boton_no = pygame.Rect(650, 550, 100, 50)
    pygame.draw.rect(pantalla, ROJO, boton_si, border_radius=10)
    pygame.draw.rect(pantalla, ROJO, boton_no, border_radius=10)
    mostrar_mensaje("Sí", (490, 565))
    mostrar_mensaje("No", (690, 565))
    pygame.display.update()

    esperando = True
    while esperando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if boton_si.collidepoint(evento.pos):
                    esperando = False
                    return True
                elif boton_no.collidepoint(evento.pos):
                    esperando = False
                    return False

    pantalla.fill(NEGRO)
    pygame.display.update()

def jugar():
    vidas = 5
    monedas = 0
    rounds = 0
    tiempos_respuestas = []
    comodines = {"Next": 1, "Half": 1, "Reload": 1}
    ya_usados = []

    ejecutando = True
    tiempo_inicio_partida = time.time()

    while ejecutando and rounds < 15:
        logo_correcto, opciones = seleccionar_logo_y_opciones(ya_usados)
        if logo_correcto is None:
            break
        nombre_empresa = logo_correcto["nombre"]
        tiempo_inicio_ronda = time.time()
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
                    if any(boton.collidepoint(x, y) and opciones_mostradas[i] == logo_correcto["imagen"] for i, boton in enumerate(botones_opciones)):
                        monedas += 20
                        siguiente_ronda = True
                    elif any(boton.collidepoint(x, y) for boton in botones_opciones):
                        monedas -= 10
                        vidas -= 1
                        siguiente_ronda = True
                    elif boton_next.collidepoint(x, y) and comodines["Next"] > 0:
                        comodines["Next"] -= 1
                        monedas += 20
                        mostrar_respuesta_correcta(logo_correcto)
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
            if tiempo_transcurrido_ronda > 30:
                vidas -= 1
                siguiente_ronda = True

            if vidas <= 0:
                siguiente_ronda = True

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

            boton_half = pygame.Rect(300, 550, 150, 50)
            boton_next = pygame.Rect(500, 550, 150, 50)
            boton_reload = pygame.Rect(700, 550, 150, 50)
            boton_temporizador = pygame.Rect(1000, 20, 180, 50)

            pygame.draw.rect(pantalla, ROJO, boton_next, border_radius=10)
            pygame.draw.rect(pantalla, ROJO, boton_half, border_radius=10)
            pygame.draw.rect(pantalla, ROJO, boton_reload, border_radius=10)
            pygame.draw.rect(pantalla, ROJO, boton_temporizador, border_radius=10)

            mostrar_mensaje("Next", (550, 565))
            mostrar_mensaje("Half", (350, 565))
            mostrar_mensaje("Reload", (730, 565))

            tiempo_restante = max(0, 30 - int(tiempo_transcurrido_ronda))
            mostrar_mensaje(f"Tiempo: {tiempo_restante} s", (1010, 35))

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

    pantalla.blit(fondo, (0, 0))
    mostrar_mensaje("Juego terminado", (300, 250))
    mostrar_mensaje(f"Promedio de tiempo de respuesta: {promedio_tiempo:.2f} segundos", (200, 300))
    mostrar_mensaje(f"Total de monedas obtenidas: {monedas}", (200, 350))
    pygame.display.update()
    time.sleep(5)


def mostrar_promedio():
    pantalla.blit(fondo, (0, 0))
    mostrar_mensaje(f"Promedio de tiempo de respuesta: {promedio_tiempo:.2f} segundos", (400, 300))
    pygame.display.update()
    time.sleep(3)

def mostrar_coins():
    pantalla.blit(fondo, (0, 0))
    mostrar_mensaje(f"Total de monedas obtenidas: {monedas}", (400, 300))
    pygame.display.update()
    time.sleep(3)

def mostrar_nivel():
    pantalla.blit(fondo, (0, 0))
    mostrar_mensaje_volumen(f"Nivel ACTUAL: {determinar_nivel(record_monedas)}", (400, 300))
    pygame.display.update()
    time.sleep(3)


def mostrar_record():
    pantalla.blit(fondo, (0, 0))
    mostrar_mensaje(f"Record de monedas: {record_monedas}", (400, 300))
    pygame.display.update()
    time.sleep(3)
ejecutando = True
while ejecutando:
    boton_jugar, boton_promedio, boton_coins, boton_record, boton_volumen, boton_nivel, boton_salir = pantalla_inicial()
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            x, y = evento.pos
            if boton_jugar.collidepoint(x, y):
                if explicacion():
                    jugar()
            elif boton_promedio.collidepoint(x, y):
                mostrar_promedio()
            elif boton_coins.collidepoint(x, y):
                mostrar_coins()
            elif boton_record.collidepoint(x, y):
                mostrar_record()
            elif boton_volumen.collidepoint(x, y):
                cambiar_volumen()
            elif boton_nivel.collidepoint(x,y):
                mostrar_nivel()
            elif boton_salir.collidepoint(x,y):
                ejecutando = False
pygame.quit()
sys.exit()
