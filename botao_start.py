import pygame

class BotaoStart:
    """Inicializa e armazena os métodos e atributos referentes ao botão
    Start, que inicia o jogo quando ele está inativo."""

    def __init__(self, jogo):
        """Inicializa a classe e armazena seus atributos."""

        # Obtém características da tela do jogo
        self.tela = jogo.tela
        self.tela_rect = jogo.tela_rect

        # Cria o atributo imagem e o Rect referente a ela
        self.imagem = pygame.image.load('imagens/botao_start.bmp')
        self.rect = self.imagem.get_rect()

        # Posiciona o botão de acorod com a tela
        self.rect.center = self.tela_rect.center

    def desenhar(self):
        self.tela.blit(self.imagem, self.rect)

