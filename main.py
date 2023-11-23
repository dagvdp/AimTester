import random
import pygame
import math
from pygame.locals import *
pygame.init()
from configs import *

def distance_points(x1, x2, y1, y2):
    a = (y2 - y1)**2
    b = (x2 - x1)**2
    return math.sqrt(a+b)

screen1 = Screen()
win1 = pygame.display.set_mode([screen1.width, screen1.height])

pygame.display.set_caption(screen1.title)
font = Font.monospace

time = 3600
time_text = font.render(F"Time Left: {int(time/60)}", True, "green")
time_rect = time_text.get_rect(center=(screen1.width/5, screen1.height/16))

score = 0
score_text = font.render(F"Score: {score}", True, "green")
score_rect = score_text.get_rect(center=(screen1.width*0.85, screen1.height/16))

exit_button = font.render(F"Exit", True, "black", "red")
exit_rect = score_text.get_rect(center=(screen1.width/2, screen1.height*0.75))
exit_coords = [exit_rect[0], exit_rect[0] + exit_rect[2], exit_rect[1], exit_rect[3] + exit_rect[1]]

vel = 5
x = random.randint(0, screen1.width)
y = random.randint(0, screen1.height)
clock = pygame.time.Clock()
run = True

while run:
    dt = clock.tick(60)
    #events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == MOUSEBUTTONDOWN and distance_points(mouse_pos[0], x, mouse_pos[1], y) < 30:
            if event.button == 1:
                score += 1
                score_text = font.render(F"Score: {score}", True, "green")
                x = random.randint(30, screen1.width - 30)
                y = random.randint(30, screen1.height - 30)
        if event.type == MOUSEBUTTONDOWN and mouse_pos[0] in range(exit_coords[0], exit_coords[1]) and mouse_pos[1] in range(exit_coords[2], exit_coords[3]) and time <=0:
            if event.button == 1:
                run = False
                
    keys = pygame.key.get_pressed()
    mouse_pos = pygame.mouse.get_pos()
    time -= 1
    
    if time > 0:
        time_text = font.render(F"Time Left: {int(time/60)}", True, "green")
        win1.fill("black")
        win1.blit(time_text, time_rect)
        win1.blit(score_text, score_rect)
        pygame.draw.circle(win1, "white", (x, y), 30)

    else:
        win1.fill("black")
        score_text = font.render(F"Final Score: {score}", True, "green")
        score_rect = score_text.get_rect(center=(screen1.width/2, screen1.height/2))
        win1.blit(score_text, score_rect)
        win1.blit(exit_button, exit_rect)

    pygame.display.update()

pygame.quit()
