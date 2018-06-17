import pygame, sys
from pygame.locals import *
from screeninfo import get_monitors
import math

def monitor():
	for m in get_monitors():
		return str(m)

def gcd(a, b):
	while b:
		a, b = b, a % b
	return a

length, width = [int(round(int(n) * 0.7)) for n in monitor()[8:-5].split("x")]

pygame.init()
FPS = 30 
fpsClock = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode((length, width), 0, 32)
pygame.display.set_caption('Welcome to the orbit explorer')
WHITE = (255, 255, 255)

# defining earth of a rectangular path
earth_object = pygame.image.load('earth.jpg')
scale_earth = 50
earth_scale_x, earth_scale_y = scale_earth, scale_earth
earth_object = pygame.transform.scale(earth_object, (earth_scale_x, earth_scale_y))
earth_x, earth_y = 300, 100
min_x, min_y, max_x, max_y = 300, 100, length-earth_scale_x*1.2*5, width-earth_scale_y*1.2*8/3
direction = 'right'
speed_earth = 10

#defining moon object
moon_object = pygame.image.load('moon.png')
scale_moon = int(round(scale_earth/6))
moon_scale_x, moon_scale_y = scale_moon, scale_moon
moon_object = pygame.transform.scale(moon_object, (moon_scale_x, moon_scale_y))
a, b = 200, 100
sideways = 400
depth = 300 # how far below the title bar the orbit occurs
moon_x, moon_y = 0, -b # initial values
quad = 0
speed_moon = 10
g = gcd(a**2, b**2)

while True: # the main game loop	
	DISPLAYSURF.fill(WHITE)
	pygame.draw.rect(DISPLAYSURF, 0x000000, (400, 300, 10, 10))

	# defines earth of the nth weird dimention
	if direction == 'right':
		earth_x += speed_earth
		if earth_x >= max_x:
			direction = 'down'
	elif direction == 'down':
		earth_y += speed_earth
		if earth_y >= max_y:
			direction = 'left'
	elif direction == 'left':
		earth_x -= speed_earth
		if earth_x <= min_x:
			direction = 'up'
	elif direction == 'up':
		earth_y -= speed_earth
		if earth_y <= min_y:
			direction = 'right'
	
	DISPLAYSURF.blit(earth_object, (earth_x, earth_y))
	### Earth object ends here

	#defines moon of the nth weird dimention
	sideways = earth_x
	depth = earth_y
	
	if abs(moon_x) == a or abs(moon_x) == 0:
		if quad < 4 :
			quad += 1 
		else:
			quad = 1

	if quad in [1, 4]:
		moon_x += speed_moon
	else:
		moon_x -= speed_moon
	moon_y = (((a**2*b**2)/g - (b**2/g)*(moon_x**2))/(a**2/g))**0.5
	if quad in [2, 3]:
		moon_y = abs(moon_y)*-1
	else:
		moon_y = abs(moon_y)

	try:
		# print(moon_x, moon_y, quad, b**2/g)
		DISPLAYSURF.blit(moon_object, (sideways + moon_x - scale_moon/2, depth - moon_y + scale_moon/2))
	except TypeError:
		None
	### Moon event ends here

	# create event
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	pygame.display.update()
	fpsClock.tick(FPS)
