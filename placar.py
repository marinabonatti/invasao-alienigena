import pygame

class Placar:
    """Responsável por reportar o placar da partida."""

    def __init__(self, jogo):
        self.tela = jogo.tela
        self.tela_rect = jogo.tela_rect
        self.stats = jogo.stats
        self.configuracoes = jogo.configuracoes

        self.cor = (249, 247, 248)
        self.fonte = pygame.font.SysFont(None, 48)
        
        self.preparar_placar()

    def preparar_placar(self):
        """Transforme o placar em uma imagem renderizada"""
        placar_arredondado = int(round(self.stats.pontuacao,-1))
        str_placar = str(placar_arredondado)
        self.imagem = self.fonte.render(
            str_placar, True, self.cor, self.configuracoes.cor_background)
        
        self.rect = self.imagem.get_rect()

        espacamento = self.tela_rect.height // 200
        self.rect.right = self.tela_rect.right - espacamento
        self.rect.top = espacamento

    def mostrar_placar(self):
        """Desenha o placar na tela."""
        self.tela.blit(self.imagem, self.rect)