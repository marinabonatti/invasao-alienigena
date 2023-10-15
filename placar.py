import pygame
from pygame.sprite import Group
from nave import Nave

class Placar:
    """Responsável por reportar o placar da partida. O placar é composto
    por pontuação, highscore, nível e naves restantes."""

    def __init__(self, jogo):
        """Inicializa a classe, acessa os atributos necessários de 'jogo'
        e prepara o placar."""
        self.tela = jogo.tela
        self.tela_rect = jogo.tela_rect
        self.stats = jogo.stats
        self.configuracoes = jogo.configuracoes
        self.jogo = jogo

        self.cor = (249, 247, 248)
        self.tamanho_fonte = int(self.configuracoes.tamanho_stats)
        self.tamanho_fonte_menor = int(self.configuracoes.tamanho_stats * 0.60)
        self.fonte = pygame.font.SysFont(None, self.tamanho_fonte)
        self.espacamento = self.configuracoes.espacamento_stats
        
        self.preparar_placar()

    def preparar_placar(self):
        """Faz a preparação de pontuação, highscore e nível. O preparo
        consiste em transformar os componentes do placar em imagens 
        renderizadas, para que possam ser exibidas na tela."""
        self._preparar_pontuacao()
        self._preparar_highscore()
        self._preparar_nivel()

    def _preparar_pontuacao(self):
        """Transforma a pontuação em uma imagem renderizada"""
        placar_arredondado = int(round(self.stats.pontuacao,-1))
        str_placar = str(placar_arredondado)
        self.imagem_placar = self.fonte.render(
            str_placar, True, self.cor, self.configuracoes.cor_background)
        
        self.rect_placar = self.imagem_placar.get_rect()

        self.rect_placar.right = self.tela_rect.right - self.espacamento
        self.rect_placar.top = self.espacamento

    def _preparar_nivel(self):
        """Transforma o nível em uma imagem renderizada."""
        str_nivel = f"LVL {self.stats.nivel}"
        tamanho_fonte = int(self.configuracoes.tamanho_stats * 0.75)
        self.fonte_menor = pygame.font.SysFont(None, tamanho_fonte)
        self.imagem_nivel = self.fonte_menor.render(
            str_nivel, True, self.cor, self.configuracoes.cor_background)
        self.rect_nivel = self.imagem_nivel.get_rect()

        espacamento = self.espacamento
        self.rect_nivel.right = self.rect_placar.right
        self.rect_nivel.top = self.rect_placar.bottom
        self.rect_nivel.height -= espacamento

    def _preparar_highscore(self):
        """Transforma o highscore em uma imagem renderizada."""
        str_highscore = str(self.stats.highscore)
        self.imagem_highscore = self.fonte.render(
            str_highscore, True, self.cor, self.configuracoes.cor_background)
        self.rect_highscore = self.imagem_highscore.get_rect()
        
        self.rect_highscore.center = self.tela_rect.center
        self.rect_highscore.top = self.espacamento

    def preparar_naves_restantes(self):
        """Cria naves de acordo com a quantidade de naves restantes em
        stats, faz o posicionamento na tela e o desenho de cada uma."""
        self.naves_restantes = Group()
        for n_nave in range(self.stats.naves_restantes):
            nave = Nave(self.jogo)
            nave.rect.x = self.espacamento + (n_nave * nave.rect.width)
            nave.rect.y = self.espacamento
            self.naves_restantes.add(nave)
        self.naves_restantes.draw(self.tela)

    def mostrar_highscore_txt(self):
        """Transforma a palavra 'highscore' em uma imagem renderizada e
        a desenha na tela."""
        str = "HIGH SCORE"
        self.imagem_highscore_txt = self.fonte_menor.render(
            str, True, self.cor, self.configuracoes.cor_background)
        self.rect_highscore_txt = self.imagem_highscore_txt.get_rect()
        self.rect_highscore_txt.midtop = (self.rect_highscore.midbottom)
        self.rect_highscore_txt.y += self.espacamento
        self.tela.blit(self.imagem_highscore_txt, self.rect_highscore_txt)

    def mostrar_placar(self):
        """Desenha a pontuação, o highscore e o nível na tela."""
        self.tela.blit(self.imagem_placar, self.rect_placar)
        self.tela.blit(self.imagem_highscore, self.rect_highscore)
        self.tela.blit(self.imagem_nivel,self.rect_nivel) 