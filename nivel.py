import pygame

class Nivel:
    """Responsável por reportar o nível da partida."""

    def __init__(self, jogo):
        self.tela = jogo.tela
        self.tela_rect = jogo.tela_rect
        self.stats = jogo.stats
        self.configuracoes = jogo.configuracoes
        self.placar = jogo.placar

        self.cor = (249, 247, 248)
        self.tamanho_fonte = int(self.configuracoes.tamanho_stats * 0.75)
        self.fonte = pygame.font.SysFont(None, self.tamanho_fonte)
        
        self.preparar_nivel()    

    
    def preparar_nivel(self):
        """Transforme o nível em uma imagem renderizada"""
        str_nivel = f"LVL {self.stats.nivel}"
        self.imagem = self.fonte.render(
            str_nivel, True, self.cor, self.configuracoes.cor_background)
        self.rect = self.imagem.get_rect()

        espacamento = self.configuracoes.espacamento_stats
        self.rect.right = self.placar.rect_placar.right
        self.rect.top = self.placar.rect_placar.bottom
        self.rect.height -= espacamento

    def mostrar_nivel(self):
        self.tela.blit(self.imagem,self.rect)