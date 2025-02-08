# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *


def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    
    Player.containers = updatable, drawable 
    Asteroid.containers = asteroids, updatable, drawable
    
    asteroid_field = pygame.sprite.Group()  # grupa musi pojawiac sie po przypisaniu containers przez Asteroids, bo korzysta z asteroids w swoim kodzie
    AsteroidField.containers = updatable 


    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    a_fields = AsteroidField()

    shots = pygame.sprite.Group()
    Shot.containers = shots, updatable, drawable


    #player.containers = (updatable, drawable) # teraz juz to nie potrzebne, ale nawet jakby bylo chyba lepiej uzywac bez nawiasu bo inaczej nie dziala bez "upacking" czyli gwiazdki w odniesieniu
    #updatable.add(player)
    #drawable.add(player)
    #updatable.add(AsteroidField)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill(color="black")
        updatable.update(dt)
        
        for asteroid in asteroids:
            if asteroid.collision(player):
                print("Game over!")
                sys.exit()
            for shot in shots:
                if shot.collision(asteroid):
                    asteroid.split()
                    shot.kill()
        
        for d in drawable:
            d.draw(screen)
        
        pygame.display.flip()
        dt = clock.tick(60)/1000



if __name__ == "__main__":
    main()

