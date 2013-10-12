import pygame, os, glob, sys, character

# Author: Alexandre Conrado
# Classe responsavel pela fisica do jogo
class Physic:
    # Aceleracao da gravidade
    gravity = 9.8
    
    # Lista os objetos
    obj_list = []
    floor_list = []
    
    # Params:
    # obj_list > lista de objetos
    def __init__(self, obj_list=[], floor_list=[]):
        # Add object to obj list
        for obj in obj_list:
            self.add_obj(obj)

        # Add floor to floor list
        for floor in floor_list:
            self.add_floor(floor)

    # Add object to physyc control
    def add_obj(self, obj):
        # Seta a gravidade do objeto
        obj.gravity = self.gravity
        self.obj_list.append(obj)

    # Add floor to physyc control
    def add_floor(self, floor):
        # Se for uma lista de objetos
        if type(floor) == type([]):
            for f in floor:
                self.floor_list.append(f)
        else:
            self.floor_list.append(floor)

    # vertor de gravidade (formula)
    def get_gravity_vector(self, obj):
        return obj.gravity * (obj.weight / 18)

    # Aplica a formula da gravidade
    def apply_gravity(self):
        for obj in self.obj_list:
            obj.pos_y = obj.pos_y + self.get_gravity_vector(obj)

    # Aplica a formula da normal a um obj
    def apply_normal(self, obj):
        obj.pos_y = obj.pos_y - self.get_gravity_vector(obj)

    # Aplica o pouso do personagem
    # quando ele encontra um chao
    def apply_land(self):
        for obj in self.obj_list:
            for floor in self.floor_list:
                if obj.rect.colliderect(floor):
                    obj.land = True
                    break
                else:
                    obj.land = False

            if obj.land == True:
                obj.gravity = 0
            else:
                obj.gravity = self.gravity