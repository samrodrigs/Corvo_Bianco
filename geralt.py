geralt_atributos = {
        "nome": "Geralt",
        "hp": 30,
        "atk": 9,
        "def": 2,
        "dinheiro": 1350,
        "itens": ["Elixir do Vesemir","Pão duro"]}

def geralt():
    print("\n Você é: \n GERALT DE RÍVIA \n")
    print(f'Seus atributos:'f'Vida:{geralt_atributos['hp']}\n'
          f'Ataque:{geralt_atributos['atk']}\n'
          f'Defesa:{geralt_atributos['def']}\n'
          f'Dinheiro:{geralt_atributos['dinheiro']}\n'
          f'Itens:{geralt_atributos['itens']}\n'
          )
    print("Após os acontecimentos com Syanna e Anna Henrieta no Palácio de Beauclair, \n"
          "Você conseguiu o vinhedo de Corvo Bianco, lá mesmo se estabilizando. \n"
          "No topo do pico mais alto de sua propriedade, você medita, ouvindo o barulho dos pássaros \n"
          "e das folhas caindo. \n"
          "Está prestes a anoitecer, o sol começou a se por. O que você faz?")
    print('1 - Ficar e ver o sol se por \n'
          '2 - Voltar para casa \n'
          '3 - Ir ao vinhedo')

    while True:
        escolha = input('Escolha:')
        if escolha == '1':
            print('Ao ficar você ver o céu se tornando escuro e a luz amarelada o sol tocar ')
            break
        elif escolha == '2':

            break
        elif escolha == '3'
        else:
            print('Opção não existente')
































    print("Fim da campanha de Geralt!")
    return "fim"