from configuracoes import Configuracoes
import pygame
from botao_start import BotaoStart
from eventos import Eventos
from nave import Nave
from aliens import Aliens

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
        self.nave = Nave(self)
        self.lasers = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

    def _criar_alien(self, n_alien, coluna):
        alien = Aliens(self)
        alien.rect.y = self.altura_alien + (2 * self.altura_alien * coluna)
        alien.rect.x = self.largura_alien + (2 * self.largura_alien * n_alien)
        self.aliens.add(alien)

    def criar_frota_alienigena(self):
        alien = Aliens(self)
        self.largura_alien = alien.rect.width
        self.altura_alien = alien.rect.height

        espaco_x_disponivel = self.tela_rect.width - (2 * self.largura_alien)
        total_alien_x = espaco_x_disponivel // (2 * self.largura_alien)

        espaco_y_disponivel = self.tela_rect.height - (2 * self.altura_alien)
        espaco_y_disponivel -= self.nave.rect.height
        colunas_alien = espaco_y_disponivel // (2 * self.altura_alien)
        if len(self.aliens) == 0:
            for coluna in range(colunas_alien):
                for n_alien in range(total_alien_x):
                    self._criar_alien(n_alien, coluna)
        self.aliens.draw(self.tela)


    def rodar_jogo(self):
        """Executa o loop principal do jogo."""

        while True:

            # Estabelece o background
            self.tela.fill(self.configuracoes.cor_background, self.tela_rect)

            self.eventos.reagir_a_eventos(self)

            # Disponibiliza o botão Start caso o jogo não esteja ativo
            if not self.configuracoes.jogo_ativo:
                self.botao_start = BotaoStart(self)
                self.botao_start.desenhar()

            # Roda as funcionalidades do jogo caso ele esteja ativo
            elif self.configuracoes.jogo_ativo:
                self.nave.desenhar()
                self.nave.atualizar_pos_nave(self)
                self.criar_frota_alienigena()
                self.aliens.update()
                for laser in self.lasers.sprites():
                    laser.desenhar()
                self.lasers.update(self.lasers)

            # Atualiza a tela com as últimas atualizações de display
            pygame.display.flip()
            
if __name__ == '__main__':
    jogo = InvasaoAlienigena()
    jogo.rodar_jogo()


