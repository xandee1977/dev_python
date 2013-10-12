# Import a library of functions called 'pygame'
import pygame, os, sys
import gutils
import character
import animation

from math import pi
from gutils import *
from character import *
from animation import *

# Initialize the game engine
pygame.init()

char_x = 25
char_y = 250
char_width = 15
char_height = 15

char = Character("mario", (char_width, char_height), (char_x, char_y), screen, "\\Users\\Alexandre\\Projetos\\game\\data\\images\\")
anim = Animation(char)
image_data  = anim.get_current_image()