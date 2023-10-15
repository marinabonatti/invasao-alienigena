import pygame

class Configuracoes:
    """Armazena as configurações necessárias para o andamento do jogo
    Invasão Alienígena."""

    def __init__(self):
        """Inicializa a classe e seus atributos."""

        # Atributos referentes ao display
        self.tela = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.tela_rect = self.tela.get_rect()
        self.cor_background = (17,23,49)

        # Flags disponíveis
        self.jogo_ativo = False
        self.movimento_direita = False
        self.movimento_esquerda = False
        
        # Atributos nave
        self.velocidade_nave = self.tela_rect.width // 500
        self.naves_restantes = 2

        # Atributos lasers
        self.largura_laser = self.tela_rect.width // 300
        self.altura_laser = self.tela_rect.height // 70
        self.cor_laser = (255,74,173)
        self.velocidade_laser = self.tela_rect.height // 500
        self.limite_lasers = 3

        # Atributos aliens
        self.velocidade_x_alien = self.tela_rect.width // 400
        self.velocidade_y_alien = self.tela_rect.height // 50
        self.direcao_frota = 1 # Direita (1) Esquerda (-1)