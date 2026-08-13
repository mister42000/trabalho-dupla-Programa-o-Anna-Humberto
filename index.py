import random
import time


# =========================
# CONFIGURAÇÕES
# =========================

MAX_VIDA = 100
MAX_FOME = 100
MAX_SEDE = 100
MAX_SONO = 100


# =========================
# JOGADOR
# =========================

class Jogador:

    def __init__(self):
        self.vida = 100
        self.fome = 100
        self.sede = 100
        self.sono = 100

        self.dia = 1
        self.hora = 8

        self.inventario = {
            "carne": 0,
            "agua": 2,
            "madeira": 0,
            "pedra": 0
        }

    # -------------------------
    # STATUS
    # -------------------------

    def mostrar_status(self):

        print("\n" + "=" * 40)
        print(f"DIA {self.dia} | {self.hora:02d}:00")
        print("=" * 40)

        print(f"❤️ Vida:  {self.vida}/100")
        print(f"🍖 Fome:  {self.fome}/100")
        print(f"💧 Sede:  {self.sede}/100")
        print(f"😴 Sono:  {self.sono}/100")

        print("\n🎒 Inventário:")

        for item, quantidade in self.inventario.items():
            print(f"  {item}: {quantidade}")

        print("=" * 40)

    # -------------------------
    # PASSAGEM DE TEMPO
    # -------------------------

    def passar_tempo(self, horas=1):

        for _ in range(horas):

            self.hora += 1

            if self.hora >= 24:
                self.hora = 0
                self.dia += 1

            # O tempo afeta o jogador
            self.fome -= random.randint(2, 5)
            self.sede -= random.randint(3, 6)
            self.sono -= random.randint(2, 4)

        self.verificar_estado()

    # -------------------------
    # ESTADO DO JOGADOR
    # -------------------------

    def verificar_estado(self):

        self.fome = max(0, self.fome)
        self.sede = max(0, self.sede)
        self.sono = max(0, self.sono)

        if self.fome == 0:
            self.vida -= 5
            print("🍖 Você está morrendo de fome!")

        if self.sede == 0:
            self.vida -= 8
            print("💧 Você está extremamente desidratado!")

        if self.sono == 0:
            self.vida -= 3
            print("😴 Você está completamente exausto!")

        if self.vida <= 0:
            self.vida = 0


    # =========================
    # COMER
    # =========================

    def comer(self):

        if self.inventario["carne"] <= 0:
            print("\nVocê não possui comida.")
            return

        self.inventario["carne"] -= 1

        recupera = random.randint(20, 35)

        self.fome = min(MAX_FOME, self.fome + recupera)

        print(f"\n🍖 Você comeu carne.")
        print(f"Fome +{recupera}")

        self.passar_tempo(1)


    # =========================
    # BEBER
    # =========================

    def beber(self):

        if self.inventario["agua"] <= 0:
            print("\n💧 Você não possui água.")
            return

        self.inventario["agua"] -= 1

        recupera = random.randint(30, 45)

        self.sede = min(MAX_SEDE, self.sede + recupera)

        print(f"\n💧 Você bebeu água.")
        print(f"Sede +{recupera}")

        self.passar_tempo(1)


    # =========================
    # DORMIR
    # =========================

    def dormir(self):

        print("\n😴 Você se deitou para dormir...")

        horas = random.randint(5, 8)

        self.passar_tempo(horas)

        recupera = random.randint(50, 80)

        self.sono = min(MAX_SONO, self.sono + recupera)

        print(f"Você dormiu por {horas} horas.")
        print(f"😴 Sono +{recupera}")


    # =========================
    # CAÇAR
    # =========================

    def cacar(self):

        print("\n🏹 Você entrou na floresta procurando animais...")

        self.passar_tempo(2)

        chance = random.randint(1, 100)

        if chance <= 60:

            carne = random.randint(1, 3)

            self.inventario["carne"] += carne

            print(f"🏹 Você conseguiu caçar um animal!")
            print(f"🍖 Carne obtida: {carne}")

        else:

            print("❌ Você não encontrou nenhum animal.")

            if random.randint(1, 100) <= 30:
                self.encontro_inimigo()


    # =========================
    # COLETAR RECURSOS
    # =========================

    def coletar(self):

        print("\n🌲 Você está procurando recursos...")

        self.passar_tempo(1)

        madeira = random.randint(1, 5)
        pedra = random.randint(0, 4)

        self.inventario["madeira"] += madeira
        self.inventario["pedra"] += pedra

        print(f"🪵 Madeira encontrada: {madeira}")
        print(f"🪨 Pedra encontrada: {pedra}")


    # =========================
    # EXPLORAR
    # =========================

    def explorar(self):

        print("\n🗺️ Você começou a explorar a região...")

        self.passar_tempo(2)

        evento = random.randint(1, 100)

        if evento <= 25:

            print("\n💧 Você encontrou uma fonte de água!")

            quantidade = random.randint(1, 3)

            self.inventario["agua"] += quantidade

            print(f"Você coletou {quantidade} garrafa(s).")

        elif evento <= 45:

            print("\n🎁 Você encontrou uma mochila abandonada!")

            comida = random.randint(1, 2)
            agua = random.randint(1, 2)

            self.inventario["carne"] += comida
            self.inventario["agua"] += agua

            print(f"🍖 Carne: +{comida}")
            print(f"💧 Água: +{agua}")

        elif evento <= 65:

            self.encontro_inimigo()

        else:

            print("\n🌲 Nada aconteceu.")
            print("A floresta permaneceu silenciosa...")


    # =========================
    # INIMIGO
    # =========================

    def encontro_inimigo(self):

        inimigos = [
            ("Lobo", 40, 8),
            ("Javali", 50, 10),
            ("Urso", 80, 15)
        ]

        nome, vida_inimigo, dano = random.choice(inimigos)

        print(f"\n⚠️ Um {nome} apareceu!")

        while vida_inimigo > 0 and self.vida > 0:

            print("\n1 - Atacar")
            print("2 - Fugir")

            escolha = input("> ")

            if escolha == "1":

                dano_player = random.randint(10, 25)

                vida_inimigo -= dano_player

                print(
                    f"⚔️ Você atacou o {nome} "
                    f"causando {dano_player} de dano."
                )

                if vida_inimigo <= 0:
                    print(f"☠️ Você matou o {nome}!")

                    carne = random.randint(1, 4)

                    self.inventario["carne"] += carne

                    print(f"🍖 Você conseguiu {carne} carne(s).")
                    break

                dano_recebido = random.randint(
                    dano - 4,
                    dano + 4
                )

                self.vida -= dano_recebido

                print(
                    f"💥 O {nome} atacou você "
                    f"causando {dano_recebido} de dano."
                )

            elif escolha == "2":

                chance = random.randint(1, 100)

                if chance <= 60:
                    print("🏃 Você conseguiu fugir!")
                    break

                else:

                    dano_recebido = random.randint(
                        dano - 3,
                        dano + 5
                    )

                    self.vida -= dano_recebido

                    print(
                        f"❌ Você não conseguiu fugir!"
                    )

                    print(
                        f"💥 O {nome} causou "
                        f"{dano_recebido} de dano."
                    )

            else:
                print("Opção inválida.")

        self.passar_tempo(1)


