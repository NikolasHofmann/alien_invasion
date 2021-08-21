import pygame
from random import randint
from time import sleep

pygame.init()
window = (1200,800)
screen = pygame.display.set_mode(window)

background = pygame.Surface(window)

background.fill((255,90,0))


# left, right, width, height #



def villager_starting_position(colony):
    #find the outer edges of colony
    left_top = (colony[0], colony[1])
    left_bottom = (left_top[0], left_top[1] + colony[2])
    right_bottom = (left_bottom + colony[2], left_bottom[1])
    right_top = (right_bottom[0], right_bottom[1] - colony[2])

    

    starting_left_top = (left_top[0] - 1, left_top[1] - 1)
    starting_left_bottom = (left_bottom[0] - 1, left_bottom[1] + 1)
    starting_right_bottom = (right_bottom[0] + 1, right_bottom[1] + 1)
    starting_right_top = (right_top[0] + 1, right_top[1] - 1)


    all_positions = []
    while starting_left_top != starting_left_bottom:
        all_positions.append(starting_left_top)
        starting_left_top = (starting_left_top[0], starting_left_top[1] - 1)
    
    while starting_left_bottom != starting_right_bottom:
        all_positions.append(starting_left_bottom)
        starting_left_bottom = (starting_left_bottom[0] + 1, starting_left_bottom[1])

    while starting_right_bottom != starting_right_top:
        all_positions.append(starting_right_bottom)
        starting_right_bottom = (starting_right_bottom[0], starting_right_bottom[1] - 1)

    while starting_right_top != starting_left_top:
        all_positions.append(starting_right_bottom)
        starting_right_bottom = (starting_right_bottom[0] + 1, starting_right_bottom[1])

    return(all_positions)




class Villager():
    def __init__(self, size, colony, position = (left_top[0] - 1, left_top[1] - 1), color=rgb((51, 153, 255))):
        self.position = position
        self.size = size
        self.color = color
        self.colony = colony

    def randomize_position(self):
        position = villager_starting_position(self.colony)
        random1 = randint(0, len(position) - 1)
        position = position[random1]
        self.position = position

        


    def rectangle():
        rectangle = pygame.Rect(position, size)
        return rectangle
    

class Colony():
    def __init__(self, position, size, population, color=rgb((204, 0, 204))):
        self.position = position
        self.population = population
        self.size = size
        self.population = population
        self.color = color
        self.rectangle = pygame.Rect(position, size)

    def randomize_position(self):
        self.position = (randint(1, window[0]), randint(1, window[1]))

    def rectangle(self.position, self.size):
        rectangle = pygame.Rect(self.position, self.size)
        return rectangle

    def spawn_villager(self, villager):
        # if position overlap colony_position: randomize again
        # make sure villager spawns at the edge of colony
        while pygame.Rect.colliderect(self.rectangle(), villager.rectangle()) or :
            villager.randomize_position()


        pygame.draw.rect(background, villager.color(), villager.rectangle())
        # not sure about blit. otherwise try blit(background, villager.position())
        # maybe move blit and flip to bottom of whole program?
        screen.blit(background, (0, 0))
        pygame.display.flip()
        return villager
        





village = Colony(window, (20, 20), (80, 80), 2)





rectangle = pygame.Rect(20, 20, 80, 80)
# left, right, width, height

pygame.draw.rect(background,(randint(0, 255),randint(0, 255),randint(0, 255)), rectangle)

screen.blit(background, (0, 0))
pygame.display.flip()
        


#screen.blit(background, (0, 0))
#pygame.display.flip()

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

pygame.quit()

