import pygame,sys,random,time,math


pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((1000,600))
caption = pygame.display.set_caption("doge game")
path = r"C:\Users\reedr\Downloads\_623ce0dd-dff3-4c9b-a4ad-868e9d7ca9c7.jpeg"
img =pygame.image.load(path)
pygame.display.set_icon(img)

fot = pygame.font.Font("freesansbold.ttf",10)
text1 = fot.render('Score :', True, (0, 255, 0))
fot = fot.render('GeeksForGeeks', True, (0,111,234), (123,231,122))
# t1 = text1.centre(10,10)
c = pygame.time.Clock()
fps = 60

class player:

    h = 10
    w = 10
    position= pygame.Vector2(500,300)

    def movementx():
        key = pygame.key.get_pressed()
        if key[pygame.K_a] and player.position.x >= 0:

            player.position.x -= 5
            return player.position.x

        elif key[pygame.K_d]:
            if player.position.x == 990:
                player.position.x = 990

            else:
                
                player.position.x +=   5
                return player.position.x

    def movementy():
        key = pygame.key.get_pressed()
        if key[pygame.K_w] and player.position.y >= 0:
            player.position.y -= 5
            
            return player.position.y

        elif key[pygame.K_s]:
            if player.position.y ==590:
     
                player.position.y += 0
                return player.position.y

            else:
                player.position.y += 5
                
                return player.position.y
    def present():
        return pygame.draw.rect(screen,(244,34,122),(player.position.x,player.position.y,player.h,player.w))
start = time.time()
elsapd = 0
sr = screen.get_rect()
class enemy:
    cms = 2000
    ccount = 0
    cs =[]

    def spawn():
        enemy.ccount +=c.get_time()
        elsapd = time.time() - start
        if enemy.ccount > enemy.cms:
            for i in range(random.randint(0,16)):
                cx = random.randint(-450,0)
                cy = random.randint(-800,0)

                    
                
                appp= pygame.draw.circle(screen,(random.randint(50,255),random.randint(50,255),random.randint(50,255)),(cx,cy),random.randint(1,20))
                enemy.cs.append(appp)
            

            enemy.cms = max(100,enemy.cms-10)
            enemy.ccount = 0

        return enemy.ccount
        return enemy.cms
        return enemy.cs

    def delenemy():
        for scar in enemy.cs[:]:
            scar.x +=2
            scar.y +=3
            if scar.x > 1000 or scar.y > 600:
                enemy.cs.remove(scar)

            

    def present():
        for i in enemy.cs:
            pygame.draw.circle(screen,(33,123,32),(i.x,i.y),20)
            distance = math.sqrt(((i.x - player.position.x) ** 2) + ((i.y - player.position.y) ** 2))
            
            if distance <= player.w + 10 or distance <= player.h + 10:  # Adjust this value based on player and enemy sizes
                # Collision detected! Perform actions (e.g., end game, lose life)
                print("Collision detected!")
                sys.exit()
            
            
 
while 1:



    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()



    screen.fill((0,0,0))
    
    player.movementx()
    player.movementy()
    player.present()
    enemy.spawn()
    enemy.delenemy()
    enemy.present()

    pygame.display.flip()
    pygame.display.update()

    c.tick(fps)
