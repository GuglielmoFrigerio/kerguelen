# https://www.pygame.org/docs/tut/newbieguide.html
import pygame

pygame.init()

color = (255,255,255) 
position = (0,0) 

canvas = pygame.display.set_mode((1920, 1280))
pygame.display.set_caption("test")
image = pygame.image.load('fellow.png').convert()


exit = False
  
while not exit: 
    canvas.fill(color) 
    canvas.blit(image, dest = position) 
  
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            exit = True
  
    pygame.display.update() 

if __name__ == '__main__':
    print("Hello")
