import pygame
from pygame.locals import *
from sys import exit
from random import randint, choice
from math import *

from invaders import Alien
from ship import Ship
from sciana import Wall

score = 0 
klasy = open('alien.txt').read()
nlev = open('nlev.txt').read()
def delete_bad(G):
   for s in G.sprites():
      if s.y < 0 or s.y > 480:
         G.remove(s)
         
pygame.init()
screen2 = pygame.display.set_mode((640, 480))
screen = pygame.image.load('2.jpg').convert_alpha()

pygame.mixer.init()
boom_sound = pygame.mixer.Sound("boom.wav")
winn = pygame.mixer.Sound("win.wav")
sound = pygame.mixer.Sound("game.wav")
gameov = pygame.mixer.Sound("gameover.wav")

gameover = pygame.image.load('lose.jpg').convert_alpha()
win = pygame.image.load('win.jpg').convert_alpha()

font1 = pygame.font.SysFont("verdana",15)
font2 = pygame.font.SysFont("tahoma",72)
font3 = pygame.font.SysFont("verdana",32)

rockets = pygame.sprite.Group()
bombs = pygame.sprite.Group()

wall = []
for i in range(3):
   wall.append(Wall((randint(0,600),randint(350,390)),randint(30,60)))
walls = pygame.sprite.Group(wall)

aliens = []
for i in range(10):
   for j in range(3):
      aliens.append(Alien((50 * i, 40 + 30 * j), bombs ))
exec(klasy)
   
my_ship = Ship( (300,470), rockets)
invaders = pygame.sprite.Group(aliens)
clock = pygame.time.Clock()

boom = False   
lev = 1
nlev = 0
p = ((0,0))

while True:
   if my_ship.life > 0:
      sound.set_volume(0.5)
      sound.play()
   clock.tick(30)
   for event in pygame.event.get():
      if event.type == QUIT:
         pygame.quit()
         exit()
      if event.type == MOUSEBUTTONDOWN:
         invaders.empty()
         pygame.time.wait(60)
      
   pressed_keys = pygame.key.get_pressed()
   my_ship.drive(pressed_keys)
   if my_ship.life <= 0: #przegrana
      tekst2 = font2.render("YOU LOSE!!", True, (255,255,255) )          
      gameover.blit( tekst2, (130,150) )
      screen2.blit(gameover, (0,0))
      gameov.play()
      pygame.display.update()
   else:
      for wall in walls: #oslona
         if pygame.sprite.spritecollide(wall,bombs,True):
            wall.delete()
         if pygame.sprite.spritecollide(wall,rockets,True):
            wall.delete()
         if wall.delt == 1:
            wall.remove(walls)
      for i in bombs: #jak uderzy mnie
         if pygame.sprite.collide_rect(i,my_ship):
            boom = True
            p = my_ship.x-13,460
            i.remove(bombs)
            my_ship.hit()
            score -= 20 * lev
            sound.stop()
            boom_sound.play()
      for i in invaders: 
         if i.y > 460:
            my_ship.life = 0
            score = 0
         if pygame.sprite.collide_rect(i,my_ship):
            my_ship.life = 0
            score = 0
         if pygame.sprite.spritecollide(i, walls, True):
            i.remove(invaders)
            boom = True
            p = i.x-13, i.y-13
            score -= 10 * lev
            sound.stop()
            boom_sound.play()
         if pygame.sprite.spritecollide(i, rockets, True):
            i.remove(invaders)
            boom = True
            p = i.x-13, i.y-13
            score += 20 * lev
            sound.stop()
            boom_sound.play()

      #jesli zabilismy wszystkich
      if len(invaders) == 0: 
         boom = True
         lev += 1
         bombs.empty()
         walls.empty()
         rockets.empty()
         pygame.time.wait(60)

         if lev == 4:
            sound.stop()
            while True:
               tekst5 = font3.render("MAY THE FORCE BE WITH YOU", True, (255,255,255) )
               win.blit( tekst5, (80,150) )
               tekst6 = font1.render("YOUR SCORE: " + str(score), True, (255,255,255) )
               win.blit( tekst6, (280,250) )
               screen2.blit(win, (0,0))
               pygame.display.update()
               winn.play()
         
         #new level
         nlev = open('nlev.txt').read()
         exec(nlev)
         
       
      screen = pygame.image.load('2.jpg').convert_alpha()

      walls.update()
      walls.draw(screen)
      invaders.update()
      my_ship.update()
      invaders.draw(screen)
      my_ship.draw(screen)  
      bombs.update()
      rockets.update()
      bombs.draw(screen)
      rockets.draw(screen)
      
      if boom:
            boom = False
            clock.tick(20)
            w = []
            n = ["exp" + str(i) + ".png" for i in range(0,8)]
            for i in n:
               w.append(pygame.image.load(i).convert_alpha())
            for i in range(8):
               screen.blit(w[i], p)
               pygame.display.update()
            
      
      tekst1 = font1.render("Score: " + str(score), True, (255,255,255) )          
      screen.blit( tekst1, (5,5) )
      tekst3 = font1.render("Live: " + str(my_ship.life), True, (255,255,255) )          
      screen.blit( tekst3, (150,5) )
      screen2.blit(screen, (0,0))
      pygame.display.update()
