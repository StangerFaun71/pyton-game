import pygame
import random

# Inicializáljuk a Pygame-et
pygame.init()

# Játékablak beállítása
screen_width = 400
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Flappy Bird")

# Színek
white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)
bird_color = (255, 255, 0)

# Madár jellemzői
bird_x = 100
bird_y = screen_height // 2
bird_speed = 0

# Csapdák (akadályok) listája
pipes = []
pipe_width = 50
pipe_height = 300
pipe_gap = 200
pipe_speed = 5

# Pontszám
score = 0
font = pygame.font.Font(None, 36)

# Madár a csövek között repül-e
is_between_pipes = False

def draw_bird(x, y):
    pygame.draw.rect(screen, bird_color, (x, y, 40, 40))

def draw_pipe(x, gap_height):
    pygame.draw.rect(screen, blue, (x, 0, pipe_width, gap_height))
    pygame.draw.rect(screen, blue, (x, gap_height + pipe_gap, pipe_width, screen_height - gap_height - pipe_gap))

def game_over():
    game_over_text = font.render("Game Over", True, red)
    screen.blit(game_over_text, (150, 250))
    pygame.display.update()
    pygame.time.delay(1000)
    main()

def main():
    global is_between_pipes  # Deklaráljuk a változót globálisnak
    bird_y = screen_height // 2
    bird_speed = 0
    pipes.clear()
    score = 0
    is_between_pipes = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird_speed = -10

        bird_speed += 1
        bird_y += bird_speed

        if bird_y <= 0:
            bird_y = 0
        if bird_y >= screen_height - 40:
            bird_y = screen_height - 40

        screen.fill(white)
        draw_bird(bird_x, bird_y)

        for pipe in pipes:
            pipe[0] -= pipe_speed
            draw_pipe(pipe[0], pipe[1])

            if pipe[0] < -pipe_width:
                pipes.remove(pipe)
                score += 1

            if is_between_pipes:
                continue

            if pipes and len(pipes) > 0 and bird_x > pipes[0][0] + pipe_width:
                is_between_pipes = True

            if bird_x + 40 > pipe[0] and bird_x < pipe[0] + pipe_width:
                if bird_y < pipe[1] or bird_y + 40 > pipe[1] + pipe_gap:
                    game_over()

        if is_between_pipes and not pipes:
            is_between_pipes = False

        if not pipes:
            gap_height = random.randint(100, 400)
            pipes.append([screen_width, gap_height])

        score_text = font.render("Score: " + str(score), True, red)
        screen.blit(score_text, (10, 10))
        pygame.display.update()

        pygame.time.delay(30)

main()

