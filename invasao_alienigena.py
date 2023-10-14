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

    def _criar_alien(self, numero_alien, coluna):
        """Cria um alien e posiciona-o na linha."""
        alien = Aliens(self)
        alien.rect.x = self.largura_alien
        alien.rect.x += (2 * self.largura_alien * numero_alien)
        alien.rect.y = self.altura_alien + (2 * self.altura_alien * coluna)
        alien.desenhar()
        self.aliens.add(alien)


    def criar_frota_alienígena(self):
        alien = Aliens(self)
        self.largura_alien = alien.rect.width
        self.altura_alien = alien.rect.height

        espaco_x_disponivel = self.tela_rect.width - (2 * self.largura_alien)
        numero_x_aliens = espaco_x_disponivel // (2 * self.largura_alien)

        espaco_y_disponivel = self.tela_rect.height - (2* self.altura_alien)
        espaco_y_disponivel -= self.nave.rect.height
        numero_y_aliens = espaco_y_disponivel // (2 * self.altura_alien)

        for coluna in range(numero_y_aliens):
            for numero_alien in range(numero_x_aliens):
                self._criar_alien(numero_alien, coluna)



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
                self.criar_frota_alienígena()
                for laser in self.lasers.sprites():
                    laser.desenhar()
                    laser.atualizar_pos_laser()
                    laser.excluir_laser_antigo(self.lasers, laser)

            # Atualiza a tela com as últimas atualizações de display
            pygame.display.flip()
            
if __name__ == '__main__':
    jogo = InvasaoAlienigena()
    jogo.rodar_jogo()


