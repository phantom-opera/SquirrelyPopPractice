import pygame
import sys
from screen import Screen
from sound import SoundManager
from typing import Tuple, List
from Menu import button
from volumeslider import UI, Slider


class Main:
    def __init__(self, dims: Tuple[int, int]) -> None:
        pygame.init()
        self.screen = Screen(dims, pygame.RESIZABLE)
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Main Menu")

        UI.init(self)

        self.width, self.height = dims

        self.sound_manager = SoundManager()

        self.start_img = pygame.image.load("Assets/UI/Buttons/StartButton.png").convert_alpha()
        self.settings_img = pygame.image.load("Assets/UI/Buttons/SettingsButton.png").convert_alpha()
        self.quit_img = pygame.image.load("Assets/UI/Buttons/QuitButton.png").convert_alpha()

        self.logo_img = pygame.image.load("Assets/UI/logo.png").convert_alpha()
        self.logo_img = pygame.transform.scale(self.logo_img, (480, 320))
        self.logoRect = self.logo_img.get_rect()
        self.logoRect.x = (self.width - self.logo_img.get_width()) // 2 

        self.background_img = pygame.image.load("Assets/UI/background.png").convert_alpha()
        self.background_img = pygame.transform.scale(self.background_img, (self.width, self.height))
        self.backgroundRect = self.background_img.get_rect()

        self.controls_img = pygame.image.load("Assets/UI/SQPOP_KEYSMOUSE.png").convert_alpha()
        self.controls_img = pygame.transform.scale(self.controls_img, (950, 400))
        self.controlRect = self.controls_img.get_rect()
        self.controlRect.x = (self.width - self.controls_img.get_width()) // 2 

        self.button_width = 200
        self.button_height = 50
        self.button_spacing = 30  # Spacing between buttons

        total_height = (
            self.button_height * 3 + self.button_spacing * 2
        )  # Three buttons, two gaps
        start_y = (self.height - total_height) // 2

        self.start_button = button.Button(
            (self.width - self.button_width) // 2,
            start_y + (self.button_height + self.button_spacing) * 2,
            self.button_width,
            self.button_height,
            self.start_img,
            1
        )

        self.settings_button = button.Button(
            (self.width - self.button_width) // 2,
            start_y + (self.button_height + self.button_spacing) * 3,
            self.button_width,
            self.button_height,
            self.settings_img,
            1
        )

        self.quit_button = button.Button(
            (self.width - self.button_width) // 2,
            start_y + (self.button_height + self.button_spacing) * 4,
            self.button_width,
            self.button_height,
            self.quit_img,
            1
        )

        self.settings = {
            "Volume": 50,  # Volume slider position, 0 to 100
        }

        # Create Slider for volume control
        self.volume_slider = Slider(
            (self.width // 2, 500), (200, 30), self.settings["Volume"] / 100, 0, 100
        )

    def draw_text(self, text, font, color, surface, x, y):
            text_obj = UI.font.render(text, 1, color)
            text_rect = text_obj.get_rect()
            text_rect.topleft = (x, y)
            surface.blit(text_obj, text_rect)

        
    def run(self) -> None:
            self.sound_manager.music("load", "Assets/Sounds/MainMusic/TownTheme.mp3")
            self.sound_manager.music("play")

         
            menu_state = "main"

            running = True

            while running:
                mx, my = pygame.mouse.get_pos()

                self.screen.screen.fill((52, 78, 91))

                self.screen.screen.blit(self.background_img, self.backgroundRect)

                if menu_state == "main":
                 self.screen.screen.blit(self.logo_img, self.logoRect)

                 if self.start_button.draw(self.screen.screen):
                    pass
                 
                 if self.settings_button.draw(self.screen.screen):
                    menu_state = "settings"
                 
                 if self.quit_button.draw(self.screen.screen):
                        running = False
                
                if menu_state == "settings":
                    self.screen.screen.blit(self.controls_img, self.controlRect)
                    self.volume_slider.render(self)
                    self.volume_slider.display_value(self)

                    self.draw_text(
                        f"Volume: {self.settings['Volume']}",
                        UI.font,
                        (255, 255, 255),
                        self.screen.screen,
                        self.volume_slider.pos[0] - self.volume_slider.size[0] // 2 - 160,
                        self.volume_slider.pos[1] - 10,
                    )


                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            if menu_state == "settings":
                                menu_state = "main"
                    
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            # Check if volume slider is clicked and update the volume

                            if self.volume_slider.container_rect.collidepoint(mx, my):
                                self.volume_slider.grabbed = True

                    elif event.type == pygame.MOUSEBUTTONUP:
                        if event.button == 1:
                            self.volume_slider.grabbed = False
                    
                     # Move the slider if it's being grabbed
                    if self.volume_slider.grabbed:
                        self.volume_slider.move_slider((mx, my))
                        # Update the settings volume based on the slider value
                        self.settings["Volume"] = int(self.volume_slider.get_value())                
                        # Set the music volume based on the slider value (0 to 1)
                        pygame.mixer.music.set_volume(self.volume_slider.get_value() / 100.0)
                
                pygame.display.update()
        

if __name__ == "__main__":
    mainmenu = Main((1280, 720))
    mainmenu.run()
