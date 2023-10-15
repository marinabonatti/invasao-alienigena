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
        self.espacamento_stats = self.tela_rect.height // 70
        self.tamanho_stats = self.tela_rect.height // 15

        # Flags disponíveis
        self.jogo_ativo = False
        self.movimento_direita = False
        self.movimento_esquerda = False

        # Atributos lasers
        self.largura_laser = self.tela_rect.width // 300
        self.altura_laser = self.tela_rect.height // 70
        self.cor_laser = (255,74,173)
        self.limite_lasers = 3

        # Atributos do jogo
        self.pontuacao = 0
        self.nivel = 1
        self.naves_restantes = 2
        self.highscore = 0

        self.escala_aceleracao = 1.1
        self.inicializar_configuracoes_dinamicas()

    def inicializar_configuracoes_dinamicas(self):
        """Inicializa configurações que mudam ao longo da partida."""
        self.velocidade_nave = self.tela_rect.width // 500
        self.velocidade_laser = self.tela_rect.height // 500
        self.velocidade_x_alien = self.tela_rect.width // 400 # 400
        self.velocidade_y_alien = self.tela_rect.height // 50 # 50
        self.ponto_por_alien = 50
        self.direcao_frota = 1 # Direita (1) Esquerda (-1)

    def aumentar_velocidade(self):
        """Aumenta configurações de velocidade."""
        self.velocidade_nave *= self.escala_aceleracao
        self.velocidade_laser *= self.escala_aceleracao
        self.velocidade_x_alien *= self.escala_aceleracao
        self.velocidade_y_alien *= self.escala_aceleracao
        self.ponto_por_alien *= self.escala_aceleracao
