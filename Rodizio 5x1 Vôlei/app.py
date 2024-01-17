import pygame
import sys

pygame.init()

largura, altura = 820, 400
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Rôdizio 5x1 Vôlei')


branco = (255, 255, 255)


background = pygame.image.load("fundo.png")
background = pygame.transform.scale(background, (largura, altura))


fonte = pygame.font.SysFont("montserrat", 36, True, True)


class Sprite(pygame.sprite.Sprite):
    def __init__(self, x, y, imagem, tamanho=(50, 50), delay_frames=0, velocidade=5):
        super(Sprite, self).__init__()
        self.carregar_imagem(imagem, tamanho)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.velocidade = velocidade
        self.caminho = []
        self.indice_caminho = 0
        self.movendo = False
        self.delay_frames = delay_frames
        self.current_frame = 0
        self.botao_ataque_ativado = False

    def carregar_imagem(self, nome_arquivo, tamanho):
        self.image = pygame.image.load(nome_arquivo)
        self.image = pygame.transform.scale(self.image, tamanho)

    def alterar_caminho(self, novo_caminho, delay_frames=0):
        if not self.botao_ataque_ativado:
            self.caminho = novo_caminho
            self.indice_caminho = 0
            self.delay_frames = delay_frames
            self.current_frame = 0

    def update(self):
        if self.current_frame < self.delay_frames:
            self.current_frame += 1
            return

        if self.movendo and self.indice_caminho < len(self.caminho):
            destino = self.caminho[self.indice_caminho]
            dx = destino[0] - self.rect.x
            dy = destino[1] - self.rect.y
            dist = (dx ** 2 + dy ** 2) ** 0.5

            if dist < self.velocidade:
                self.rect.topleft = destino
                self.indice_caminho += 1
            else:
                dx = dx / dist * self.velocidade
                dy = dy / dist * self.velocidade
                self.rect.x += dx
                self.rect.y += dy


#os 15 jogadores e a bola
sprite2 = Sprite(256, 254, "assets/timeA/Aponteiro1.png", tamanho=(50, 50), delay_frames=60, velocidade=5)
sprite2.alterar_caminho([(256, 254), (254, 59)], delay_frames=30)

sprite3 = Sprite(145, 70, "assets/timeA/Aponteiro2.png", tamanho=(50, 50), delay_frames=60, velocidade=5)
sprite3.alterar_caminho([(145, 70), (119, 160)], delay_frames=45)

sprite4 = Sprite(119, 166, "assets/timeA/Alibero.png", tamanho=(50, 50), delay_frames=60, velocidade=5)
sprite4.alterar_caminho([(119, 166), (145, 70)], delay_frames=40)

sprite5 = Sprite(254, 59, "assets/timeA/Aoposto.png", tamanho=(50, 50), delay_frames=60, velocidade=5)
sprite5.alterar_caminho([(254, 59), (256, 254)], delay_frames=35)

sprite6 = Sprite(22, 270, "assets/timeA/Alevantador.png", tamanho=(50, 50), delay_frames=60, velocidade=5)
sprite6.alterar_caminho([(22, 270), (145, 254)], delay_frames=50)

sprite7 = Sprite(279, 160, "assets/timeA/Acentral.png", tamanho=(50, 50), delay_frames=60, velocidade=5)
sprite7.alterar_caminho([(279, 160)], delay_frames=55)

sprite8 = Sprite(348, 265, "assets/timeB/Bcentral.png", tamanho=(50, 50), delay_frames=120, velocidade=5)
sprite8.alterar_caminho([(348, 265), (339, 170)], delay_frames=70)

sprite9 = Sprite(350, 59, "assets/timeB/Blevantador.png", tamanho=(50, 50), delay_frames=120, velocidade=6)
sprite9.alterar_caminho([(350, 59), (347, 120)], delay_frames=80)

sprite10 = Sprite(457, 69, "assets/timeB/Blibero.png", tamanho=(50, 50), delay_frames=110, velocidade=7)
sprite10.alterar_caminho([(457, 69),(510, 160), (440, 254)], delay_frames=65)

sprite11 = Sprite(520, 210, "assets/timeB/Boposto.png", tamanho=(50, 50), delay_frames=110, velocidade=7)
sprite11.alterar_caminho([(520, 210), (536, 106), (423, 50)], delay_frames=75)
sprite12 = Sprite(460, 230, "assets/timeB/Bponteiro1.png", tamanho=(50, 50), delay_frames=110, velocidade=5)
sprite12.alterar_caminho([(440, 254), (358, 254)], delay_frames=90)

