import pygame
from pygame.sprite import Sprite
from math import hypot
from random import randint
class Bad_guy(Sprite):
	def __init__(self,screen):
		super(Bad_guy,self).__init__()
		self.image = pygame.image.load('bad_guy.png')
		self.x = 20
		self.y = randint(20, 780)
		self.screen = screen
		self.speed = 1
		self.rect = self.image.get_rect()

	def update_me(self, the_player):
		dx = self.x - the_player.x
		dy = self.y - the_player.y
		dist = hypot(dx,dy)
		dx = dx / dist
		dy = dy / dist
		self.x -= dx * self.speed
		self.y -= dy * self.speed
		self.rect.left = self.x
		self.rect.top = self.y

	def draw_me(self):
		# self.rect.left = self.x
		# self.rect.top = self.y
		self.screen.blit(self.image,[self.x,self.y])


	def reset(self):
		self.x = 100
		self.y = randint(20,780)
		self.speed += .5

