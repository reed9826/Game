import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((1000, 1000))
img = "bullet.PNG"

i = 0

while True:
    image = pygame.image.load(img)
    w, h = image.get_size()
    box = [pygame.math.Vector2(k) for k in [(0, 0), (w, 0), (w, -h), (0, -h)]]
    br = [k.rotate(i) for k in box]
    mib = (min(br, key=lambda p: p[0])[0], min(br, key=lambda p: p[1])[1])
    mab = (max(br, key=lambda p: p[0])[0], max(br, key=lambda p: p[1])[1])

    pivot = pygame.math.Vector2(w / 2,- h / 2)  # Center of the image
    pr = pivot.rotate(i)
    pm = pr - pivot
    origin = (500 - pm.x, 500 - pm.y)  # Center of the screen

    rotated_image = pygame.transform.rotate(image, i)
    screen.fill((0, 0, 0))  # Clear the screen
    screen.blit(rotated_image, origin)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        i += 1
    if key[pygame.K_RIGHT]:
        i -= 1

    pygame.display.flip()
