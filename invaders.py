import pygame
from pygame.locals import *
from sys import exit
from random import randint,choice
from math import *
from kula import Bullet

class Alien(pygame.sprite.Sprite):
  def __init__(self, pos, bullets):
    pygame.sprite.Sprite.__init__(self)
    self.x, self.y = pos
    self.states = [ (1,0), (0,1), (-1,0), (0,1) ]
    self.state = 0
    self.state_lens = [80,10,80,10]
    self.state_len = self.state_lens[self.state]
    self.image = pygame.image.load('a.png').convert_alpha()
    self.rect = self.image.get_rect()
    self.rect.centerx = self.x
    self.rect.centery = self.y
    self.bullets = bullets
    
  def update(self):
    dx,dy = self.states[self.state]
    self.x += 2*dx
    self.y += dy
    self.rect.centerx = self.x
    self.rect.centery = self.y
    self.state_len -= 1
    if self.state_len < 0:
      self.state += 1
      if self.state > 3: self.state = 0
      self.state_len = self.state_lens[self.state]
    if randint(0,400) == 0:
      self.fire()        
     
  def fire(self):
    vx = 0
    vy = 4
    bullet = Bullet( (self.rect.centerx + 3 * vx, self.rect.centery + 3 *vy), vx, vy)
    self.bullets.add(bullet)

  def draw(self, screen):
    screen.blit(self.image, (self.rect.left,self.rect.top) )   
