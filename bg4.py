import pygame
from pygame.sprite import Sprite
from math import hypot
from random import randint
class Bg4(Sprite):
	def __init__(self,screen):
		super(Bg4,self).__init__()
		self.image = pygame.image.load('bg4.png')
		self.x = randint(201,400)
		self.y = 50
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
		self.x = randint(20,1150)
		self.y = 50
		self.speed += .5
		num = randint(1,4)
		if num == 1:
			self.image = pygame.image.load("monster.png")
		if num == 2:
			self.image = pygame.image.load("bad_guy.png")
		if num == 3:
			self.image = pygame.image.load("bad_guy2.png")
		if num == 4:
			self.image = pygame.image.load("bg3.png")
		if num == 5:
			self.image = pygame.image.load("bg4.png")
		if num == 6:
			self.image = pygame.image.load("bg5.png")
		if num == 7:
			self.image = pygame.image.load("bg6.png")
		





