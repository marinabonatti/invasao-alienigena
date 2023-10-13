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
        self.velocidade_nave = self.tela_rect.width // 450
        