import pygame
import random

# Inicializa o pygame
pygame.init()

# Configurações da tela
screen_width, screen_height = 1680, 960
display = pygame.display.set_mode([screen_width, screen_height])
pygame.display.set_caption("Mate-mágico")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 74)  # Fonte para o texto
small_font = pygame.font.Font(None, 50)  # Fonte menor para balão

# Carrega a imagem de fundo
background = pygame.image.load("assests/9956010-pixel-art-game-cena-na-neve-com-pinheiros-nuvens-e-pedra-fundo-de-8-bits-vetor.jpg")
background = pygame.transform.scale(background, (screen_width, screen_height))

# Configuração do personagem
drawgroup = pygame.sprite.Group()
guy = pygame.sprite.Sprite(drawgroup)
guy.image = pygame.image.load("assests/download.png")
guy.image = pygame.transform.scale(guy.image, [124, 124])
guy.rect = pygame.Rect(100, screen_height // 2 - 62, 100, 100)  # Posição inicial

# Variável de velocidade
speed = 5

# Posicionamento das árvores (coordenadas fixas)
tree_positions = [600, 1200]  # Coordenadas fixas relativas ao fundo
tree_offset = 0  # Offset que acompanha o movimento das árvores

# Variáveis de controle
paused = False
current_tree_index = 0
current_question = ""
correct_answer = 0
user_input = ""

# Posição do fundo
bg_x1 = 0  # Primeira imagem do fundo
bg_x2 = screen_width  # Segunda imagem do fundo

# Função para gerar uma pergunta matemática
def generate_question():
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    question = f"{a} + {b} = ?"
    answer = a + b
    return question, answer

# Função para reiniciar o jogo ao errar a resposta
def reset_game():
    global bg_x1, bg_x2, tree_offset, guy
    guy.rect.x = 100  # Personagem volta ao início
    tree_offset = 0   # Reseta o deslocamento das árvores
    bg_x1 = 0         # Reseta a posição do fundo
    bg_x2 = screen_width

# Loop do jogo
gameloop = True
while gameloop:
    clock.tick(60)  # Limita o jogo a 60 quadros por segundo

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameloop = False
        
        if paused:  # Se o jogo estiver pausado, captura input do teclado
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  # Verifica a resposta
                    if user_input.isdigit() and int(user_input) == correct_answer:
                        # Resposta correta: vai para a próxima árvore
                        paused = False
                        user_input = ""
                        current_tree_index += 1
                        if current_tree_index >= len(tree_positions):  # Reinicia ao passar por todas as árvores
                            current_tree_index = 0
                    else:
                        # Resposta errada: reseta o jogo
                        reset_game()
                        paused = False
                        user_input = ""
                        current_tree_index = 0
                elif event.key == pygame.K_BACKSPACE:  # Apaga um caractere
                    user_input = user_input[:-1]
                else:
                    user_input += event.unicode  # Adiciona o input do usuário

    if not paused:
        # Movimento do fundo para a esquerda
        bg_x1 -= speed
        bg_x2 -= speed

        # Reposiciona o fundo para criar um loop
        if bg_x1 <= -screen_width:
            bg_x1 = screen_width
        if bg_x2 <= -screen_width:
            bg_x2 = screen_width

        # Movimento do personagem e árvores
        guy.rect.x += speed
        tree_offset -= speed

        # Verifica se o personagem chegou na árvore atual
        tree_x = tree_positions[current_tree_index] + tree_offset
        if abs(guy.rect.x - tree_x) < 10:
            paused = True
            current_question, correct_answer = generate_question()

    # Desenha o fundo em loop
    display.blit(background, (bg_x1, 0))
    display.blit(background, (bg_x2, 0))

    # Desenha o personagem
    drawgroup.draw(display)

    # Desenha o balão de pensamento e a pergunta quando parado
    if paused:
        pygame.draw.rect(display, (255, 255, 255), (guy.rect.x - 50, guy.rect.y - 100, 300, 100))  # Balão
        pygame.draw.circle(display, (255, 255, 255), (guy.rect.x + 20, guy.rect.y - 30), 10)
        pygame.draw.circle(display, (255, 255, 255), (guy.rect.x + 30, guy.rect.y - 20), 5)
        question_text = small_font.render(current_question, True, (0, 0, 0))
        display.blit(question_text, (guy.rect.x - 40, guy.rect.y - 90))

        # Mostra a resposta do usuário
        input_text = font.render(user_input, True, (0, 0, 0))
        display.blit(input_text, (guy.rect.x - 40, guy.rect.y - 40))

    pygame.display.update()

pygame.quit()