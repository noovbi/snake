import pygame
from settings import *

class MainMenu:
    def __init__(self, screen):
        self.screen = screen
        self.font_title = pygame.font.Font(None, 72)
        self.font_options = pygame.font.Font(None, 48)
        self.selected = 0  # 0: Jugar, 1: Salir
        self.options = ["Jugar", "Cerrar"]
        
    def draw(self):
        self.screen.fill(BG_COLOR)
        
        # Título
        title = self.font_title.render("SNAKE", True, TEXT_COLOR)
        title_rect = title.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//3))
        self.screen.blit(title, title_rect)
        
        # Opciones
        for i, option in enumerate(self.options):
            color = SNAKE_COLOR if i == self.selected else TEXT_COLOR
            text = self.font_options.render(option, True, color)
            text_rect = text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 + i*60))
            self.screen.blit(text, text_rect)
            
        pygame.display.update()
        
    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return "exit"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    self.selected = (self.selected + 1) % 2
                elif event.key == pygame.K_UP:
                    self.selected = (self.selected - 1) % 2
                elif event.key == pygame.K_RETURN:
                    return self.options[self.selected].lower()
        return ""