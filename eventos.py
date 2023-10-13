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
            if evento.type == pygame.MOUSEBUTTONDOWN:
                pos_mouse = pygame.mouse.get_pos()
                self._verificar_eventos_mouse(pos_mouse, jogo)
            if evento.type == pygame.KEYDOWN:
                self._verificar_eventos_keydown(evento, jogo)         
            if evento.type == pygame.KEYUP:
                self._verificar_eventos_keyup(evento, jogo)             
    
    def _verificar_eventos_keydown(self, evento, jogo):
        if evento.key == pygame.K_ESCAPE:
            sys.exit()
        elif evento.key == pygame.K_LEFT:
            jogo.configuracoes.movimento_esquerda = True
        elif evento.key == pygame.K_RIGHT:
            jogo.configuracoes.movimento_direita = True

    def _verificar_eventos_keyup(self, evento, jogo):
        if evento.key == pygame.K_LEFT:
            jogo.configuracoes.movimento_esquerda = False
        elif evento.key == pygame.K_RIGHT:
            jogo.configuracoes.movimento_direita = False

    def _verificar_eventos_mouse(self, pos_mouse, jogo):
        if not self.configuracoes.jogo_ativo:
            botao_start = jogo.botao_start.rect
            if botao_start.collidepoint(pos_mouse):
                self.configuracoes.jogo_ativo = True
    
    def _atualizar_pos_nave(self, jogo):
        if jogo.configuracoes.movimento_direita:
            if jogo.nave.rect.right < jogo.tela_rect.right:
                jogo.nave.rect.x += jogo.configuracoes.velocidade_nave
        if jogo.configuracoes.movimento_esquerda:
            if jogo.nave.rect.x > 0:
                jogo.nave.rect.x -= jogo.configuracoes.velocidade_nave