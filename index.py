import random

MAX_VIDA = 100
MAX_FOME = 100
MAX_SEDE = 100
MAX_SONO = 100

RECEITAS = {
    "machado": {
        "madeira": 3,
        "pedra": 2
    },

    "lanca": {
        "madeira": 2,
        "pedra": 1
    },

    "fogueira": {
        "madeira": 5,
        "pedra": 3
    },

    "abrigo": {
        "madeira": 10,
        "pedra": 5
    }
}


# Matriz de recursos.
# Cada linha representa uma região diferente.
REGIOES = [
    ["floresta", "floresta", "rio", "floresta"],
    ["campo", "floresta", "montanha", "rio"],
    ["floresta", "campo", "campo", "montanha"],
    ["rio", "floresta", "montanha", "floresta"]
]

def limpar_texto(texto):
    """Remove espaços desnecessários e deixa o texto formatado."""
    return texto.strip().title()


def mostrar_linha():
    print("=" * 55)


def pausar():
    input("\nPressione ENTER para continuar...")

def cadastrar_sobrevivente(sobreviventes):

    mostrar_linha()
    print("CADASTRO DE SOBREVIVENTE")
    mostrar_linha()

    nome = limpar_texto(input("Nome: "))

    while not nome:
        print("O nome não pode ficar vazio.")
        nome = limpar_texto(input("Nome: "))

    while True:
        try:
            idade = int(input("Idade: "))

            if idade <= 0:
                print("Digite uma idade válida.")
            else:
                break

        except ValueError:
            print("Digite apenas números.")

    print("\nProfissões disponíveis:")
    print("1 - Caçador")
    print("2 - Engenheiro")
    print("3 - Médico")
    print("4 - Coletor")

    profissao_opcoes = [
        "Caçador",
        "Engenheiro",
        "Médico",
        "Coletor"
    ]

    while True:
        escolha = input("Escolha: ")

        if escolha in ["1", "2", "3", "4"]:
            profissao = profissao_opcoes[int(escolha) - 1]
            break

        print("Opção inválida.")

    sobrevivente = {
        "nome": nome,
        "idade": idade,
        "profissao": profissao,
        "vida": 100,
        "fome": 100,
        "sede": 100,
        "sono": 100
    }

    sobreviventes.append(sobrevivente)

    print(f"\n{nome} foi cadastrado como {profissao}!")
    return sobrevivente


def listar_sobreviventes(sobreviventes):

    mostrar_linha()
    print("SOBREVIVENTES")
    mostrar_linha()

    if not sobreviventes:
        print("Nenhum sobrevivente cadastrado.")
        return

    for i, sobrevivente in enumerate(sobreviventes, start=1):

        print(
            f"{i} - {sobrevivente['nome']} | "
            f"{sobrevivente['idade']} anos | "
            f"{sobrevivente['profissao']}"
        )

def mostrar_status(sobrevivente, inventario, dia, hora):

    mostrar_linha()
    print(f"DIA {dia} | {hora:02d}:00")
    print(f"SOBREVIVENTE: {sobrevivente['nome']}")
    mostrar_linha()

    print(f"❤️ Vida: {sobrevivente['vida']}/100")
    print(f"🍖 Fome: {sobrevivente['fome']}/100")
    print(f"💧 Sede: {sobrevivente['sede']}/100")
    print(f"😴 Sono: {sobrevivente['sono']}/100")

    print("\n🎒 INVENTÁRIO")

    for item, quantidade in inventario.items():
        print(f"- {item.title()}: {quantidade}")

def passar_tempo(sobrevivente, horas):

    for _ in range(horas):

        sobrevivente["fome"] -= random.randint(2, 5)
        sobrevivente["sede"] -= random.randint(3, 6)
        sobrevivente["sono"] -= random.randint(2, 4)

    verificar_estado(sobrevivente)


def verificar_estado(sobrevivente):

    sobrevivente["fome"] = max(0, sobrevivente["fome"])
    sobrevivente["sede"] = max(0, sobrevivente["sede"])
    sobrevivente["sono"] = max(0, sobrevivente["sono"])

    if sobrevivente["fome"] == 0:
        sobrevivente["vida"] -= 5
        print("🍖 Você está morrendo de fome!")

    if sobrevivente["sede"] == 0:
        sobrevivente["vida"] -= 8
        print("💧 Você está extremamente desidratado!")

    if sobrevivente["sono"] == 0:
        sobrevivente["vida"] -= 3
        print("😴 Você está completamente exausto!")

    sobrevivente["vida"] = max(0, sobrevivente["vida"])

