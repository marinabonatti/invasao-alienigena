from pygame.sprite import Sprite
import pygame

class Aliens(Sprite):
    """Armazena e gerencia os atributos e métodos dos aliens, que buscam
    destruir a nave principal."""

    def __init__(self, jogo):
        """Inicializa a classe acessando atributos externos e próprios
        importantes para o seu funcionamento. Também cria e posiciona o
        rect do objeto."""

        super().__init__()
        self.tela = jogo.tela
        self.configuracoes = jogo.configuracoes

        self.velocidade_x = self.configuracoes.velocidade_x_alien
        self.velocidade_y = self.configuracoes.velocidade_y_alien
        self.imagem = pygame.image.load("imagens/alien.bmp")
        self.rect = self.imagem.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

    def desenhar(self):
        """Desenha o alien na tela de acordo com o rect."""

        self.tela.blit(self.imagem, self.rect)

    