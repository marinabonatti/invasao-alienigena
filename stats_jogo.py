import pygame

class StatsJogo:
    """Rastreia as estatísticas do jogo para que ele possa terminar e/ou
    ser resetado."""

    def __init__(self, jogo):
        """Inicializa a classe e os atributos que dependem do argumento
        passado em 'jogo'."""
        self.configuracoes = jogo.configuracoes
        self.pontuacao = self.configuracoes
        self.nivel = self.configuracoes.nivel
        self.highscore = jogo.configuracoes.highscore
        self.jogo = jogo
        self.resetar_stats()

    def resetar_stats(self):
        """Reseta os componentes do placar da partida, com exceção de
        highscore. O highscore depende de todas as partidas jogadas, não
        apenas da partida atual e, assim, não deve ser resetado."""
        self.naves_restantes = self.configuracoes.naves_restantes
        self.pontuacao = self.configuracoes.pontuacao
        self.nivel = self.configuracoes.nivel
    
    def perder_vida(self):
        """Faz as alterações necessárias toda vez que o usuário perde a
        vida, ou seja, quando ele é atingido por um alien ou quando um
        alien encosta na parte inferior da tela."""
        self.jogo.stats.naves_restantes -= 1
        self.jogo.placar.preparar_naves_restantes()
        self.jogo.aliens.empty()
        self.jogo.lasers.empty()
        self.jogo.criar_frota_alienigena()
        self.jogo.nave.centralizar_nave()
        pygame.time.wait(1000 * 5)