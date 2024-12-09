import pygame
pygame.init()       # Inicia o pygame

display = pygame.display.set_mode([1680, 960])
clock = pygame.time.Clock()

'''            ^^^
* Abre uma tela na resoluçao do pc;
* O 'Display = ...' serve para a tela virar um CANVA (para "Desenhar" nele) 
--->   display = DISPLAYSURF = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)   <---Voce pode usar esse para tela cheia
'''

pygame.display.set_caption("Mate-magico")        # Da um nome para sua janela

drawgroup = pygame.sprite.Group()                           # Cria agrupamento de sprites que ser'ao desenhados
guy = pygame.sprite.Sprite(drawgroup)                       # Define o 'bonequinho' do grupo (jogador)
guy.image = pygame.image.load("assests\download.png")         # Carrega o boneco como a imagem
guy.image = pygame.transform.scale(guy.image,[124, 124])    # Escala ele nas especificações
guy.rect = pygame.Rect(50, 50, 100, 100)                   # O posiciona

gameloop = True     # loop para manter a tela "rodando" ate ter algum comado de sair do jogo (encerrar loop)
while gameloop:
    clock.tick(60)                                 # Limita o jogo a 60 quadros por segundo

    keys = pygame.key.get_pressed()               #Variavel que permite manter pressionado (para nao ter que ficar apertando varias vezes ao mover o boneco)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameloop = False  # Sai do loop
        elif event.type == pygame.VIDEORESIZE:                                       # Verifica se a janela foi redimensionada
            display = pygame.display.set_mode(event.size, pygame.RESIZABLE)          # Ajusta o tamanho da janela
        elif keys[pygame.K_d]:                                                               # Se a tecla (K = Key) d for apertada, faça:
            guy.rect.x += 5                                                                  #Faça isso aqui (some dois pixels no eixo 'x')
            '''^^^^^^
                                            *"Keys" foi definido como (manter pressionado)
                                            *Se você deseja apertar uma vez por tecla, use este comando no lugar:
                                            elif event.type == pygame.KEYDOWN:
                                            if event.key == pygame.K_d: (e na proxima linha escreva o que deve acontecer)'''
        elif keys[pygame.K_a]:
            guy.rect.x -= 5
        elif keys[pygame.K_w]:
            guy.rect.y -= 5
        elif keys[pygame.K_s]:
            guy.rect.y += 5

        display.fill([24, 18, 89])        # Preenche a tela aberta com uma cor, ela e definida por RGB(Red Green Blue); Basta digitar 'Color Pick' no Google e ele te da os valores
        drawgroup.draw(display)           # Desenha o que foi especificado no drawgroup, exibindo-o no (display)
        pygame.display.update()           # Atualiza a janela
