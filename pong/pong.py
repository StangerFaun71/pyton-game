import pygame
import sys

# Inicializáld a Pygame-et
pygame.init()

# Képernyő beállításai
WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

# Színek
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Játékosok
player1 = pygame.Rect(10, HEIGHT // 2 - 50, 10, 100)
player2 = pygame.Rect(WIDTH - 20, HEIGHT // 2 - 50, 10, 100)

# Labda
ball = pygame.Rect(WIDTH // 2 - 10, HEIGHT // 2 - 10, 20, 20)
ball_speed_x = 7
ball_speed_y = 7

# Játékosok sebessége
player1_speed = 0
player2_speed = 0

# Mozgások
PLAYER_SPEED = 10

# Pontszámok
player1_score = 0
player2_score = 0

# Pontszámlálók beállítása
font = pygame.font.Font(None, 36)
text1 = font.render(f"Player 1: {player1_score}", True, WHITE)
text2 = font.render(f"Player 2: {player2_score}", True, WHITE)
text1_rect = text1.get_rect(center=(WIDTH // 4, 50))
text2_rect = text2.get_rect(center=(3 * WIDTH // 4, 50))

# Nyertes szövegek
winner_font = pygame.font.Font(None, 48)
winner_text1 = winner_font.render("Player 1 Won!", True, WHITE)
winner_text2 = winner_font.render("Player 2 Won!", True, WHITE)
winner_rect = winner_text1.get_rect(center=(WIDTH // 2, HEIGHT // 2))

# Nyertes flag
winner_flag = False

# Játék ciklus
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player2_speed += PLAYER_SPEED
            if event.key == pygame.K_UP:
                player2_speed -= PLAYER_SPEED
            if event.key == pygame.K_s:
                player1_speed += PLAYER_SPEED
            if event.key == pygame.K_w:
                player1_speed -= PLAYER_SPEED
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player2_speed -= PLAYER_SPEED
            if event.key == pygame.K_UP:
                player2_speed += PLAYER_SPEED
            if event.key == pygame.K_s:
                player1_speed -= PLAYER_SPEED
            if event.key == pygame.K_w:
                player1_speed += PLAYER_SPEED

    # Játékosok mozgatása, de nem engedjük ki a képernyőről
    player1.y += player1_speed
    player2.y += player2_speed

    player1.y = max(0, player1.y)  # Ne mehessen ki felfelé
    player1.y = min(HEIGHT - player1.height, player1.y)  # Ne mehessen ki lefelé

    player2.y = max(0, player2.y)  # Ne mehessen ki felfelé
    player2.y = min(HEIGHT - player2.height, player2.y)  # Ne mehessen ki lefelé

    # Labda mozgatása
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Fal ütközés
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed_y = -ball_speed_y

    # Játékosok ütközés
    if ball.colliderect(player1) or ball.colliderect(player2):
        ball_speed_x = -ball_speed_x

    # Labda elhagyja a pályát
    if ball.left <= 0:
        player2_score += 1
        if player2_score == 10:
            winner_text = winner_text2
            winner_flag = True
        ball = pygame.Rect(WIDTH // 2 - 10, HEIGHT // 2 - 10, 20, 20)
        ball_speed_x = 7
        ball_speed_y = 7
    if ball.right >= WIDTH:
        player1_score += 1
        if player1_score == 10:
            winner_text = winner_text1
            winner_flag = True
        ball = pygame.Rect(WIDTH // 2 - 10, HEIGHT // 2 - 10, 20, 20)
        ball_speed_x = -7
        ball_speed_y = 7

    # Frissítsd a pontszámlálókat
    text1 = font.render(f"Player 1: {player1_score}", True, WHITE)
    text2 = font.render(f"Player 2: {player2_score}", True, WHITE)

    # Képernyő törlése
    screen.fill(BLACK)

    # Játékosok rajzolása
    pygame.draw.rect(screen, WHITE, player1)
    pygame.draw.rect(screen, WHITE, player2)

    # Labda rajzolása
    pygame.draw.ellipse(screen, WHITE, ball)

    # Ha valaki elérte a 10 pontot, akkor jelenítsük meg a győztest
    if winner_flag:
        screen.blit(winner_text, winner_rect)
        pygame.display.flip()
        pygame.time.wait(5000)  # Várakozás 5 másodpercig
        pygame.quit()
        sys.exit()
    else:
        # Pontszámlálók megjelenítése
        screen.blit(text1, text1_rect)
        screen.blit(text2, text2_rect)

    # Képernyő frissítése
    pygame.display.flip()

    # FPS beállítása
    pygame.time.Clock().tick(60)
