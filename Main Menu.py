# Necessary imports
import pygame
from pygame import mixer
import sys
import subprocess

# Initializing modules
pygame.init()
mixer.init()

# Colors I like to use
org = (253, 123, 7)
blk = (0, 0, 0)
wit = (255, 255, 255)
gry = (128, 128, 128)
blu = (0, 0, 255)
cya = (0, 255, 255)

# Configuring the window
wid = 960
hig = 540
win = pygame.display.set_mode((wid, hig))
bg = pygame.image.load("BG.png")
win.blit(bg, (0, 0))
pygame.display.set_caption("Sudoku - Overhauled!")
icn = pygame.image.load("heart.png")
pygame.display.set_icon(icn)
pygame.display.flip()

# Welcome Text
pygame.draw.rect(win, blk, [0, 0, wid, 100], 0)
font1 = pygame.font.SysFont('BlackChancery', 75)
text = font1.render("Welcome To Sudoku", True, cya)
tr1 = text.get_rect()
tr1.center = (wid/2, 50)
win.blit(text, tr1)

# Background music
mixer.music.load("LG.mp3")
mixer.music.set_volume(0.5)
mixer.music.play(-1)

# Toggle Music
paused = False

def pause():
    global paused
    mixer.music.pause()
    paused = True


pause()

def unpause():
    global paused
    mixer.music.unpause()
    paused = False


unpause()

# Infinite while loop to actually run the game
while True:
    for event in pygame.event.get():

# Mouse detection
        mouse = pygame.mouse.get_pos()

# X button functionality
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

# What to do when hovering over buttons
        if event.type == pygame.MOUSEMOTION:
            if 330 <= mouse[0] <= 630 and 145 <= mouse[1] <= 215:
                pygame.draw.rect(win, blk, [330, 145, 300, 70], 0, 20)
                pygame.draw.rect(win, wit, [335, 150, 290, 60], 5, 20)
                font = pygame.font.SysFont('AnonymousPro', 25)
                text2 = font.render("Start Game", True, cya)
                tr2 = text2.get_rect()
                tr2.center = (480, 180)
                win.blit(text2, tr2)

            elif 330 <= mouse[0] <= 630 and 270 <= mouse[1] <= 340:
                pygame.draw.rect(win, blk, [330, 270, 300, 70], 0, 20)
                pygame.draw.rect(win, wit, [335, 275, 290, 60], 5, 20)
                font = pygame.font.SysFont('AnonymousPro', 25)
                text3 = font.render("Credits", True, cya)
                tr3 = text3.get_rect()
                tr3.center = (480, 305)
                win.blit(text3, tr3)

            elif 330 <= mouse[0] <= 630 and 395 <= mouse[1] <= 465:
                pygame.draw.rect(win, blk, [330, 395, 300, 70], 0, 20)
                pygame.draw.rect(win, wit, [335, 400, 290, 60], 5, 20)
                font = pygame.font.SysFont('AnonymousPro', 25)
                text4 = font.render("Quit Game", True, cya)
                tr4 = text4.get_rect()
                tr4.center = (480, 430)
                win.blit(text4, tr4)

            elif 675 <= mouse[0] <= 945 and 230 <= mouse[1] <= 310:
                pygame.draw.rect(win, blk, [675, 230, 270, 80], 0, 20)
                pygame.draw.rect(win, wit, [680, 235, 260, 70], 5, 20)
                font = pygame.font.SysFont('AnonymousPro', 25)
                txt = font.render("Mute/Unmute Music", True, cya)
                tx = txt.get_rect()
                tx.center = (810, 270)
                win.blit(txt, tx)

            else:
                # Buttons to press
                pygame.draw.rect(win, gry, [330, 145, 300, 70], 0, 20)
                pygame.draw.rect(win, blk, [335, 150, 290, 60], 5, 20)
                pygame.draw.rect(win, gry, [330, 270, 300, 70], 0, 20)
                pygame.draw.rect(win, blk, [335, 275, 290, 60], 5, 20)
                pygame.draw.rect(win, gry, [330, 395, 300, 70], 0, 20)
                pygame.draw.rect(win, blk, [335, 400, 290, 60], 5, 20)
                pygame.draw.rect(win, gry, [675, 230, 270, 80], 0, 20)
                pygame.draw.rect(win, blk, [680, 235, 260, 70], 5, 20)

                # Start Game Button
                font = pygame.font.SysFont('AnonymousPro', 25)
                text2 = font.render("Start Game", True, wit)
                tr2 = text2.get_rect()
                tr2.center = (480, 180)
                win.blit(text2, tr2)

                # Credits Button
                text3 = font.render("Credits", True, wit)
                tr3 = text3.get_rect()
                tr3.center = (480, 305)
                win.blit(text3, tr3)

                # Quit Game Button
                text4 = font.render("Quit Game", True, wit)
                tr4 = text4.get_rect()
                tr4.center = (480, 430)
                win.blit(text4, tr4)

                # Mute Sound Button
                txt = font.render("Mute/Unmute Music", True, wit)
                tx = txt.get_rect()
                tx.center = (810, 270)
                win.blit(txt, tx)

# What to do when pressing the buttons
        if event.type == pygame.MOUSEBUTTONDOWN:

# Start Game button
            if 330 <= mouse[0] <= 630 and 145 <= mouse[1] <= 215:
                subprocess.call(["python", "test2.py"])
                pygame.quit()
                quit()

# Credits Button
            if 330 <= mouse[0] <= 630 and 270 <= mouse[1] <= 340:
                a = pygame.draw.rect(win, blk, [20, 125, 300, 130], 0, 20)
                b = pygame.draw.rect(win, wit, [30, 135, 280, 110], 5, 20)
                font = pygame.font.SysFont('AnonymousPro', 20)
                cred = font.render("Made by:-", True, cya)
                cred_ = cred.get_rect()
                cred_.center = (100, 160)
                win.blit(cred, cred_)
                cre = font.render("> Mohan 9B", True, cya)
                cre_ = cred.get_rect()
                cre_.center = (100, 185)
                win.blit(cre, cre_)
                cr = font.render("> Erica 9B", True, cya)
                cr_ = cred.get_rect()
                cr_.center = (100, 210)
                win.blit(cr, cr_)

# Quit button
            if 330 <= mouse[0] <= 630 and 395 <= mouse[1] <= 465:
                pygame.quit()
                quit()

# Pause/Unpause Music button
            if 675 <= mouse[0] <= 945 and 220 <= mouse[1] <= 320:
                if paused == False:
                    pause()
                elif paused == True:
                    unpause()

    pygame.display.update()
