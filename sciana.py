import pygame
from pygame.locals import *
from sys import exit
from random import randint,choice
from math import *

class Wall(pygame.sprite.Sprite):
     def __init__(self, pos, width):
          pygame.sprite.Sprite.__init__(self)
          self.x, self.y = pos
          self.width = width
          self.image = pygame.Surface( (self.width,10) )
          self.image.fill( (120,220,180) )
          self.rect = self.image.get_rect()
          self.rect.centerx = self.x
          self.hit = 0
          self.delt = 0
     def update(self):     
          self.rect.centerx = self.x
          self.rect.centery = self.y
     def delete(self):
          self.hit = self.hit + 10
          self.image.fill( (120+self.hit,220-self.hit,180-self.hit) ) 
          if self.hit >= 100: 
               self.delt = 1
               self.hit = 0
     def draw(self, screen):
          screen.blit(self.image, (self.rect.left,self.rect.top) ) 
