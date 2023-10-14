from pygame.sprite import Sprite
import pygame

class Lasers(Sprite):
    """Armazena e gerencia os atributos e métodos do laser que a nave
    lança para tentar se defender contra os alienígenas."""

    def __init__(self, jogo):
        """Inicializa a classe acessando atributos externos e próprios
        importantes para o seu funcionamento. Também cria e posiciona o 
        rect do objeto."""
        super().__init__()
        self.tela = jogo.tela
        self.configuracoes = jogo.configuracoes

        self.cor = self.configuracoes.cor_laser
        self.largura = self.configuracoes.largura_laser
        self.altura = self.configuracoes.altura_laser
        self.velocidade = self.configuracoes.velocidade_laser

        self.rect = pygame.Rect(0,0,self.largura,self.altura)
        self.rect.midtop = jogo.nave.rect.midtop
    
    def desenhar(self):
        """Desenha o laser de acordo com a tela (Surface), a cor e seu
        Rect."""
        pygame.draw.rect(self.tela,self.cor,self.rect)
    
    def atualizar_pos_laser(self):
        """Atualiza a posição do laser de acordo com a velocidade para
        ele estabelecida nas configurações."""
        self.rect.y -= self.velocidade

    def excluir_laser_antigo(self, grupo_sprite, laser):
        """Exclui lasers que já ultrapassaram o topo da tela, para que
        não gastem memória e processamento sem que haja necessidade."""
        if laser.rect.bottom < 0:
            grupo_sprite.remove(laser)


        