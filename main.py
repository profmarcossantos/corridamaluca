import pygame
import random
pygame.init()
tamanho = (1000,592)
clock = pygame.time.Clock()
tela = pygame.display.set_mode( tamanho )
icone = pygame.image.load("assets/icone.ico")
pygame.display.set_icon(icone)
pygame.display.set_caption("Corrida Maluca")
branco = (255,255,255)
preta = (0,0,0)
fundo = pygame.image.load("assets/fundo.png")
carro1 = pygame.image.load("assets/carro1.png")
carro2 = pygame.image.load("assets/carro2.png")

movXCar1 = 0
movXCar2 = 0
posYCar1 = 50
posYCar2 = 180
vitoria = pygame.mixer.Sound("assets/vitoria.mp3")
vitoria.set_volume(0.5)
pygame.mixer.music.load("assets/trilha.mp3")
pygame.mixer.music.play(-1) #-1 looping, 1,2 3 vezes
acabou = False
somDaVitoria = False
while True:
    for evento in pygame.event.get(): 
        if evento.type == pygame.QUIT:
            quit()
   
    tela.fill( branco )
    tela.blit(fundo, (0,0))
    tela.blit(carro1, (movXCar1,posYCar1))
    tela.blit(carro2, (movXCar2,posYCar2))
    
    if not acabou :
        movXCar1 = movXCar1 + random.randint(0,10)
        movXCar2 = movXCar2 + random.randint(0,10)
    else:
        pygame.mixer.music.stop()
        if somDaVitoria == False:
            pygame.mixer.Sound.play(vitoria)
            somDaVitoria = True
        
    
    if movXCar1 > 1000:
        movXCar1 = 0
        posYCar1 = 350
        
    if movXCar2 > 1000:
        movXCar2 = 0
        posYCar2 = 480
    
    fonte = pygame.font.Font("freesansbold.ttf",60)
    textoVermelho = fonte.render("Vermelho Ganhou!", True, branco)
    textoAmarelo = fonte.render("Amarelo Ganhou!", True, branco)
    
    if posYCar1 == 350 and movXCar1 >= 900 and movXCar1 > movXCar2:
        tela.blit(textoVermelho, (270,70))
        acabou = True
        
    elif posYCar2 == 480 and movXCar2 >= 900 and movXCar2 > movXCar1:
        tela.blit(textoAmarelo, (270,180))
        acabou = True
    
    
    pygame.display.update()
    clock.tick(60)
pygame.quit()
    

