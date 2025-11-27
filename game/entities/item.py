from game.config import TILE, ITEM_COLOR
import pygame

class Item:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, surf):
        cx = self.x*TILE + TILE//2
        cy = self.y*TILE + TILE//2
        pygame.draw.circle(surf, ITEM_COLOR, (cx, cy), 4)