def mostrar_inventario(inventario):

    mostrar_linha()
    print("INVENTÁRIO")
    mostrar_linha()

    for item, quantidade in inventario.items():
        print(f"{item.title()}: {quantidade}")


def adicionar_item(inventario, item, quantidade):

    if item not in inventario:
        inventario[item] = 0

    inventario[item] += quantidade

def comer(sobrevivente, inventario):

    if inventario["carne"] <= 0:
        print("\nVocê não possui carne.")
        return

    inventario["carne"] -= 1

    recuperacao = random.randint(20, 35)

    sobrevivente["fome"] = min(
        MAX_FOME,
        sobrevivente["fome"] + recuperacao
    )

    print(f"\n🍖 Você comeu carne.")
    print(f"Fome +{recuperacao}")

    passar_tempo(sobrevivente, 1)


def beber(sobrevivente, inventario):

    if inventario["agua"] <= 0:
        print("\n💧 Você não possui água.")
        return

    inventario["agua"] -= 1

    recuperacao = random.randint(30, 45)

    sobrevivente["sede"] = min(
        MAX_SEDE,
        sobrevivente["sede"] + recuperacao
    )

    print(f"\n💧 Você bebeu água.")
    print(f"Sede +{recuperacao}")

    passar_tempo(sobrevivente, 1)

def dormir(sobrevivente):

    print("\n😴 Você foi dormir...")

    horas = random.randint(5, 8)

    passar_tempo(sobrevivente, horas)

    recuperacao = random.randint(50, 80)

    sobrevivente["sono"] = min(
        MAX_SONO,
        sobrevivente["sono"] + recuperacao
    )

    print(f"Você dormiu por {horas} horas.")
    print(f"😴 Sono +{recuperacao}")

def escolher_regiao():

    print("\nEscolha onde procurar recursos:")

    for i, regiao in enumerate(REGIOES, start=1):
        print(f"{i} - Região {i}: {regiao}")

    while True:

        escolha = input("Escolha: ")

        try:
            numero = int(escolha)

            if 1 <= numero <= len(REGIOES):
                linha = REGIOES[numero - 1]

                # Escolhe uma posição aleatória da matriz
                local = random.choice(linha)

                print(f"\nVocê foi para uma região de {local}.")
                return local

        except ValueError:
            pass

        print("Escolha inválida.")


def coletar_recursos(sobrevivente, inventario):

    regiao = escolher_regiao()

    passar_tempo(sobrevivente, 1)

    print("\n🌲 Procurando recursos...")

    if regiao == "floresta":

        madeira = random.randint(2, 6)
        pedra = random.randint(0, 2)

        adicionar_item(inventario, "madeira", madeira)
        adicionar_item(inventario, "pedra", pedra)

        print(f"🪵 Madeira encontrada: {madeira}")
        print(f"🪨 Pedra encontrada: {pedra}")

    elif regiao == "montanha":

        pedra = random.randint(2, 7)

        adicionar_item(inventario, "pedra", pedra)

        print(f"🪨 Pedra encontrada: {pedra}")

    elif regiao == "rio":

        agua = random.randint(1, 4)

        adicionar_item(inventario, "agua", agua)

        print(f"💧 Água coletada: {agua}")

    elif regiao == "campo":

        comida = random.randint(1, 3)

        adicionar_item(inventario, "carne", comida)

        print(f"🍖 Comida encontrada: {comida}")

def cacar(sobrevivente, inventario):

    print("\n🏹 Você entrou na floresta para caçar...")

    passar_tempo(sobrevivente, 2)

    chance = random.randint(1, 100)

    if chance <= 65:

        carne = random.randint(1, 4)

        adicionar_item(inventario, "carne", carne)

        print("🏹 Você conseguiu caçar um animal!")
        print(f"🍖 Carne obtida: {carne}")

    else:

        print("❌ Você não encontrou nenhum animal.")

        if random.randint(1, 100) <= 30:
            combate(sobrevivente, inventario)

