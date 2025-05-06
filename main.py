import pygame, sys
import random
import math
import os
from os.path import join
from random import randint as rnd
from pygame.time import delay as slp

from colors import *
from pygame_config import *
import classes_and_objects.shapes as shapes
import classes_and_objects.boxes as boxes
import ball

def init_game():
    """Initiates Pygame, Pygame.font, and sets the Screen window and caption"""
    pygame.init()
    pygame.font.init()
    pygame.display.set_caption(PYGAME_CAPTION) # Window Caption
    # pygame.display.set_icon(ICON) #UNCOMMENT WHEN ICON IS DEFINED

    #Pygame Window
    window = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    return window

# Draw Function to update graphics
def draw(window,balls,text,nightmode):
    """DRAW FUNCTION | allows screen graphics to be added"""
    #BACKGROUND
    if nightmode:
        window.fill(BLACK) # 15
    else:
        window.fill(WHITE)
    

    #FOREGROUND

    for b in balls:
        b.draw()

    for t in text:
        t.draw_text()
    #UPDATE DISPLAY
    pygame.display.update()

def handle_events(balls,ball_info, night, text):
    """Handles any pygame event such as key input"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # QUIT
            return False, night
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                balls.append(ball.Ball(ball_info[0], rand_color(), [rnd(0,SCREEN_WIDTH), rnd(0,SCREEN_HEIGHT)], rnd(1,50))) # adds instance of ball class
            if event.key == pygame.K_DOWN:
                if len(balls) > 0:
                    balls.pop(0)
            if event.key == pygame.K_SPACE:
                night = not night

                if night:
                    for t in text:
                        t.change_font_color(WHITE)
                else:
                    for t in text:
                        t.change_font_color(BLACK)


                

    

    keys = pygame.key.get_pressed()

    for b in balls:
        b.move()

    return True, night



def main(): # MAIN FUNCTION
    """Main Function : main"""
    window = init_game()
    clock = pygame.time.Clock()
    # ADD ALL OBJECTS/CLASSES BELOW HERE

    ball_info = [window]
    balls = []
    instructions = boxes.Text_box(window, 10, 10, 50, 50, "Press UP: to add ball Press DOWN: to delete a ball", BLACK)
    nightmode_text = boxes.Text_box(window, 10, 30, 50, 50, "Press SPACEBAR: to switch between day and night mode", BLACK)
    texts = [instructions, nightmode_text]
    night = False
    
    # ADD ALL OBJECTS/CLASSES ABOVE HERE
    run = True
    while run: # run set to true, program runs while run is true.

        clock.tick(FPS) # FPS Tick

        run,night = handle_events(balls,ball_info, night,texts)
        

        
        draw(window,balls,texts,night) # UPDATES SCREEN

    pygame.quit()
    sys.exit()
    quit()
# ADD CLASSES HERE



# ADD CLASSES ABOVE
if __name__ == "__main__": 
    main()

