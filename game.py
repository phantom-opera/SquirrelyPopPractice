import pygame
import sys
from screen import Screen
from typing import Tuple, List
from Menu import button
from bubble import Bubble
from Sprite.staticsprite import StaticSprite
from Sprite.lifesprite import LifeSprite

class Game:
    def __init__(self, dims: Tuple[int, int]) -> None:
        pygame.init()
        self.screen = Screen(dims, pygame.RESIZABLE)
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("SquirrelyPop")

        self.width, self.height = dims

        self.bubbles = [Bubble("Assets/UI/bubble.png", (0, 0)) for k in range(7)]

        self.life_list = [
           LifeSprite("Assets/UI/SharkLife.png", (70, 150), 70, 160),
           LifeSprite("Assets/UI/SharkLife.png", (70, 250), 230, 320),
           LifeSprite("Assets/UI/SharkLife.png", (70, 350), 330, 490),

           LifeSprite("Assets/UI/SharkLife.png", (500, 150), 70, 160),
           LifeSprite("Assets/UI/SharkLife.png", (500, 250), 230, 320),
           LifeSprite("Assets/UI/SharkLife.png", (500, 350), 330, 490)
        ]

        self.frame_counter = 0  # Frame counter
        self.frame_interval = 10  # Set the interval for when to move the sprite


        self.healthcounter_img = pygame.image.load("Assets/UI/FE_Health_Counter.png").convert_alpha()
        self.healthcounter_img = pygame.transform.scale(self.healthcounter_img, (300, 600))

        self.map_img = pygame.image.load("Assets/UI/SandGrid.png").convert_alpha()
        self.map_img = pygame.transform.scale(self.map_img, (600,600))

        self.coralbutton_img = pygame.image.load("Assets/UI/Buttons/PlaceCoralButton.png").convert_alpha()

        self.background_img = pygame.image.load("Assets/UI/background.png").convert_alpha()
        self.background_img = pygame.transform.scale(self.background_img, (self.width, self.height))
        self.backgroundRect = self.background_img.get_rect()

        self.button_width = 200
        self.button_height = 50

        self.coral_button = button.Button(
            190,
            230,
            self.button_width,
            self.button_height,
            self.coralbutton_img,
            2.5
        )

    def run(self) -> None:

        running = True

        while running:
            mx, my = pygame.mouse.get_pos()

            self.screen.screen.blit(self.background_img, self.backgroundRect)

            self.frame_counter += 1
            

            for bubble in self.bubbles:
                self.screen.screen.blit(bubble.sprite, (bubble.x, bubble.y))
                bubble.move()

            self.screen.screen.blit(self.healthcounter_img, (199, 0))
            self.screen.screen.blit(self.map_img, (640, 100))
            
            self.coral_button.draw(self.screen.screen)

            if self.frame_counter >= self.frame_interval:
                for life in self.life_list:
                    life.move()

                self.frame_counter = 0  

            for life in self.life_list:
                self.screen.screen.blit(life.sprite, life.rect)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    
                    
            pygame.display.update()


if __name__ == "__main__":
    game = Game((1280, 720))
    game.run()
