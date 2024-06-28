import pygame
import sys
import random
import time


# Inicialización de Pygame
pygame.init()

# Tamaño de la pantalla
TAMAÑO_PANTALLA = (1200, 700)
pantalla = pygame.display.set_mode(TAMAÑO_PANTALLA)
pygame.display.set_caption("Logoman")

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)

# Fuente
fuente = pygame.font.Font(None, 36)

logos_correctos = [
    {"nombre": "Apple", "imagen": pygame.image.load("logos_correctos\logo_correcto_apple.png"), "incorrectas": [
        pygame.image.load("logos_incorrectos\logo_incorrecto_apple_1.png"),
        pygame.image.load("logos_incorrectos\logo_incorrecto_apple_2.png"),
        pygame.image.load("logos_incorrectos\logo_incorrecto_apple_3.png")
    ]},
    {"nombre": "Pepsi", "imagen": pygame.image.load("logos_correctos\logo_correcto_pepsi.png"), "incorrectas": [
        pygame.image.load("logos_incorrectos\logo_incorrecto_pepsi_1.png"),
        pygame.image.load("logos_incorrectos\logo_incorrecto_pepsi_2.png"),
        pygame.image.load("logos_incorrectos\logo_incorrecto_pepsi_3.png")
    ]},
    {"nombre": "Youtube", "imagen": pygame.image.load("logos_correctos\logo_correcto_youtube.png"), "incorrectas": [
        pygame.image.load("logos_incorrectos\logo_incorrecto_youtube_1.png"),
        pygame.image.load("logos_incorrectos\logo_incorrecto_youtube_2.png"),
        pygame.image.load("logos_incorrectos\logo_incorrecto_youtube_3.png")
    ]},
    {"nombre": "Mercedes", "imagen": pygame.image.load("logos_correctos\logo_correcto_mercedes.png"), "incorrectas": [
        pygame.image.load("logos_incorrectos\logo_incorrecto_mercedes_1.png"),
        pygame.image.load("logos_incorrectos\logo_incorrecto_mercedes_2.png"),
        pygame.image.load("logos_incorrectos\logo_incorrecto_mercedes_3.png")
    ]},
    {"nombre": "Mcdonald", "imagen": pygame.image.load("logos_correctos\logo_correcto_mcdonalds.png"), "incorrectas": [
        pygame.image.load("logos_incorrectos\logo_incorrecto_mcdonalds_1.png"),
        pygame.image.load("logos_incorrectos\logo_incorrecto_mcdonalds_2.png"),
        pygame.image.load("logos_incorrectos\logo_incorrecto_mcdonalds_3.png")
    ]},
    {"nombre": "Nike", "imagen": pygame.image.load("logos_correctos\logo_correcto_nike.png"), "incorrectas": [
        pygame.image.load("logos_incorrectos\logo_incorrrecto_nike_1.png"),
        pygame.image.load("logos_incorrectos\logo_incorrrecto_nike_2.png"),
        pygame.image.load("logos_incorrectos\logo_incorrrecto_nike_3.png")
    ]},
    {"nombre": "Toyota", "imagen": pygame.image.load("logos_correctos\logo_correcto_toyota.png"), "incorrectas": [
        pygame.image.load("logos_incorrectos\logo_incorrecto_toyota_1.png"),
        pygame.image.load("logos_incorrectos\logo_incorrecto_toyota_2.png"),
        pygame.image.load("logos_incorrectos\logo_incorrecto_toyota_3.png")
    ]},
    {"nombre": "LG", "imagen": pygame.image.load("logos_correctos\logo_correcto_lg.png"), "incorrectas": [
        pygame.image.load("logos_incorrectos\logo_incorrecto_lg_1.png"),
        pygame.image.load("logos_incorrectos\logo_incorrecto_lg_2.png"),
        pygame.image.load("logos_incorrectos\logo_incorrecto_lg_3.png")
    ]},
    {"nombre": "Superman", "imagen": pygame.image.load("logos_correctos\logo_correcto_superman.png"), "incorrectas": [
        pygame.image.load("logos_incorrectos\logo_incorrecto_superman_1.png"),
        pygame.image.load("logos_incorrectos\logo_incorrecto_superman_2.png"),
        pygame.image.load("logos_incorrectos\logo_incorrecto_superman_3.png")
    ]},
    {"nombre": "Lego", "imagen": pygame.image.load("logos_correctos\logo_correcto_lego.png"), "incorrectas": [
        pygame.image.load("logos_incorrectos\logo_incorrecto_lego_1.png"),
        pygame.image.load("logos_incorrectos\logo_incorrecto_lego_2.png"),
        pygame.image.load("logos_incorrectos\logo_incorrecto_lego_3.png")
    ]},
    {"nombre": "Snickers", "imagen": pygame.image.load("logos_correctos\logo_correcto_snickers.png"), "incorrectas": [
        pygame.image.load("logos_incorrectos\logo_incorrecto_snickers_1.png"),
        pygame.image.load("logos_incorrectos\logo_incorrecto_snickers_2.png"),
        pygame.image.load("logos_incorrectos\logo_incorrecto_snickers_3.png")
    ]},
    {"nombre": "Adidas", "imagen": pygame.image.load("logos_correctos\logo_correcto_adidas.png"), "incorrectas": [
        pygame.image.load("logos_incorrectos\logo_incorrecto_adidas_1.png"),
        pygame.image.load("logos_incorrectos\logo_incorrecto_adidas_2.png"),
        pygame.image.load("logos_incorrectos\logo_incorrecto_adidas_3.png")
    ]},
    {"nombre": "Microsoft", "imagen": pygame.image.load("logos_correctos\logo_correcto_microsoft.png"), "incorrectas": [
        pygame.image.load("logos_incorrectos\logo_incorrecto_microsoft_1.png"),
        pygame.image.load("logos_incorrectos\logo_incorrecto_microsoft_2.png"),
        pygame.image.load("logos_incorrectos\logo_incorrecto_microsoft_3.png")
    ]},
    {"nombre": "Kinder", "imagen": pygame.image.load("logos_correctos\logo_correcto_kinder.png"), "incorrectas": [
        pygame.image.load("logos_incorrectos\logo_incorrecto_kinder_1.png"),
        pygame.image.load("logos_incorrectos\logo_incorrecto_kinder_2.png"),
        pygame.image.load("logos_incorrectos\logo_incorrecto_kinder_3.png")
    ]},
    {"nombre": "Nokia", "imagen": pygame.image.load("logos_correctos\logo_correcto_nokia.png"), "incorrectas": [
        pygame.image.load("logos_incorrectos\logo_incorrecto_nokia_1.png"),
        pygame.image.load("logos_incorrectos\logo_incorrecto_nokia_2.png"),
        pygame.image.load("logos_incorrectos\logo_incorrecto_nokia_3.png")
    ]}
    # Añade más logos correctos con sus incorrectos según sea necesario
]



