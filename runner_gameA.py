import pygame
import random

from city_scroller import Building
from city_scroller import Scroller
clock = pygame.time.Clock()
pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0,)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #make it into argument = meaning put it in the init function


FRONT_SCROLLER_COLOR = (224,255,255)
MIDDLE_SCROLLER_COLOR = (0,191,255)
BACK_SCROLLER_COLOR = (70,130,180)
BACKGROUND_COLOR = (173,216,230)

front_scroller = Scroller(SCREEN_WIDTH, 400, SCREEN_HEIGHT, FRONT_SCROLLER_COLOR, 3)
middle_scroller = Scroller(SCREEN_WIDTH, 200, (SCREEN_HEIGHT - 50), MIDDLE_SCROLLER_COLOR, 2)
back_scroller = Scroller(SCREEN_WIDTH, 20, (SCREEN_HEIGHT - 100), BACK_SCROLLER_COLOR, 1)

class RunnerSprite(pygame.sprite.Sprite):

	def __init__(self, color, size):
		pygame.sprite.Sprite.__init__(self)
		self.color = color
		self.size = size
		self.image = pygame.Surface([size, size])
		self.image.fill(color)
		self.rect= self.image.get_rect()
	
def update(self):
	
	player1 = RunnerSprite(BLACK, 50)

	WHITE = (255, 255, 255)
	done = False
	good_sprites = []
	bad_sprites = []


	
while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
		 	done = True

	mouse_pos = pygame.mouse.get_pos()
	player1.rect.x = mouse_pos[0]
	player1.rect.y = mouse_pos[1]
	screen.fill(BACKGROUND_COLOR)
	all_sprites_list = pygame.sprite.Group()	
	all_sprites_list.add(player1)
	all_sprites_list.draw(screen)
	
	
	front_scroller.draw_buildings()
	front_scroller.move_buildings()
	
	
	
	
	
	
	# dokill = True # a group is a list of sprites
# 	pygame.sprite.spritecollide(sprite, good_sprites, dokill)
# 	pygame.sprite.spritecollide(sprite, bad_sprites, dokill)

	pygame.display.flip()
	clock.tick(60)
	
pygame.quit()
exit()