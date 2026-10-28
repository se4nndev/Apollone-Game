from personagem import Personagem

class Heroi(Personagem):
    def __init__(self, nome, vida, ataque, defesa):
        super().__init__(nome, vida, ataque, defesa)
        self.itens = {'kit_reparo': 3} #Não deixar o kit de reparo infinito
        self.habilidades = ['Canhão de Plasma', 'Escudos', 'Kit de Reparo']

    def ativar_escudos(self):
        self.defesa += 10
        print(f"\n[Avencier]: Capitão, os escudos de força foram amplificados! Defesa atualizada para: {self.defesa}")

    def usar_kit_reparo(self):
        if self.itens['kit_reparo'] <= 0:
            print("\n[Avencier]: Capitão, não tem mais kits de reparo!")
            return
        self.itens['kit_reparo'] -= 1
        print(f"\n[Avencier]: Ativando protocolo de emergência, capitão. Os bots com kits de reparo emergencial foram liberados! Kits restantes: {self.itens['kit_reparo']}")
        self.upgrade_vida(25)