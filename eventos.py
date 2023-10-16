import pygame
import sys
from lasers import Lasers

class Eventos:
    """Classe renposável pela gestão de todos os eventos possíveis do
    jogo: desde cliques de mouse a teclas pressionadas ou liberadas."""

    def __init__(self, jogo):
        """Inicializa a classe e acessa as configurações de 'jogo'."""
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
        """Reage a eventos do tipo keydown (pressão de tecla). A reação
        varia de acordo com qual tecla foi pressionada."""
        if evento.key == pygame.K_ESCAPE:
            sys.exit()
        elif evento.key == pygame.K_LEFT:
            jogo.configuracoes.movimento_esquerda = True
        elif evento.key == pygame.K_RIGHT:
            jogo.configuracoes.movimento_direita = True
        elif evento.key == pygame.K_SPACE:
            if len(jogo.lasers) < self.configuracoes.limite_lasers:
                self._atira_laser(jogo)

    def _verificar_eventos_keyup(self, evento, jogo):
        """Reage a eventos do tipo keyup (liberação de tecla). A reação
        varia de acordo com qual tecla foi liberada."""        
        if evento.key == pygame.K_LEFT:
            jogo.configuracoes.movimento_esquerda = False
        elif evento.key == pygame.K_RIGHT:
            jogo.configuracoes.movimento_direita = False

    def _verificar_eventos_mouse(self, pos_mouse, jogo):
        """Reage a cliques de mouse."""
        if not self.configuracoes.jogo_ativo:
            botao_start = jogo.botao_start.rect
            if botao_start.collidepoint(pos_mouse):
                self.configuracoes.jogo_ativo = True
                pygame.mouse.set_visible(False)
    
    def _atira_laser(self, jogo):
        """Cria um novo laser e adiciona-o ao grupo de lasers presente no
        argumento passado em 'jogo'."""
        laser = Lasers(jogo)
        jogo.lasers.add(laser)
