#1st sound game file - beeps.wav

import pygame,sys,time

from pygame.locals import *

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400,300))
pygame.display.set_caption("First Sound")
soundObj = pygame.mixer.Sound("beeps.wav")

while True:
	soundObj.play()
	time.sleep(2)
	soundObj.stop()
	for event in pygame.event.get():
		if event.type==QUIT:
			pygame.quit()
			sys.exit()
	pygame.display.update()