sprite13 = Sprite(500, 150, "assets/timeB/Bponteiro2.png", tamanho=(50, 50), delay_frames=110, velocidade=5)
sprite13.alterar_caminho([(500, 150), (416, 140)], delay_frames=85)

sprite14 = Sprite(240, -50, "assets/timeA/Acentral2.png", tamanho=(50, 50), delay_frames=110, velocidade=5)
sprite13.alterar_caminho([(500, 150), (416, 140)], delay_frames=85)

sprite15 = Sprite(355, 450, "assets/timeB/Bcentral2.png", tamanho=(50, 50), delay_frames=110, velocidade=5)
sprite13.alterar_caminho([(500, 150), (416, 140)], delay_frames=85)

sprite1 = Sprite(66, 286, "assets/bola.png", tamanho=(25, 25), delay_frames=0, velocidade=7)
sprite1.alterar_caminho([(511, 170), (347, 130)], delay_frames=0)


todos_sprites = pygame.sprite.Group([sprite2, sprite3, sprite4, sprite5, sprite6, sprite7, sprite8, sprite9, sprite10, sprite11, sprite12, sprite13, sprite14, sprite15, sprite1])
#Saqu inicial
class Botao(pygame.sprite.Sprite):
    def __init__(self, x, y, sprites):
        super(Botao, self).__init__()
        fonte = pygame.font.Font(None, 36)
        self.image = fonte.render("INICIAR", True, branco)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.sprites = sprites
        self.acionado = False

    def acionar(self):
        self.acionado = True

    def update(self):
        if self.acionado:
            for sprite in self.sprites:
                sprite.movendo = True
                self.kill()



botao = Botao(655, 40, todos_sprites)


todos_sprites.add(botao)

#ataque
botao_ataque = Botao(655, 91, todos_sprites)
botao_ataque.image = fonte.render("Ataque", True, branco)


tempo_inicial = pygame.time.get_ticks()


estado_botao_ataque = 0


def definir_novo_ataque_1(): #AJEITADO
    global estado_botao_ataque
    if estado_botao_ataque == 0:
        sprite1.alterar_caminho([(503, 161), (347, 120)], delay_frames=0)
        sprite2.alterar_caminho([(254, 59)], delay_frames=0)
        sprite3.alterar_caminho([(119, 160)], delay_frames=0)
        sprite4.alterar_caminho([(145, 70)], delay_frames=0)
        sprite5.alterar_caminho([(256, 254)], delay_frames=0)
        sprite6.alterar_caminho([(145, 254)], delay_frames=0)
        sprite7.alterar_caminho([(279, 160)], delay_frames=0)
        sprite8.alterar_caminho([(339, 170)], delay_frames=0)
        sprite9.alterar_caminho([(347, 120)], delay_frames=60)
        sprite10.alterar_caminho([(440, 254)], delay_frames=0)
        sprite11.alterar_caminho([(423, 50)], delay_frames=0)
        sprite12.alterar_caminho([(358, 254),(390, 304), (343, 270)], delay_frames=0)
        sprite13.alterar_caminho([(416, 140)], delay_frames=90)
        estado_botao_ataque = 1


def definir_novo_ataque_2(): #AJEITADO
    global estado_botao_ataque
    if estado_botao_ataque == 1:
        sprite1.alterar_caminho([(343, 270), (266, 172)], delay_frames=0)
        sprite2.alterar_caminho([(230, 90)], delay_frames=0)
        sprite3.alterar_caminho([(95, 140)], delay_frames=0)
        sprite4.alterar_caminho([(145, 70)], delay_frames=0)
        sprite5.alterar_caminho([(280, 260)], delay_frames=0)
        sprite6.alterar_caminho([(175, 280)], delay_frames=0)
        sprite7.alterar_caminho([(280, 230)], delay_frames=0)
        sprite8.alterar_caminho([(339, 170)], delay_frames=0)
        sprite9.alterar_caminho([(347, 120)], delay_frames=60)
        sprite10.alterar_caminho([(440, 254)], delay_frames=0)
        sprite11.alterar_caminho([(423, 50)], delay_frames=0)
        sprite12.alterar_caminho([(385,312), (343,270)], delay_frames=0)
        sprite13.alterar_caminho([(416, 140)], delay_frames=0)

        estado_botao_ataque = 2


