import random
import time

class Combate:
    def __init__(self):
        self.historico = []  # lista com o registro das ações

    def executar_combate(self, heroi, vilao):
        print("\n--------------------- PREPARE-SE PARA O COMBATE: TENTE DERROTAR O DEVEMORTH! ---------------------")

        while heroi.vida > 0 and vilao.vida > 0:
            print("-------------------------------------------------------------")
            print(f"{heroi.nome} - Vida: {heroi.vida} - Defesa: {heroi.defesa}")
            print(f"{vilao.nome} - Vida: {vilao.vida} - Defesa: {vilao.defesa}")
            print("-------------------------------------------------------------")

            while True:
                print("\nCapitão, escolha a sua ação: ")
                print("1. Canhões de Laser (Ataque padrão)")
                print("2. Ativar os Escudos")
                print("3. Usar o Kit de Reparo")

                opcao = input("Digite o número da ação (1, 2 ou 3): ").strip() #tirar os espaços

                if opcao in ["1", "2", "3"]:
                    break  #sai do loop e avança
                else:
                    print("\nComando inválido. Digite apenas 1, 2 ou 3.")

            escudo_ativo = False

            if opcao == "1":
                print(f"\nFogo! Canhões de Laser atingiram o monstro!")

                dano_heroi_vilao = heroi.ataque - vilao.defesa
                if dano_heroi_vilao < 0:
                    dano_heroi_vilao = 0
                vilao.vida -= dano_heroi_vilao
                print(f"{vilao.nome} tomou {dano_heroi_vilao} de dano!")
                self.historico.append(f"O Cap. Castyel (Apollonne) atacou com os Canhões de Laser e causou {dano_heroi_vilao} de dano")

            elif opcao == "2":
                heroi.ativar_escudos()
                escudo_ativo = True
                self.historico.append(f"O Cap. Castyel (Apollonne) ativou os escudos")

            elif opcao == "3":
                heroi.usar_kit_reparo()
                self.historico.append(f"O Cap. Castyel (Apollonne) usou o Kit de Reparo")

            time.sleep(2)

            if vilao.vida > 0:
                acao_vilao = random.randint(1, 3)  #sorteia uma ação do Devemorth

                if acao_vilao == 1:
                    print(f"\nO Devemorth ataca com seus tentáculos!")

                    dano_vilao_heroi = vilao.ataque - heroi.defesa
                    if dano_vilao_heroi < 0:
                        dano_vilao_heroi = 0
                    heroi.vida -= dano_vilao_heroi
                    print(f"A Apollonne sofreu {dano_vilao_heroi} de dano!")
                    self.historico.append(f"O Devemorth atacou com os tentáculos e causou {dano_vilao_heroi} de dano")

                elif acao_vilao == 2:
                    vilao.absorver_energia_estrela()
                    self.historico.append(f"O Devemorth absorveu energia de uma estrela")

                elif acao_vilao == 3:
                    vilao.raio_eclipse(heroi)
                    self.historico.append(f"O Devemorth disparou o Raio Eclipse")

                time.sleep(2)

            if escudo_ativo:  #o escudo dura só 1 turno
                heroi.defesa -= 10

        print("\n--------------------- FIM DA BATALHA ---------------------")
        if heroi.vida > 0:
            print("VITÓRIA! Devemorth foi destruído! O capitão ainda poderá salvar a humanidade da crise! 🏆")
        else:
            print("DERROTA... A Apollonne foi destruída e o capitão se foi... Fim da linha... 💀")

        print("\n--------------------- Histórico das ações ---------------------")
        for evento in self.historico:
            print(f"- {evento}")