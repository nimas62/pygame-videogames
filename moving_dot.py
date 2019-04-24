"""
an initial blank screen for a pygame video game

@author: Nima Created on Wed Apr 24 16:14:45 2019
"""

import pygame
   
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
        pygame.display.update()
    pygame.quit()
    
# game main loop
if __name__=="__main__":
    main()
        