def definir_novo_ataque_3(): #AJEITADO
    global estado_botao_ataque
    if estado_botao_ataque == 2:
        sprite1.alterar_caminho([(312,220), (435, 211)], delay_frames=0)
        sprite2.alterar_caminho([(130, 148), (180, 148)], delay_frames=0)
        sprite3.alterar_caminho([(254, 30)], delay_frames=60)
        sprite4.alterar_caminho([(119, 150), (143, 72)], delay_frames=0)
        sprite5.alterar_caminho([(254, 293)], delay_frames=60)
        sprite6.alterar_caminho([(281, 175)], delay_frames=40)
        sprite7.alterar_caminho([(278,220)], delay_frames=0)
        sprite8.alterar_caminho([(341, 173)], delay_frames=60)
        sprite9.alterar_caminho([(476, 75)], delay_frames=60)
        sprite10.alterar_caminho([(477, 241)], delay_frames=0)
        sprite11.alterar_caminho([(340, 63)], delay_frames=0)
        sprite12.alterar_caminho([(343, 264)], delay_frames=0)
        sprite13.alterar_caminho([(504, 155)], delay_frames=0)

        estado_botao_ataque = 3


def definir_novo_ataque_4(): #AJEITADO
    global estado_botao_ataque
    if estado_botao_ataque == 3:
        sprite1.alterar_caminho([(407, 184), (319,223), (337, 282), (365, 330)], delay_frames=0)  # bola
        sprite2.alterar_caminho([(116, 152)], delay_frames=0)  # 1° Ponteiro
        sprite3.alterar_caminho([(283, 128)], delay_frames=0)  # 2° Ponteiro
        sprite4.alterar_caminho([(240, -50)], delay_frames=0)  # Libero
        sprite5.alterar_caminho([(282, 205)], delay_frames=0)  # Oposto
        sprite6.alterar_caminho([(149, 245)], delay_frames=0)  # Levantador
        sprite7.alterar_caminho([(283, 162)], delay_frames=0)  # 1° Central
        sprite8.alterar_caminho([(340, 153)], delay_frames=0)  # 1° Central
        sprite9.alterar_caminho([(341, 102)], delay_frames=0)  # Levantador
        sprite10.alterar_caminho([(504, 155)], delay_frames=0)  # Libero
        sprite11.alterar_caminho([(393, 298), (383, 283)], delay_frames=0)  # Oposto
        sprite12.alterar_caminho([(404, 28)], delay_frames=0)  # 1° Ponteiro
        sprite13.alterar_caminho([(410, 169)], delay_frames=0)  # 2° Ponteiro
        sprite14.alterar_caminho([(140, 73)], delay_frames=0)  # 2° Central
        estado_botao_ataque = 4


def definir_novo_ataque_5(): #AJEITANDO
    global estado_botao_ataque
    if estado_botao_ataque == 4:
        sprite1.alterar_caminho([(315, 295), (443,301)], delay_frames=0)  # bola
        sprite2.alterar_caminho([(202, 168)], delay_frames=0)  # 1° Ponteiro
        sprite3.alterar_caminho([(250, 34)], delay_frames=0)  # 2° Ponteiro
        sprite4.alterar_caminho([(151, 85)], delay_frames=0)  # Libero
        sprite5.alterar_caminho([(253, 306), (281, 282)], delay_frames=0)  # Oposto
        sprite6.alterar_caminho([(282, 170)], delay_frames=0)  # Levantador
        sprite7.alterar_caminho([(285, 125)], delay_frames=0)  # 1° Central
        sprite8.alterar_caminho([(339, 229)], delay_frames=0)  # 1° Central
        sprite9.alterar_caminho([(472, 91)], delay_frames=0)  # Levantador
        sprite10.alterar_caminho([(487, 283)], delay_frames=0)  # Libero
        sprite11.alterar_caminho([(375, 110)], delay_frames=0)  # Oposto
        sprite12.alterar_caminho([(512, 145)], delay_frames=0)  # 1° Ponteiro
        sprite13.alterar_caminho([(340, 256)], delay_frames=0)  # 2° Ponteiro
        sprite14.alterar_caminho([(200, -50)], delay_frames=0)  # 2° Central
        estado_botao_ataque = 5


