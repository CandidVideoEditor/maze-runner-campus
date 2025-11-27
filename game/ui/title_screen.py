# Simple title screen placeholder (blocking)
import pygame
from game.config import WHITE

def show_title(screen):
    screen.fill((10,10,30))
    font = pygame.font.SysFont(None, 48)
    t = font.render("Maze Runner & Catcher", True, WHITE)
    screen.blit(t, (screen.get_width()//2 - t.get_width()//2, 120))
    small = pygame.font.SysFont(None, 24)
    s = small.render("Press any key to start", True, WHITE)
    screen.blit(s, (screen.get_width()//2 - s.get_width()//2, 200))
    pygame.display.flip()
    # wait for key
    waiting = True
    while waiting:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit
            if e.type == pygame.KEYDOWN:
                waiting = False
