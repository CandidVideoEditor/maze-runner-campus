from game.config import TILE, HOD_COLOR

import pygame

class HOD:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.px = x * TILE
        self.py = y * TILE
        self.rescue_cooldown = 0

    def update(self):
        if self.rescue_cooldown > 0:
            self.rescue_cooldown -= 1

    def draw(self, surf):
        desk = pygame.Rect(self.px+2, self.py+TILE//2, TILE-4, TILE//3)
        pygame.draw.rect(surf, (120,90,60), desk)
        pygame.draw.circle(surf, HOD_COLOR, (int(self.px+TILE/2), int(self.py+TILE*0.35)), TILE//4)
