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
        self.centralizar_nave()

    def desenhar(self):
        """Desenha a imagem na tela considerando seu Rect."""        
        self.tela.blit(self.imagem, self.rect)

    def atualizar_pos_nave(self, jogo):
        direita = jogo.configuracoes.movimento_direita
        esquerda = jogo.configuracoes.movimento_esquerda
        rect = jogo.nave.rect
        if direita and rect.right < jogo.tela_rect.right:
            jogo.nave.rect.x += jogo.configuracoes.velocidade_nave
        if esquerda and rect.x > 0:
            jogo.nave.rect.x -= jogo.configuracoes.velocidade_nave

    def centralizar_nave(self):
        self.rect.midbottom = self.tela_rect.midbottom
