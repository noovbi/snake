import pygame, sys
from settings import *
from game import Snake, Food
from sound import SoundManager

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Snake Game")
    clock = pygame.time.Clock()
    
    snake = Snake()
    food = Food()
    sound = SoundManager()
    font = pygame.font.Font(None, 36)
    
    game_over = False
    paused = False
    sound.play('background', loops=-1)  
    
    while True:
        screen.fill(BG_COLOR)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_p and not game_over:
                    paused = not paused
                elif event.key == pygame.K_r and game_over:
                    snake.reset()
                    food.randomize()
                    game_over = False
                elif not game_over and not paused:
                    if event.key == pygame.K_UP:
                        snake.change_direction(0, -1)
                    elif event.key == pygame.K_DOWN:
                        snake.change_direction(0, 1)
                    elif event.key == pygame.K_LEFT:
                        snake.change_direction(-1, 0)
                    elif event.key == pygame.K_RIGHT:
                        snake.change_direction(1, 0)
        
        if not game_over and not paused:
            if not snake.move():
                game_over = True
                if SOUND_ENABLED:
                    sound.play('game_over')
                    sound.stop('background')
            else:
                # Comprobar si come comida
                if snake.body[0] == food.position:
                    snake.grow = True
                    food.randomize()
                    if SOUND_ENABLED:
                        sound.play('eat')
        
        # Dibujar elementos siempre
        snake.draw(screen)
        food.draw(screen)
        
        # Mostrar puntuación
        score = len(snake.body) - 1
        text = font.render(f"Puntuación: {score}", True, TEXT_COLOR)
        screen.blit(text, (10, 10))
        
        if paused:
            pause_text = font.render("PAUSA - Presiona P para continuar", True, TEXT_COLOR)
            screen.blit(pause_text, (SCREEN_WIDTH//2 - 160, SCREEN_HEIGHT//2 - 20))
        elif game_over:
            game_over_text = font.render("Game Over! Presiona R para reiniciar", True, TEXT_COLOR)
            screen.blit(game_over_text, (SCREEN_WIDTH//2 - 180, SCREEN_HEIGHT//2 - 20))
        
        pygame.display.update()
        clock.tick(SPEED)

if __name__ == "__main__":
    main()