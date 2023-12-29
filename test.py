import pygame
import random

pygame.init()
screen = pygame.display.set_mode((700, 700))

def restart_game():
    global snake_x, snake_y, snake_speed_x, snake_speed_y, snake_segments, game_started
    snake_x = 350
    snake_y = 350
    snake_speed_x = 5
    snake_speed_y = 0
    snake_segments = [(snake_x, snake_y)]
    Snake.current_head = Snake.head_right
    game_started = False

run = True
snake_x = 350
snake_y = 350
snake_speed_x = 5
snake_speed_y = 0
clock = pygame.time.Clock()

class Snake:
    head_left = pygame.image.load("image/head_left.png")
    head_right = pygame.transform.rotate(head_left, 180)
    head_down = pygame.transform.rotate(head_left, 90)
    head_up = pygame.transform.rotate(head_left, 270)

    current_head = head_right

class Color:
    dark = (0, 0, 0)
    white = (255,255,255)
    green_light = (0, 200, 0)
    green_dark = (0, 100, 0)

snake_segments = [(snake_x, snake_y)]
game_started = False

font = pygame.font.Font(None, 36)  

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pressed = pygame.key.get_pressed()

    if not game_started:
        screen.fill(Color.green_dark)  
        text = font.render("Appuyez sur Espace pour commencer", True, Color.white)
        text_rect = text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
        screen.blit(text, text_rect)

        if pressed[pygame.K_SPACE]:
            game_started = True

    if game_started:
        if pressed[pygame.K_LEFT] and snake_speed_x == 0:
            Snake.current_head = Snake.head_left
            snake_speed_x = -5
            snake_speed_y = 0
        if pressed[pygame.K_RIGHT] and snake_speed_x == 0:
            Snake.current_head = Snake.head_right
            snake_speed_x = 5
            snake_speed_y = 0
        if pressed[pygame.K_UP] and snake_speed_y == 0:
            Snake.current_head = Snake.head_up
            snake_speed_y = -5
            snake_speed_x = 0
        if pressed[pygame.K_DOWN] and snake_speed_y == 0:
            Snake.current_head = Snake.head_down
            snake_speed_y = 5
            snake_speed_x = 0

        snake_x += snake_speed_x
        snake_y += snake_speed_y

        if snake_x > 700 or snake_x < 0 or snake_y > 700 or snake_y < 0:
            restart_game()

        snake_segments.insert(0, (snake_x, snake_y))

        screen.fill(Color.green_light)

        for segment in snake_segments:
            screen.blit(Snake.current_head, segment)

        clock.tick(10)

        pygame.display.flip()

        if len(snake_segments) > 1:
            snake_segments.pop()

pygame.quit()
