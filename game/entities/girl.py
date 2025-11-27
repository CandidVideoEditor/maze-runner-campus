import pygame
from game.config import TILE, PLAYER_COLOR, BLACK

class Girl:
    def __init__(self, x, y):
        # tile coords
        self.x = x
        self.y = y
        # pixel coords
        self.px = x * TILE
        self.py = y * TILE
        self.target = (x, y)
        self.speed = 8
        self.lives = 5
        self.score = 0
        self.boost_timer = 0

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

    def update(self, keys, in_bounds_fn, passable_fn):
        # speed boost handler
        if self.boost_timer > 0:
            self.boost_timer -= 1
            self.speed = 12
        else:
            self.speed = 8

        if (self.px, self.py) == (self.x * TILE, self.y * TILE):
            wanted_dir = None
            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                wanted_dir = (-1, 0)
            elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                wanted_dir = (1, 0)
            elif keys[pygame.K_UP] or keys[pygame.K_w]:
                wanted_dir = (0, -1)
            elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
                wanted_dir = (0, 1)

            if wanted_dir:
                nx, ny = self.x + wanted_dir[0], self.y + wanted_dir[1]
                if in_bounds_fn(nx, ny) and passable_fn(nx, ny):
                    self.target = (nx, ny)

        self.move_towards(*self.target)

    def draw(self, surf):
        r = pygame.Rect(self.px+4, self.py+4, TILE-8, TILE-8)
        pygame.draw.ellipse(surf, PLAYER_COLOR, r)
        eye_w = 4
        pygame.draw.circle(surf, BLACK, (int(self.px+TILE*0.35), int(self.py+TILE*0.35)), eye_w//2)
        pygame.draw.circle(surf, BLACK, (int(self.px+TILE*0.65), int(self.py+TILE*0.35)), eye_w//2)
