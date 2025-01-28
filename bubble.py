import pygame as pg
import sys, os

from Sprite.staticsprite import StaticSprite

import random as r


class Bubble(StaticSprite):
    def __init__(self, path, coords):
        super().__init__(path, coords)
        self.set_pos()

    def set_pos(self):
        self.x = r.randint(5, 1275)
        self.dy = r.randint(1, 2) * 0.3
        self.y = r.randint(1281, 1381)

    def move(self):
        self.y -= self.dy

        if self.y <= -45:
            self.set_pos()
