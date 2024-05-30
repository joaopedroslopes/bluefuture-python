import time

def start():
    print("Olá, seja bem-vindo(a) à central de controle de microplástico!")
    #time.sleep(3)
    print("Este programa foi desenvolvido para ajudar a controlar a quantidade de microplástico no oceano.")
    #time.sleep(3)
    qtd_microplastico = input("Digite a quantidade de microplástico que existe em sua amostra para calcularmos quantas bactérias Ideonella sakaiensis serão necessárias para degradá-lo!"
                              "\nDigite a quantidade em miligramas -> ")

    while not qtd_microplastico.isnumeric():
        qtd_microplastico = input("Digite um valor válido -> ")

    qtd_microplastico = int(qtd_microplastico)

    calculo(qtd_microplastico)

def calculo(qtd_microplastico):
    # 1mg petase -> 1.000.000 bactérias
    # 1mg petase / dia -> 0,25mg PET
    # 1 bactéria -> 10^-6 g petase



start()