# Función para mostrar un mensaje en la pantalla
def mostrar_mensaje(texto, posicion):
    texto_superficie = fuente.render(texto, True, NEGRO)
    pantalla.blit(texto_superficie, posicion)

# Función para seleccionar un logo correcto y opciones incorrectas
def seleccionar_logo_y_opciones(ya_usados):
    disponibles = [logo for logo in logos_correctos if logo["nombre"] not in ya_usados]
    if not disponibles:
        return None, None  # No hay más logos disponibles
    logo_correcto = random.choice(disponibles)
    opciones = random.sample(logo_correcto["incorrectas"], 3)
    opciones.append(logo_correcto["imagen"])
    random.shuffle(opciones)
    ya_usados.append(logo_correcto["nombre"])
    return logo_correcto, opciones

# Variables del juego
vidas = 5
monedas = 0
rounds = 0
tiempos_respuestas = []
comodines = {"Next": 1, "Half": 1, "Reload": 1}
ya_usados = []  # Lista para llevar el seguimiento de los logos ya usados
mostrar_alerta = False
tiempo_alerta = 0

# Función para mostrar las vidas restantes
def mostrar_vidas(vidas):
    for i in range(vidas):
        pygame.draw.circle(pantalla, ROJO, (30 + i * 30, 30), 10)

# Función para usar comodín Half
def usar_half(opciones, logo_correcto):
    incorrectas = [op for op in opciones if op != logo_correcto["imagen"]]
    opciones_mostradas = [logo_correcto["imagen"], random.choice(incorrectas)]
    random.shuffle(opciones_mostradas)
    return opciones_mostradas

