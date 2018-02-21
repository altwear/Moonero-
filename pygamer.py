import pygame
import time
import random
import os, sys
from os import path

pygame.init()
pygame.mixer.pre_init(44100, 16, 2, 4096)

#crash_Sound = pygame.mixer.Sound(".wav")
pygame.mixer.music.load('music\\TRAPFORD.wav')

#Display Size
display_width = 800
display_height = 600

#Colors
black = (0,0,0)
white = (255,255,255)

red = (200,0,0)
bright_red = (255,0,0)

green = (0,200,0)
bright_green = (0,255,0)

blue = (0,0,255)


all_sprites_list = pygame.sprite.Group()
block_list = pygame.sprite.Group()
bullet_list = pygame.sprite.Group()

#Display 
gameDisplay = pygame.display.set_mode((display_width,display_height))
clock = pygame.time.Clock()

HS_FILE = "highscore.txt"

#def load_data():
#	dir = path.dirname(__file__)
#	with open(path.join(dir, HS_FILE), 'r') as f:
#		try:
#			highscore = int(f.read())
#		except:
#			highscore = 0
#Images
icon = pygame.image.load('img\\icon.png')
shitcoin = pygame.image.load('img\\shitcoin.png')
shitcoin1 = pygame.image.load('img\\shitcoin1.png')

spaceImg = pygame.image.load('img\\XMR.png')
bkgd = pygame.image.load('img\\starcloud.jpg').convert()
bkgd_main = pygame.image.load('img\\moonero.png')
#ICON
pygame.display.set_icon(icon)
#Title
pygame.display.set_caption('Monero to the Moon')
#Globals
car_width = 100
pause = False







class Block(pygame.sprite.Sprite):
	def __init__(self,color):
		pygame.sprite.Sprite.__init__(self)
		
		self.image = pygame.image.load('img\\blockImg.png')
		self.rect = self.image.get_rect()
		