def combate(sobrevivente, inventario):

    inimigos = [
        ["Lobo", 40, 8],
        ["Javali", 50, 10],
        ["Urso", 80, 15]
    ]

    inimigo = random.choice(inimigos)

    nome = inimigo[0]
    vida_inimigo = inimigo[1]
    dano_inimigo = inimigo[2]

    print(f"\n⚠️ Um {nome} apareceu!")

    while vida_inimigo > 0 and sobrevivente["vida"] > 0:

        print("\n1 - Atacar")
        print("2 - Fugir")

        escolha = input("> ")

        if escolha == "1":

            dano = random.randint(10, 25)

            # Bônus para quem possui uma lança
            if inventario["lanca"] > 0:
                dano += 10

            vida_inimigo -= dano

            print(f"⚔️ Você causou {dano} de dano!")

            if vida_inimigo <= 0:

                print(f"☠️ Você derrotou o {nome}!")

                carne = random.randint(1, 4)

                adicionar_item(
                    inventario,
                    "carne",
                    carne
                )

                print(f"🍖 Você conseguiu {carne} carne(s).")
                break

            dano_recebido = random.randint(
                max(1, dano_inimigo - 4),
                dano_inimigo + 4
            )

            sobrevivente["vida"] -= dano_recebido

            print(
                f"💥 O {nome} causou "
                f"{dano_recebido} de dano!"
            )

        elif escolha == "2":

            if random.randint(1, 100) <= 60:

                print("🏃 Você conseguiu fugir!")
                break

            dano = random.randint(
                max(1, dano_inimigo - 3),
                dano_inimigo + 5
            )

            sobrevivente["vida"] -= dano

            print("❌ Você não conseguiu fugir!")
            print(f"💥 Você sofreu {dano} de dano.")

        else:
            print("Opção inválida.")

    verificar_estado(sobrevivente)

def possui_materiais(inventario, receita):

    for material, quantidade in receita.items():

        if inventario.get(material, 0) < quantidade:
            return False

    return True


def construir(sobrevivente, inventario):

    mostrar_linha()
    print("CONSTRUÇÃO")
    mostrar_linha()

    itens = list(RECEITAS.keys())

    for i, item in enumerate(itens, start=1):

        receita = RECEITAS[item]

        materiais = []

        for material, quantidade in receita.items():
            materiais.append(
                f"{quantidade} {material}"
            )

        print(f"{i} - {item.title()}")
        print("    " + " + ".join(materiais))

    print("0 - Voltar")

    escolha = input("\nEscolha: ")

    if escolha == "0":
        return

    try:
        indice = int(escolha) - 1

        if indice < 0 or indice >= len(itens):
            print("Opção inválida.")
            return

        item = itens[indice]
        receita = RECEITAS[item]

        if not possui_materiais(inventario, receita):

            print("\n❌ Você não possui materiais suficientes.")

            return

        for material, quantidade in receita.items():
            inventario[material] -= quantidade

        adicionar_item(inventario, item, 1)

        print(f"\n🔨 Você construiu: {item.title()}!")

        if item == "abrigo":
            print("🏕️ Agora você possui um abrigo.")

    except ValueError:
        print("Digite um número válido.")

def evento_aleatorio(sobrevivente, inventario):

    chance = random.randint(1, 100)

    if chance > 35:
        return

    eventos = [
        "cabana",
        "tempestade",
        "ferimento",
        "suprimentos",
        "animal"
    ]

    evento = random.choice(eventos)

    print("\n🎲 EVENTO ALEATÓRIO!")

    if evento == "cabana":

        print("🏚️ Você encontrou uma cabana abandonada.")

        if random.randint(1, 100) <= 60:

            agua = random.randint(1, 3)
            madeira = random.randint(1, 4)

            adicionar_item(inventario, "agua", agua)
            adicionar_item(inventario, "madeira", madeira)

            print(f"💧 Água encontrada: {agua}")
            print(f"🪵 Madeira encontrada: {madeira}")

        else:
            print("A cabana estava completamente vazia.")

    elif evento == "tempestade":

        print("⛈️ Uma tempestade começou!")

        dano = random.randint(5, 15)

        sobrevivente["vida"] -= dano

        print(f"❤️ Você sofreu {dano} de dano.")

    elif evento == "ferimento":

        print("🌿 Você se feriu enquanto caminhava.")

        dano = random.randint(5, 12)

        sobrevivente["vida"] -= dano

        print(f"❤️ Vida -{dano}")

    elif evento == "suprimentos":

        print("🎒 Você encontrou uma mochila abandonada!")

        carne = random.randint(1, 3)
        agua = random.randint(1, 2)

        adicionar_item(inventario, "carne", carne)
        adicionar_item(inventario, "agua", agua)

        print(f"🍖 Carne: +{carne}")
        print(f"💧 Água: +{agua}")

    elif evento == "animal":

        print("🐺 Você ouviu um animal se aproximando...")

        combate(sobrevivente, inventario)

