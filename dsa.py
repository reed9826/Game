import pygame
import sys
pygame.init()

screen = pygame.display.set_mode((1000,600))

c = pygame.time.Clock()
fps = 60

class player:

  h = 10
  w = 10
  position = pygame.Vector2(500, 300)
  # Movement speed (adjust this value to control overall speed)
  speed =  1  

  def movement():
    key = pygame.key.get_pressed()
    # Initialize movement vector
    move_vec = pygame.Vector2(0, 0)

    if key[pygame.K_a]:
      move_vec.x = -player.speed

    if key[pygame.K_d]:
      move_vec.x = player.speed

    if key[pygame.K_w]:
      move_vec.y = -player.speed

    if key[pygame.K_s]:
      move_vec.y = player.speed

    # Normalize the movement vector to ensure same speed in all directions
    if move_vec.x != 0 and move_vec.y != 0:
      move_vec.normalize()  # Makes the vector length 1

    # Update player position based on the normalized movement vector and speed
    player.position += move_vec * player.speed

    return player.position

  def present():
    return pygame.draw.rect(screen, (244, 34, 122), (player.position.x, player.position.y, player.h, player.w))


while 1:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit()


  screen.fill((0, 0, 0))
  player.movement()
  player.present()


  pygame.display.flip()
  pygame.display.update()
  c.tick(fps)
