import pygame
from game.config import TILE, ENEMY_COLOR, BLACK
from game.pathfinding.bfs import bfs

class Boy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.px = x * TILE
        self.py = y * TILE
        self.speed = 4
        self.path = []
        self.tick = 0
        self.freeze_timer = 0
        self.chase_delay = 10  # frames between recalculations

    def move_towards(self, tx, ty):
        target_px = tx * TILE
        target_py = ty * TILE
        dx = target_px - self.px
        dy = target_py - self.py
        if dx == 0 and dy == 0:
            self.x, self.y = tx, ty
            return True
        dist = (dx*dx + dy*dy) ** 0.5
        step = self.speed
        if dist <= step:
            self.px, self.py = target_px, target_py
            self.x, self.y = tx, ty
            return True
        self.px += step * (dx / dist)
        self.py += step * (dy / dist)
        return False

    def update(self, player_pos, neighbors_fn):
        if self.freeze_timer > 0:
            self.freeze_timer -= 1
            return
        self.tick += 1
        if self.tick % self.chase_delay == 0 or not self.path:
            start = (self.x, self.y)
            goal = player_pos
            self.path = bfs(start, goal, neighbors_fn)
        if self.path:
            next_tile = self.path.pop(0)
            arrived = self.move_towards(*next_tile)
            if not arrived:
                self.path.insert(0, next_tile)

    def draw(self, surf):
        r = pygame.Rect(self.px+2, self.py+2, TILE-4, TILE-4)
        pygame.draw.rect(surf, ENEMY_COLOR, r)
        pygame.draw.line(surf, BLACK, (self.px+6, self.py+10), (self.px+10, self.py+8), 2)
        pygame.draw.line(surf, BLACK, (self.px+TILE-6, self.py+10), (self.px+TILE-10, self.py+8), 2)

    def freeze(self, frames):
        self.freeze_timer = frames
        self.path = []
