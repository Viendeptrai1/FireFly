import pygame
from entities.firefly import Firefly
from entities.color_target import ColorTarget
from utils.colors import COLORS

class Game:
    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.firefly = Firefly()
        self.targets = pygame.sprite.Group()
        self.score = 0
        self.font = pygame.font.Font(None, 36)
        self.background_img = pygame.image.load('/Users/kotori/Desktop/testgit/FireFly/assets/bachgroud.webp')
        self.background_img = pygame.transform.scale(self.background_img, (800, 600))
        self.reset_game()
        self.input_active = False  # Thêm biến input_active

    def reset_game(self):
        self.targets.empty()
        for color in COLORS.values():
            self.targets.add(ColorTarget(color))
        self.score = 0

    def run(self):
        running = True
        input_text = ""
        input_rect = pygame.Rect(400 - 100, 300 - 25, 200, 50)

        while running:
            self.screen.blit(self.background_img, (0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if self.input_active:  # Chỉnh thành self.input_active
                        if event.key == pygame.K_RETURN:
                            if self.check_color(input_text.upper()):
                                running = False
                            self.input_active = False  # Chỉnh thành self.input_active
                            input_text = ""
                        elif event.key == pygame.K_BACKSPACE:
                            input_text = input_text[:-1]
                        else:
                            input_text += event.unicode

            keys = pygame.key.get_pressed()
            self.firefly.move(keys[pygame.K_RIGHT] - keys[pygame.K_LEFT],
                              keys[pygame.K_DOWN] - keys[pygame.K_UP])
            collided = pygame.sprite.spritecollide(self.firefly, self.targets, False)
            if collided and not self.input_active:
                self.input_active = True  # Chỉnh thành self.input_active
            elif not collided:  # Kiểm tra khi không va chạm
                self.input_active = False  # Chỉnh thành self.input_active

            self.targets.draw(self.screen)
            self.screen.blit(self.firefly.image, self.firefly.rect)

            score_text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
            self.screen.blit(score_text, (10, 10))

            if self.input_active:  # Chỉnh thành self.input_active
                pygame.draw.rect(self.screen, (255, 255, 255), input_rect, 2)
                text_surface = self.font.render(input_text, True, (255, 255, 255))
                self.screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))

            pygame.display.flip()
            self.clock.tick(60)

        return self.score

    def check_color(self, color_name):
        collided = pygame.sprite.spritecollide(self.firefly, self.targets, False)
        if collided:
            target = collided[0]
            if color_name == target.color_name:
                self.score += 1
                self.targets.remove(target)
                if not self.targets:
                    print("Congratulations! You've found all colors!")
                    return True
            else:
                print(f"Wrong! That was {target.color_name}")
                return True
        return False
