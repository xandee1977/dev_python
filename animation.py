import pygame, os, glob, sys, character

# Author: Alexandre Conrado
# Classe que gerencia  as animacoes
class Animation:
    char = False
    image_path = False
    base_path = False
    image_list = []
    obj_type = "char" # Tipo de objeto
    move_type = "walk" # Tipo de movimento
    sp_number = 0 # Numero do sprite atual
    total_frames  = 0 #Numero total de frames

    def __init__(self, char):
        self.char = char
        self.base_path = self.get_base_path();
        self.move_type = char.action

    def set_move_type(self, move_type):
        self.move_type = move_type

    def get_base_path(self):
        base = os.path.dirname(character.__file__)
        result = "{0}\data\images\{1}\{2}\{3}".format(base, self.obj_type, self.char.nickname, self.move_type)
        return result

    def load_img(self):
        image_path = "{0}\{1}_*.*".format(self.base_path, self.move_type)
        result = glob.glob(image_path)
        self.total_frames = len(result)  
        return result       
    
    def get_current_image(self):
        self.image_list = self.load_img()

        if (len(self.image_list)) == 0:
            return ()
        
        image = pygame.image.load(self.image_list[self.sp_number])
        sprite = pygame.sprite.Sprite()
        sprite.image = image
        sprite.rect = self.char.get_rectangle()
 
         # Retorno (image, rectangle)
        return (sprite.image, sprite.rect)