import random
import pygame as pg
import sys

# Startup for pygame
pg.init()
clock = pg.time.Clock()
# Game display settings
screen = pg.display.set_mode((1500, 700))
pg.display.set_caption("Plaid on Plaid")

# Load assets
background = pg.Surface(screen.get_size())

num_x_strings = 2
x_surfaces = []
x_rects = []
x_speeds = []

for num in range(num_x_strings):
    x_surfaces.append(pg.Surface((random.randint(10, screen.get_size()[0]), 2)))
    x_rects.append(x_surfaces[num].get_rect(center=(random.randint(1, screen.get_size()[0]),random.randint(1, screen.get_size()[1]))))
    x_surfaces[num].fill((random.randint(0, 255),random.randint(0, 255),random.randint(0, 255),255))
    x_speeds.append(random.randint(1, 10))

# Main Game Loop
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()

    # Draw
    screen.blit(background, (0,0))
    for num in range(num_x_strings):
        # Draw
        screen.blit(x_surfaces[num], x_rects[num])

        # Move
        x_rects[num].left -= x_speeds[num]

        # Conditional
        if x_rects[num].right < 0:
            x_rects[num].left = screen.get_size()[0]

    pg.display.update()

    # Framerate
    clock.tick(60)