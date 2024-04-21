import pygame
import sys
import random
import math
import time


#font
pygame.font.init()

#screen
pygame.init()

#setting screen size 
screen = pygame.display.set_mode((1000,600))

#player's information
class player:
    x = 100
    y =100
    position= pygame.Vector2(100,100)
    size = pygame.Vector2(10,10)

#storing player's information outsidee of the vector
px = player.position.x
py = player.position.y


#selecting font for the time text
font = pygame.font.SysFont("comicsans",30)




clock = pygame.time.Clock()


starttime = time.time()
elspad = 0


starms = 2000    #star will increase in 2 millisec  ond
starcount = 0    #nahi pata
stars= []        #a list in which all the stars are stored
hit = 0          #iska nahi pata
while 1:


    starcount += clock.tick(60)         #nahi pta
    elspad = round(time.time() - starttime, 2)      #nahi pata
    if starcount > starms:          #if no of stars i
        for _ in range(5):
            starx = random.randint(0,1000-50)
            star = pygame.Rect(starx,-10,50,50)
            stars.append(star)
        starms = max(100,starms -50)
        starcount = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            
          sys.exit()

    

    for star in stars[:]:
        star.y += 1
        if star.y > 600:
            stars.remove(star)
        elif star.y == py :
            stars.remove(star)
            sys.exit()
        
        
    key = pygame.key.get_pressed()
    if key[pygame.K_a] and px >= 0:
        px -=10
        

    if key[pygame.K_d] and px <= 988-90:
        px +=10
        
    # if hit:
    #     lt = font.render("You lost!",1,"white")
    #     screen.blit(lt,(600 - lt.get_width()/2,1000 - lt.get_height()/2))
    #     pygame.display.update()
    #     pygame.time.delay(10000)  
    #     sys.exit()
        
    # if key[pygame.K_w] and py >= 0:
    #     py -= 1
        
    # if key[pygame.K_s] and py <=600-12:
    #     py +=1
        
    
    
    # if key[pygame.K_UP] and cy >=1:
    #     cy -=1
        

    # if key[pygame.K_DOWN] and cy <= 600:
    #     cy +=1
        
        
        
    # if key[pygame.K_RIGHT] and cx <= 988:
    #     cx += 1
        
    # if key[pygame.K_LEFT] and cx >=0:
    #     cx -=1
   


    screen.fill((0,0,0))

    time_text = font.render(f"Time: {(elspad)}s", 1,"blue")
    screen.blit(time_text,(10,10))
    for star in stars:
        pygame.draw.rect(screen,"red",star)
    pygame.draw.rect(screen,(222,225,225),(px,600-102,10,10))
    
   
    # x+=1
    # y += 1
    # for i,obj in enumerate(objects):
    #      x,y= obj
    #      #random.randint(-4,4)*x+ random.randint(1,10)
         
    #      pygame.draw.circle(screen,(244,34,0),(x,y),10)






        
    

    pygame.display.flip()
    pygame.display.update()
    

