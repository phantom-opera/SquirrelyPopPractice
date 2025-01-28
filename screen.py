import pygame
import sys
from typing import Tuple, List


class Screen:
    def __init__(self, dims: Tuple[int, int], flags) -> None:
        pygame.display.init()
        self.screen = pygame.display.set_mode(size=dims, flags=flags)
        self.flags = flags
        self.dims = dims

        self.clock = pygame.time.Clock()

    def events(self, e):
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if e.type == pygame.VIDEORESIZE:
            self.toggle_fs()


if __name__ == "__main__":
    screen = Screen((450, 360), flags=pygame.RESIZABLE)

    while True:
        for e in pygame.event.get():
            screen.events(e)
