import pygame
import sys

class Eventos:
    """Classe renposável pela gestão de todos os eventos possíveis do
    jogo: desde cliques de mouse a teclas pressionadas ou liberadas."""

    def __init__(self, jogo):
        self.configuracoes = jogo.configuracoes

    def reagir_a_eventos(self, jogo):
        """Obtém e reage a eventos do jogo."""
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                self._verificar_eventos_keydown(evento)
            if evento.type == pygame.MOUSEBUTTONDOWN:
                pos_mouse = pygame.mouse.get_pos()
                self._verificar_eventos_mouse(pos_mouse, jogo)
    
    def _verificar_eventos_keydown(self, evento):
        if evento.key == pygame.K_ESCAPE:
            sys.exit()
    def _verificar_eventos_mouse(self, pos_mouse, jogo):
        if not self.configuracoes.jogo_ativo:
            botao_start = jogo.botao_start.rect
            if botao_start.collidepoint(pos_mouse):
                self.configuracoes.jogo_ativo = True