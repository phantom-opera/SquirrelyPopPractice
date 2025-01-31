import pygame
import sys
from Menu import button

UNSELECTED = "red"
SELECTED = "white"
BUTTONSTATES = {True: SELECTED, False: UNSELECTED}


class UI:
    @staticmethod
    def init(app):
        UI.font = pygame.font.SysFont("Consolas", 25)
        UI.sfont = pygame.font.SysFont("Consolas", 20)
        UI.lfont = pygame.font.SysFont("Consolas", 40)
        UI.xlfont = pygame.font.SysFont("Consolas", 50)
        UI.center = (app.screen.screen.get_size()[0] // 2, app.screen.screen.get_size()[1] // 2)
        UI.fonts = {"sm": UI.sfont, "m": UI.font, "l": UI.lfont, "xl": UI.xlfont}

class Slider:
    def __init__(
        self, pos: tuple, size: tuple, initial_val: float, min: int, max: int
    ) -> None:
        self.pos = pos
        self.size = size
        self.slider_left_pos = self.pos[0] - (size[0] // 2)
        self.slider_right_pos = self.pos[0] + (size[0] // 2)
        self.slider_top_pos = self.pos[1] - (size[1] // 2)
        self.min = min
        self.max = max
        self.initial_val = (self.slider_right_pos - self.slider_left_pos) * initial_val

        self.container_rect = pygame.Rect(
            self.slider_left_pos, self.slider_top_pos, self.size[0], self.size[1]
        )
        self.button_rect = pygame.Rect(
            self.slider_left_pos + self.initial_val - 5,
            self.slider_top_pos,
            10,
            self.size[1],
        )

        self.text = UI.fonts["m"].render(
            str(int(self.get_value())), True, "white", None
        )
        self.label_rect = self.text.get_rect(
            center=(self.pos[0], self.slider_top_pos - 15)
        )

        self.grabbed = False

    def move_slider(self, mouse_pos):
        if self.grabbed:
            pos = mouse_pos[0]
            pos = max(self.slider_left_pos, min(pos, self.slider_right_pos))
            self.button_rect.centerx = pos
            pygame.mixer.music.set_volume(self.get_value() / 100)

    def render(self, app):
        pygame.draw.rect(app.screen.screen, "darkgray", self.container_rect)
        pygame.draw.rect(app.screen.screen, BUTTONSTATES[self.hovered()], self.button_rect)

    def hovered(self):
        return self.container_rect.collidepoint(pygame.mouse.get_pos())

    def get_value(self):
        val_range = self.slider_right_pos - self.slider_left_pos
        button_val = self.button_rect.centerx - self.slider_left_pos
        return (button_val / val_range) * (self.max - self.min) + self.min

    def display_value(self, app):
        self.text = UI.fonts["m"].render(
            str(int(self.get_value())), True, "white", None
        )
        app.screen.screen.blit(self.text, self.label_rect)