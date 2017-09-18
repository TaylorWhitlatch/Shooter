# Duh
# We have access to pygame, because we did:
# $ pip install pygame
# it is NOT part of core. This is a 3rd party module.
import pygame
from pygame.sprite import Group, groupcollide, spritecollide, spritecollideany

import math
# -----CUSTOM CLASSES HERE-----
from Player import Player
from Bad_guy import Bad_guy
from Bullet import Bullet
from monster1 import Monster
from bad_guy2 import Bad_guy2
from bad_guy3 import Bad_guy3
background = pygame.image.load('background2.png')

# Have to init the pygame object so we can use it
pygame.init()
screen_size = (1200,800)
pygame_screen = pygame.display.set_mode(screen_size)
# Screen size is a tuple

# Because we are going to paint the background, we need a tuple for the color
background_color = (82,111,53)

# Create a screen for pygame to use to draw on
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("An epic shooter made with python")

the_player = Player('batman_l.png',200,200,screen)
# Make a bad_guy
bad_guy = Bad_guy(screen)
bad_guy2 =Bad_guy2(screen)
monster = Monster(screen)
bad_guy3 =Bad_guy3(screen)
# make a group for the bad_guys
# bad_guys = Group()
# add our bad_guy to the bad_guys group
# bad_guys.add(bad_guy)
# bad_guys.add(bad_guy2)
# bad_guys.add(bad_guy3)
bad_guy_g = Group()
bad_guy_g.add(bad_guy)
bad_guy2_g = Group()
bad_guy2_g.add(bad_guy2)
bad_guy3_g = Group()
bad_guy3_g.add(bad_guy3)
monster_g = Group()
monster_g.add(monster)
player = Group()
player.add(the_player)
# bad_guys.add(monster)
# Make a new Group called bullets. Group is a pygame "list"
# the_player = Group()
bullets = Group()
the_player_group = Group()
the_player_group.add(the_player)
bg = 0
hit = 0
# the_player_image = pygame.image.load('batman.png')
# player = {
# 	"x": 100,
# 	"y": 100
# }

game_on = True
# Set up the main game loop
while game_on: #will run forever (until break)
	# Loop through all the pygame events.
	# This is pygames escape hatch. (Quit)
	for event in pygame.event.get():
		# print event
		if event.type == pygame.QUIT:
			game_on = False
		elif event.type == pygame.KEYDOWN:
			print event.key
			# print "User pressed a key!!!"
			if event.key == 273:
				# user pressed up!
				# the_player.y -= the_player.speed
				the_player.should_move("up",True)
				
			elif event.key == 274:
				# the_player.y += the_player.speed
				the_player.should_move("down",True)
			if event.key == 275:
				# the_player.x += the_player.speed
				# the_player = Player('batman_r.png',100,100,screen)
				the_player.should_move("right",True)
			elif event.key == 276:
				# the_player.x -= the_player.speed
				# the_player = Player('batman_l.png',100,100,screen)
				the_player.should_move("left",True)
				

			# elif event.key == 115:
			# 	# 32 = SPACE BAR... FIRE!!!!
			# 	new_bullet = Bullet(screen, the_player, 2	)
			# 	bullets.add(new_bullet)
			# elif event.key == 102:	
			# 	new_bullet = Bullet(screen, the_player, 3)
				
			elif event.key == 32:	
				new_bullet = Bullet(screen, the_player, 1)
				bullets.add(new_bullet)
			# elif event.key == 113:	
			# 	new_bullet = Bullet(screen, the_player, 4)
				bullets.add(new_bullet)
		elif event.type == pygame.KEYUP:
			if event.key == 273:
				the_player.should_move("up",False)
			
			elif event.key == 274: 
				the_player.should_move("down",False)
			if event.key == 275:
				the_player.should_move("right",False)
			elif event.key == 276:
				the_player.should_move("left",False)
				

	# print bullets

	# paint the screen
	# screen.fill(background_color)
	pygame_screen.blit(background,[0,0])
	for bad_guy2 in bad_guy2_g:
	
		# update the bad guy (based on where the player is)
			bad_guy2.update_me(the_player)
		# draw the bad guy
			bad_guy2.draw_me()
	for bad_guy in bad_guy_g:
		# update the bad guy (based on where the player is)
		bad_guy.update_me(the_player)
		# draw the bad guy
		bad_guy.draw_me()

	for bad_guy3 in bad_guy3_g:
		# update the bad guy (based on where the player is)
		bad_guy3.update_me(the_player)
		# draw the bad guy
		bad_guy3.draw_me()

	
	

	for monster in monster_g:
		# update the bad guy (based on where the player is)
		monster.update_me(the_player)
		# draw the bad guy
		monster.draw_me()

	# # Must be after fill, or we won't be able to see the hero
	# screen.blit(the_player.image, [the_player.x,the_player.y])
	the_player.draw_me()

	for bullet in bullets:
		# update teh bullet location
		bullet.update()
		# draw the bullet on the screen
		bullet.draw_bullet()

	# Check for collions...
	
	bullet_hit = groupcollide(bullets,bad_guy2_g,True,True)
	bullet_hit = groupcollide(bullets,bad_guy_g,True,True)
	bullet_hit = groupcollide(bullets,bad_guy3_g,True,True)
	bullet_hit = groupcollide(bullets,monster_g,True,True)
	enemy_hit = groupcollide(player,bad_guy_g,True, True)
	# print the_player_group
	# print bad_guy2_g
	print player
	print monster_g
	
	if len(bad_guy_g) == 0:
		bad_guy.reset()
		bad_guy_g.add(bad_guy)

		hit += 1

	if len(bad_guy2_g) == 0:
		bad_guy2.reset()
		bad_guy2_g.add(bad_guy2)
		hit += 1
	if len(bad_guy3_g) == 0:
		bad_guy3.reset()
		bad_guy3_g.add(bad_guy3)
		hit += 1
	if len(monster_g) == 0:
		monster.reset()
		monster_g.add(monster)
		# bad_guy.reset
		# bad_guys.add(bad_guy)
		hit += 1

	# if bullet_hit == True:
	# 	bad_guys.add(bad_guy)

	# enemy_hit = groupcollide(the_player,bad_guys,False,True)

	# print bullet_hit

	# flip the screen, i.e.clear it so we can draw again... and again... and again
	font = pygame.font.Font(None, 32)
	wins_text = font.render("Hits: %d" % (hit), True, (0,0,0))
	pygame_screen.blit(wins_text,[40,40])
	print hit
	pygame.display.flip()

