import sys, random, pygame

screen_width = 600
screen_height = 600

pygame.init()
screen = pygame.display.set_mode((screen_width,screen_height))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((255,0,0))
    rect = pygame.Rect(100,100,200,200)
    pygame.draw.rect(screen,(255,255,255),rect)


    pygame.display.update()