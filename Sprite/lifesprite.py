import pygame 
import sys, os
import random as r


from Sprite.staticsprite import StaticSprite
from screen import Screen

from typing import Tuple


class LifeSprite(StaticSprite):
    def __init__(
        self,
        path: str,
        position: Tuple[int, int],
        top_bounds: int,
        bottom_bounds: int,
    ):

        super().__init__(path, position)
        
        self.rect = self.sprite.get_rect()

        self.rect.x, self.rect.y = position

        self.sprite = pygame.transform.scale(self.sprite, (128, 128))

        self.top_bounds = top_bounds
        self.bottom_bounds = bottom_bounds

        self.dy = r.randint(1, 2) * 0.6

        if r.random() >= 0.5:
            self.dy *= -1
        

    def move(self) -> None:

        self.rect.y += self.dy
        print(f"Y position: {self.rect.y}, Dy: {self.dy}")

        if self.rect.y <= self.top_bounds or self.rect.y >= self.bottom_bounds:
            self.dy *= -1






