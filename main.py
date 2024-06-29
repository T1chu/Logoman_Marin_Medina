
import sys
import random
import pygame
from logoman import *

def main():
    ejecutando = True
    boton_jugar, boton_promedio, boton_coins = pantalla_inicial()

    while ejecutando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                ejecutando = False
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                x, y = evento.pos
                if boton_jugar.collidepoint(x, y):
                    jugar()
                    boton_jugar, boton_promedio, boton_coins = pantalla_inicial()
                elif boton_promedio.collidepoint(x, y):
                    pantalla.blit(fondo, (0, 0))  # Dibujar fondo de pantalla
                    mostrar_mensaje(f"Promedio de tiempo de respuesta: {promedio_tiempo:.2f} segundos", (200, 300))
                    pygame.display.flip()
                    time.sleep(5)
                    pantalla_inicial()
                elif boton_coins.collidepoint(x, y):
                    pantalla.blit(fondo, (0, 0))  # Dibujar fondo de pantalla
                    mostrar_mensaje(f"Total de monedas obtenidas: {monedas}", (200, 350))
                    pygame.display.flip()
                    time.sleep(5)
                    pantalla_inicial()

    pygame.quit()
    sys.exit()

main()