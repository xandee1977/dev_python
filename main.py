# Import a library of functions called 'pygame'
import pygame, os, sys
import gutils
import character
import animation
import physic
import scene

from math import pi
from gutils import *
from character import *
from animation import *
from physic import *
from scene import *

# Initialize the game engine
pygame.init()

# Define the colors we will use in RGB format
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)
SKY = (103, 156, 248)
 
# Set the height and width of the screen
size = [640, 480]
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Joguinho mucho-loco do Conrado")
 
#Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()

char_x = 25
char_y = 0
char_width = 15
char_height = 15
char_weight = 25 # Peso do personagem

mario = Character("mario", (char_width, char_height), (char_x, char_y), char_weight, screen, RED, True)

# Instancia a classe de fisica, adicionando o mario
phys = Physic([mario])
scene = Scene(screen)


target = False
# Posicao da colisao da queda
pos_drop_collid = False

while not done:
    # This limits the while loop to a max of 10 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(20)
    
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop
        elif event.type == pygame.KEYDOWN:
            key = pygame.key.get_pressed()
            if key[pygame.K_RIGHT]:
                target = "right"
            if key[pygame.K_LEFT]:
                target = "left"
            if key[pygame.K_UP]:
                mario.jump()
        elif event.type == pygame.KEYUP:
            target = False
    
    # All drawing code happens after the for loop and but
    # inside the main while done==False loop.
     
    # Clear the screen and set the screen background
    screen.fill(WHITE)
 
    # Draw a rectangle outline
    #pygame.draw.rect(screen, BLACK, [10, 10, 380, 280], 2)
    #bordas = draw_rectangle(10, 10, 380, 280, 2, BLACK, screen)

    phys.apply_gravity()

    # redesenha o personagem    
    mario.walk(target, 5)
    mario.draw()

    # Chao
    
    ball = scene.draw_ball(20, (30,30), BLUE)
    stair = scene.draw_stair(SKY, 6, (size[1] * 0.9), 40, (120,30))

    # Chão principal
    main_floor = pygame.draw.rect(screen, GREEN, [0, (size[1] * 0.9), size[0], 2])
    
    floor2 = pygame.draw.rect(screen, GREEN, [(size[0] - 300), (size[1] * 0.85), 300, 2])
    floor3 = pygame.draw.rect(screen, GREEN, [(size[0] - 150), (size[1] * 0.80), 150, 2])
    floor4 = pygame.draw.rect(screen, GREEN, [(size[0] - 100), (size[1] * 0.75), 100, 2])

    # adiciona um chao ao controle da physyca
    phys.add_floor(main_floor) # chao principal
    phys.add_floor(floor2)
    phys.add_floor(floor3)
    phys.add_floor(floor4)
    phys.add_floor(stair)

    #if mario.rect.colliderect(floor):
    #    if not pos_drop_collid:
    #        pos_drop_collid = mario.pos_y

    #if pos_drop_collid:
    #    mario.pos_y = pos_drop_collid        
    #    normal(mario, time)

    phys.apply_land()

    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    pygame.display.flip()

    #print ("Timer:", clock)