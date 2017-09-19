# Duh
# We have access to pygame, because we did:
# $ pip install pygame
# it is NOT part of core. This is a 3rd party module.
import pygame
from pygame.sprite import Group, groupcollide, spritecollide, spritecollideany
from pygame.sprite import Sprite
import math
# -----CUSTOM CLASSES HERE-----
from Player import Player
from Bad_guy import Bad_guy
from Bullet import Bullet
from monster1 import Monster
from bad_guy2 import Bad_guy2
from bad_guy3 import Bad_guy3
from bg4 import Bg4
from bg5 import Bg5
from bg6 import Bg6
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
bg4 = Bg4(screen)
bg5 = Bg5(screen)
bg6 = Bg6(screen)
bad_guy_g = Group()
bad_guy_g.add(bad_guy)
bad_guy2_g = Group()
bad_guy2_g.add(bad_guy2)
bad_guy3_g = Group()
bad_guy3_g.add(bad_guy3)
monster_g = Group()
monster_g.add(monster)
bg4_g = Group()
bg4_g.add(bg4)
bg5_g = Group()
bg5_g.add(bg5)
bg6_g = Group()
bg6_g.add(bg6)

bullets = Group()
the_player_group = Group()
the_player_group.add(the_player)
bg = 0
hit = 0


game_on = True

while game_on: 
	for event in pygame.event.get():
		
		if event.type == pygame.QUIT:
			game_on = False
		elif event.type == pygame.KEYDOWN:
			print event.key
			
			if event.key == 273:
				
				the_player.should_move("up",True)
				
			elif event.key == 274:
				
				the_player.should_move("down",True)
			if event.key == 275:	
				the_player.should_move("right",True)
			elif event.key == 276:
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
				

	
	pygame_screen.blit(background,[0,0])
	for bad_guy2 in bad_guy2_g:
		bad_guy2.update_me(the_player)
		bad_guy2.draw_me()
	for bad_guy in bad_guy_g:
		bad_guy.update_me(the_player)
		bad_guy.draw_me()

	for bad_guy3 in bad_guy3_g:
		bad_guy3.update_me(the_player)
		bad_guy3.draw_me()

	if hit > 7:
		for bg4 in bg4_g:
			bg4.update_me(the_player) 
			bg4.draw_me()

	if hit > 15:
		for bg5 in bg5_g:
			bg5.update_me(the_player) 
			bg5.draw_me()

	if hit > 25:
		for bg6 in bg6_g:
			bg6.update_me(the_player) 
			bg6.draw_me()
	
	

	for monster in monster_g:
		monster.update_me(the_player)
		monster.draw_me()

	the_player.draw_me()

	for bullet in bullets:
		bullet.update()
		bullet.draw_bullet()


	
	bullet_hit = groupcollide(bullets,bad_guy2_g,True,True)
	bullet_hit = groupcollide(bullets,bad_guy_g,True,True)
	bullet_hit = groupcollide(bullets,bad_guy3_g,True,True)
	bullet_hit = groupcollide(bullets,monster_g,True,True)
	bullet_hit = groupcollide(bullets,bg4_g,True,True)
	bullet_hit = groupcollide(bullets,bg5_g,True,True)
	bullet_hit = groupcollide(bullets,bg6_g,True,True)
	# enemy_hit = groupcollide(the_player_group,monster_g, True, True)
	print the_player_group
	print bad_guy_g
	# print player
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
	if len(bg4_g) == 0:
		bg4.reset()
		bg4_g.add(bg4)
		# bad_guy.reset
		# bad_guys.add(bad_guy)
		hit += 1
	if len(bg5_g) == 0:
		bg5.reset()
		bg5_g.add(bg5)
		# bad_guy.reset
		# bad_guys.add(bad_guy)
		hit += 1

	if len(bg6_g) == 0:
		bg6.reset()
		bg6_g.add(bg6)
		# bad_guy.reset
		# bad_guys.add(bad_guy)
		hit += 1
	# if bullet_hit == True:
	# 	bad_guys.add(bad_guy)

	# enemy_hit = groupcollide(the_player,bad_guys,False,True)

	# print bullet_hit

	
	font = pygame.font.Font(None, 32)
	wins_text = font.render("Hits: %d" % (hit), True, (0,0,0))
	pygame_screen.blit(wins_text,[40,40])
	# font2 = pygame.font.Font(None, 64)
	# boss_text = font2.render("BOSS", True, (0,0,0))
	# if hit > 25:
	# 	pygame_screen.blit(boss_text,[1050,40])
	print hit
	pygame.display.flip()

