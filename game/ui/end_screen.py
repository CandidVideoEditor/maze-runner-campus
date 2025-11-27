import pygame
from game.config import WHITE

def show_end(screen, msg):
    screen.fill((0,0,0))
    font = pygame.font.SysFont(None, 36)
    t = font.render(msg, True, WHITE)
    screen.blit(t, (screen.get_width()//2 - t.get_width()//2, screen.get_height()//2 - 20))
    small = pygame.font.SysFont(None, 20)
    s = small.render("Press any key to restart", True, WHITE)
    screen.blit(s, (screen.get_width()//2 - s.get_width()//2, screen.get_height()//2 + 30))
    pygame.display.flip()
    waiting = True
    while waiting:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit
            if e.type == pygame.KEYDOWN:
                waiting = False