# Bucle principal del juego
ejecutando = True
while ejecutando and rounds < 15:
    logo_correcto, opciones = seleccionar_logo_y_opciones(ya_usados)
    if logo_correcto is None:  # No hay más logos disponibles
        break
    nombre_empresa = logo_correcto["nombre"]
    tiempo_inicio = time.time()
    usar_comodin_half = False
    opciones_mostradas = opciones  # Mantener una copia de las opciones originales
    siguiente_ronda = False
    
    while not siguiente_ronda and ejecutando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                ejecutando = False
                break
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_1 and opciones_mostradas[0] == logo_correcto["imagen"]:
                    monedas += 20
                    siguiente_ronda = True
                elif evento.key == pygame.K_2 and opciones_mostradas[1] == logo_correcto["imagen"]:
                    monedas += 20
                    siguiente_ronda = True
                elif evento.key == pygame.K_3 and opciones_mostradas[2] == logo_correcto["imagen"]:
                    monedas += 20
                    siguiente_ronda = True
                elif evento.key == pygame.K_4 and opciones_mostradas[3] == logo_correcto["imagen"]:
                    monedas += 20
                    siguiente_ronda = True
                elif evento.key == pygame.K_1 or evento.key == pygame.K_2 or evento.key == pygame.K_3 or evento.key == pygame.K_4:
                    monedas -= 10
                    vidas -= 1
                    siguiente_ronda = True
                elif evento.key == pygame.K_n and comodines["Next"] > 0:
                    comodines["Next"] -= 1
                    monedas += 20
                    siguiente_ronda = True
                elif evento.key == pygame.K_h and comodines["Half"] > 0:
                    comodines["Half"] -= 1
                    opciones_mostradas = usar_half(opciones, logo_correcto)
                elif evento.key == pygame.K_r and comodines["Reload"] > 0:
                    comodines["Reload"] -= 1
                    logo_correcto, opciones = seleccionar_logo_y_opciones(ya_usados)
                    if logo_correcto is None:  # No hay más logos disponibles
                        break
                    nombre_empresa = logo_correcto["nombre"]
                    opciones_mostradas = opciones
                    tiempo_inicio = time.time()

        if not ejecutando or rounds >= 15 or vidas <= 0:
            break

        # Llenar la pantalla de blanco
        pantalla.fill(BLANCO)

        # Mostrar el nombre de la empresa
        mostrar_mensaje(f"¿Cuál es el logo de {nombre_empresa}?", (400, 100))

        # Mostrar las opciones de logos
        for i, opcion in enumerate(opciones_mostradas):
            separacion = 250
            pantalla.blit(opcion, (i * separacion + 100, 200))

        # Mostrar las opciones numeradas
        mostrar_mensaje("1                                 2                                  3                                   4", (200, 400))

        # Mostrar las vidas restantes
        mostrar_vidas(vidas)

        # Mostrar los comodines restantes
        mostrar_mensaje(f"Next (N para ejecutar): {comodines['Next']}", (50, 550))
        mostrar_mensaje(f"Half (H para ejecutar): {comodines['Half']}", (50, 610))
        mostrar_mensaje(f"Reload (R para ejecutar): {comodines['Reload']}", (50, 660))

        # Mostrar alerta si hay error
        if mostrar_alerta and time.time() - tiempo_alerta < 2:
            mostrar_mensaje("¡Incorrecto!", (350, 50), color=ROJO)
        else:
            mostrar_alerta = False

        # Actualizar la pantalla
        pygame.display.update()

    # Incrementar el número de rondas y registrar el tiempo de respuesta
    if siguiente_ronda:
        rounds += 1
        tiempo_respuesta = time.time() - tiempo_inicio
        tiempos_respuestas.append(tiempo_respuesta)

    # Verificar si el juego debe terminar
    if vidas <= 0:
        ejecutando = False

# Calcular promedio de tiempo de respuesta
promedio_tiempo = sum(tiempos_respuestas) / len(tiempos_respuestas) if tiempos_respuestas else 0

# Mostrar resultados finales
pantalla.fill(BLANCO)
mostrar_mensaje("Juego terminado", (300, 250))
mostrar_mensaje(f"Promedio de tiempo de respuesta: {promedio_tiempo:.2f} segundos", (200, 300))
mostrar_mensaje(f"Total de monedas obtenidas: {monedas}", (200, 350))
pygame.display.update()
time.sleep(5)

# Salir de Pygame
pygame.quit()
sys.exit()