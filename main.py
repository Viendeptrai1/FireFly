import pygame
import sys
from game import Game
from ui.button import Button

pygame.init()

WIDTH = 800
HEIGHT = 600
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Đom Đóm Tìm Màu")
clock = pygame.time.Clock()

def show_menu():
    start_button = Button(300, 200, 200, 50, 'Start Game', GRAY, BLACK)
    high_scores_button = Button(300, 300, 200, 50, 'High Scores', GRAY, BLACK)
    quit_button = Button(300, 400, 200, 50, 'Quit', GRAY, BLACK)

    background_img = pygame.image.load('/Users/kotori/Desktop/testgit/FireFly/assets/bachgroud.webp')
    background_img = pygame.transform.scale(background_img, (WIDTH, HEIGHT))

    while True:
        screen.blit(background_img, (0, 0))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 'quit'
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.is_clicked(event.pos):
                    return 'start'
                if high_scores_button.is_clicked(event.pos):
                    return 'high_scores'
                if quit_button.is_clicked(event.pos):
                    return 'quit'

        start_button.draw(screen)
        high_scores_button.draw(screen)
        quit_button.draw(screen)

        title_font = pygame.font.Font(None, 64)
        title_text = title_font.render("Đom Đóm Tìm Màu", True, WHITE)
        screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, 100))

        pygame.display.flip()
        clock.tick(60)

def show_high_scores(scores):
    back_button = Button(300, 500, 200, 50, 'Back to Menu', GRAY, BLACK)

    background_img = pygame.image.load('/Users/kotori/Desktop/testgit/FireFly/assets/bachgroud.webp')
    background_img = pygame.transform.scale(background_img, (WIDTH, HEIGHT))

    while True:
        screen.blit(background_img, (0, 0))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 'quit'
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.is_clicked(event.pos):
                    return 'menu'

        back_button.draw(screen)

        title_font = pygame.font.Font(None, 48)
        title_text = title_font.render("High Scores", True, WHITE)
        screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, 50))

        score_font = pygame.font.Font(None, 36)
        for i, score in enumerate(scores):
            score_text = score_font.render(f"{i+1}. {score}", True, WHITE)
            screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, 150 + i * 50))

        pygame.display.flip()
        clock.tick(60)

def main():
    game = Game(screen, clock)
    high_scores = []

    while True:
        choice = show_menu()
        
        if choice == 'start':
            score = game.run()
            high_scores.append(score)
            high_scores.sort(reverse=True)
            high_scores = high_scores[:5]  # Keep only top 5 scores
            game.reset_game()
        elif choice == 'high_scores':
            show_high_scores(high_scores)
        elif choice == 'quit':
            break

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
