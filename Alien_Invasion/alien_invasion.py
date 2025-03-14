import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullets
from alien import Alien

class AlienInvasion:
    """Overall class to manage game assets and behaviour"""

    def __init__(self):
        """Initialize thr game and create game resources"""
        pygame.init()
        self.settings=Settings()

        self.screen=pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_width=self.screen.get_rect().width
        self.settings.screen_height=self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")
        self.ship=Ship(self)
        self.bullets=pygame.sprite.Group()
        self.aliens=pygame.sprite.Group()
        self._create_fleet()

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            self._check_events()
            self.ship.update()
            self.bullets.update()
            self._update_bullets()
            self._update_screen()

            
        
    def _check_events(self):
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)
                    
                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)
                    
    def _check_keydown_events(self,event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right=True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left=True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key==pygame.K_SPACE:
             self._fire_bullet()
                    
    def _check_keyup_events(self,event):
        if event.key == pygame.K_RIGHT:
             self.ship.moving_right=False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left=False
    
    def _fire_bullet(self):
         """Create a new bullet and ass it to the bullets group"""
         if len(self.bullets)< self.settings.bullets_allowed:
              new_bullet=Bullets(self)
              self.bullets.add(new_bullet)

    def _update_bullets(self):
         ##Getting rid of bullets that have disappeared
        for bullet in self.bullets.copy():
            if bullet.rect.bottom<=0:
                self.bullets.remove(bullet)
        #print(len(self.bullets))

    def _create_fleet(self):
        """Creating a fleet of aliens"""
        alien=Alien(self)
        alien_width=alien.rect.width
        available_space_x=self.settings.screen_width-(2*alien_width)
        number_aliens_x=available_space_x//(2*alien_width)

        ##Creating the first row of aliens
        for alien_number in range(number_aliens_x):
            alien=Alien(self)
            alien.x= alien_width+2*alien_width*alien_number
            alien.rect.x=alien.x
            self.aliens.add(alien)


    def _update_screen(self):
         # redraw the screen during each pass through the loop
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()
            for bullet in self.bullets.sprites():
                 bullet.draw_bullet()
            self.aliens.draw(self.screen)
            #Make the most recently drawn screen visible
            pygame.display.flip()
           

if __name__=="__main__":
    # MAke a game instance and run the game
    ai=AlienInvasion()
    ai.run_game()