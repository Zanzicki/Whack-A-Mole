import pygame
import sys
from menu import menu

pygame.init()

def end_screen(screen, font, score):
    
    width = screen.get_width()
    height = screen.get_height()

    button_width = 200
    button_height = 50
    color = (255, 255, 255)
    color_light = (170, 170, 170)
    color_dark = (100, 100, 100)
    menu_running = True

    def draw_button(x, y, text):
        
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x <= mouse[0] <= x + button_width and y <= mouse[1] <= y + button_height:
            pygame.draw.rect(screen, color_light, [x, y, button_width, button_height])
            if click[0]:  # Venstre klik
                return True
        else:
            pygame.draw.rect(screen, color_dark, [x, y, button_width, button_height])

        # Tegn tekst
        text_render = font.render(text, True, color)
        screen.blit(text_render, (x + 50, y + 10))
        return False

    while menu_running:
        screen.fill((60, 25, 60))  # Baggrundsfarve

        # Tegn knapper
        back_clicked = draw_button(width / 3, height / 2.5, "Back to Menu")
        quit_clicked = draw_button(width / 3, height / 2, "Quit")

        # Tegn "Game Over" tekst
        game_over_text = font.render("GAME OVER", True, color)
        screen.blit(game_over_text, (width / 3 + 20, height / 3))
        
        score_text=font.render(f"Score: {score}", True, color)
        screen.blit(score_text,(width/3+20, height/4))

        # Tjek hændelser
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        
        if back_clicked:
            menu_running=False
            return
            

        
        if quit_clicked:
            pygame.quit()
            sys.exit()

        pygame.display.update()
