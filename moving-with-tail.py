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
NOMINAL_FRAME_RATE = 12000
SCREEN_WIDTH, SCREEN_HEIGHT = 360, 240
SHAPE_WIDTH, SHAPE_HEIGHT = 8, 8
#X_MOVE, Y_MOVE = 1, 1
    
BG_COLOR=(0, 0, 0)
SHAPES_COLOR = (136, 187, 0)
TEXT_COLOR = (17, 119, 136)
    
class MovingShape(pygame.sprite.Sprite):
    """Defines a shape."""
    def __init__(self, color, shape_width, shape_height):
        # calls the Sprite initializer
        pygame.sprite.Sprite.__init__(self)
        self.rect=pygame.Rect(0, 0, SHAPE_WIDTH, SHAPE_HEIGHT)
        self.image=pygame.Surface([SHAPE_WIDTH, SHAPE_HEIGHT])
        self.color=color
        self.image.fill(self.color)

    def move_shape(self, X_MOVE, Y_MOVE):
        """move the shape by x and y steps. Before each 
        move, the previous position on the last frame is
        repainted()erased with black color."""         
        self.rect=self.rect.move(X_MOVE,Y_MOVE)
        
def main():
    """this function is called when the program starts.
       it initializes everything it needs, then runs in
       a loop until the function returns."""
       
    #Initialize Everything     
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Bouncing square!')    
    background = pygame.Surface(screen.get_size())
    textpos = pygame.Rect(10, 10, 160, 17)
    
    if pygame.font:
        font = pygame.font.Font(None, 24)
    
    text = font.render('', 1, (255,0,0))
    
    X_MOVE, Y_MOVE = 1, 1
    # a list as a buffer to save the recent samples of frame rate
    BUFFER_SIZE=10
    frame_rate_buffer=[0]*BUFFER_SIZE
    frame_counter=0
    clock=pygame.time.Clock()

    # creates a shape object from the MovingShape class
    shape_1=MovingShape(SHAPES_COLOR, SHAPE_WIDTH, SHAPE_HEIGHT)
    tail_list=[shape_1.rect]*250

    # main loop
    while True:
        # a clock keeps the frame rate to a fixed number
        clock.tick(NOMINAL_FRAME_RATE)
        frame_counter+=1

        #move the shape 1 step
        shape_1.move_shape(X_MOVE,Y_MOVE)
        # reverse the shape when it colides with the screen walls       
        rect_1=shape_1.rect
        if rect_1.left < 0 or rect_1.right > SCREEN_WIDTH:
            X_MOVE = -X_MOVE
        if rect_1.top < 0 or rect_1.bottom > SCREEN_HEIGHT:
            Y_MOVE = -Y_MOVE
            
        utils.shift_buffer(tail_list, [rect_1.left,rect_1.top])

        """ displays the real frame rate which might be different
        from the nominal frame rate."""
        if frame_counter > 20:
            if pygame.font:
                frame_rate = utils.list_average(utils.shift_buffer(frame_rate_buffer, clock.get_fps()))
                # erase the last text with black color
                text = font.render('Frame rate: {} fps'.format(str(round(frame_rate))), 1, (255,0,0))
                frame_counter=0

        screen.blit(background, (0, 0))
        for key, value in enumerate(tail_list):
#            shape = MovingShape((0,(key*1),0), SHAPE_WIDTH, SHAPE_HEIGHT)
            rect=pygame.Rect(value[0],value[1], SHAPE_WIDTH, SHAPE_HEIGHT)
            pygame.draw.rect(screen, (0,(key*1),0), rect)

        #Draw Everything
        screen.blit(text, textpos)
        pygame.display.update()
        
        # handles the exit event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
          
    pygame.quit()
    
# Calls the main funcion
if __name__=="__main__":
    main()
        