def definir_novo_ataque_6(): #falta AJEITAR
    global estado_botao_ataque
    if estado_botao_ataque == 5:
        sprite1.alterar_caminho([(315, 295), (443, 301)], delay_frames=0)  # bola
        sprite2.alterar_caminho([(202, 168)], delay_frames=0)  # 1° Ponteiro
        sprite3.alterar_caminho([(250, 34)], delay_frames=0)  # 2° Ponteiro
        sprite4.alterar_caminho([(151, 85)], delay_frames=0)  # Libero
        sprite5.alterar_caminho([(253, 306), (281, 282)], delay_frames=0)  # Oposto
        sprite6.alterar_caminho([(282, 170)], delay_frames=0)  # Levantador
        sprite7.alterar_caminho([(285, 125)], delay_frames=0)  # 1° Central
        sprite8.alterar_caminho([(339, 229)], delay_frames=0)  # 1° Central
        sprite9.alterar_caminho([(472, 91)], delay_frames=0)  # Levantador
        sprite10.alterar_caminho([(487, 283)], delay_frames=0)  # Libero
        sprite11.alterar_caminho([(375, 110)], delay_frames=0)  # Oposto
        sprite12.alterar_caminho([(512, 145)], delay_frames=0)  # 1° Ponteiro
        sprite13.alterar_caminho([(340, 256)], delay_frames=0)  # 2° Ponteiro
        sprite14.alterar_caminho([(200, -50)], delay_frames=0)  # 2° Central
        estado_botao_ataque = 0



botao_ataque.acionar = definir_novo_ataque_1()

#proxima rotaçao
botao_proxima_rotacao = Botao(655, 131, todos_sprites)
botao_proxima_rotacao.image = fonte.render("Rodar", True, branco)




estado_botao_proxima_rotacao = 0


def definir_nova_rotacao_1(): #AJEITADO
    global estado_botao_proxima_rotacao
    if estado_botao_proxima_rotacao == 0:
        sprite1.alterar_caminho([(284, 166), (285, 166), (324, 25), (579, 25), (572, 65)], delay_frames=0)
        sprite2.alterar_caminho([(280, 230), (145, 254)], delay_frames=0)
        sprite3.alterar_caminho([(145, 70), (254, 59), (145, 70)], delay_frames=0)
        sprite4.alterar_caminho([(119, 166), (145, 70), (119, 150)], delay_frames=0)
        sprite5.alterar_caminho([(279, 160), (279, 224)], delay_frames=0)
        sprite6.alterar_caminho([(145, 254), (119, 166), (240, 205)], delay_frames=0)
        sprite7.alterar_caminho([(279, 160), (256, 254)], delay_frames=0)
        sprite8.alterar_caminho([(348, 265), (340, 160)], delay_frames=0)
        sprite9.alterar_caminho([(350, 59), (457, 69), (572, 55)], delay_frames=60)
        sprite10.alterar_caminho([(457, 69), (490, 160)], delay_frames=0)
        sprite11.alterar_caminho([(457, 265), (348, 265),(355,200)], delay_frames=0)
        sprite12.alterar_caminho([(340, 160), (350, 59),(380,140)], delay_frames=0)
        sprite13.alterar_caminho([(490, 160), (457, 265)], delay_frames=0)
        estado_botao_proxima_rotacao = 1



def definir_nova_rotacao_2(): #AJEITADO
    global estado_botao_proxima_rotacao
    if estado_botao_proxima_rotacao == 1:
        sprite1.alterar_caminho([(67, 268)], delay_frames=0) #bola
        sprite2.alterar_caminho([(116, 152)], delay_frames=0) #1° Ponteiro
        sprite3.alterar_caminho([(282,159)], delay_frames=0) #2° Ponteiro
        sprite4.alterar_caminho([(240, -50)], delay_frames=0) #Libero
        sprite5.alterar_caminho([(259, 257)], delay_frames=0) #Oposto
        sprite6.alterar_caminho([(140, 74)], delay_frames=0) #Levantador
        sprite7.alterar_caminho([(269, 78)], delay_frames=0) #1° Central
        sprite8.alterar_caminho([(340, 173)], delay_frames=30) #1° Central
        sprite9.alterar_caminho([(474, 70), (517,48)], delay_frames=30) #Levantador
        sprite10.alterar_caminho([(504, 155)], delay_frames=30) #Libero
        sprite11.alterar_caminho([(352, 257)], delay_frames=30) #Oposto
        sprite12.alterar_caminho([(476, 80)], delay_frames=30) #1° Ponteiro
        sprite13.alterar_caminho([(454, 245)], delay_frames=30) #2° Ponteiro
        sprite14.alterar_caminho([(23, 259)], delay_frames=0) #2° Central

        estado_botao_proxima_rotacao = 2


