import pygame, os, glob, sys, character

# Author: Alexandre Conrado
# Classe que gerencia  os cenários
class Scene:
    surface = None

    def __init__(self, surface):
        self.surface = surface
    

    def draw_ball(self, radius, center=(0,0), color=(0,0,0)):
        pygame.draw.circle(self.surface, color, center, radius)


    def draw_block(self, pos_x, pos_y, width, height, color=(0,0,0)):
        result = pygame.draw.rect(
            self.surface, 
            (0,0,0), 
            [
                pos_x,
                pos_y, 
                width, 
                height
            ]
        )
        return result

    # Draw an stair
    def draw_stair(self, color, step_num=3, pos_y=480, pos_x=10, step_size=(50,50)):
        blocks = []
        cont = 0
        while (cont < step_num):
            pos_x = step_size[0] + (step_size[0] * cont)
            height = step_size[1] + (step_size[1] * cont)
            width = step_size[0]
            pos_y = pos_y - step_size[1]

            blocks.append(self.draw_block(pos_x, pos_y, width, height, color))
            cont += 1
        return blocks