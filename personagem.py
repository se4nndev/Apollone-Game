class Personagem:
    def __init__(self, nome, vida, ataque, defesa):
        self.ficha_personagem = {
            'nome': nome,
            'vida': vida,
            'ataque': ataque,
            'defesa': defesa,
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
