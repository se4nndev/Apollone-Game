class Personagem:
    def __init__(self, nome, vida, ataque, defesa):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa
        self.habilidades = []
        self.itens = {} 

    def dialogar(self, texto):
        print(f'\n[{self.nome}]: {texto}')

    def upgrade_vida(self, incremento=10):
        self.vida += incremento
        print(f'Vida de {self.nome} após upgrade: {self.vida}')

    def downgrade_vida(self):
        if self.vida > 15:
            self.vida -= 15
        else:
            self.vida = 0
        print(f'Vida de {self.nome} após downgrade: {self.vida}')

    def __str__(self):
        return f'Personagem: {self.nome}, Vida: {self.vida}, Ataque: {self.ataque}, Defesa: {self.defesa}'