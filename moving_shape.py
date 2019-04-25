"""
an initial blank screen for a pygame video game

@author: Nima Created on Wed Apr 24 16:14:45 2019
"""

import pygame
import sys

if not pygame.font: print ('Warning, fonts disabled')

class MovingShape():
    def __init__(self,left, top, width, height):
        self.shape_rect=pygame.Rect(left, top, width, height)
        self.color=(255, 0, 0)
        self.screen = pygame.display.get_surface()
        print('screen', self.screen)
    def set_pos_size(self,left, top, width, height):
        """sets the position of the top left corrner of the player rectangle"""
        self.shape_rect=pygame.Rect(left, top, width, height)

    def display_shape(self, color, rect):        
        pygame.draw.rect(self.screen, color, rect)
        
    def move_shape(self, x_move, y_move):
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
    shape_1=MovingShape(0, 0, 64, 64)
    shape_1.set_pos_size(40,40,64,64)
    shape_1.display_shape(shape_1.color, shape_1.shape_rect)
    # main loop
    while True: 
        # a clock keeps the frame rate under 60
        clock.tick(480)
        
        if pygame.font:
            font = pygame.font.Font(None, 24)
            text = font.render('Frame rate: {} fps'.format(str(round(last_frame_rate))), 1, (0, 0, 0))
            textpos = pygame.Rect(10, 10, 140, 17)
            background.blit(text, textpos)
            screen.blit(background, (0, 0))
            
            frame_rate=clock.get_fps()
#            print(frame_rate)
            
            text = font.render('Frame rate: {} fps'.format(str(round(frame_rate))), 1, (255, 0, 0))
            textpos = pygame.Rect(10, 10, 140, 17)
#            print(textpos)
            background.blit(text, textpos)
            screen.blit(background, (0, 0))
            last_frame_rate = frame_rate
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        shape_1.move_shape(x_move,y_move)
        shape_1.display_shape(shape_1.color, shape_1.shape_rect)
        

        
        pygame.display.update()
        
        rect_1=shape_1.shape_rect
        if rect_1.left < 0 or rect_1.right > screen_width:
            x_move = -x_move
        if rect_1.top < 0 or rect_1.bottom > screen_height:
            y_move = -y_move
  

            
    pygame.quit()
    
# game main loop
if __name__=="__main__":
    main()
        
