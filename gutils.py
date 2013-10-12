import pygame

def draw_rectangle(pos_x, pos_y, width, height, outline, color, surface):
    result  = pygame.draw.rect(surface, color, [pos_x, pos_y, width, height], outline)
    return result