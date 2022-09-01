import random
import pygame as pg
import sys

# Startup for pygame
pg.init()
clock = pg.time.Clock()
# Game display settings
screen = pg.display.set_mode((800, 400))
pg.display.set_caption("Plaid on Plaid")

# Load assets
background = pg.Surface(screen.get_size())

red_surface = pg.Surface((screen.get_size()[0] // 1.3, screen.get_size()[1] // 4))
red_rect = red_surface.get_rect(topleft=(random.randint(0, screen.get_size()[0]),10))
red_surface.fill("DarkRed")

green_surface = pg.Surface((screen.get_size()[0] // 1.9, screen.get_size()[1] // 4))
green_rect = green_surface.get_rect(midleft=(random.randint(0, screen.get_size()[0]),screen.get_size()[1] // 2))
green_surface.fill("DarkGreen")

blue_surface = pg.Surface((screen.get_size()[0] // 2.4, screen.get_size()[1] // 4))
blue_rect = blue_surface.get_rect(bottomleft=(random.randint(0, screen.get_size()[0]),screen.get_size()[1] - 10))
blue_surface.fill("DarkBlue")

lblue_surface = pg.Surface((screen.get_size()[0] // 40, 300))
lblue_rect = lblue_surface.get_rect(midtop=(random.randint(0, screen.get_size()[0]),random.randint(0, screen.get_size()[1])))
lblue_surface.fill("LightBlue")

# Main Game Loop
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()

    # Mind the layer order!!
    screen.blit(background, (0, 0))
    screen.blit(red_surface, red_rect)
    screen.blit(blue_surface, blue_rect)
    screen.blit(green_surface, green_rect)
    screen.blit(lblue_surface, lblue_rect)

    # Movement
    red_rect.left -= 3
    blue_rect.left -= 4
    green_rect.left -= 3
    lblue_rect.bottom += 2

    # Conditionals
    if red_rect.right < 0:
        red_rect.left = screen.get_size()[0]
    if blue_rect.right < 0:
        blue_rect.left = screen.get_size()[0]
    if green_rect.right < 0:
        green_rect.left = screen.get_size()[0]
    if lblue_rect.top > screen.get_size()[1]:
        lblue_rect.bottom = 0
        lblue_rect.centerx = random.randint(0, screen.get_size()[0])

    pg.display.update()

    # Framerate
    clock.tick(60)