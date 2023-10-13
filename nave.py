import pygame

class Nave():
    """Armazena e gerencia os atributos e métodos associados à nave
    principal, a ser controlada e utilizada pelo usuário para destruir
    naves alienígenas."""

    def __init__(self, jogo):
        self.tela = jogo.tela
        self.tela_rect = jogo.tela_rect

        # Cria o atributo imagem e o Rect referente a ela
        self.imagem = pygame.image.load("imagens/nave.bmp")
        self.rect = self.imagem.get_rect()

        # Posiciona a nave no centro, na parte inferior da tela
        self.rect.midbottom = self.tela_rect.midbottom

    def desenhar(self):
        """Desenha a imagem na tela considerando seu Rect."""        
        self.tela.blit(self.imagem, self.rect)
