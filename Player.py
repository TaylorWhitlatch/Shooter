import pygame
from pygame.sprite import Sprite

class Player(Sprite):
	# Classes always contain 2 parts:
	# 1. the __init__ section where you define all attributes. 
	# Init, only runs once. When the object is instantiated
	# Because this is a subclass, we need to call the parent's (Sprite) __init__
	def __init__(self,image,start_x,start_y,screen):
		super(Player,self).__init__()
		self.image = pygame.image.load(image)
		self.image = pygame.transform.scale(self.image,(125,125))
		self.x = 400						
		self.y = 700
		self.speed = 10
		self.screen = screen
		self.should_move_up = False
		self.should_move_down = False
		self.should_move_left = False
		self.should_move_right = False
		# self.rect = self.image.get_rect()

	# 2. The methods where you define all the class functions (methods)

	def draw_me(self):
		if(self.should_move_up):
			if self.y > 600:

				self.y -= self.speed
			
				
		elif(self.should_move_down):
			if self.y < 700:
				self.y += self.speed

		if(self.should_move_left):
			if self.x > 20:
				self.x -= self.speed
				self.image = pygame.image.load("batman_r.png")
		elif(self.should_move_right):
			if self.x < 1180:
				self.x += self.speed
				self.image = pygame.image.load("batman_l.png")
		self.screen.blit(self.image, [self.x,self.y])

	def should_move(self,direction,yes_or_no):
		if(direction == "up"):
			# the up key is down. update self.
			self.should_move_up = yes_or_no
		if(direction == "down"):
			# the up key is down. update self.
			self.should_move_down = yes_or_no
		if(direction == "left"):
			# the up key is down. update self.
			self.should_move_left = yes_or_no
		if(direction == "right"):
			# the up key is down. update self.
			self.should_move_right = yes_or_no
