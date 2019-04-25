"""
A moving shape in a bounded screen.

@author: Nima Sanjabi
Created on Wed Apr 24 16:14:45 2019
"""

import pygame
import sys
from lib import utils

if not pygame.font: print ('Warning, fonts disabled')

# game constants
NOMINAL_FRAME_RATE = 12000
SCREEN_WIDTH, SCREEN_HEIGHT = 480, 300
SJAPE_WIDTH, SHAPE_HEIGHT = 64, 64

BG_COLOR=(0, 0, 0)
SHAPES_COLOR = (136, 187, 0)
TEXT_COLOR = (17, 119, 136)
    
class MovingShape():
    """Defines a rectangle shape."""
    def __init__(self,left, top, width, height):
        self.shape_rect=pygame.Rect(left, top, width, height)
        self.color=(SHAPES_COLOR)
        self.screen = pygame.display.get_surface()
        print('screen', self.screen)
        
    def set_pos_size(self,left, top, width, height):
        """sets the position of the top left corrner of
        the player rectangle."""
        self.shape_rect=pygame.Rect(left, top, width, height)

    def display_shape(self, color, rect):
        """draw the initiated shape."""        
        pygame.draw.rect(self.screen, color, rect)
        
    def move_shape(self, x_move, y_move):
        """move the shape by x and y steps. Before each 
        move, the previous position on the last frame is
        repainted()erased with black color."""
        self.display_shape(BG_COLOR, self.shape_rect)           
        self.shape_rect=self.shape_rect.move(x_move,y_move)
  
def main():
    """this function is called when the program starts.
       it initializes everything it needs, then runs in
       a loop until the function returns."""
       
    #Initialize Everything     
    pygame.init()
    x_move, y_move = 1, 1
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    background = pygame.Surface(screen.get_size())
    background.fill(BG_COLOR)
    
    # a list as a buffer to save the recent samples of frame rate
    BUFFER_SIZE=10
    frame_rate_buffer=[0]*BUFFER_SIZE
    last_frame_rate=0
    frame_counter=0
    clock=pygame.time.Clock()
    
    # creates a shape object from the MovingShape class
    shape_1=MovingShape(0, 0, SJAPE_WIDTH, SHAPE_HEIGHT)
    shape_1.set_pos_size(40,40,SJAPE_WIDTH,SHAPE_HEIGHT)
    shape_1.display_shape(shape_1.color, shape_1.shape_rect)
    
    # main loop
    while True: 
        # a clock keeps the frame rate to a fixed number
        clock.tick(NOMINAL_FRAME_RATE)
        frame_counter+=1
        #move the shape 1 step
        shape_1.move_shape(x_move,y_move)
        shape_1.display_shape(shape_1.color, shape_1.shape_rect)
        pygame.display.update()

        # reverse the shape when it colides with the screen walls       
        rect_1=shape_1.shape_rect
        if rect_1.left < 0 or rect_1.right > SCREEN_WIDTH:
            x_move = -x_move
        if rect_1.top < 0 or rect_1.bottom > SCREEN_HEIGHT:
            y_move = -y_move
  
        
        """ displays the real frame rate which might be different
        from the nominal frame rate."""
        if frame_counter > 20:
            frame_counter=0
            if pygame.font:
                font = pygame.font.Font(None, 24)
                # erase the last text with black color
                text = font.render('Frame rate: {} fps'.format(str(round(last_frame_rate))), 1, BG_COLOR)
                textpos = pygame.Rect(10, 10, 140, 17)
                background.blit(text, textpos)
                screen.blit(background, (0, 0))
                
                #get the frame rate            
                frame_rate = utils.list_average(utils.shift_buffer(frame_rate_buffer, clock.get_fps()))
                #frame_rate = clock.get_fps()
                
                # write the frame rate on the screen with red color
                text = font.render('Frame rate: {} fps'.format(str(round(frame_rate))), 1, TEXT_COLOR)
                textpos = pygame.Rect(10, 10, 140, 17)
                background.blit(text, textpos)
                screen.blit(background, (0, 0))
                last_frame_rate = frame_rate
            
        # handles the exit event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
          
    pygame.quit()
    
# Calls the main funcion
if __name__=="__main__":
    main()
        