def definir_nova_rotacao_3(): #AJEITADO
    global estado_botao_proxima_rotacao
    if estado_botao_proxima_rotacao == 2:
        sprite1.alterar_caminho([(583,334),(576,51)], delay_frames=0)  # bola
        sprite2.alterar_caminho([(145, 151)], delay_frames=0)  # 1° Ponteiro
        sprite3.alterar_caminho([(142, 77)], delay_frames=0)  # 2° Ponteiro
        sprite4.alterar_caminho([(153, 231)], delay_frames=0)  # Libero
        sprite5.alterar_caminho([(289, 271)], delay_frames=0)  # Oposto
        sprite6.alterar_caminho([(273, 78)], delay_frames=0)  # Levantador
        sprite7.alterar_caminho([(286, 47)], delay_frames=0)  # 1° Central
        sprite8.alterar_caminho([(349, 74)], delay_frames=0)  # 1° Central
        sprite9.alterar_caminho([(505, 156)], delay_frames=0)  # Levantador
        sprite10.alterar_caminho([(467, 253)], delay_frames=0)  # Libero
        sprite11.alterar_caminho([(345, 178)], delay_frames=0)  # Oposto
        sprite12.alterar_caminho([(471, 74),(585,42)], delay_frames=0)  # 1° Ponteiro
        sprite13.alterar_caminho([(360, 252)], delay_frames=0)  # 2° Ponteiro
        sprite14.alterar_caminho([(240, -50)], delay_frames=0)  # 2° Central
        estado_botao_proxima_rotacao = 3


def definir_nova_rotacao_4(): #AJEITADO
    global estado_botao_proxima_rotacao
    if estado_botao_proxima_rotacao == 3:
        sprite1.alterar_caminho([(452,371), (66, 358), (69,288)], delay_frames=0)  # bola
        sprite2.alterar_caminho([(145, 80), (270,206)], delay_frames=0)  # 1° Ponteiro
        sprite3.alterar_caminho([(263,244), (132,75)], delay_frames=0)  # 2° Ponteiro
        sprite4.alterar_caminho([(147, 153), (186,153)], delay_frames=0)  # Libero
        sprite5.alterar_caminho([(155, 232), (24,267)], delay_frames=0)  # Oposto
        sprite6.alterar_caminho([(273, 78), (272,127)], delay_frames=0)  # Levantador
        sprite7.alterar_caminho([(276, 163)], delay_frames=0)  # 1° Central
        sprite8.alterar_caminho([(385, 90)], delay_frames=0)  # 1° Central
        sprite9.alterar_caminho([(374,131)], delay_frames=0)  # Levantador
        sprite10.alterar_caminho([(504,156)], delay_frames=0)  # Libero
        sprite11.alterar_caminho([(341, 83)], delay_frames=0)  # Oposto
        sprite12.alterar_caminho([(484,91)], delay_frames=0)  # 1° Ponteiro
        sprite13.alterar_caminho([(469, 253)], delay_frames=0)  # 2° Ponteiro
        sprite14.alterar_caminho([(240, -50)], delay_frames=0)  # 2° Central TIME A
        sprite15.alterar_caminho([(350, 450)], delay_frames=0)  # 2° Central TIME B
        estado_botao_proxima_rotacao = 4


def definir_nova_rotacao_5(): #FALTA AJEITAR
    global estado_botao_proxima_rotacao
    if estado_botao_proxima_rotacao == 4:
        sprite1.alterar_caminho([(600, 300), (700, 350), (800, 400)], delay_frames=0)
        sprite2.alterar_caminho([(650, 250), (750, 300)], delay_frames=0)

        estado_botao_proxima_rotacao = 5


def definir_nova_rotacao_6(): #Falta ajeitar
    global estado_botao_proxima_rotacao
    if estado_botao_proxima_rotacao == 5:
        sprite1.alterar_caminho([(50, 50), (100, 100), (150, 150)], delay_frames=0)
        sprite2.alterar_caminho([(200, 200), (250, 250)], delay_frames=0)

        estado_botao_proxima_rotacao = 0


botao_proxima_rotacao.acionar = definir_nova_rotacao_1



todos_sprites.add(botao_proxima_rotacao)

