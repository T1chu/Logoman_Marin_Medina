import pygame
import sys
import random
import time
from logos import *
import json
from funciones import *

pygame.init()

# Definir colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
GRIS = (128, 136, 142)


pygame.display.set_caption("Logoman")
TAMAÑO_PANTALLA = (1200, 700)
fondo = pygame.image.load("fondoymusica\descarga.gif").convert()
fondo = pygame.transform.scale(fondo, TAMAÑO_PANTALLA)
pantalla = pygame.display.set_mode(TAMAÑO_PANTALLA)

fondo_explicacion = pygame.image.load("fondoymusica\images (3).jpg")
fondo_explicacion = pygame.transform.scale(fondo_explicacion, TAMAÑO_PANTALLA)

logo = pygame.image.load("logos_correctos/logo.png")
logo = pygame.transform.scale(logo, (320, 170))


pygame.mixer.music.load("fondoymusica\Y2meta.app - Rap de Fernanfloo [Karaoke] (Instrumental) (128 kbps).mp3")
pygame.mixer.music.set_volume(0.1)  # Volumen inicial
pygame.mixer.music.play(-1)  # Reproducir en bucle

icono = pygame.image.load("logos_correctos/icono_izquierda.png")
pygame.display.set_icon(icono)





vidas = 5
monedas = 0
rounds = 0
tiempos_respuestas = []
comodines = {"Next": 1, "Half": 1, "Reload": 1}
ya_usados = []  # Lista para llevar el seguimiento 
promedio_tiempo = 0
record_monedas = 0  






[boton_coins, boton_jugar, boton_nivel, boton_promedio, boton_record, boton_salir, boton_volumen] = pantalla_inicial(pantalla, fondo, logo)
ejecutando = True
while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            x, y = evento.pos
            if boton_jugar.collidepoint(x, y):
                if explicacion(pantalla, fondo_explicacion):
                    jugar(pantalla, fondo)
                pantalla_inicial(pantalla, fondo, logo)
            elif boton_promedio.collidepoint(x, y):
                mostrar_promedio(pantalla,fondo)
                pantalla_inicial(pantalla, logo, fondo)
            elif boton_coins.collidepoint(x, y):
                mostrar_coins(pantalla,fondo)
                pantalla_inicial(pantalla, logo, fondo)
                linea = "" 
                with open("agenda.csv", "w") as archivo: 
                    for i in range(monedas): 
                        linea = f"el record de monedas es: {monedas}\n" 
                        archivo.write(linea) 
            elif boton_record.collidepoint(x, y):
                mostrar_record(pantalla,fondo)
                pantalla_inicial(pantalla, logo, fondo)
                with open("funcion4.json", 'w') as archivo:
                    json.dump(f"El record de monedas obtenido en la partida es: {record_monedas}", archivo)
            elif boton_volumen.collidepoint(x, y):
                cambiar_volumen()
                pantalla_inicial(pantalla, logo, fondo)
            elif boton_nivel.collidepoint(x,y):
                mostrar_nivel(pantalla,fondo)
                pantalla_inicial(pantalla, logo, fondo)
            elif boton_salir.collidepoint(x, y):
                ejecutando = False

pygame.quit()
sys.exit()

