class StatsJogo:
    """Rastreia as estatísticas do jogo para que ele possa terminar e/ou
    ser resetado."""

    def __init__(self, jogo):
        self.configuracoes = jogo.configuracoes
        self.resetar_stats()

    def resetar_stats(self):
        self.naves_restantes = self.configuracoes.naves_restantes
    
        