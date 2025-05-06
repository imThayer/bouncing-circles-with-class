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
            if event.key == pygame.K_RETURN:
                balls.append(ball.Ball(ball_info[0], rand_color(), [rnd(0,SCREEN_WIDTH), rnd(0,SCREEN_HEIGHT)], rnd(1,50))) # adds instance of ball class
                text[2].update_text("Ball Counter: "+ str(len(balls)))
            if event.key == pygame.K_BACKSPACE:
                if len(balls) > 0:
                    balls.pop(0)
                    text[2].update_text("Ball Counter: "+str(len(balls)))
            if event.key == pygame.K_r:
                balls.clear()
                text[2].update_text("Ball Counter: "+str(len(balls)))

            if event.key == pygame.K_LSHIFT:
                for i in range(10):
                    balls.append(ball.Ball(ball_info[0], rand_color(), [rnd(0,SCREEN_WIDTH), rnd(0,SCREEN_HEIGHT)], rnd(1,50))) # adds instance of ball class
                text[2].update_text("Ball Counter: "+str(len(balls)))
            if event.key == pygame.K_RSHIFT:
                for i in range(100):
                    balls.append(ball.Ball(ball_info[0], rand_color(), [rnd(0,SCREEN_WIDTH), rnd(0,SCREEN_HEIGHT)], rnd(1,50))) # adds instance of ball class
                text[2].update_text("Ball Counter: "+str(len(balls)))

            if event.key == pygame.K_TAB:
                for i in range(10000):
                    balls.append(ball.Ball(ball_info[0], rand_color(), [rnd(0,SCREEN_WIDTH), rnd(0,SCREEN_HEIGHT)], rnd(1,50))) # adds instance of ball class
                text[2].update_text("Ball Counter: "+str(len(balls)))
            if event.key == pygame.K_SPACE:
                night = not night

                if night:
                    for t in text:
                        t.change_font_color(WHITE)
                else:
                    for t in text:
                        t.change_font_color(BLACK)

            if event.key == pygame.K_UP:
                for b in balls:
                    b.y_vel = -(abs(b.y_vel))

            if event.key == pygame.K_DOWN:
                for b in balls:
                    b.y_vel = abs(b.y_vel)

            if event.key == pygame.K_RIGHT:
                for b in balls:
                    b.x_vel = abs(b.x_vel)


            if event.key == pygame.K_LEFT:
                for b in balls:
                    b.x_vel = -(abs(b.x_vel))


                

    

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        balls.append(ball.Ball(ball_info[0], rand_color(), [rnd(0,SCREEN_WIDTH), rnd(0,SCREEN_HEIGHT)], rnd(1,50))) # adds instance of ball class
        text[2].update_text("Ball Counter: "+ str(len(balls)))
    if keys[pygame.K_s]:
        if len(balls) > 0:
                    balls.pop(0)
                    text[2].update_text("Ball Counter: "+str(len(balls)))

    
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
    instructions1 = boxes.Text_box(window, 10, 10, 50, 50, "Press ENTER: to add ball Press BACKSPACE: to delete a ball", BLACK)
    instructions2 = boxes.Text_box(window, 10, 30, 50, 50, "Press R: to delete all balls", BLACK)
    nightmode_text = boxes.Text_box(window, 10, 50, 50, 50, "Press SPACEBAR: to switch between day and night mode", BLACK)
    counter = boxes.Text_box(window, 10, SCREEN_HEIGHT - 50, 50, 50, "Ball Counter: "+ str(len(balls)), BLACK)
    texts = [instructions1, nightmode_text,counter, instructions2]
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

