import pygame, sys
from settings import *
from menu import MainMenu
from sound import SoundManager
from game import Snake, Food

def game_loop(screen, sound):
    clock = pygame.time.Clock()
    snake = Snake()
    food = Food()
    font = pygame.font.Font(None, 36)

    game_over = False
    paused = False

    sound.load_music("assets/background.ogg")
    sound.play_music()

    while True:
        screen.fill(BG_COLOR)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "exit"
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return "menu"
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
                    sound.play_sound('eat')

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

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Snake Game")

    menu = MainMenu(screen)
    sound = SoundManager()
    font = pygame.font.Font(None, 36)

    sound.load_sound('eat', 'assets/eat.wav')
    sound.load_sound('game_over', 'assets/game_over.wav')

    game_result = game_loop(screen, sound)

    game_over = False
    paused = False

    while True:
        result = ""
        while result == "":
            menu.draw()
            result = menu.handle_input()
            pygame.time.wait(100)

        if result == "exit" or result == "cerrar":
            pygame.quit()
            sys.exit()
        elif result == "jugar":
            game_result = game_loop(screen, sound)
            if game_result == "exit":
                pygame.quit()
                sys.exit()
                sound.stop('background')
            sound.play_music() 

if __name__ == "__main__":
    main()