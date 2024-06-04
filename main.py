# Variáveis que armazenam as strings de cada opção do menu
microplasticoStr = "O que é microplástico?"
ideonella_sakaiensisStr = "O que é Ideonella sakaiensis?"
petaseStr = "O que é PETase?"
calculadoraStr = "Calculadora de bactérias"

# Função que inicia e apresenta o programa
def start():
    print(f"Olá, seja bem-vindo(a) ao BioWave, uma central de controle de microplástico!\n\n"
          f"1 - {microplasticoStr}\n"
          f"2 - {ideonella_sakaiensisStr}\n"
          f"3 - {petaseStr}\n"
          f"4 - {calculadoraStr}\n")

    opcao = input("Digite o número correspondente à opção desejada -> ")

    while not opcao.isnumeric() or int(opcao) not in range(1, 5):
        opcao = input("Digite um valor válido -> ")

    opcao = int(opcao)

    # Redireciona o usuário para o tópico escolhido
    if opcao == 1:
        microplastico()
    elif opcao == 2:
        ideonella_sakaiensis()
    elif opcao == 3:
        petase()
    elif opcao == 4:
        calculadora()

# Função que finaliza o programa
def end():
    print("Obrigado por utilizar o BioWave! Até a próxima!")

# Função que permite ao usuário escolher um novo tópico para navegar
def teleporte(local):

    continuar = input("Deseja continuar navegando? (Digite 'sim' ou 'nao')\n"
                      "-> ")

    while continuar.lower() not in ["sim", "nao"]:
        continuar = input("Digite uma resposta válida -> ")

    if continuar.lower() == "nao":
        end()
        return None

    opcao_local = []

    # Verifica qual o tópico que o usuário está para apresentar as opções corretas
    if local == 'microplastico':
        opcao_local = [ideonella_sakaiensisStr, petaseStr, calculadoraStr]
    elif local == 'ideonella_sakaiensis':
        opcao_local = [microplasticoStr, petaseStr, calculadoraStr]
    elif local == 'petase':
        opcao_local = [microplasticoStr, ideonella_sakaiensisStr, calculadoraStr]
    elif local == 'calculadora':
        opcao_local = [microplasticoStr, ideonella_sakaiensisStr, petaseStr]

    print("\nEscolha uma das opções abaixo para continuar a navegação:\n")

    # Apresenta as opções disponíveis
    for i, opcao in enumerate(opcao_local, start=1):
        print(f"{i} - {opcao}")

    opcao = input("\nDigite o número correspondente à opção desejada -> ")

    while not opcao.isnumeric() or int(opcao) not in range(1, 4):
        opcao = input("Digite um valor válido -> ")

    opcao = int(opcao)

    # Redireciona o usuário para o tópico escolhido
    if opcao_local[opcao - 1] == microplasticoStr:
        microplastico()
    elif opcao_local[opcao - 1] == ideonella_sakaiensisStr:
        ideonella_sakaiensis()
    elif opcao_local[opcao - 1] == petaseStr:
        petase()
    elif opcao_local[opcao - 1] == calculadoraStr:
        calculadora()


# Função que mostra informações sobre os microplásticos
def microplastico():
    print("Microplástico é um termo que se refere a pequenas partículas de plástico com menos de 5mm de diâmetro, que são encontradas em diversos ambientes, como oceanos, rios, solo e até mesmo no ar.\n"
          "Essas partículas são geradas a partir da degradação de plásticos maiores, como garrafas PET, sacolas plásticas, embalagens, entre outros, e também são utilizadas em produtos de higiene pessoal, como esfoliantes e pastas de dente.\n"
          "O microplástico é um grande problema ambiental, pois é facilmente ingerido por animais marinhos e terrestres, podendo causar sérios danos à saúde, além de poluir o meio ambiente.\n")

    teleporte("microplastico")

# Função que mostra informações sobre a bactéria Ideonella sakaiensis
def ideonella_sakaiensis():
    print("Ideonella sakaiensis é uma bactéria que chamou a atenção dos cientistas por sua capacidade de degradar o plástico PET (polietileno tereftalato), amplamente usado em garrafas de bebidas, embalagens de alimentos e roupas.\n"
          "Descoberta em 2016 em uma usina de reciclagem de PET no Japão, essa bactéria pode quebrar o PET em componentes menores que ela utiliza como fonte de energia.\n"
          "A Ideonella sakaiensis faz isso produzindo enzimas específicas que atacam e decompõem as longas cadeias de moléculas de PET.\n"
          "Essa habilidade única torna a bactéria uma aliada promissora na luta contra a poluição por plásticos, especialmente microplásticos.\n"
          "No projeto BioWave, utilizamos bactérias sintéticas baseadas na Ideonella sakaiensis para descontaminar amostras de água, auxiliando na redução significativa dos microplásticos presentes no ambiente marinho.\n")

    teleporte("ideonella_sakaiensis")

# Função que mostra informações sobre a enzima PETase
def petase():
    print("A PETase é uma enzima produzida pela bactéria Ideonella sakaiensis, e é essa enzima que lhe confere a habilidade extraordinária de degradar o PET.\n"
          "A PETase funciona quebrando as longas cadeias moleculares do PET em componentes menores, como o tereftalato e o etilenoglicol, que podem ser usados pela bactéria como energia.\n"
          "Essa capacidade de degradação é particularmente valiosa porque o PET é um plástico muito resistente e que leva centenas de anos para se decompor naturalmente.\n"
          "Com a PETase, a decomposição ocorre de forma muito mais rápida e eficiente. No âmbito do projeto BioWave, a PETase é utilizada em conjunto com sensores e drones subaquáticos para mapear e reduzir a concentração de microplásticos nos oceanos.\n"
          "Essa tecnologia inovadora nos permite combater a poluição de forma sustentável e eficaz, contribuindo para a preservação dos ecossistemas marinhos e a promoção da economia azul.")

    teleporte("petase")

# Função que calcula a quantidade de bactérias Ideonella sakaiensis necessárias para degradar uma quantidade de microplástico em condições ideais
# O cálculo não está 100% correto nem preciso mas é uma aproximação ideal que conseguimos chegar, ainda mais pela falta de informações e estudos sobre o assunto
def calculadora():
    # Algumas informações que temos:

    # 1mg petase consome 0,25mg PET / dia
    # 1 bactéria produz 10^(-6) mg PETase / dia
    # 1 bacteria pesa 10^(-9) mg
    # 1M bactérias pesa 10^(-3) mg
    # 1M bactérias produz 10^(-3) mg PETase / dia

    qntd_microplastico = input("Digite a quantidade de microplástico que existe em sua amostra para calcularmos quantas bactérias Ideonella sakaiensis serão necessárias para degradá-lo!"
                              "\nDigite a quantidade em miligramas -> ")

    while not qntd_microplastico.isnumeric():
        qntd_microplastico = input("Digite um valor válido -> ")

    qntd_microplastico = int(qntd_microplastico)

    degradacao_petase = 0.25 # mg PET / dia
    producao_petase = 10**(-6) # mg PETase / bactéria / dia

    qntd_petase = qntd_microplastico / degradacao_petase # Quantidade de PETase em mg para 1 dia
    qtnd_bacterias = qntd_petase / producao_petase # Quantidade de bactérias necessárias para degradar o PET

    print(f"\nPensando em condições ideais, serão necessárias {qtnd_bacterias} bactérias Ideonella sakaiensis, que produzirão {qntd_petase}mg de PETase, para degradar {qntd_microplastico}mg de microplástico em 1 dia!")

    teleporte("calculadora")


start()