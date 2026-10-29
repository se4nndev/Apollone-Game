from heroi import Heroi
from vilao import Vilao
from combate import Combate


def pausar():
    input("(Pressione Enter para continuar...)")

def main():
    
    herois = [Heroi('Cap. Castyel (Apollonne)', 150, 35, 5)]

    viloes = [Vilao('Devemorth', 120, 20, 5)]

    heroi = herois[0]
    vilao = viloes[0]

    #dialogo inicial, se tivesse interface, imagine como uma cutscene, rs
    pular_dialogo = input("Pressione enter para começar ou digite P para pular a intro: ").strip().lower()

    if pular_dialogo != "p":
        print("\n===================== APOLLONNE: A ÚLTIMA ESPERANÇA =====================")
        print("\nA humanidade enfrenta uma crise energética global... A Apollonne é a última esperança dos humanos...")
        print("A nave Apollonne chega ao planeta de destino na galáxia de Triângulo e encontra apenas poeira e escuridão.")
        pausar()
        heroi.dialogar("Ué, o planeta não deveria estar aqui? Porque só tem poeira?")
        pausar()
        heroi.dialogar("Avencier, estamos mesmo no lugar certo?")
        pausar()
        print("\n[Avencier]: Afirmativo, capitão. Estamos na localização exata... Embora eu não detecte o planeta")
        pausar()
        heroi.dialogar("Ah... qual é? O que aconteceu com este planeta?")
        pausar()
        print("\n[Avencier]: Eu não sei dizer, capitão. Parece que o planeta foi consumido... Aliás, detecto uma presença gigantesca se aproximando!")
        pausar()
        heroi.dialogar("Isso definitivamente não é bom...")
        pausar()
        heroi.dialogar("Cara... OLHA O TAMANHO DESSE ALIENÍGENA!!")
        pausar()
        vilao.dialogar("Humano... Eu sinto o poder da sua nave...")
        pausar()
        heroi.dialogar("Um dos eclipsadores de mundos, isso explica o motivo do planeta não estar aqui")
        pausar()
        heroi.dialogar("Avencier, fugir dessa criatura é quase impossível, ative os mecanismos de combate, teremos que lutar!")
        pausar()
        print("\n[Avencier]: Afirmativo, capitão. Inicializando sistema de combate.")
        pausar()
        vilao.dialogar("Que armas fofinhas, não são páreas para mim. Consumirei sua nave e seu fim será breve...")
        pausar()
        heroi.dialogar("Se for para salvar a humanidade, tentarei cumprir minha missão a todo custo! Vamos ver quem sai dessa com vida...")
        pausar()

    combate = Combate()
    combate.executar_combate(heroi, vilao)


main()