#Saque
class BotaoNovoSaque(pygame.sprite.Sprite):
    def __init__(self, x, y, sprites):
        super(BotaoNovoSaque, self).__init__()
        fonte = pygame.font.Font(None, 36)
        self.image = fonte.render("Saque", True, branco)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.sprites = sprites
        self.acionado = False

    def acionar(self):
        self.acionado = True

    def update(self):
        if self.acionado:
            for sprite in self.sprites:
                sprite.movendo = True
            self.kill()


botao_novo_saque = BotaoNovoSaque(655, 170, todos_sprites)


todos_sprites.add(botao_novo_saque)

#novo saque

estado_botao_novo_saque = 0


def definir_novo_saque_1(): #AJEITADO
    global estado_botao_novo_saque
    if estado_botao_novo_saque == 0:
        sprite1.alterar_caminho([(142,148), (281,175)], delay_frames=0)
        sprite2.alterar_caminho([(130,148),(180,148)], delay_frames=60)
        sprite3.alterar_caminho([(254,30)], delay_frames=60)
        sprite4.alterar_caminho([(119, 150), (143,72)], delay_frames=60)
        sprite5.alterar_caminho([(254,293)], delay_frames=60)
        sprite6.alterar_caminho([(281,175)], delay_frames=40)
        sprite7.alterar_caminho([(238,203),(238,210)], delay_frames=60)
        sprite8.alterar_caminho([(341,173)], delay_frames=60)
        sprite9.alterar_caminho([(476,75)], delay_frames=60)
        sprite10.alterar_caminho([(477,241)], delay_frames=0)
        sprite11.alterar_caminho([(340,63)], delay_frames=0)
        sprite12.alterar_caminho([(343, 264)], delay_frames=0)
        sprite13.alterar_caminho([(504,155)], delay_frames=0)
        estado_botao_novo_saque = 1


def definir_novo_saque_2(): #AJEITADO
    global estado_botao_novo_saque
    if estado_botao_novo_saque == 1:
        sprite1.alterar_caminho([(440, 186), (341,102)], delay_frames=0)  # bola
        sprite2.alterar_caminho([(116, 152)], delay_frames=0)  # 1° Ponteiro
        sprite3.alterar_caminho([(268, 79)], delay_frames=0)  # 2° Ponteiro
        sprite4.alterar_caminho([(240, -50)], delay_frames=0)  # Libero
        sprite5.alterar_caminho([(259, 257)], delay_frames=0)  # Oposto
        sprite6.alterar_caminho([(149, 245)], delay_frames=0)  # Levantador
        sprite7.alterar_caminho([(283, 162)], delay_frames=0)  # 1° Central
        sprite8.alterar_caminho([(370, 147), (356,154)], delay_frames=30)  # 1° Central
        sprite9.alterar_caminho([(437, 38), (341,102)], delay_frames=0)  # Levantador
        sprite10.alterar_caminho([(504, 155)], delay_frames=30)  # Libero
        sprite11.alterar_caminho([(393, 298)], delay_frames=30)  # Oposto
        sprite12.alterar_caminho([(404, 28)], delay_frames=30)  # 1° Ponteiro
        sprite13.alterar_caminho([(440, 186)], delay_frames=30)  # 2° Ponteiro
        sprite14.alterar_caminho([(140, 73)], delay_frames=0)  # 2° Central
        estado_botao_novo_saque = 2


def definir_novo_saque_3(): #AJEITADO
    global estado_botao_novo_saque
    if estado_botao_novo_saque == 2:
        sprite1.alterar_caminho([(165,231), (282,170)], delay_frames=0)  # bola
        sprite2.alterar_caminho([(198, 163)], delay_frames=80)  # 1° Ponteiro
        sprite3.alterar_caminho([(250, 33)], delay_frames=80)  # 2° Ponteiro
        sprite4.alterar_caminho([(117, 157), (147,82)], delay_frames=100)  # Libero
        sprite5.alterar_caminho([(278, 280)], delay_frames=0)  # Oposto
        sprite6.alterar_caminho([(282, 170)], delay_frames=30)  # Levantador
        sprite7.alterar_caminho([(285, 125)], delay_frames=80)  # 1° Central
        sprite8.alterar_caminho([(340, 170)], delay_frames=0)  # 1° Central
        sprite9.alterar_caminho([(481, 84)], delay_frames=0)  # Levantador
        sprite10.alterar_caminho([(467, 253)], delay_frames=0)  # Libero
        sprite11.alterar_caminho([(346, 82)], delay_frames=0)  # Oposto
        sprite12.alterar_caminho([(508,157)], delay_frames=0)  # 1° Ponteiro
        sprite13.alterar_caminho([(360, 252)], delay_frames=0)  # 2° Ponteiro
        sprite14.alterar_caminho([(240, -50)], delay_frames=0)  # 2° Central
        estado_botao_novo_saque = 3


