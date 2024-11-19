import pygame
import sys
import random

# Inicializar Pygame
pygame.init()

# Configurar la pantalla
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Juego Plataforma')

# Colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Superficie plana
ground_y = 550

# Posición inicial del jugador
player_pos = [400, ground_y - 50]
player_size = 50

# Velocidad del jugador
player_speed = 5
jump_speed = 10
gravity = 0.5
is_jumping = False
jump_velocity = 0

# Meta
goal_size = 50
goal_pos = [0, 0]

# Plataformas
platforms = [
    pygame.Rect(200, 450, 100, 10),
    pygame.Rect(400, 350, 100, 10),
    pygame.Rect(600, 250, 100, 10)
]

# Cargar sonido de victoria
victory_sound = pygame.mixer.Sound('victory.wav')

def reset_level():
    global player_pos, is_jumping, jump_velocity, goal_pos
    player_pos = [400, ground_y - 50]
    is_jumping = False
    jump_velocity = 0
    randomize_platforms()
    place_goal()

def randomize_platforms():
    for platform in platforms:
        platform.x = random.randint(0, 700)
        platform.y = random.randint(100, 500)

def place_goal():
    platform = random.choice(platforms)
    goal_pos[0] = platform.x + (platform.width - goal_size) // 2
    goal_pos[1] = platform.y - goal_size

# Inicializar el primer nivel
reset_level()

# Bucle principal del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Obtener las teclas presionadas
    keys = pygame.key.get_pressed()

    # Mover al jugador horizontalmente
    if keys[pygame.K_LEFT]:
        player_pos[0] -= player_speed
    if keys[pygame.K_RIGHT]:
        player_pos[0] += player_speed

    # Saltar
    if keys[pygame.K_SPACE]:
        jump_velocity = -jump_speed
        is_jumping = True

    # Aplicar gravedad
    if is_jumping:
        player_pos[1] += jump_velocity
        jump_velocity += gravity
        if player_pos[1] >= ground_y - player_size:
            player_pos[1] = ground_y - player_size
            is_jumping = False
            jump_velocity = 0

    # Colisiones con plataformas
    player_rect = pygame.Rect(player_pos[0], player_pos[1], player_size, player_size)
    for platform in platforms:
        if player_rect.colliderect(platform) and jump_velocity > 0:
            player_pos[1] = platform.y - player_size
            is_jumping = False
            jump_velocity = 0

    # Verificar si el jugador ha llegado a la meta
    goal_rect = pygame.Rect(goal_pos[0], goal_pos[1], goal_size, goal_size)
    if player_rect.colliderect(goal_rect):
        victory_sound.play()
        reset_level()

    # Rellena la pantalla con el color de fondo
    screen.fill(BLUE)

    # Dibuja la superficie plana
    pygame.draw.rect(screen, GREEN, (0, ground_y, 800, 50))

    # Dibuja la meta
    pygame.draw.rect(screen, RED, goal_rect)

    # Dibuja las plataformas
    for platform in platforms:
        pygame.draw.rect(screen, WHITE, platform)

    # Dibuja la persona hecha a palos
    # Cuerpo
    pygame.draw.line(screen, WHITE, (player_pos[0] + player_size // 2, player_pos[1]), (player_pos[0] + player_size // 2, player_pos[1] + player_size), 5)
    # Cabeza
    pygame.draw.circle(screen, WHITE, (player_pos[0] + player_size // 2, player_pos[1] - 10), 10)
    # Brazos
    pygame.draw.line(screen, WHITE, (player_pos[0] + player_size // 2, player_pos[1] + 20), (player_pos[0] + player_size // 2 - 20, player_pos[1] + 40), 5)
    pygame.draw.line(screen, WHITE, (player_pos[0] + player_size // 2, player_pos[1] + 20), (player_pos[0] + player_size // 2 + 20, player_pos[1] + 40), 5)
    # Piernas
    pygame.draw.line(screen, WHITE, (player_pos[0] + player_size // 2, player_pos[1] + player_size), (player_pos[0] + player_size // 2 - 20, player_pos[1] + player_size + 20), 5)
    pygame.draw.line(screen, WHITE, (player_pos[0] + player_size // 2, player_pos[1] + player_size), (player_pos[0] + player_size // 2 + 20, player_pos[1] + player_size + 20), 5)

    # Actualiza la pantalla
    pygame.display.flip()

    # Controla la velocidad del juego
    pygame.time.Clock().tick(30)

pygame.quit()
sys.exit()




