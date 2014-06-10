import pygame
from pygame.locals import *
from sys import exit
from random import randint,choice
from math import *

class Bullet(pygame.sprite.Sprite):
  def __init__(self, pos, vx, vy):
    pygame.sprite.Sprite.__init__(self)
    self.x, self.y = pos
    self.vx = vx
    self.vy = vy
    self.image = pygame.Surface( (5,5) )
    self.image.fill( (0,0,0) )
    pygame.draw.circle(self.image, (255,255,255), (3,3), 2)
    self.image.set_colorkey( (0,0,0) )
    self.rect = self.image.get_rect()
    self.rect.centerx = self.x
    self.rect.centery = self.y
     
  def update(self):
    self.x += self.vx
    self.y += self.vy
    self.rect.centerx = self.x
    self.rect.centery = self.y
     
  def draw(self, screen):
    screen.blit(self.image, (self.rect.left,self.rect.top) )   

