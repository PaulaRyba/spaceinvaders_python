import pygame
from pygame.locals import *
from sys import exit
from random import randint,choice
from math import *
from kula import Bullet

class Ship(pygame.sprite.Sprite):
  def __init__(self, pos, bullets):
    pygame.sprite.Sprite.__init__(self)
    self.x, self.y = pos
    self.dx = 0
    
    self.image = pygame.image.load('ship.png').convert_alpha()
    self.image.set_colorkey()
    self.rect = self.image.get_rect()
    self.rect.centerx = self.x
    self.rect.centery = self.y
    self.bullets = bullets
    self.wait = 0
    self.life = 8
     
  def update(self):     
    self.x += self.dx
    self.rect.centerx = self.x
    self.rect.centery = self.y
    if self.wait > 0: self.wait -= 1       
    
  def fire(self):
    if self.wait == 0:
      vx = 0
      vy = -4
      bullet = Bullet( (self.rect.centerx + 3 * vx, self.rect.centery + 3 *vy), vx, vy)
      self.bullets.add(bullet)
      self.wait = 10

  def hit(self):
    self.life -= 1
     
  def drive(self,key_pressed):
    self.dx = 0
    if key_pressed[K_LEFT]: 
      if self.x > 13:
        self.dx = -7
    if key_pressed[K_RIGHT]: 
      if self.x < 627:
        self.dx = +9
    if key_pressed[K_SPACE]: self.fire()
     
  def draw(self, screen):
    screen.blit(self.image, (self.rect.left,self.rect.top) )

    
