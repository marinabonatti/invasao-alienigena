from pygame.sprite import Sprite
import pygame

class Lasers(Sprite):
    """Armazena e gerencia os atributos e métodos do laser que a nave
    lança para tentar se defender contra os alienígenas."""

    def __init__(self, jogo):

        # Acessa atributos externos importantes
        super().__init__()
        self.tela = jogo.tela
        self.configuracoes = jogo.configuracoes

        # Acessa atributos próprios
        self.cor = self.configuracoes.cor_laser
        self.largura = self.configuracoes.largura_laser
        self.altura = self.configuracoes.altura_laser
        self.velocidade = self.configuracoes.velocidade_laser

        # Cria um rect e o posiciona
        self.rect = pygame.Rect(0,0,self.largura,self.altura)
        self.rect.midtop = jogo.nave.rect.midtop
    
    def desenhar(self):
        pygame.draw.rect(self.tela,self.cor,self.rect)
    
    def atualizar_pos_laser(self):
        self.rect.y -= self.velocidade

        