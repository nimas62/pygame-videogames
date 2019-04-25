"""
an initial blank screen for a pygame video game

@author: Nima Created on Wed Apr 24 16:14:45 2019
"""

import pygame
import sys

if not pygame.font: print ('Warning, fonts disabled')

class MovingShape():
    """Defines a rectangle shape."""
    def __init__(self,left, top, width, height):
        self.shape_rect=pygame.Rect(left, top, width, height)
        self.color=(255, 0, 0)
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
        black_color=(0, 0, 0)
        self.display_shape(black_color, self.shape_rect)           
        self.shape_rect=self.shape_rect.move(x_move,y_move)
     
  
def main():
    """this function is called when the program starts.
       it initializes everything it needs, then runs in
       a loop until the function returns."""
       
    #Initialize Everything     
    pygame.init()
    screen_width, screen_height = 800, 400
    x_move, y_move = 1, 1
    screen = pygame.display.set_mode((screen_width, screen_height))
    background = pygame.Surface(screen.get_size())
    last_frame_rate=0
    clock=pygame.time.Clock()
    
    # creates a shape object from the MovingShape class
    shape_1=MovingShape(0, 0, 64, 64)
    shape_1.set_pos_size(40,40,64,64)
    shape_1.display_shape(shape_1.color, shape_1.shape_rect)
    
    # main loop
    while True: 
        # a clock keeps the frame rate to a fixed number
        clock.tick(480)
        
        #move the shape 1 step
        shape_1.move_shape(x_move,y_move)
        shape_1.display_shape(shape_1.color, shape_1.shape_rect)
        pygame.display.update()

        # reverse the shape when it colides with the screen walls       
        rect_1=shape_1.shape_rect
        if rect_1.left < 0 or rect_1.right > screen_width:
            x_move = -x_move
        if rect_1.top < 0 or rect_1.bottom > screen_height:
            y_move = -y_move
  
        
        # displays the real frame rate which might be different
        from the nominal frame rate.
        if pygame.font:
            font = pygame.font.Font(None, 24)
            # erase the last text with black color
            text = font.render('Frame rate: {} fps'.format(str(round(last_frame_rate))), 1, (0, 0, 0))
            textpos = pygame.Rect(10, 10, 140, 17)
            background.blit(text, textpos)
            screen.blit(background, (0, 0))
            
            #get the frame rate
            frame_rate=clock.get_fps()
            
            # write the frame rate on the screen with red color
            text = font.render('Frame rate: {} fps'.format(str(round(frame_rate))), 1, (255, 0, 0))
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
        
