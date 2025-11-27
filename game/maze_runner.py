#!/usr/bin/env python3
# Maze Runner & Catcher Game - By Shravani & Medha
# Fully working version with character sprites, items, HOD mechanics

import pygame
import sys
import random
from pathlib import Path

from game.config import *
from game.entities.girl import Girl
from game.entities.boy import Boy
from game.entities.hod import HOD
from game.pathfinding.bfs import bfs
from game.pathfinding.astar import astar
from game.ui.hud import draw_hud
from game.ui.title_screen import show_title

# Assets folder
ASSETS_DIR = Path(__file__).parent / "assets"

# Load character images
GIRL_IMG = pygame.image.load(str(ASSETS_DIR / "girl.png")).convert_alpha()
BOY_IMG = pygame.image.load(str(ASSETS_DIR / "boy.png")).convert_alpha()
HOD_IMG = pygame.image.load(str(ASSETS_DIR / "hod.png")).convert_alpha()
# Optional item image
try:
    ITEM_IMG = pygame.image.load(str(ASSETS_DIR / "item.png")).convert_alpha()
except Exception:
    ITEM_IMG = None

# Handcrafted campus map (1 = wall, 0 = floor)
RAW_MAP = [
    "111111111111111111111",
    "100000000010000000001",
    "101111011010111101101",
    "100001010000100001001",
    "111101011110101111101",
    "100100000000001000001",
    "101101111011111011101",
    "100001000010000000001",
    "111101011010111101101",
    "100001010000100001001",
    "101111011110111101101",
    "100000000010000000001",
    "111101011011110111101",
    "100001000000000100001",
    "101111011111110111101",
    "100000000000000000001",
    "111111111111111111111",
]

GAME_MAP = [[int(ch) for ch in row] for row in RAW_MAP]

def in_bounds(x, y):
    return 0 <= x < GRID_W and 0 <= y < GRID_H

def passable(x, y):
    return GAME_MAP[y][x] == 0

def neighbors(x, y):
    for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
        nx, ny = x+dx, y+dy
        if in_bounds(nx, ny) and passable(nx, ny):
            yield (nx, ny)

def draw_map(surface):
    surface.fill(PATH_COLOR)
    for y in range(GRID_H):
        for x in range(GRID_W):
            rect = pygame.Rect(x*TILE, y*TILE, TILE, TILE)
            if GAME_MAP[y][x] == 1:
                pygame.draw.rect(surface, WALL_COLOR, rect)
            else:
                pygame.draw.rect(surface, PATH_COLOR, rect)
                pygame.draw.rect(surface, (30,30,30), rect, 1)

def make_items():
    items = set()
    for y in range(GRID_H):
        for x in range(GRID_W):
            if GAME_MAP[y][x] == 0 and random.random() < 0.08:
                items.add((x,y))
    return items

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
    pygame.display.set_caption("Maze Runner & Catcher - Maze Runner By Shravani & Medha")
    clock = pygame.time.Clock()

    # Show title screen
    show_title(screen)

    # Start positions
    player_start = (2, 2)
    boy_start = (GRID_W-3, GRID_H-3)
    hod_start = (GRID_W//2, GRID_H//2)

    # Initialize characters
    girl = Girl(*player_start, GIRL_IMG)
    boy = Boy(*boy_start, BOY_IMG)
    hod = HOD(*hod_start, HOD_IMG)

    # Generate items
    items = make_items()
    items.discard((girl.x, girl.y))
    items.discard((boy.x, boy.y))
    items.discard((hod.x, hod.y))

    game_over = False
    win = False
    message_timer = 0

    while True:
        dt = clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and (game_over or win):
                return main()  # restart

        keys = pygame.key.get_pressed()

        if not game_over and not win:
            girl.update(keys, in_bounds, passable)
            boy.update((girl.x, girl.y), neighbors)
            hod.update()

            # Pickup items
            if (girl.x, girl.y) in items:
                items.remove((girl.x, girl.y))
                girl.score += 10

            # HOD rescue
            if (girl.x, girl.y) == (hod.x, hod.y) and hod.rescue_cooldown == 0:
                boy.freeze(frames=FPS*4)
                girl.boost_timer = FPS*3
                girl.score += 50
                hod.rescue_cooldown = FPS*6
                message_timer = FPS*2

            # Collision with boy
            if (girl.x, girl.y) == (boy.x, boy.y) and boy.freeze_timer == 0:
                girl.lives -= 1
                message_timer = FPS*2
                if girl.lives <= 0:
                    game_over = True
                else:
                    girl.x, girl.y = player_start
                    girl.px, girl.py = girl.x * TILE, girl.y * TILE
                    boy.freeze(frames=FPS*2)

            if not items:
                win = True
                message_timer = FPS*3

        # Draw map and items
        draw_map(screen)
        for (ix, iy) in items:
            if ITEM_IMG:
                screen.blit(ITEM_IMG, (ix*TILE, iy*TILE))
            else:
                cx = ix*TILE + TILE//2
                cy = iy*TILE + TILE//2
                pygame.draw.circle(screen, ITEM_COLOR, (cx, cy), 4)

        # Draw characters
        hod.draw(screen)
        if getattr(boy, "path", None):
            for (px, py) in boy.path[:12]:
                rect = pygame.Rect(px*TILE+TILE//4, py*TILE+TILE//4, TILE//2, TILE//2)
                pygame.draw.rect(screen, (100,100,140), rect)
        boy.draw(screen)
        girl.draw(screen)

        # HUD
        draw_hud(screen, girl, hod, boy)

        # Message overlay
        if message_timer > 0:
            message_timer -= 1
            if game_over:
                msg = "Aww Pookie... No worries lets play"
            elif win:
                msg = "Hoorah Pookie. Click Your Name First Letter To start new game"
            else:  # lost 1 life
                msg = "Hey, don't worry! You still have chances to continue. Come on Pookie! I am made by Shravani & Medha."
            font = pygame.font.SysFont(None, 22)
            surf = font.render(msg, True, WHITE)
            screen.blit(surf, (SCREEN_W//2 - surf.get_width()//2, SCREEN_H//2 - 10))

        pygame.display.flip()


if __name__ == "__main__":
    main()
