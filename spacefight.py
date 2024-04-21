import pygame
import sys
import math


pygame.init()


ss = pygame.display.get_desktop_sizes()
print(ss)
screen = pygame.display.set_mode(ss[0])
def d2r(d):
    s = d*(math.pi/180)
    return s




class player:
    x = 1000
    y = 600
    img = "gh.PNG"
    d = 720
    def movementx():
        key = pygame.key.get_pressed()
        if key[pygame.K_a] and player.x >= 0:
            player.x -= 3
            
        if key[pygame.K_d] and player.x <=ss[0][0]-100:
            player.x += 3

    def movementy():
        key = pygame.key.get_pressed()
        if key[pygame.K_w] and player.y >=0:
            player.y -= 3
            
        if key[pygame.K_s] and player.y <= ss[0][1]-100:
            player.y+= 3
        
    def rotate():
        
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            player.d +=1
        if key[pygame.K_RIGHT]:
            player.d -= 1
        if player.d >= 360:
            player.d = 0
        if player.d <= 0:
            player.d = 360

    def cs():
        print("x : " + str(player.x)+"  | y : "+ str(player.y)+ " | D : "+str(player.d))  
        
        

    def show():

        im = pygame.image.load(player.img)


        w, h = im.get_size()
            
            
        box = [pygame.math.Vector2(p) for p in [(0, 0), (w, 0), (w, -h), (0, -h)]]
            
        box_rotate = [p.rotate(player.d) for p in box]
            

        min_box = (min(box_rotate, key=lambda p: p[0])[0], min(box_rotate, key=lambda p: p[1])[1])
            
        max_box = (max(box_rotate, key=lambda p: p[0])[0], max(box_rotate, key=lambda p: p[1])[1])
        pivot = pygame.math.Vector2(w/2, -h/2)
            
        pivot_rotate = pivot.rotate(player.d)

        pivot_move   = pivot_rotate - pivot
                
        origin = (player.x + min_box[0] - pivot_move[0],  player.y - max_box[1] + pivot_move[1])
        X = (origin[0]*math.cos(d2r(player.d)) + origin[1]*math.sin(d2r(player.d))) + origin[0]
        Y = (origin[1]*math.cos(d2r(player.d)) + origin[1]*math.sin(d2r(player.d))) + origin[1]         
        rotated_image = pygame.transform.rotate(im, player.d)
        screen.blit(rotated_image, (X,Y))
        

    def  attack():
        bullet = []
        h = player.x
        k = player.y
        bx = 0
        by = 0
        bulletorigin = (bx+h,by+k)



        
        key = pygame.key.get_pressed()

        if key[pygame.K_SPACE]:

            im = pygame.image.load("bullet.PNG")


            w, h = im.get_size()
            
      
            box = [pygame.math.Vector2(p) for p in [(0, 0), (w, 0), (w, -h), (0, -h)]]
           
            box_rotate = [p.rotate(player.d) for p in box]
         

            min_box = (min(box_rotate, key=lambda p: p[0])[0], min(box_rotate, key=lambda p: p[1])[1])
       
            max_box = (max(box_rotate, key=lambda p: p[0])[0], max(box_rotate, key=lambda p: p[1])[1])
        
            pivot = pygame.math.Vector2(w/2, -h/2)
          
            pivot_rotate = pivot.rotate(player.d)
 
            pivot_move   = pivot_rotate - pivot

            origin = [player.x + min_box[0] - pivot_move[0] + 55, player.y - max_box[1] + pivot_move[1]]

            rotated_image = pygame.transform.rotate(im, player.d)


            screen.blit(rotated_image,origin) 


        for i in bullet:

            i[0]+=1
            
            screen.blit(rotated_image,(i[0],i[1]))
                
            


    
while 1:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_1:
            pygame.quit()
            sys.exit()


    screen.fill((0,0,0))
    player.movementx()
    player.movementy()
    player.rotate()
    player.cs()
    player.attack()
    player.show()
    pygame.display.flip()
    pygame.display.update()

