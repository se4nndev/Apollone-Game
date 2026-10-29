from personagem import Personagem

class Vilao(Personagem):
    def __init__(self, nome, vida, ataque, defesa):
        super().__init__(nome, vida, ataque, defesa)
        self.habilidades = ['Tentáculos', 'Absorver Energia', 'Raio Eclipse']

    def absorver_energia_estrela(self):
        print(f"\nDevemorth absorveu a energia de uma estrela próxima para se regenerar!")
        self.upgrade_vida(25)

    def raio_eclipse(self, heroi):
        print(f"\nDevemorth disparou o Raio Eclipse contra a Apollonne!")
        dano = (self.ataque * 2) - heroi.defesa
        if dano < 0:
            dano = 0
        heroi.vida -= dano
        print(f"NOSSA! A Apollonne sofreu {dano} de dano!")