def definir_novo_saque_4(): #Falta ajeitar
    global estado_botao_novo_saque
    if estado_botao_novo_saque == 3:
        sprite1.alterar_caminho([(165, 231), (282, 170)], delay_frames=0)  # bola
        sprite2.alterar_caminho([(265, 69)], delay_frames=0)  # 1° Ponteiro
        sprite3.alterar_caminho([(188, 153)], delay_frames=0)  # 2° Ponteiro
        sprite4.alterar_caminho([(135, 75)], delay_frames=0)  # Libero
        sprite5.alterar_caminho([(153, 241)], delay_frames=0)  # Oposto
        sprite6.alterar_caminho([(272, 252)], delay_frames=0)  # Levantador
        sprite7.alterar_caminho([(288, 173)], delay_frames=0)  # 1° Central
        sprite8.alterar_caminho([(385, 90)], delay_frames=0)  # 1° Central
        sprite9.alterar_caminho([(374, 131)], delay_frames=0)  # Levantador
        sprite10.alterar_caminho([(504, 156)], delay_frames=0)  # Libero
        sprite11.alterar_caminho([(341, 83)], delay_frames=0)  # Oposto
        sprite12.alterar_caminho([(484, 91)], delay_frames=0)  # 1° Ponteiro
        sprite13.alterar_caminho([(469, 253)], delay_frames=0)  # 2° Ponteiro
        sprite14.alterar_caminho([(240, -50)], delay_frames=0)  # 2° Central TIME A
        sprite15.alterar_caminho([(350, 450)], delay_frames=0)  # 2° Central TIME B
        estado_botao_novo_saque = 4


def definir_novo_saque_5(): #Falta ajeitar
    global estado_botao_novo_saque
    if estado_botao_novo_saque == 4:
        sprite1.alterar_caminho([(230,100), (281,175)], delay_frames=0)
        sprite2.alterar_caminho([(130,148),(180,148)], delay_frames=60)
        sprite3.alterar_caminho([(254,30)], delay_frames=60)
        sprite4.alterar_caminho([(119, 150), (143,72)], delay_frames=60)
        sprite5.alterar_caminho([(254,293)], delay_frames=60)
        sprite6.alterar_caminho([(281,175)], delay_frames=40)
        sprite7.alterar_caminho([(238,203),(238,210)], delay_frames=60)
        sprite8.alterar_caminho([(341,173)], delay_frames=60)
        sprite9.alterar_caminho([(476,75)], delay_frames=60)
        sprite10.alterar_caminho([(477,241)], delay_frames=0)
        sprite11.alterar_caminho([(340,63)], delay_frames=0)
        sprite12.alterar_caminho([(343, 264)], delay_frames=0)
        sprite13.alterar_caminho([(504,155)], delay_frames=0)
        estado_botao_novo_saque = 5


def definir_novo_saque_6(): #Falta ajeitar
    global estado_botao_novo_saque
    if estado_botao_novo_saque == 5:
        sprite1.alterar_caminho([(400,148), (300,175)], delay_frames=0)
        sprite2.alterar_caminho([(130,148),(180,148)], delay_frames=60)
        sprite3.alterar_caminho([(254,30)], delay_frames=60)
        sprite4.alterar_caminho([(119, 150), (143,72)], delay_frames=60)
        sprite5.alterar_caminho([(254,293)], delay_frames=60)
        sprite6.alterar_caminho([(281,175)], delay_frames=40)
        sprite7.alterar_caminho([(238,203),(238,210)], delay_frames=60)
        sprite8.alterar_caminho([(341,173)], delay_frames=60)
        sprite9.alterar_caminho([(476,75)], delay_frames=60)
        sprite10.alterar_caminho([(477,241)], delay_frames=0)
        sprite11.alterar_caminho([(340,63)], delay_frames=0)
        sprite12.alterar_caminho([(343, 264)], delay_frames=0)
        sprite13.alterar_caminho([(504,155)], delay_frames=0)
        estado_botao_novo_saque = 0


botao_novo_saque.acionar = definir_novo_saque_1

rodizio = 0

