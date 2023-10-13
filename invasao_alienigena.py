from configuracoes import Configuracoes
import pygame
from botao_start import BotaoStart
from eventos import Eventos

class InvasaoAlienigena:
    """Inicializa e faz a gestão dos atributos e métodos do jogo, assim
    como instancia as classes necessárias."""

    def __init__(self):

        # Obtém as configurações
        self.configuracoes = Configuracoes()

        # Cria o display
        self.tela = self.configuracoes.tela  # Surface
        self.tela_rect = self.configuracoes.tela_rect # Rect

        # Instancia classes necessárias
        self.eventos = Eventos(self)

    def rodar_jogo(self):
        """Executa o loop principal do jogo."""

        while True:

            # Estabelece o background
            self.tela.fill(self.configuracoes.cor_background, self.tela_rect)

            # Disponibiliza o botão Start caso o jogo não esteja ativo
            if not self.configuracoes.jogo_ativo:
                self.botao_start = BotaoStart(self)
                self.botao_start.desenhar()

            self.eventos.reagir_a_eventos(self)

            # Atualiza a tela com as últimas atualizações de display
            pygame.display.flip()
            
if __name__ == '__main__':
    jogo = InvasaoAlienigena()
    jogo.rodar_jogo()


