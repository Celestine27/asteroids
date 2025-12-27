import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from logger import log_event, log_state



def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroid = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroid, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatable.update(dt)

        for rock in asteroid:
            if player.collisions(rock):
                log_event("Player_hit")
                print("Game over!")
                sys.exit()

            for shot in shots:
                if shot.collisions(rock):
                    log_event("asteroid_shot")
                    shot.kill()
                    rock.split()


            
        screen.fill("black")

        for drawing in drawable:
            drawing.draw(screen)

        pygame.display.flip()
        
        # Limit the framerate to 60 fps
        dt = clock.tick(60) / 1000
        

if __name__ == "__main__":
    main()
