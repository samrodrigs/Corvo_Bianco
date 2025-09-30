from geralt import geralt
from yennefer import yennefer

def menu_inicial():
    print('Olá Viajante, bem vindo a Corvo Bianco.\n Escolha seu personagem')
    print('1 - Geralt - Bruxo')
    print('2 - Yennefer - Feiticeira')
    print('3 - Sair')

    def jogarComo_Geralt():
        print('Você escolheu Geralt, o Lobo Branco')

    def jogarComo_Yennefer():
        print('Você escolheu Yennefer, a Feiticeira do Caos')

    while True:
        escolha = input('Escolha:')
        if escolha == '1':
            (jogarComo_Geralt())
            (geralt())
            break
        elif escolha == '2':
            (jogarComo_Yennefer())
            (yennefer())
            break
        elif escolha == '3':
            print('Até a vista, viajante...')
            break
        else:
            print('Opção não existente')


menu_inicial()
