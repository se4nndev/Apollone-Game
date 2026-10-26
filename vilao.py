from personagem import Personagem

class Vilao(Personagem):
    def __init__(self, nome, vida, ataque, defesa):
        super().__init__(nome, vida, ataque, defesa)

    def absorver_energia_estrela(self):
        print(f"\n[{self.ficha_personagem['nome']}]: Devemorth absorve o calor de uma estrela para se regenerar!")
        self.upgrade_vida(30)

    def raio_eclipse(self):
        print(f"\n[{self.ficha_personagem['nome']}]: CONCENTRAÇÃO DE ENERGIA NEGRA! Devemorth dispara o Raio Eclipse contra a Apollonne!")
        # No arquivo de combate, faremos esse método causar o dobro de dano!