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
a_earth, b_earth = 400, 200
sideways_earth = 550
depth_earth = 250 # how far below the title bar the orbit occurs
earth_x, earth_y = 0, -b_earth # initial values
quad_earth = 0
speed_earth = 5
g_earth = gcd(a_earth**2, b_earth**2)

#defining moon object
moon_object = pygame.image.load('moon.png')
scale_moon = int(round(scale_earth/6))
moon_scale_x, moon_scale_y = scale_moon, scale_moon
moon_object = pygame.transform.scale(moon_object, (moon_scale_x, moon_scale_y))
a, b = 70, 70
# sideways = 400
# depth = 300 # how far below the title bar the orbit occurs
moon_x, moon_y = 0, -b # initial values
quad = 0
speed_moon = 5
g = gcd(a**2, b**2)

while True: # the main game loop	
	DISPLAYSURF.fill(0x708090)
	# pygame.draw.rect(DISPLAYSURF, 0x000000, (400, 300, 10, 10))

	# defines earth of the nth weird dimention
	if abs(earth_x) == a_earth or abs(earth_x) == 0:
		if quad_earth < 4 :
			quad_earth += 1 
		else:
			quad_earth = 1

	if quad_earth in [1, 4]:
		earth_x += speed_earth
	else:
		earth_x -= speed_earth
	earth_y = (((a_earth**2*b_earth**2)/g_earth - (b_earth**2/g_earth)*(earth_x**2))/(a_earth**2/g_earth))**0.5
	if quad_earth in [2, 3]:
		earth_y = abs(earth_y)*-1
	else:
		earth_y = abs(earth_y)
	# print(earth_x, earth_y, quad_earth, b_earth**2/g_earth)
	x_base = sideways_earth + earth_x - scale_earth/2
	y_base = depth_earth - earth_y + scale_earth/2
	try:
		DISPLAYSURF.blit(earth_object, (x_base, y_base))
	except TypeError:
		None
	### Earth object ends here

	#defines moon of the nth weird dimention
	sideways = x_base
	depth = y_base

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
