from pygame.sprite import Sprite
import pygame

class Aliens(Sprite):
    """Armazena e gerencia os atributos e métodos dos aliens, que querem
    destruir a nave principal. Herda de Sprite, portanto é necessário
    tomar cuidado especial com o nome de alguns atributos e métodos."""

    def __init__(self, jogo):
        super().__init__()
        self.tela = jogo.tela
        self.tela_rect = self.tela.get_rect()
        self.configuracoes = jogo.configuracoes

        # Cria image e rect
        self.image = pygame.image.load("imagens/alien.bmp")
        self.rect = self.image.get_rect()

    def update(self):
        """Método especial da classe Sprite, pode ser aplicado a todos
        os membros do grupo simultaneamente. Neste caso, será utilizado
        para a movimentação dos aliens."""
        self.rect.x += self.configuracoes.velocidade_x_alien

        
