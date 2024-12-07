import pygame
import sys
import random
from enum import Enum
from typing import List, Tuple

# Initialize Pygame
pygame.init()

# Constants
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 400
FPS = 60
GRAVITY = 0.5
JUMP_SPEED = -8
PIPE_SPEED = 3
PIPE_GAP = 150
PIPE_FREQUENCY = 1500  # milliseconds
BIRD_SIZE = (40, 40)
PIPE_WIDTH = 50
PIPE_HEIGHT = 300

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
SKY_BLUE = (135, 206, 235)

class GameState(Enum):
    RUNNING = 1
    PAUSED = 2
    GAME_OVER = 3

class Bird(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface(BIRD_SIZE)
        self.image.fill(GREEN)
        self.rect = self.image.get_rect(center=(WINDOW_WIDTH//4, WINDOW_HEIGHT//2))
        self.velocity = 0
        
    def jump(self):
        self.velocity = JUMP_SPEED
        
    def update(self):
        self.velocity += GRAVITY
        self.rect.y += self.velocity
        
        # Keep bird on screen
        if self.rect.top <= 0:
            self.rect.top = 0
            self.velocity = 0
        if self.rect.bottom >= WINDOW_HEIGHT:
            self.rect.bottom = WINDOW_HEIGHT
            self.velocity = 0

class Pipe(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, is_top: bool):
        super().__init__()
        self.image = pygame.Surface((PIPE_WIDTH, PIPE_HEIGHT))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y if is_top else y + PIPE_GAP

    def update(self):
        self.rect.x -= PIPE_SPEED
        if self.rect.right < 0:
            self.kill()

class FlappyGame:
    def __init__(self):
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Flappy Bird")
        self.clock = pygame.time.Clock()
        
        self.all_sprites = pygame.sprite.Group()
        self.pipes = pygame.sprite.Group()
        self.bird = Bird()
        self.all_sprites.add(self.bird)
        
        self.score = 0
        self.state = GameState.RUNNING
        self.last_pipe = pygame.time.get_ticks()
        self.font = pygame.font.Font(None, 36)

    def create_pipe_pair(self):
        height = random.randint(50, WINDOW_HEIGHT - PIPE_GAP - 50)
        pipe_top = Pipe(WINDOW_WIDTH, height - PIPE_HEIGHT, True)
        pipe_bottom = Pipe(WINDOW_WIDTH, height, False)
        self.pipes.add(pipe_top, pipe_bottom)
        self.all_sprites.add(pipe_top, pipe_bottom)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if self.state == GameState.RUNNING:
                        self.bird.jump()
                if event.key == pygame.K_p:
                    if self.state == GameState.RUNNING:
                        self.state = GameState.PAUSED
                    elif self.state == GameState.PAUSED:
                        self.state = GameState.RUNNING
        return True

    def update(self):
        if self.state != GameState.RUNNING:
            return
            
        self.all_sprites.update()
        
        # Generate new pipes
        now = pygame.time.get_ticks()
        if now - self.last_pipe > PIPE_FREQUENCY:
            self.create_pipe_pair()
            self.last_pipe = now
            
        # Check collisions
        if pygame.sprite.spritecollide(self.bird, self.pipes, False):
            self.state = GameState.GAME_OVER
            
        # Update score
        self.score = len([p for p in self.pipes if p.rect.right < self.bird.rect.left]) // 2

    def draw(self):
        self.screen.fill(SKY_BLUE)
        self.all_sprites.draw(self.screen)
        score_text = self.font.render(f'Score: {self.score}', True, BLACK)
        self.screen.blit(score_text, (10, 10))
        
        if self.state == GameState.PAUSED:
            pause_text = self.font.render('PAUSED', True, BLACK)
            self.screen.blit(pause_text, (WINDOW_WIDTH//2 - 40, WINDOW_HEIGHT//2))
        elif self.state == GameState.GAME_OVER:
            game_over_text = self.font.render('GAME OVER', True, BLACK)
            self.screen.blit(game_over_text, (WINDOW_WIDTH//2 - 70, WINDOW_HEIGHT//2))
            
        pygame.display.flip()

    def run(self):
        running = True
        while running:
            running = self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
        
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = FlappyGame()
    game.run()