class Bullet(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load('img\\icon.png')
		self.rect = self.image.get_rect()
		
	def update(self):
		
		self.rect.y -= 3 

#Functions




def points_gained(count):
	

	font = pygame.font.Font("goth.ttf", 25)
	text = font.render("Score: " + str(count), True, black)
	gameDisplay.blit(text,(0,0))
	

		

def things(thingx, thingy, thingw, thingh):
	#pygame.draw.rect(gameDisplay,color,[thingx, thingy, thingw, thingh])
	gameDisplay.blit(shitcoin,(thingx, thingy, thingw, thingh))
	
def points(pointsx, pointsy, pointsw, pointsh):
#pygame.draw.rect(gameDisplay,color,[thingx, thingy, thingw, thingh])
	gameDisplay.blit(shitcoin1,(pointsx, pointsy, pointsw, pointsh))	

def car(x,y):
	gameDisplay.blit(spaceImg,(x,y))
	

def text_objects(text, font):
	textSurface = font.render(text, True, red)
	return textSurface, textSurface.get_rect()

def message_display(text):
	largeText = pygame.font.Font("goth.ttf", 115)
	TextSurf, TextRect = text_objects(text, largeText)
	TextRect.center = ((display_width/2),(display_height/2))
	gameDisplay.blit(TextSurf, TextRect)

	pygame.display.update()

	time.sleep(2)
	game_loop()


def crash():

	pygame.mixer.music.stop()
	#pygame.mixer.Sound(crash_sound)

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit

		gameDisplay.fill(black)
		largeText = pygame.font.Font("goth.ttf", 115)
		TextSurf, TextRect = text_objects("Try Again!",largeText)
		TextRect.center = ((display_width/2),(display_height/2))
		gameDisplay.blit(bkgd_main,(1,1))
		gameDisplay.blit(TextSurf, TextRect)

		button("Play Again",150,450,100,50,green,bright_green,game_loop)
		button("Quit",550,450,100,60,black,black,quit_game)


		pygame.display.update()
		clock.tick(15)

def win():
	

	pygame.mixer.music.stop()
	#pygame.mixer.Sound(crash_sound)
	
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit

		gameDisplay.fill(black)
		largeText = pygame.font.Font("goth.ttf", 115)
		TextSurf, TextRect = text_objects("You Win!",largeText)
		TextRect.center = ((display_width/2),(display_height/2))
		gameDisplay.blit(bkgd_main,(1,1))
		gameDisplay.blit(TextSurf, TextRect)

		button("Next Level",150,450,125,50,green,bright_green,game_loop2)
		button("Quit",550,450,100,50,black,black,quit_game)


		pygame.display.update()
		clock.tick(15)

def button(msg, x, y, w, h, ic, ac, action=None):
	mouse = pygame.mouse.get_pos() 
	click = pygame.mouse.get_pressed()
	if x+w > mouse[0] > x and y+h > mouse[1] > y:
		pygame.draw.rect(gameDisplay, ac, (x,y,w,h))
		if click[0] == 1 and action != None:
			action()
	else:
		pygame.draw.rect(gameDisplay, ic, (x,y,w,h))
	smallText = pygame.font.Font("goth.ttf", 20)
	textSurf,textRect = text_objects(msg, smallText)
	textRect.center = ( (x+(w/2)), (y+(h/2)) )
	gameDisplay.blit(textSurf, textRect)

def quit_game():
	pygame.quit()
	quit()

def unpause():
	global pause
	pause = False
	pygame.mixer.music.unpause()
		

def paused():
	
	pygame.mixer.music.pause()
			

	while pause:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit

		gameDisplay.fill(black)
		largeText = pygame.font.Font("goth.ttf", 115)
		TextSurf, TextRect = text_objects("Paused",largeText)
		TextRect.center = ((display_width/2),(display_height/2))
		gameDisplay.blit(bkgd_main,(1,1))
		gameDisplay.blit(TextSurf, TextRect)
		pygame.mixer.music.pause()

		button("Continue",150,450,100,50,green,bright_green,unpause)
		button("Quit",550,450,100,50,black,black,quit_game)


		pygame.display.update()
		clock.tick(15)

def game_intro():
	intro = True

	while intro:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit

		
		
		gameDisplay.fill(black)
		myfont = pygame.font.Font("goth.ttf", 20)
		scorefile = open('highscore.txt', 'r')
		highscores = scorefile.read()
		label = myfont.render("High Score:  " + (highscores), 1, (white))
		gameDisplay.blit(label, (250, 5))
		largeText = pygame.font.Font("goth.ttf", 100)
		TextSurf, TextRect = text_objects("oonero!",largeText)		
		TextRect.center = ((display_width/1 - 220),(display_height/2 + 50)) 
		gameDisplay.blit(bkgd_main,(-100,1))
		gameDisplay.blit(TextSurf, TextRect)
		
		button("Go!",600,450,100,50,green,bright_green,game_loop)
		button("Quit",600,50,100,50,black,black,quit_game)

		scorefile.close()
		pygame.display.update()
		clock.tick(15)


#Main Game Loop
def game_loop():
	global pause
	pygame.mixer.music.play(-1)
	
	x = (display_width * 0.45)
	y = (display_height * 0.8)
	z = 0
	x_change = 0
	
	for i in range(60):
		block = Block(red)
		block.rect.x = random.randrange(display_width)
		block.rect.y = random.randrange(300)
		block_list.add(block)
		all_sprites_list.add(block)

	thing_startx = random.randrange(0, display_width)
	thing_starty = -600
	thing_speed = 5
	thing_width = 51
	thing_height = 51
	gained = 0

	points_startx = random.randrange(0, display_width)
	points_starty = -500
	points_speed = 7
	points_width = 33
	points_height = 33
	
	game_Exit = False
	
     

### Game Logic ###
	while not game_Exit:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					x_change = -5
				if event.key == pygame.K_RIGHT:
				    x_change = 5
				elif event.key == pygame.K_p:
					pause = True
					paused()			
			
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
						x_change = 0

			elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
				bullet = Bullet()
				bullet.rect.x = x 
				bullet.rect.y = y
				all_sprites_list.add(bullet)
				bullet_list.add(bullet)
		
		x += x_change
		
		all_sprites_list.update()

		for bullet in bullet_list:

			block_hit_list = pygame.sprite.spritecollide(bullet,block_list,True)

			for block in block_hit_list:
				bullet_list.remove(bullet)
				all_sprites_list.remove(bullet)
				gained += 50

			if bullet.rect.y < -10:
				bullet_list.remove(bullet)
				all_sprites_list.remove(bullet)

		things(thing_startx, thing_starty, thing_width, thing_height)
		thing_starty += thing_speed
		points(points_startx, points_starty, points_width, points_height)
		points_starty += points_speed
		car(x,y)
		points_gained(gained)


		#if x > display_width - car_width or x < 0:
		#		 crash()

		if thing_starty > display_height:
			thing_starty = 0 - thing_height
			thing_startx = random.randrange(0,display_width)
			thing_speed += 0.7


		if y < thing_starty + thing_height:
		
			if x > thing_startx and x < thing_startx + thing_width or x + car_width > thing_startx and x + car_width < thing_startx + thing_width:
				crash()

		if points_starty > display_height:
			points_starty = 0 - points_height
			points_startx = random.randrange(0,display_width)
			points_speed += 0.5
			

		if y < points_starty + points_height:
		
			if x > points_startx and x < points_startx + points_width or x + car_width > points_startx and x + car_width < points_startx + points_width:
				crash()	
		

		

		

		if not block_list:
			with open(path.join(HS_FILE), 'r') as f:
				try:
					highscore = str(f.read())
				except:
					highscore = 0
	
				if int(gained) > int(highscore):
					highscore = gained
					with open(path.join(HS_FILE), 'w') as f:
						f.write(str(gained))
			win()
		gained += 1		
		pygame.display.update()
		rel_z = z % bkgd.get_rect().height
		gameDisplay.blit(bkgd, (0, rel_z - bkgd.get_rect().height))
		if rel_z < display_width:
			gameDisplay.blit(bkgd, (0, rel_z))
		z -= 1
		all_sprites_list.draw(gameDisplay)
		clock.tick(60)

def game_loop2():
	global pause
	pygame.mixer.music.play(-1)
	
	x = (display_width * 0.45)
	y = (display_height * 0.8)
	z = 0
	x_change = 0
	
	for i in range(120):
		block = Block(red)
		block.rect.x = random.randrange(display_width)
		block.rect.y = random.randrange(300)
		block_list.add(block)
		all_sprites_list.add(block)

	thing_startx = random.randrange(0, display_width)
	thing_starty = -600
	thing_speed = 7
	thing_width = 51
	thing_height = 51
	gained = 0

	points_startx = random.randrange(0, display_width)
	points_starty = -500
	points_speed = 9
	points_width = 33
	points_height = 33
	
	game_Exit = False
	
     

### Game Logic ###
	while not game_Exit:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					x_change = -5
				if event.key == pygame.K_RIGHT:
				    x_change = 5
				elif event.key == pygame.K_p:
					pause = True
					paused()			
			
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
						x_change = 0

			elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
				bullet = Bullet()
				bullet.rect.x = x 
				bullet.rect.y = y
				all_sprites_list.add(bullet)
				bullet_list.add(bullet)
		
		x += x_change
		
		all_sprites_list.update()

		for bullet in bullet_list:

			block_hit_list = pygame.sprite.spritecollide(bullet,block_list,True)

			for block in block_hit_list:
				bullet_list.remove(bullet)
				all_sprites_list.remove(bullet)
				gained += 100

			if bullet.rect.y < -10:
				bullet_list.remove(bullet)
				all_sprites_list.remove(bullet)

		things(thing_startx, thing_starty, thing_width, thing_height)
		thing_starty += thing_speed
		points(points_startx, points_starty, points_width, points_height)
		points_starty += points_speed
		car(x,y)
		points_gained(gained)


		#if x > display_width - car_width or x < 0:
		#		 crash()

		if thing_starty > display_height:
			thing_starty = 0 - thing_height
			thing_startx = random.randrange(0,display_width)
			thing_speed += 0.7


		if y < thing_starty + thing_height:
		
			if x > thing_startx and x < thing_startx + thing_width or x + car_width > thing_startx and x + car_width < thing_startx + thing_width:
				crash()

		if points_starty > display_height:
			points_starty = 0 - points_height
			points_startx = random.randrange(0,display_width)
			points_speed += 0.3
			

		if y < points_starty + points_height:
		
			if x > points_startx and x < points_startx + points_width or x + car_width > points_startx and x + car_width < points_startx + points_width:
				crash()	
		

		 

		if not block_list:
			with open(path.join(HS_FILE), 'r') as f:
				highscore = str(f.read())
				
	
				if int(gained) > int(highscore):
					highscore = gained
					with open(path.join(HS_FILE), 'w') as f:
						f.write(str(gained))
			win()
			
		gained += 1		
		pygame.display.update()
		rel_z = z % bkgd.get_rect().height
		gameDisplay.blit(bkgd, (0, rel_z - bkgd.get_rect().height))
		if rel_z < display_width:
			gameDisplay.blit(bkgd, (0, rel_z))
		z += 1
		all_sprites_list.draw(gameDisplay)
		clock.tick(60)

game_intro()
game_loop()
pygame.quit()
quit()