# =========================
# JOGO
# =========================

def jogo():

    jogador = Jogador()

    print("=" * 40)
    print("       SOBREVIVÊNCIA")
    print("=" * 40)

    print("\nVocê acorda sozinho no meio de uma floresta.")
    print("Não sabe onde está.")
    print("Seu objetivo é sobreviver.")

    while jogador.vida > 0:

        jogador.mostrar_status()

        print("\nO que você deseja fazer?")

        print("1 - 🏹 Caçar")
        print("2 - 💧 Beber água")
        print("3 - 🍖 Comer")
        print("4 - 😴 Dormir")
        print("5 - 🌲 Coletar recursos")
        print("6 - 🗺️ Explorar")
        print("7 - ⏳ Esperar")
        print("8 - ❌ Sair")

        escolha = input("\n> ")

        if escolha == "1":
            jogador.cacar()

        elif escolha == "2":
            jogador.beber()

        elif escolha == "3":
            jogador.comer()

        elif escolha == "4":
            jogador.dormir()

        elif escolha == "5":
            jogador.coletar()

        elif escolha == "6":
            jogador.explorar()

        elif escolha == "7":

            print("\n⏳ Você esperou uma hora...")
            jogador.passar_tempo(1)

        elif escolha == "8":

            print("\nVocê abandonou a floresta.")
            break

        else:
            print("\n❌ Opção inválida.")

        if jogador.vida <= 0:

            print("\n" + "=" * 40)
            print("☠️ VOCÊ MORREU")
            print("=" * 40)

            print(f"Você sobreviveu até o dia {jogador.dia}.")

            break


# =========================
# INICIAR
# =========================

if __name__ == "__main__":
    jogo()