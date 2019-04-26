"""
A moving shape in a bounded screen.

@author: Nima Sanjabi
Created on Wed Apr 24 16:14:45 2019
"""

import pygame
import sys
from lib import utils
from pygame.locals import *
from pygame.compat import geterror

if not pygame.font: print ('Warning, fonts disabled')

# game constants
NOMINAL_FRAME_RATE = 60
SCREEN_WIDTH, SCREEN_HEIGHT = 480, 300
SHAPE_WIDTH, SHAPE_HEIGHT = 64, 64
#X_MOVE, Y_MOVE = 1, 1
    
BG_COLOR=(255, 0, 0)
SHAPES_COLOR = (136, 187, 0)
TEXT_COLOR = (17, 119, 136)
    
class MovingShape(pygame.sprite.Sprite):
    """Defines a shape."""
    def __init__(self):
        # calls the Sprite initializer
        pygame.sprite.Sprite.__init__(self)
        self.shape_rect=pygame.Rect(0, 0, SHAPE_WIDTH, SHAPE_HEIGHT)
        self.shape_surface=pygame.Surface([SHAPE_WIDTH, SHAPE_HEIGHT])
        self.color=(0, 255, 0)
        #self.screen = pygame.display.get_surface()
        #print('screen', self.screen)
        
        
    def move_shape(self, X_MOVE, Y_MOVE):
        """move the shape by x and y steps. Before each 
        move, the previous position on the last frame is
        repainted()erased with black color."""         
        self.shape_rect=self.shape_rect.move(X_MOVE,Y_MOVE)
  
def main():
    """this function is called when the program starts.
       it initializes everything it needs, then runs in
       a loop until the function returns."""
       
    #Initialize Everything     
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.fill((255,0,0))
    pygame.display.set_caption('Bouncing square!')    
    background = pygame.Surface(screen.get_size())
    background = background.convert()
#    background.fill((255,255,0))
    X_MOVE, Y_MOVE = 1, 1
    # a list as a buffer to save the recent samples of frame rate
    BUFFER_SIZE=10
    frame_rate_buffer=[0]*BUFFER_SIZE
    last_frame_rate=0
    frame_counter=0
    clock=pygame.time.Clock()
    

    #Display The Background
#    screen.blit(background, (0, 0))
#    pygame.display.flip()
    
    
    # creates a shape object from the MovingShape class
    shape_1=MovingShape()
    #pygame.draw.rect(shape_1.screen, shape_1.color, shape_1.shape_rect)
    allsprites = pygame.sprite.Group()
    
    # main loop
    while True: 
        # a clock keeps the frame rate to a fixed number
        clock.tick(NOMINAL_FRAME_RATE)
        frame_counter+=1
        #move the shape 1 step
        shape_1.move_shape(X_MOVE,Y_MOVE)
        # reverse the shape when it colides with the screen walls       
        rect_1=shape_1.shape_rect
        if rect_1.left < 0 or rect_1.right > SCREEN_WIDTH:
            X_MOVE = -X_MOVE
        if rect_1.top < 0 or rect_1.bottom > SCREEN_HEIGHT:
            Y_MOVE = -Y_MOVE
            print('collision')
  
        allsprites.update()
#        """ displays the real frame rate which might be different
#        from the nominal frame rate."""
#        if frame_counter > 20:
#            frame_counter=0
#            if pygame.font:
#                font = pygame.font.Font(None, 24)
#                # erase the last text with black color
#                text = font.render('Frame rate: {} fps'.format(str(round(last_frame_rate))), 1, BG_COLOR)
#                textpos = pygame.Rect(10, 10, 140, 17)
#                background.blit(text, textpos)
#                screen.blit(background, (0, 0))
#                
#                #get the frame rate            
#                frame_rate = utils.list_average(utils.shift_buffer(frame_rate_buffer, clock.get_fps()))
#                #frame_rate = clock.get_fps()
#                
#                # write the frame rate on the screen with red color
#                text = font.render('Frame rate: {} fps'.format(str(round(frame_rate))), 1, TEXT_COLOR)
#                textpos = pygame.Rect(10, 10, 140, 17)
#                background.blit(text, textpos)
#                screen.blit(background, (0, 0))
#                last_frame_rate = frame_rate
         


        #Draw Everything
        allsprites.draw(screen)
        pygame.display.flip()
        
        # handles the exit event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
          
    pygame.quit()
    
# Calls the main funcion
if __name__=="__main__":
    main()
        
