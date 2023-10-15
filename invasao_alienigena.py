from configuracoes import Configuracoes
import pygame
from botao_start import BotaoStart
from eventos import Eventos
from nave import Nave
from aliens import Aliens
from stats_jogo import StatsJogo
from fim_jogo import FimJogo
from placar import Placar

class InvasaoAlienigena:
    """Faz a gestão dos atributos e métodos necessários para a execução
    do jogo."""

    def __init__(self):
        """Inicializa a classe, faz a gestão dos atributos e instancia
        as outras classes necessárias para o andamento do jogo."""

        # Obtém as configurações
        pygame.init()
        self.configuracoes = Configuracoes()

        # Cria o display
        self.tela = self.configuracoes.tela  # Surface
        self.tela_rect = self.configuracoes.tela_rect # Rect

        # Instancia classes necessárias
        self.stats = StatsJogo(self)
        self.placar = Placar(self)
        self.eventos = Eventos(self)
        self.nave = Nave(self)
        self.lasers = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.fim_jogo = FimJogo(self)

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
        if len(self.aliens) == 0 and self.stats.naves_restantes > 0:
            for coluna in range(colunas_alien):
                for n_alien in range(total_alien_x):
                    self._criar_alien(n_alien, coluna)
        self.aliens.draw(self.tela)

    def validar_fim_jogo(self):
        if self.stats.naves_restantes == 0:
            return True
    
    def reagir_fim_jogo(self):
            self.stats.resetar_stats()
            self.placar.preparar_placar()
            self.configuracoes.jogo_ativo = False


    def _verificar_bordas_frota(self):
        """Reage adequadamente caso algum alien tenha atingido a borda
        da tela."""

        for alien in self.aliens.sprites():
            if alien.verificar_bordas():
                self._mudar_direcao_frota()
                break

    def _mudar_direcao_frota(self):
        """Faz com que a frota inteira desça na tela de acordo com a 
        velocidade_y_alien estabelecida em configurações, além de mudar
        a direção da frota."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.configuracoes.velocidade_y_alien
        self.configuracoes.direcao_frota *= -1

    def _verificar_colisao_aliens_nave(self):
        """Verifica se houve colisão entre algum alien e a nave. Se sim,
        paralisa o jogo - pois o jogador acabou de perder uma vida."""
        if pygame.sprite.spritecollideany(self.nave, self.aliens):
            self.stats.naves_restantes -= 1
            self.aliens.empty()
            self.lasers.empty()

            self.criar_frota_alienigena()
            self.nave.centralizar_nave()

            pygame.time.wait(1000 * 5)

    def _verificar_alien_terra(self):
        """Verifica se algum alien encostou no chão. Se sim, paralisa o
        jogo - pois o jogador acabou de perder uma vida."""
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.tela_rect.bottom:
                self.stats.naves_restantes -= 1
                self.aliens.empty()
                self.lasers.empty()

                self.criar_frota_alienigena()
                self.nave.centralizar_nave()

                pygame.time.wait(1000 * 5)
                break

    def _verificar_colisao_aliens_lasers(self):
        """Verifica se houve colisão entre aliens e lasers. Se sim,
        ambos os membros de cada grupo envolvido na colisão serão 
        removidos."""
        colisoes = pygame.sprite.groupcollide(
            self.lasers, self.aliens, True, True)
        if colisoes:
            for aliens in colisoes.values():
                self.stats.pontuacao += (self.configuracoes.ponto_por_alien *
                                         len(aliens)) 
            if len(self.aliens) == 0:
                self.configuracoes.nivel += 1
                self.configuracoes.aumentar_velocidade()
            self.placar.preparar_placar()


    def _atualizar_aliens(self):
        """Verifica se uma frota está em alguma borda e, em seguida, faz
        a atualização necessária nas posições de cada alien da frota."""
        self._verificar_bordas_frota()
        self.aliens.update()
        self._verificar_colisao_aliens_nave()
        self._verificar_alien_terra()


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
                self.placar.mostrar_placar()
                self.nave.desenhar()
                self.nave.atualizar_pos_nave(self)
                self.criar_frota_alienigena()
                self._atualizar_aliens()
                for laser in self.lasers.sprites():
                    laser.desenhar()
                self.lasers.update(self.lasers)
                self._verificar_colisao_aliens_lasers()
                if self.validar_fim_jogo():
                    self.reagir_fim_jogo()

            # Atualiza a tela com as últimas atualizações de display
            pygame.display.flip()
            
if __name__ == '__main__':
    jogo = InvasaoAlienigena()
    jogo.rodar_jogo()


