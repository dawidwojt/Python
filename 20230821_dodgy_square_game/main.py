# % pip install pygame

import pygame
from pygame.font import Font
from pygame.time import Clock
import random                   # to generate random  squares location
import sys                      # to be able to exit app when user wants it


class DodgySquare:
    def __init__(self):
        pygame.init()                       # init pygame
        pygame.mouse.set_visible(False)     # we do not want mouse to be visible

        # Screen
        self.screen_width, self.screen_height = 600, 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption('Dodgy Square')

        # Colors
        self.WHITE: tuple = (255,255,255)
        self.BLACK: tuple = (0,0,0)
        self.RED: tuple = (255,99,71)
        self.BLUE: tuple = (65, 105, 225)

        # Font
        self.default_font: str = pygame.font.get_default_font()
        self.font: Font = pygame.font.Font(self.default_font, 26)

        # Player
        self.player_size: int = 30 ###
        self.player_pos: list[int] = [0,0]

        # Enemies
        self.enemy_size: int = 50
        self.enemy_position: list[int] = []
        self.enemy_list: list[list[int]] = []
        self.enemy_speed: float = 3
        self.enemy_frequency: int = 20 # 60 frames per second, so new enemies per second in the beginning

        # Clock
        self.clock: Clock = pygame.time.Clock()

        # Game Data
        self.game_over: bool = False
        self.score:  int = 0
        self.frame_count: int = 0

    def create_random_color(self):
        self.rgb_r = random.randint(0,255)
        self.rgb_g = random.randint(0, 255)
        if self.rgb_r > 100 or self.rgb_g > 100:
            self.rgb_b = random.randint(0, 255)
        else:
            self.rgb_b = random.randint(100, 255)
        self.COLOR_RANDOM: tuple = (self.rgb_r, self.rgb_g, self.rgb_b)

    def create_enemy(self):
        enemy_pos: list[int] = [random.randint(0, self.screen_width - self.enemy_size), -self.enemy_size]
        self.enemy_list.append(enemy_pos)

    def update_enemy_position(self):
        if self.frame_count % self.enemy_frequency == 0:
            self.create_enemy()

        for idx, enemy_pos in enumerate(self.enemy_list):
            if -self.enemy_size <= enemy_pos[1] < self.screen_height:
                enemy_pos[1] += self.enemy_speed
            else:
                self.enemy_list.pop(idx)
                self.score += 1
                if self.score < 100:
                    self.enemy_speed += 0.1
                elif self.score < 150:
                    self.enemy_speed += 0.025
                else:
                    self.enemy_speed += 0.01

                if self.enemy_frequency > 10:
                    if self.score % 15 == 0:
                        self.enemy_frequency -= 2

    def detect_collision(self, player_pos: list[int], enemy_pos: list[int]) -> bool:
        px, py = player_pos     # player coordinates
        ex, ey = enemy_pos      # enemy coordinates

        if (px <= ex < (px + self.player_size)) or (ex <= px < (ex + self.enemy_size)):
            if (py <= ey < (py + self.player_size)) or (ey <= py < (ey + self.enemy_size)):
                return True
        return False

    def show_game_over(self):
        game_over_text = self.font.render('Game Over', True, self.WHITE)
        self.screen.blit(game_over_text, (self.screen_width // 2 - 70, self.screen_height // 2 - 16))

    # to reset game settings/data
    def replay_game(self):
        self.enemy_list: list[list[int]] = []
        self.enemy_speed: float = 3
        self.enemy_frequency: int = 20
        self.game_over = False
        self.frame_count: int = 0
        self.score: int = 0

    def draw_character(self, color: tuple, position: list[int], size: int):
        pygame.draw.rect(self.screen, color, (position[0], position[1], size, size))

    def run(self):
        self.create_random_color()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # Resetting game
                if event.type == pygame.KEYDOWN:
                    if self.game_over and event.key == pygame.K_r:
                        self.replay_game()

                # Getting the current mouse position
                mouse_pos: tuple[int, int] = pygame.mouse.get_pos()

                # Update player position
                self.player_pos[0] = mouse_pos[0] - self.player_size // 2
                self.player_pos[1] = mouse_pos[1] - self.player_size // 2

                # Make sure the player stays on the screen
                self.player_pos[0] = max(0, min(self.player_pos[0], self.screen_width - self.player_size))
                self.player_pos[1] = max(1, min(self.player_pos[1], self.screen_height - self.player_size))


            if not self.game_over:
                self.update_enemy_position()

                for enemy_pos in self.enemy_list:
                    if self.detect_collision(self.player_pos, enemy_pos):
                        self.game_over = True
                        break

                # Resetting everything for the next frame (overlaying)
                self.screen.fill(self.BLACK)

                # Drawing the player
                self.draw_character(self.WHITE, self.player_pos, self.player_size)


                # Draw the enemies
                for enemy_pos in self.enemy_list:
                    if self.score > 150:
                        #self.draw_character(self.RED, enemy_pos, self.enemy_size)
                        self.create_random_color()
                        self.draw_character(self.COLOR_RANDOM, enemy_pos, self.enemy_size)
                    else:
                        self.draw_character(self.COLOR_RANDOM, enemy_pos, self.enemy_size)

                # Displaying the score
                score_text = self.font.render(f'Score: {self.score}', True, self.WHITE)
                self.screen.blit(score_text, [10,10])

                # Increment the frame count
                self.frame_count += 1
            else:
                self.show_game_over()

            pygame.display.update()
            self.clock.tick(60)
            if self.score % 5 == 0 and self.score != 0:
                self.create_random_color()


if __name__ == '__main__':
    game = DodgySquare()
    game.run()