def menu_jogo(sobrevivente):

    inventario = {
        "carne": 2,
        "agua": 2,
        "madeira": 0,
        "pedra": 0,
        "machado": 0,
        "lanca": 0,
        "fogueira": 0,
        "abrigo": 0
    }

    dia = 1
    hora = 8

    while sobrevivente["vida"] > 0:

        mostrar_status(
            sobrevivente,
            inventario,
            dia,
            hora
        )

        print("\nO que deseja fazer?")

        print("1 - 🏹 Caçar")
        print("2 - 🌲 Coletar recursos")
        print("3 - 🔨 Construir")
        print("4 - 🍖 Comer")
        print("5 - 💧 Beber água")
        print("6 - 😴 Dormir")
        print("7 - 🎒 Ver inventário")
        print("8 - ⏳ Esperar")
        print("9 - ❌ Sair")

        escolha = input("\n> ")

        horas_passadas = 0

        if escolha == "1":

            cacar(sobrevivente, inventario)
            horas_passadas = 2

        elif escolha == "2":

            coletar_recursos(
                sobrevivente,
                inventario
            )

            horas_passadas = 1

        elif escolha == "3":

            construir(
                sobrevivente,
                inventario
            )

        elif escolha == "4":

            comer(
                sobrevivente,
                inventario
            )

            horas_passadas = 1

        elif escolha == "5":

            beber(
                sobrevivente,
                inventario
            )

            horas_passadas = 1

        elif escolha == "6":

            dormir(sobrevivente)

            horas_passadas = random.randint(5, 8)

        elif escolha == "7":

            mostrar_inventario(inventario)

        elif escolha == "8":

            print("\n⏳ Você esperou uma hora.")
            horas_passadas = 1

        elif escolha == "9":

            print("\nVocê abandonou a floresta.")
            break

        else:

            print("\n❌ Opção inválida.")

        # Atualização do relógio
        hora += horas_passadas

        while hora >= 24:
            hora -= 24
            dia += 1

        # Eventos aleatórios
        if horas_passadas > 0:
            evento_aleatorio(
                sobrevivente,
                inventario
            )

        # Verifica morte
        verificar_estado(sobrevivente)

        if sobrevivente["vida"] <= 0:

            mostrar_linha()
            print("☠️ VOCÊ MORREU")
            mostrar_linha()

            print(
                f"{sobrevivente['nome']} "
                f"não conseguiu sobreviver."
            )

            print(f"Você chegou ao dia {dia}.")

            break

def main():

    sobreviventes = []

    mostrar_linha()
    print("🌲 SOBREVIVÊNCIA 🌲")
    mostrar_linha()

    while True:

        print("\nMENU PRINCIPAL")
        print("1 - 👤 Cadastrar sobrevivente")
        print("2 - 📋 Listar sobreviventes")
        print("3 - 🎮 Iniciar jogo")
        print("4 - ❌ Sair")

        escolha = input("\n> ")

        if escolha == "1":

            cadastrar_sobrevivente(
                sobreviventes
            )

        elif escolha == "2":

            listar_sobreviventes(
                sobreviventes
            )

            pausar()

        elif escolha == "3":

            if not sobreviventes:

                print(
                    "\n❌ Cadastre pelo menos "
                    "um sobrevivente primeiro."
                )

                continue

            listar_sobreviventes(
                sobreviventes
            )

            try:

                numero = int(
                    input("\nEscolha o sobrevivente: ")
                )

                if 1 <= numero <= len(sobreviventes):

                    sobrevivente = sobreviventes[
                        numero - 1
                    ]

                    menu_jogo(sobrevivente)

                else:
                    print("Sobrevivente inválido.")

            except ValueError:

                print("Digite um número válido.")

        elif escolha == "4":

            print("\nObrigado por jogar!")
            break

        else:

            print("\n❌ Opção inválida.")

if __name__ == "__main__":
    main()
