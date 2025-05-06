import classes_and_objects.shapes as shapes
import pygame_config as cfig
from random import randint as r

class Ball(shapes.Circ):

    def __init__(self, window, color, center_coords, radius, width=0):
        super().__init__(window,color,center_coords, radius, width)\
        
        self.x_vel = r(1,10)
        self.y_vel = r(1,10)

    def check_collisons(self):
        if self.x - self.r < 0:
            self.change_x_pos(self.r)
            self.x_vel = r(1,10)
        if self.x + self.r > cfig.SCREEN_WIDTH:
            self.change_x_pos(cfig.SCREEN_WIDTH - self.r)
            self.x_vel = r(-10,-1)
        if self.y - self.r < 0:
            self.change_y_pos(self.r)
            self.y_vel = r(1,10)
        if self.y + self.r > cfig.SCREEN_HEIGHT:
            self.change_y_pos(cfig.SCREEN_HEIGHT - self.r)
            self.y_vel = r(-10,-1)

    def move(self):
        self.change_pos(self.x + self.x_vel, self.y + self.y_vel)
        self.check_collisons()

        

        
