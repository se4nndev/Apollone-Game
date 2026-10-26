from personagem import Personagem

class Heroi(Personagem):
    def __init__(self, nome, vida, ataque, defesa):
        super().__init__(nome, vida, ataque, defesa)
        
    def ativar_escudos(self):
        self.ficha_personagem['defesa'] += 10
        print(f"\n[Avencier]: Capitão, os escudos de força foram amplificados! Defesa atualizada para: {self.ficha_personagem['defesa']}")

    def usar_kit_reparo(self):
        print(f"\n[Avencier]: Ativando protocolo de emergência, os robôs de manutenção emergencial foram liberados!")
        self.upgrade_vida(25)