import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	def __init__(self,screen,the_player,direction):
		super(Bullet, self).__init__()
		self.screen = screen

		self.rect = pygame.Rect(0,200,12,12)
		self.color = (41, 62, 96)
		self.rect.centerx = the_player.x
		self.rect.top = the_player.y
		self.speed = 15
		self.direction = direction
		self.x = self.rect.x + 50
		self.y = self.rect.y 

	def update(self):
		if self.direction == 1: #up
			self.y -= self.speed #change the y, each time update is run, by bullet speed
			self.rect.y = self.y #update rect position
		elif self.direction == 2: #right
			self.x += self.speed #change the y, each time update is run, by bullet speed
			 #update rect position
			self.rect.x = self.x
		elif self.direction == 3: #down
			
			self.x -= self.speed #change the y, each time update is run, by bullet speed
			
			self.rect.x = self.x
		elif self.direction == 4: #down
			self.y -= self.speed
			self.x += self.speed
			self.x += self.speed #change the y, each time update is run, by bullet speed
			self.rect.y = self.y
			self.rect.x = self.x #update rect position
		else: #left
			self.x -= self.speed #change the y, each time update is run, by bullet speed
			self.rect.x = self.x #update rect position

# pygame.draw.circle(screen, color, (x,y), radius, thickness)
	def draw_bullet(self):
		pygame.draw.rect(self.screen, self.color, self.rect) #draw the bullet!