# Loop principal
clock = pygame.time.Clock()

while True:
    tempo_decorrido = pygame.time.get_ticks() - tempo_inicial
    mensagem = f"Rodizio {rodizio}"
    texto_formatado = fonte.render(mensagem, True, (255,255,255))
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if botao.rect.collidepoint(pygame.mouse.get_pos()):
                botao.acionar()
            elif botao_ataque.rect.collidepoint(pygame.mouse.get_pos()):
                if estado_botao_ataque == 0:
                    botao_ataque.acionar = definir_novo_ataque_1
                elif estado_botao_ataque == 1:
                    botao_ataque.acionar = definir_novo_ataque_2
                elif estado_botao_ataque == 2:
                    botao_ataque.acionar = definir_novo_ataque_3
                elif estado_botao_ataque == 3:
                    botao_ataque.acionar = definir_novo_ataque_4
                elif estado_botao_ataque == 4:
                    botao_ataque.acionar = definir_novo_ataque_5
                elif estado_botao_ataque == 5:
                    botao_ataque.acionar = definir_novo_ataque_6
                botao_ataque.acionar()
            elif botao_proxima_rotacao.rect.collidepoint(pygame.mouse.get_pos()):
                rodizio = estado_botao_proxima_rotacao +1
                if estado_botao_proxima_rotacao == 0:
                    rodizio = estado_botao_proxima_rotacao + 1
                    botao_proxima_rotacao.acionar = definir_nova_rotacao_1
                elif estado_botao_proxima_rotacao == 1:
                    rodizio = estado_botao_proxima_rotacao + 1
                    botao_proxima_rotacao.acionar = definir_nova_rotacao_2
                elif estado_botao_proxima_rotacao == 2:
                    rodizio = estado_botao_proxima_rotacao + 1
                    botao_proxima_rotacao.acionar = definir_nova_rotacao_3
                elif estado_botao_proxima_rotacao == 3:
                    rodizio = estado_botao_proxima_rotacao + 1
                    botao_proxima_rotacao.acionar = definir_nova_rotacao_4
                elif estado_botao_proxima_rotacao == 4:
                    rodizio = estado_botao_proxima_rotacao + 1
                    botao_proxima_rotacao.acionar = definir_nova_rotacao_5
                elif estado_botao_proxima_rotacao == 5:
                    rodizio = estado_botao_proxima_rotacao + 1
                    botao_proxima_rotacao.acionar = definir_nova_rotacao_6
                botao_proxima_rotacao.acionar()
            elif botao_novo_saque.rect.collidepoint(pygame.mouse.get_pos()):
                if estado_botao_novo_saque == 0:
                    botao_novo_saque.acionar = definir_novo_saque_1
                elif estado_botao_novo_saque == 1:
                    botao_novo_saque.acionar = definir_novo_saque_2
                elif estado_botao_novo_saque == 2:
                    botao_novo_saque.acionar = definir_novo_saque_3
                elif estado_botao_novo_saque == 3:
                    botao_novo_saque.acionar = definir_novo_saque_4
                elif estado_botao_novo_saque == 4:
                    botao_novo_saque.acionar = definir_novo_saque_5
                elif estado_botao_novo_saque == 5:
                    botao_novo_saque.acionar = definir_novo_saque_6
                botao_novo_saque.acionar()
            elif botao_saque.rect.collidepoint(pygame.mouse.get_pos()):
                if estado_botao_saque == 0:
                    botao_saque.acionar = definir_saque_1
                elif estado_botao_saque == 1:
                    botao_saque.acionar = definir_saque_2
                elif estado_botao_saque == 2:
                    botao_saque.acionar = definir_saque_3
                elif estado_botao_saque == 3:
                    botao_saque.acionar = definir_saque_4
                elif estado_botao_saque == 4:
                    botao_saque.acionar = definir_saque_5
                elif estado_botao_saque == 5:
                    botao_saque.acionar = definir_saque_6
                botao_saque.acionar()
            elif evento.button == 1:
                print(f"Coordenadas: {pygame.mouse.get_pos()}")

    #fundo e texto rodizio
    tela.blit(background, (0, 0))
    tela.blit(texto_formatado,(7,4))

    todos_sprites.update()

    if tempo_decorrido > 4000 and not botao_ataque.alive() and botao.acionado:
        todos_sprites.add(botao_ataque)

    #desenhar os sprites
    todos_sprites.draw(tela)


    pygame.display.flip()

    clock.tick(30)
