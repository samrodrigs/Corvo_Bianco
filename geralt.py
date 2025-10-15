
geralt_atributos = {
    "nome": "Geralt",
    "hp": 30,
    "atk": 9,
    "def": 2,
    "dinheiro": 1350,
    "itens": ["Elixir do Vesemir", "Pão duro"]
}


def primeira_parte():
    print('Após os acontecimentos com Syanna e Anna Henrieta no Palácio de Beauclair, \n'
          'Você conseguiu o vinhedo de Corvo Bianco, lá mesmo se estabilizando. \n'
          'No topo do pico mais alto de sua propriedade, você medita, ouvindo o barulho dos pássaros \n'
          'e das folhas caindo. \n')
    print('Está prestes a anoitecer, o sol começou a se por. O que você faz?')

    escolha_feita = False

    print('1 - Ficar e ver o sol se por')
    print('2 - Voltar para casa')
    print('3 - Ir ao vinhedo')
    escolha = input('Escolha: ')

    while True:
        if escolha == '1' and not escolha_feita:
            geralt_atributos["hp"] += 2
            print('🌅 Você ganhou mais 2 Pontos de vida! Ao ficar você ver o céu se tornando escuro e a '
                  'luz amarelada do sol tocar o chão. A paz interior \n'
                  'toca seu peito e você respira ')
            print('Já não resta nada para explorar agora\n'
                  'Volte para casa. ')
            print('HP:')
            print(geralt_atributos['hp'])
            escolha_feita = True

        elif escolha == '2':
            print('🌄 Quando o sol se vai, você desce aos poucos observando os musgos se apossarem das pedras, a lua ganhar força\n'
                ' e as luzes do Castelo de Beauclair se acenderem. Puxa o ar com força ao pisar nos pedregulhos '
                'que te guiam a casa principal.')
            break

        elif escolha == '3' and not escolha_feita:
            geralt_atributos["itens"].append('Uvas de Corvo Bianco')
            print(
                '🍇 Você vai ao vinhedo, mas nada lá lhe parece diferente do que antes. Você vai até as vinhas, e pega algumas uvas\n'
                'colocando-as em seu saquinho de pano e logo em seguida de volta em seu gibão\n'
                'Você conseguiu: Uvas de Corvo Bianco ')
            print('Já não resta nada para explorar agora\n'
                  'Volte para casa. ')
            print(geralt_atributos['itens\n'])
            escolha_feita = True

        else:
            print('Opção não existente')

        if escolha_feita:
            print('Não restou mais nada para explorar, você foi para casa\n')
            break



def segunda_parte():
    print('Voltando para casa você percebe as lamparinas se ascendendo, a calmaria da propriedade e os \n'
          'funcionários indo cada um aos seus respectivos lugares.\n'
          ' \n - Hora de descansar - Você murmura. ')
    print('Porém ao entrar você sente um arrepio estranho, uma energia e um cheiro familiar...')
    print('O que fazer, bruxo?')
    escolha_feita1 = False


    while True:
        print('1 - Ignorar e ir dormir')
        print('2 - Investigar a casa')
        escolha2 = input('Escolha: ')

        if escolha2 == '1' and not escolha_feita1:
            print('😴 Você sobe para o quarto, tira seu gibão e roupas; sem tomar banho, deita-se na cama mas o arrepio\n'
                'ainda persiste.\n'
                '- Esse cheiro...'
                'Você, ainda inseguro com o tal cheiro, fica inquieto na cama por um período de tempo\n'
                'que pareciam ser horas atá ouvir um curto susurro vindo das sombras.\n'
                'Aroma de Lilás e Groselha\n'
                '- Meu Lobo Branco...\n'
                '- Merda. - Você diz em voz baixa. - Quando planejou vir aqui, Yennefer?\n'
                'Estava resolvendo problemas de estado e senti sua falta - Ela responde\n\n'
                'Delicadamente, Yennefer se aproxima e se revela ')
            print('Você, dando um longo suspiro sente cada vez mais o cheiro que te desarma.'
                  'Yennefer usa um robe de seda preto, os cachos negros estão soltos. Ela se aproxima mais.\n'
                  '- Suponho que você saiba o que quero. - Yennefer diz'
                  '- Não estou com energia para seus joguinhos.'
                  '- Não estou jogando desta vez.'
                  '- Então o que veio fazer aqui exatamente?'
                  '- '
                  '- Hum')


        elif escolha2 == '2':
            print(
                'Rodeando a casa, você puxa a adaga em seu cinto e começa a procurar pelo tal invasor ou monstro.\n'
                'Andando em passos lentos, você mantém a lâmina próxima, seguindo o som misterioso...\n'
                'Até que...você reconhece o cheiro. \n'
                'Aroma de lilás e groselha\n'
                '- Merda, Yen.\n'
                '- O que? - Yennefer aparece em meio a escuridão, usando sua roupa preta e branca, como se estivesse\n'
                'acabado de sair de um portal.\n'
                '- Você não pode aparecer aqui assim.\n'
                '- Não é sempre assim que nos encontramos? Nos susurros?\n'
                '- Costumava ser.\n'
                '- Você me pediu para ficar, estou aqui.\n'
                '- Pedi isso meses atrás. Ciri seguiu a própria vida, fiquei com isso, sozinho.\n'
                '- Não era você que gostava da solidão?\n'
                '- Não quando se tratava de você Yen. Mas você foi embora.'
                '- Eu tinha assuntos de Estado, você, os seus de Bruxo.\n'
                '- Minha vida se trata disso que tenho agora.'
                '- Vim para fazer parte dela, se você permitir, Geralt. - Yennefer diz, se aproximando devagar\n'
                '- Hum '
                )
            break

        else:
            print('Opção não existente')


def campanha():
    print("\nVocê é GERALT DE RÍVIA\n")
    print(f"Vida: {geralt_atributos['hp']}")
    print(f"Ataque: {geralt_atributos['atk']}")
    print(f"Defesa: {geralt_atributos['def']}")
    print(f"Dinheiro: {geralt_atributos['dinheiro']}")
    print(f"Itens: {geralt_atributos['itens']}\n")

    primeira_parte()
    segunda_parte()
    print("Fim da campanha de Geralt!")














