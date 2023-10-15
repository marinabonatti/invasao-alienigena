from configuracoes import Configuracoes
import pygame
from botao_start import BotaoStart
from eventos import Eventos
from nave import Nave
from aliens import Aliens
from stats_jogo import StatsJogo
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
        self.tela = self.configuracoes.tela 
        self.tela_rect = self.configuracoes.tela_rect

        # Instancia classes necessárias
        self.stats = StatsJogo(self)
        self.placar = Placar(self)
        self.eventos = Eventos(self)
        self.nave = Nave(self)
        self.lasers = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

    def _criar_alien(self, n_alien, coluna):
        """Cria um único alien, posiciona-o de acordo com os parâmetros
        passados e adiciona-o ao grupo Sprite 'aliens'."""
        alien = Aliens(self)
        alien.rect.y = self.altura_alien + (2 * self.altura_alien * coluna)
        alien.rect.x = self.largura_alien + (2 * self.largura_alien * n_alien)
        self.aliens.add(alien)

    def criar_frota_alienigena(self):
        """Cria uma frota alienígena de acordo com o espaço disponível
        na tela. O tamanho da frota será proporcional à tela na qual o 
        jogador está jogando - pois é FULLSCREEN."""
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
        """Retorna True se a partida acabou - ou seja, se não há naves
        restantes."""
        if self.stats.naves_restantes == 0:
            return True
    
    def reagir_fim_jogo(self):
        """Reinicia os stats (naves restantes, pontuação e nível), salva
        a pontuação atual como highscore se ela de fato for um highscore
        e altera a flag jogo_ativo para False: o jogador deve escolher
        se irá jogar novamente."""
        if self.stats.pontuacao > self.stats.highscore:
            self.stats.highscore = int(round(self.stats.pontuacao,-1))
            with open ("highscore.txt", 'w') as f:
                f.write(str(self.stats.highscore))
        self.stats.resetar_stats()
        self.placar.preparar_placar()
        self.configuracoes.jogo_ativo = False

    def _verificar_bordas_frota(self):
        """Reage adequadamente caso algum alien tenha atingido a borda
        da tela, mudando a direção da frota e fazendo com que ela desça
        em direção à nave do jogador."""
        for alien in self.aliens.sprites():
            if alien.verificar_bordas():
                alien._mudar_direcao_frota()
                break
    
    def verificar_colisoes(self):
        """Verifica os três tipos de colisões possíveis no jogo: laser
        colidindo com alien, alien colidindo com a nave e alien chegando
        no chão. Para cada colisão haverá a reação esperada."""
        for alien in self.aliens.sprites():
            alien._verificar_colisao_aliens_lasers()
            alien._verificar_colisao_aliens_nave()
            alien._verificar_alien_terra()
            break

    def _atualizar_aliens(self):
        """Verifica se uma frota está em alguma borda e, em seguida, faz
        a atualização necessária nas posições de cada alien da frota."""
        self._verificar_bordas_frota()
        self.aliens.update()
        self.verificar_colisoes()

    def disponibilizar_start(self):
        """Disponibiliza o botão Start caso o jogo não esteja ativo."""
        if not self.configuracoes.jogo_ativo:
            self.botao_start = BotaoStart(self)
            self.botao_start.desenhar()

    def atualizar_jogo(self):
        """Roda as funcionalidades do jogo caso ele esteja ativo,
        atualizando a tela conforme necessário."""
        if self.configuracoes.jogo_ativo:
            self.placar.mostrar_placar()
            self.placar.mostrar_highscore_txt()
            self.placar.preparar_naves_restantes()
            self.nave.desenhar()
            self.nave.atualizar_pos_nave(self)
            self.criar_frota_alienigena()
            self._atualizar_aliens()
            for laser in self.lasers.sprites():
                laser.desenhar()
            self.lasers.update(self.lasers)
            if self.validar_fim_jogo():
                self.reagir_fim_jogo()

    def rodar_jogo(self):
        """Executa o loop principal do jogo."""

        while True:

            # Estabelece o background
            self.tela.fill(self.configuracoes.cor_background, self.tela_rect)

            self.eventos.reagir_a_eventos(self)
            self.disponibilizar_start()
            self.atualizar_jogo()

            # Atualiza a tela com as últimas atualizações de display
            pygame.display.flip()
            
if __name__ == '__main__':
    jogo = InvasaoAlienigena()
    jogo.rodar_jogo()


