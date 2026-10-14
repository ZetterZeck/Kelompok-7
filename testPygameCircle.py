import pygame
import numpy as np
import sys

WIDTH, HEIGHT = 1000, 750
frame_buffer = np.zeros((HEIGHT, WIDTH, 3), dtype=np.uint8)

pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Minggu 1: Lingkaran NumPy")

def set_pixel(x, y, color):
    if 0 <= x < WIDTH and 0 <= y < HEIGHT:
        frame_buffer[y, x] = color

def draw_circle(cx, cy, radius, color):
    x = radius
    y = 0
    p = 1 - radius

    while x >= y:
        set_pixel(cx + x, cy + y, color)
        set_pixel(cx - x, cy + y, color)
        set_pixel(cx + x, cy - y, color)
        set_pixel(cx - x, cy - y, color)
        set_pixel(cx + y, cy + x, color)
        set_pixel(cx - y, cy + x, color)
        set_pixel(cx + y, cy - x, color)
        set_pixel(cx - y, cy - x, color)

        y += 1
        if p <= 0:
            p = p + 2 * y + 1
        else:
            x -= 1
            p = p + 2 * y - 2 * x + 1

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    frame_buffer.fill(0)
    
    draw_circle(WIDTH // 2, HEIGHT // 2, 200, [255, 255, 0])
    
    surf = pygame.surfarray.make_surface(np.transpose(frame_buffer, (1, 0, 2)))
    window.blit(surf, (0, 0))
    pygame.display.flip()

pygame.quit()
sys.exit()