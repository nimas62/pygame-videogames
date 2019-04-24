"""
an initial blank screen for a pygame video game

@author: Nima Created on Wed Apr 24 16:14:45 2019
"""

import pygame
import sys

class MovingDot():
    def __init__(self):
        
        self.rect_pos=(0, 0, 64, 64)
        player_rect=pygame.Rect(self.rect_pos)
        self.color=(255, 0, 0)
        screen = pygame.display.get_surface()
        pygame.draw.rect(screen, self.color, player_rect)
        
    def get_size(self,left,top,width,height):
        self.rect_pos=()
        
        
  
def main():
    """this function is called when the program starts.
       it initializes everything it needs, then runs in
       a loop until the function returns."""
    #Initialize Everything     
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock=pygame.time.Clock()
    
    # main loop
    while True: 
        # a clock keeps the frame rate under 60
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        dot_1=MovingDot()
        pygame.display.update()
    pygame.quit()
    
# game main loop
if __name__=="__main__":
    main()
        