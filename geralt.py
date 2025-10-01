geralt_atributos = {
        "nome": "Geralt",
        "hp": 30,
        "atk": 9,
        "def": 2,
        "dinheiro": 1350,
        "itens": ["Elixir do Vesemir","Pão duro"]}

def primeira_parte():
    print("\n Você é: \n GERALT DE RÍVIA \n")
    print(f'Seus atributos:'f'Vida:{geralt_atributos['hp']}\n'
          f'Ataque:{geralt_atributos['atk']}\n'
          f'Defesa:{geralt_atributos['def']}\n'
          f'Dinheiro:{geralt_atributos['dinheiro']}\n'
          f'Itens:{geralt_atributos['itens']}\n'
          )
    print('Após os acontecimentos com Syanna e Anna Henrieta no Palácio de Beauclair, \n'
          'Você conseguiu o vinhedo de Corvo Bianco, lá mesmo se estabilizando. \n'
          'No topo do pico mais alto de sua propriedade, você medita, ouvindo o barulho dos pássaros \n'
          'e das folhas caindo. \n')
    print('Está prestes a anoitecer, o sol começou a se por. O que você faz?')
    print('1 - Ficar e ver o sol se por \n'
          '2 - Voltar para casa \n'
          '3 - Ir ao vinhedo')

    escolha_feita = False


    while True:
        escolha = input('Escolha:')
        if escolha == '1' and not escolha_feita:
            geralt_atributos["hp"] += 2
            print('🌅 Você ganhou mais 2 Pontos de vida! Ao ficar você ver o céu se tornando escuro e a '
            'luz amarelada do sol tocar o chão. A paz interior \n'
            'toca seu peito e você respira ')
            escolha_feita = True
            print(geralt_atributos['hp'])

        elif escolha == '2':
            print('🌄 Quando o sol se vai, você desce aos poucos observando os musgos se apossarem das pedras, a lua ganhar força\n'
                  ' e as luzes do Castelo de Beauclair se acenderem. Puxa o ar com força ao pisar nos pedregulhos '
                  'que te guiam a casa principal.')
            break

        elif escolha == '3' and not escolha_feita:
            geralt_atributos["itens"].append('Uvas de Corvo Bianco')
            print('🍇 Você vai ao vinhedo, mas nada lá lhe parece diferente do que antes. Você vai até as vinhas, e pega algumas uvas\n'
                  'colocando-as em seu saquinho de pano e logo em seguida de volta em seu gibão\n'
                  'Você conseguiu: Uvas de Corvo Bianco ')
            escolha_feita = True
            print(geralt_atributos['itens'])

        else:
            print('Opção não existente')

        if escolha_feita1 and escolha_feita:
            print('Já não resta nada para explorar agora\n'
                  'Volte para casa. ')


        def segunda_parte():
            print('Voltando para casa você percebe as lamparinas se ascendendo, a calmaria da propriedade e os \n'
                  'funcionários indo cada um aos seus respectivos lugares.\n'
                  ' - Hora de descansar - Você murmura. ')
            print('Porém ao entrar você sente um arrepio estranho, uma energia e um cheiro familiar...')
            print('O que fazer, bruxo?')
            print('1 - Ignorar e ir dormir \n'
                  '2 - Investigar a casa \n'


    escolha_feita1 = False
    escolha_feita2 = False

    while True:
        escolha2 = input('Escolha:')
        if escolha2 == '1' and not escolha_feita1:
            print('😴	Você sobe para o quarto, tira seu gibão e roupas; sem tomar banho, deita-se na cama mas o arrepio\n'
                  'ainda persiste.\n'
                  '- Esse cheiro...')
            escolha_feita1 = True

        elif escolha2 == '2':
            print('Rodeando a casa, você puxa a adaga em seu cinto e começa a procurar pelo tal invasor ou monstro. Andando\n'
                  'em pessos lentos você mantém a lâmina próxima, seguindo esse  ')

            break


        else:
            print('Opção não existente')


























    print("Fim da campanha de Geralt!")
    return 'Fim'