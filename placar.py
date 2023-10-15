import pygame

class Placar:
    """Responsável por reportar o placar da partida."""

    def __init__(self, jogo):
        self.tela = jogo.tela
        self.tela_rect = jogo.tela_rect
        self.stats = jogo.stats
        self.configuracoes = jogo.configuracoes

        self.cor = (249, 247, 248)
        self.tamanho_fonte = int(self.configuracoes.tamanho_stats)
        self.fonte = pygame.font.SysFont(None, self.tamanho_fonte)
        self.espacamento = self.configuracoes.espacamento_stats
        
        self.preparar_placar()
        self.preparar_highscore()

    def preparar_placar(self):
        """Transforma o placar em uma imagem renderizada"""
        placar_arredondado = int(round(self.stats.pontuacao,-1))
        str_placar = str(placar_arredondado)
        self.imagem_placar = self.fonte.render(
            str_placar, True, self.cor, self.configuracoes.cor_background)
        
        self.rect_placar = self.imagem_placar.get_rect()

        self.rect_placar.right = self.tela_rect.right - self.espacamento
        self.rect_placar.top = self.espacamento

    def preparar_highscore(self):
        """Transforma o highscore em uma imagem renderizada."""
        str_highscore = str(self.stats.highscore)
        self.imagem_highscore = self.fonte.render(
            str_highscore, True, self.cor, self.configuracoes.cor_background)
        self.rect_highscore = self.imagem_highscore.get_rect()
        
        self.rect_highscore.center = self.tela_rect.center
        self.rect_highscore.top = self.espacamento

        
    def mostrar_placar(self):
        """Desenha o placar na tela."""
        self.tela.blit(self.imagem_placar, self.rect_placar)
    
    def mostrar_highscore(self):
        """Desenha o placar na tela."""
        self.tela.blit(self.imagem_highscore, self.rect_highscore)