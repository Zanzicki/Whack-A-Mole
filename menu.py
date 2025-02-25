import pygame
import sys

 
class Menu:
    pygame.init()

# Skærmopløsning
res = (720, 720)
screen = pygame.display.set_mode(res)

# Farver
color = (255, 255, 255)  # Hvid tekst
color_light = (170, 170, 170)  # Lys farve til knapper
color_dark = (100, 100, 100)  # Mørk farve til knapper

# Skærm dimensioner
width = screen.get_width()
height = screen.get_height()

# Font
font = pygame.font.SysFont("corbel", 35)

# Knapstørrelse
button_width = 200
button_height = 50
menu_running = True


def draw_button(x, y, text):
    """ Tegner en knap og returnerer True, hvis den klikkes """
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


def menu():
    from gameworld import game_loop
    while menu_running:
        screen.fill((60, 25, 60))  # Baggrundsfarve

        # Tegn knapper
        start_clicked = draw_button(width / 3, height / 2.5, "Start")
        quit_clicked = draw_button(width / 3, height / 2, "Quit")

        # Tjek hændelser
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if start_clicked:
            
            pygame.mixer.music.load('background_music.wav')
            pygame.mixer.music.play(-1)
            
            game_loop(screen, font)
            pygame.init()
            
            
           # end_screen(screen, font)  #  Kald end_screen() fra end_screen.py

        if quit_clicked:
            pygame.quit()
            sys.exit()

        pygame.display.update()

if __name__ == "__main__":
    menu()