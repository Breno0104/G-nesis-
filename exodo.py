import pygame
from gui import Genisis
from asteroides import asteroide
from ptojetil import shot
import random
# inicializando o pygame e criando a janela
pygame.init()

display = pygame.display.set_mode([840, 480])
pygame.display.set_caption("monster attk")

#objetcs
objetcgroup = pygame.sprite.Group()
asteroidegroup = pygame.sprite.Group()
shotgroup = pygame.sprite.Group()

#pontuação
score = 0
font = pygame.font.Font('fonte/Arial.ttf', 20 )
text = font.render("score :"+ str(score),True, (0, 255,0), (0,0,0))
textRect = text.get_rect()
textRect.center = (420, 20)


#background
bg = pygame.sprite.Sprite(objetcgroup)
bg.image = pygame.image.load("data/espaço.png")
bg.image = pygame.transform.scale(bg.image,[840, 500])
bg.rect = bg.image.get_rect()




player = Genisis(objetcgroup)
aste1 = asteroide(objetcgroup)



#music
pygame.mixer.music.load("data/music1.wav")
pygame.mixer.music.play(-1)

#sounds
shoot = pygame.mixer.Sound("data/rlaunch.wav")




gameloop = True
gameover = False
timer = 20
clock = pygame.time.Clock()
if __name__ == "__main__":
    while gameloop:
        clock.tick(60)
        for event in  pygame.event.get():
            if event.type == pygame.QUIT:
                gameloop = False
            elif event.type == pygame.KEYDOWN:
               if event.key == pygame.K_SPACE and not gameover:
                   shoot.play()
                   newshot = shot(objetcgroup, shotgroup)
                   newshot.rect.center = player.rect.center

        #update logic:
        if not gameover:
            objetcgroup.update()
            timer += 1.8
            if timer > 30:
                timer = 0
                if random.random() <0.5:
                    novoasteroide = asteroide(objetcgroup, asteroidegroup)



            colisao = pygame.sprite.spritecollide(player, asteroidegroup, False,pygame.sprite.collide_mask)




            if colisao:
               gameover = True
               bg1 = pygame.sprite.Sprite(objetcgroup)
               bg1.image = pygame.image.load("data/game_over_.png")
               bg1.image = pygame.transform.scale(bg1.image, [480, 300])
               bg1.rect = bg1.image.get_rect()
               bg1.rect.center = (420, 200)
               pygame.mixer.music.load("data/music2.wav")
               pygame.mixer.music.play(-1)


            hits = pygame.sprite.groupcollide(shotgroup, asteroidegroup, True, True,pygame.sprite.collide_mask)
            if hits:
                score= score+1
                text = font.render("score : " + str(score), True, (0, 255, 0), (0, 0, 0))






        #draw:
        display.fill([46, 46, 46])
        objetcgroup.draw(display)
        display.blit(text, textRect)
        pygame.display.update()




