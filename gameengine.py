## Bu kod oyundaki harita tasarımını kolaylaştırmak için yazdığım bir oyun motorudur esas oyunumu main.py dan çalıştırabilirsiniz.
import pygame
from pygame.locals import *
from pygame import mixer
import pickle
from os import path
import os
import random
pygame.init()
clock = pygame.time.Clock()
fps = 60
mouse_position = (0, 0)
drawing = False
last_pos = None
screen_width = 1050
screen_height = 1000
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('GameEngine By Furkan Ceran')

white = (255, 255, 255)
blue = (0, 0, 255)
BLACK = (0, 0, 0)
tile_size = 50
bg_img = [pygame.image.load('img/sky.png'),pygame.image.load('img/purple.png'),pygame.image.load('img/mountain.png'),pygame.image.load('img/stars.png'),pygame.image.load('img/desert.png'),pygame.image.load('img/forest.png')]
bg_selected=bg_img[random.randint(0,5)]

dirt=pygame.image.load('img/dirt.png')
dirt = pygame.transform.scale(dirt, (tile_size, tile_size))
dirt_rect = dirt.get_rect()
dirt_rect.x = 20 * tile_size
dirt_rect.y = 20 * tile_size

grass=pygame.image.load('img/grass.png')
grass = pygame.transform.scale(grass, (tile_size, tile_size))
grass_rect = grass.get_rect()
grass_rect.x = 20 * tile_size
grass_rect.y = 20 * tile_size

blob=pygame.image.load('img/blob.png')
blob = pygame.transform.scale(blob, (tile_size, tile_size))
blob_rect = blob.get_rect()
blob_rect.x = 20 * tile_size
blob_rect.y = 20 * tile_size

coin=pygame.image.load('img/coin.png')
coin = pygame.transform.scale(coin, ((tile_size // 2, tile_size // 2)))
coin_rect = coin.get_rect()
coin_rect.x = 20 * tile_size
coin_rect.y = 20 * tile_size

lava=pygame.image.load('img/lava.png')
lava = pygame.transform.scale(lava, (tile_size, tile_size // 2))
lava_rect = lava.get_rect()
lava_rect.x = 20 * tile_size
lava_rect.y = 20 * tile_size


platform=pygame.image.load('img/platform.png')
platform = pygame.transform.scale(platform, (tile_size, tile_size // 2))
platform_rect = platform.get_rect()
platform_rect.x = 20 * tile_size
platform_rect.y = 20 * tile_size

door=pygame.image.load('img/exit.png')
door = pygame.transform.scale(door,(tile_size, int(tile_size * 1.5)))
door_rect = door.get_rect()
door_rect.x = 20 * tile_size
door_rect.y = 20 * tile_size

kaydet=pygame.image.load('img/kaydet.png')
kaydet = pygame.transform.scale(kaydet,(tile_size, int(tile_size * 1.5)))
kaydet_rect = kaydet.get_rect()
kaydet_rect.x = 20 * tile_size
kaydet_rect.y = 20 * tile_size

temizle=pygame.image.load('img/temizle.png')
temizle = pygame.transform.scale(temizle,(tile_size, int(tile_size * 1.5)))
temizle_rect = temizle.get_rect()
temizle_rect.x = 20 * tile_size
temizle_rect.y = 20 * tile_size

save=0
class Button():
	def __init__(self, x, y, image):
		self.image = image
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.clicked = False

	def draw(self):
		action = False

		#mouse pozisyonlarını alıyorum
		pos = pygame.mouse.get_pos()

		# Mouse tıklandı mı kontrolü
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				action = True
				self.clicked = True

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False


		#butonu çizdirdim
		screen.blit(self.image, self.rect)

		return action
world=[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

run = True
dirt_button = Button(1000, 0, dirt)
grass_button = Button(1000, 50, grass)
blob_button=Button(1000, 100, blob)
coin_button=Button(1000, 150, coin)
lava_button=Button(1000, 200, lava)
platform_button=Button(1000, 250, platform)
door_button=Button(1000, 300, door)
temizle_button=Button(1000, 450, temizle)
kaydet_button=Button(1000, 550, kaydet)
screen.blit(bg_selected, (0, 0))

while run:
	clock.tick(fps)
	if dirt_button.draw():
		mouse="DIRT"
	elif grass_button.draw():
		mouse="GRASS"
	elif blob_button.draw():
		mouse="BLOB"
	elif coin_button.draw():
		mouse="COIN"
	elif	lava_button.draw():
		mouse="LAVA"
	elif platform_button.draw():
		mouse="PLATFORM"
	elif door_button.draw():
		mouse="EXIT"	
	elif temizle_button.draw():
		screen.blit(bg_selected, (0, 0))
		world=[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
	elif kaydet_button.draw():
		save=1
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
		if event.type == MOUSEMOTION:
			if (drawing):
				mouse_position = pygame.mouse.get_pos()
				if mouse_position is not None:
					x=round(mouse_position[0]/50)
					y=round(mouse_position[1]/50)
					
					
						

					if x<20 and y<20:
						
						x1=x*50
						y1=y*50
						if mouse=="DIRT" :
							screen.blit(dirt, (x1,y1))
							world[y-1][x-1]=1
						elif mouse=="GRASS":
							screen.blit(grass, (x1,y1))
							world[y-1][x-1]=2
						elif mouse=="BLOB":
							screen.blit(blob,(x1,y1))
							world[y-1][x-1]=3
						elif mouse=="COIN":
							screen.blit(coin,(x1,y1))
							world[y-1][x-1]=7
						elif mouse=="LAVA":
							screen.blit(lava,(x1,y1))
							world[y-1][x-1]=6
						elif mouse=="PLATFORM":
							screen.blit(platform,(x1,y1))
							world[y-1][x-1]=4
						elif mouse=="EXIT":
							screen.blit(door,(x1,y1))
							world[y-1][x-1]=8
						else:
							pass
				
		elif event.type == MOUSEBUTTONUP:
			mouse_position = (0, 0)
			drawing = False
			
		elif event.type == MOUSEBUTTONDOWN:
			drawing = True

	if save==1:
		levels=[]
		arr = os.listdir()
		for i in arr:
			try:
				if i[0:5]=="level":
					
					levels.append(int(i[5]))
			except:
				pass
		
		lastlevel=max(levels)
		
		level=lastlevel+1
		with open(f'level{level}_data', 'wb') as f:
			pickle.dump(world, f)
		print(level,"Kaydedildi")
		save=0
	pygame.display.update()
pygame.quit()






