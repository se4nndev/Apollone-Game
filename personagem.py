class Personagem:
    def __init__(self, nome, vida, ataque, defesa):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa
        self.habilidades = []

    def dialogar(self, texto):
        print(f'\n[{self.nome}]: {texto}')


    def upgrade_vida(self, incremento=10):  #Aumenta a vida do personagem. O valor padrão de incremento é 10.
        self.vida += incremento
        print(f'Vida de {self.nome} após upgrade: {self.vida}')

    def downgrade_vida(self):  #Reduz a vida do personagem, garantindo que não fique negativa
        if self.vida > 15:
            self.vida -= 15
        else:
            self.vida = 0
        print(f'Vida de {self.nome} após downgrade: {self.vida}')

    def __str__(self):
        return f'Personagem: {self.nome}, Vida: {self.vida}, Ataque: {self.ataque}, Defesa: {self.defesa}'

'''
class Personagem:
    def __init__(self, nome, vida, ataque, defesa):
        self.ficha_personagem = {
            'nome': nome,
            'vida': vida,
            'ataque': ataque,
            'defesa': defesa,
            'habilidades': []
        }

    def dialogar(self, texto):
        print(f'\n[{self.ficha_personagem["nome"]}]: {texto}')

    def upgrade_vida(self, incremento=10):
        self.ficha_personagem['vida'] += incremento
        print(f'Vida de {self.ficha_personagem["nome"]} após upgrade: {self.ficha_personagem["vida"]}')

    def downgrade_vida(self):
        if self.ficha_personagem['vida'] > 15:
            self.ficha_personagem['vida'] -= 15
        else:
            self.ficha_personagem['vida'] = 0
        print(f'Vida de {self.ficha_personagem["nome"]} após downgrade: {self.ficha_personagem["vida"]}')

    def __str__(self):
        nome = self.ficha_personagem['nome']
        vida = self.ficha_personagem['vida']
        ataque = self.ficha_personagem['ataque']
        defesa = self.ficha_personagem['defesa']
        return f'Personagem: {nome}, Vida: {vida}, Ataque: {ataque}, Defesa: {defesa}'
'''