class StatsJogo:
    """Rastreia as estatísticas do jogo para que ele possa terminar e/ou
    ser resetado."""

    def __init__(self, jogo):
        self.configuracoes = jogo.configuracoes
        self.pontuacao = self.configuracoes
        self.nivel = self.configuracoes.nivel
        self.highscore = jogo.configuracoes.highscore
        self.resetar_stats()

    def resetar_stats(self):
        self.naves_restantes = self.configuracoes.naves_restantes
        self.pontuacao = self.configuracoes.pontuacao
        self.nivel = self.configuracoes.nivel