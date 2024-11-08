import pygame
import random

pygame.init()


SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Simple 2D Game")


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)


player_size = 50
player_pos = [SCREEN_WIDTH//2, SCREEN_HEIGHT-2*player_size]
player_speed = 10

enemy_size = 50
enemy_pos = [random.randint(0, SCREEN_WIDTH-enemy_size), 0]
enemy_speed = 5


clock = pygame.time.Clock()


def detect_collision(player_pos, enemy_pos):
    p_x = player_pos[0]
    p_y = player_pos[1]

    e_x = enemy_pos[0]
    e_y = enemy_pos[1]

    if (e_x >= p_x and e_x < (p_x + player_size)) or (p_x >= e_x and p_x < (e_x + enemy_size)):
        if (e_y >= p_y and e_y < (p_y + player_size)) or (p_y >= e_y and p_y < (e_y + enemy_size)):
            return True
    return False


game_over = False
score = 0

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and player_pos[0] > 0:
        player_pos[0] -= player_speed
    if keys[pygame.K_RIGHT] and player_pos[0] < SCREEN_WIDTH - player_size:
        player_pos[0] += player_speed

    
    if enemy_pos[1] >= 0 and enemy_pos[1] < SCREEN_HEIGHT:
        enemy_pos[1] += enemy_speed
    else:
        enemy_pos[0] = random.randint(0, SCREEN_WIDTH - enemy_size)
        enemy_pos[1] = 0
        score += 1

    
    if detect_collision(player_pos, enemy_pos):
        game_over = True

    
    screen.fill(BLACK)

    
    pygame.draw.rect(screen, WHITE, (player_pos[0], player_pos[1], player_size, player_size))
    pygame.draw.rect(screen, RED, (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))

    
    font = pygame.font.SysFont("monospace", 35)
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    
    pygame.display.update()

    
    clock.tick(30)


pygame.quit()
