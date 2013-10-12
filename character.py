import pygame, glob, animation
from animation import *

# Author: Alexandre Conrado
# Classe que cria personagens
class Character:
    nickname = ""
    name = ""
    width = 0
    height = 0
    weight = 0
    pos_x = 0
    pos_y = 0
    surface = False
    color = (0,0,0)
    target = False
    image_path = False
    image = False
    sprite = False

    #Area ativa do personagem
    rect = False

    # Propriedades fisicas
    gravity = False
    land = True

    cur_move = "walk"
    # Dict com os status dos movimentos
    moves = {
        "walk" : {
                    "cur_frame" : 0,
                    "end_frame" : 0,
                },
        "jump" : {
                    "cur_frame" : 0,
                    "end_frame" : 0,
                }
    }


    # Acao do personagem
    action = "stop"
    jumping = False
    has_anim = False # Define se tera ou nao animacao

    def __init__(self, nickname, dimension, position, weight, surface, color=(0,0,0), has_anim=True):
        self.nickname = nickname
        self.width = dimension[0]
        self.height = dimension[1]
        self.weight = weight
        self.pos_x = position[0]
        self.pos_y = position[1]
        self.surface = surface
        self.color = color
        self.has_anim = has_anim

    def get_rectangle(self):
        self.rect = pygame.draw.rect(self.surface, self.color, [self.pos_x, self.pos_y, self.width, self.height])
        if self.image:
            # Corrige o tamanho do retangulo
            img_rect = self.image.get_rect()
            self.rect.width = img_rect.width * 1.30
            self.rect.height = img_rect.height * 1.30
        return self.rect


    def draw(self):
        rect = self.get_rectangle()

        if self.has_anim:
            anim  = Animation(self)
            anim.set_move_type(self.cur_move)
            anim.sp_number = self.moves[self.cur_move]["cur_frame"]
            image_data  = anim.get_current_image() 
            if len(image_data) == 0:
                #print ("Nao ha dados de imagem.")
                result = rect
            else:
                # informa o total de frames
                self.moves[self.cur_move]["end_frame"] = (anim.total_frames - 1)

                #print ("Ha dados de imagem.")
                self.image = image_data[0]
                self.surface.blit(self.image, image_data[1])
                result = image_data[1]
        else:
            result  = rect
        
        return result

    def update_move(self):
        #print ("END: {0}".format(self.moves[self.cur_move]["end_frame"]))

        if self.moves[self.cur_move]["cur_frame"] == self.moves[self.cur_move]["end_frame"]:
            self.moves[self.cur_move]["cur_frame"] = 0
        else:
            self.moves[self.cur_move]["cur_frame"] += 1

    # Caminha para alguma direcao
    # where => "left" ou "right"
    # value => valor em px
    def walk(self, where, value):
        self.cur_move =  "walk"
        if where == False:
            self.pos_x = self.pos_x
        elif where == "right":
            self.update_move()
            self.pos_x += value
        elif where == "left":
            self.update_move()
            self.pos_x -= value

    # Pula até uma altura especifica
    def jump(self):
        if self.land == True:
            self.gravity = -50