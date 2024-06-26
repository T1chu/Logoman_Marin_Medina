import pygame
import sys
import random
import time

pygame.init()

TAMAÑO_PANTALLA = (800, 600)
pantalla = pygame.display.set_mode(TAMAÑO_PANTALLA)
pygame.display.set_caption("Logoman")

BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)

fuente = pygame.font.SysFont("consolas", 20)

logos_correctos = [
    pygame.image.load("logos_incorrectos\logo_incorrecto_apple_1.png"),
    pygame.image.load("logos_incorrectos\logo_incorrecto_apple_2.png"),
    pygame.image.load("logos_incorrectos\logo_incorrecto_apple_3.png"),
    pygame.image.load("logos_incorrectos\logo_incorrecto_pepsi_1.png"),
    pygame.image.load("logos_incorrectos\logo_incorrecto_pepsi_2.png"),
    pygame.image.load("logos_incorrectos\logo_incorrecto_pepsi_3.png"),
    pygame.image.load("logos_incorrectos\logo_incorrecto_youtube_1.png"),
    pygame.image.load("logos_incorrectos\logo_incorrecto_youtube_2.png"),
    pygame.image.load("logos_incorrectos\logo_incorrecto_youtube_3.png"),
]

logos_incorrectos = [
    pygame.image.load("logos_correctos\logo_correcto_apple.png"),
    pygame.image.load("logos_correctos\logo_correcto_pepsi.png"),
    pygame.image.load("logos_correctos\logo_correcto_youtube.png"),

]