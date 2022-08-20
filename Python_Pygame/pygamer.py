import pygame
from pygame import mixer
import sys
import os


#def start_music():
    #mixer.init()
    #mixer.music.set_volume(0.1)
    #mixer.music.load("elfen_lied.wav")
    #mixer.music.play()


def start_game():
    pygame.init()
    pygame.display.set_caption('Dumb Game')
    #Icon = pygame.image.load("eric.ico")
    #pygame.display.set_icon(Icon)


def write_text(string, coordx, coordy, fontSize):
    # set the font to write with
    font = pygame.font.Font('freesansbold.ttf', fontSize)
    # (0, 0, 0) is black, to make black text
    text = font.render(string, True, (0, 0, 100))
    # get the rect of the text
    textRect = text.get_rect()
    # set the position of the text
    textRect.center = (coordx, coordy)
    # add text to window
    display.blit(text, textRect)
    # update window
    pygame.display.update()


start_game()
display = pygame.display.set_mode((1000, 1000))
clock = pygame.time.Clock()
color = (155, 0, 0)
pink = (220, 50, 130)
os.chdir(r'/home/mark/Documents/Games/Games/Python_Pygame')
image_penguin = open("penguin.png")
image = pygame.image.load(image_penguin)
image_final = pygame.transform.scale(image, (350, 350))
#start_music()
x = 325
y = 325
counter = 0
while True:
    counter += 1
    clock.tick(30) #FPS
    #print(clock.get_time())
    #print(clock.get_fps()) FPS per second
    display.fill(color)
    display.blit(image_final, (x, y))
    pygame.display.flip()
    pygame.draw.circle(display, pink, (200, 300), 100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                y -= 15
            if event.key == pygame.K_s:
                y += 15
            if event.key == pygame.K_a:
                x -= 15
            if event.key == pygame.K_d:
                x += 15
            if event.key == pygame.K_z:
                if color == (155, 0, 0):
                    color = (0, 122, 0)
                else:
                    color = (155, 0, 0)
            if event.key == pygame.K_p:
                mixer.music.pause()
            if event.key == pygame.K_u:
                mixer.music.unpause()
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
    write_text(f"seconds: {counter / 20:.0f}", 370, 80, 40)
    pygame.display.update()
