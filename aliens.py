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
        self.jogo = jogo

        # Cria image e rect
        self.image = pygame.image.load("imagens/alien.bmp")
        self.rect = self.image.get_rect()

    def update(self):
        """Método especial da classe Sprite, pode ser aplicado a todos
        os membros do grupo simultaneamente. Neste caso, será utilizado
        para a movimentação dos aliens: direita ou esquerda, a depender
        da direção estabelecida para a frota naquele momento."""
        
        self.rect.x += (self.configuracoes.velocidade_x_alien *
                        self.configuracoes.direcao_frota)

    def verificar_bordas(self):
        """Retorna True caso um alien esteja em alguma borda lateral da
        tela."""

        if self.rect.right >= self.tela_rect.right or self.rect.left <= 0:
            return True
        
    def _mudar_direcao_frota(self):
        """Faz com que a frota inteira desça na tela de acordo com a 
        velocidade_y_alien estabelecida em configurações, além de mudar
        a direção da frota."""
        for alien in self.jogo.aliens.sprites():
            alien.rect.y += self.configuracoes.velocidade_y_alien
        self.configuracoes.direcao_frota *= -1
        


        
