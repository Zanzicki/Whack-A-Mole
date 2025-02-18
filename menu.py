import pygame
import sys

class Menu:
    #initialize pygame constructor
    pygame.init()

    # screen resolution
    res = (720,720)
    
    #opens window
    screen = pygame.display.set_mode(res)
    
    #sets collors
    color = (255,255,255)
    color_light = (170,170,170)
    color_dark = (100,100,100)
    
    # variable for width and heigth
    width = screen.get_width()
    height = screen.get_height()
    
    #sets font
    font = pygame.font.SysFont("corbel", 35)
    
    #whats written on the button
    quit_text = font.render("Quit", True, color)
    start_text = font.render("Start", True, color)

     # Button sizes
    button_width = 140
    button_height = 40

    # Button positions
    quit_x = width / 3
    quit_y = height / 2
    start_x = width / 3
    start_y = height / 2.5

    while True:
        # what happens when the buttons pushed
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()

            if ev.type == pygame.MOUSEBUTTONDOWN:

                if quit_x <= mouse[0] <= quit_x + button_width and quit_y <= mouse[1] <= quit_y + button_height:
                    pygame.quit()
                    sys.exit()

                # Start button click
                if start_x <= mouse[0] <= start_x + button_width and start_y <= mouse[1] <= start_y + button_height:
                    print("Start game!")  # Skal erstattes med metode, der starter spillet

        # random screen color
        screen.fill((60,25,60))
    
        # stores mouse x,y position
        mouse = pygame.mouse.get_pos()

        if quit_x <= mouse[0] <= quit_x + button_width and quit_y <= mouse[1] <= quit_y + button_height:
            pygame.draw.rect(screen, color_light, [quit_x, quit_y, button_width, button_height])
        else:
            pygame.draw.rect(screen, color_dark, [quit_x, quit_y, button_width, button_height])

        # 🔹 HOVER CHECK FOR START-KNAPPEN
        if start_x <= mouse[0] <= start_x + button_width and start_y <= mouse[1] <= start_y + button_height:
            pygame.draw.rect(screen, color_light, [start_x, start_y, button_width, button_height])
        else:
            pygame.draw.rect(screen, color_dark, [start_x, start_y, button_width, button_height])

        #puts text onto button
        screen.blit(quit_text, (quit_x + 40, quit_y + 10))
        screen.blit(start_text, (start_x + 35, start_y + 10))
        #updates the game
        pygame.display.update()


