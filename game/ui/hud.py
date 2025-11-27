from game.config import WHITE, FPS
import pygame

def draw_hud(surface, player, hod, boy):
    font = pygame.font.SysFont(None, 22)
    txt = f"Score: {player.score}   Lives: {player.lives}"
    surface.blit(font.render(txt, True, WHITE), (8, 8))
    if hod.rescue_cooldown > 0:
        surface.blit(font.render(f"HOD cooldown: {hod.rescue_cooldown//FPS}s", True, WHITE), (8, 28))
    if boy.freeze_timer > 0:
        surface.blit(font.render(f"Boy frozen: {boy.freeze_timer//FPS}s", True, WHITE), (surface.get_width()-180, 8))
