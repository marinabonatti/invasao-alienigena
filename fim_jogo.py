import pygame

class FimJogo:
    """Prepara a tela de fim de jogo."""

    def __init__(self, jogo):
        self.tela = jogo.tela
        self.tela_rect = self.tela.get_rect()
        
        self.imagem = pygame.image.load("imagens/game_over.bmp")
        self.rect = self.imagem.get_rect()

        self.rect.center = self.tela_rect.center

    def desenhar(self):
        self.tela.blit(self.imagem, self.rect)