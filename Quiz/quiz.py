import random
import json
NUMERO_PERGUNTAS = 5


def iniciar_jogo():
    nome = input("Digite seu nome: ")
    nivel = int(input("1 = Nível Fácil\n2 = Nível Médio\n3 = Nível Dificíl\nResposta: "))
    lista_perguntas = carregar_perguntas(nivel)
    pontos = 0 
    numeros_sorteados = []
    for i in range(0, NUMERO_PERGUNTAS):
        while True:
            numero = random.randint(0, len(lista_perguntas) - 1)
            if numero not in numeros_sorteados:
                numeros_sorteados.append(numero)
                break
        acertou = fazer_perguntas(numero, lista_perguntas)
        if acertou is True:
            print("voce acertou")
            pontos += 1
        else:
            print("voce errou")
    print(f"seus pontos foram {pontos}")
    atualizar_ranking(nome, pontos)
    visualizar_ranking(top_10 = True)
    
def carregar_perguntas (nivel):
    # recebe: uma string que indica o nivel de dificuldade da questão 
    # faz: carrega as perguntas do arquivo e trasforma em lista
    # retorna: uma lista de perguntas
    if nivel == 1:
        with open('questoes_fáceis.json') as json_file:
            lista_perguntas = json.load(json_file)
    if nivel == 2:
        with open('questoes_medias.json') as json_file:
            lista_perguntas = json.load(json_file)
    if nivel == 3:
        with open('questoes_difíceis.json') as json_file:
            lista_perguntas = json.load(json_file)
    return lista_perguntas 


def fazer_perguntas (numero, lista_perguntas):
    pergunta = lista_perguntas[numero]['pergunta']
    alternativa_1 = lista_perguntas[numero]['alternativas'][0]['titulo']
    alternativa_2 = lista_perguntas[numero]['alternativas'][1]['titulo']
    alternativa_3 = lista_perguntas[numero]['alternativas'][2]['titulo']
    print(pergunta)
    print(f"A = {alternativa_1}")
    print(f"B = {alternativa_2}")
    print(f"C = {alternativa_3}")
    resposta = input("Digite A, B, C: ").upper()
    if resposta == "A":
        if lista_perguntas[numero]['alternativas'][0]['verdadeiro'] is True:
            return True 
        else:
            return False
    if resposta == "B":
        if lista_perguntas[numero]['alternativas'][1]['verdadeiro'] is True:
            return True 
        else:
            return False
    if resposta == "C":
        if lista_perguntas[numero]['alternativas'][2]['verdadeiro'] is True:
            return True 
        else:
            return False
        
        
def carregar_ranking ():
    # recebe: nada
    # faz: carrega as nomes dos antigos jogadores.
    # retorna: uma lista de jogadores do ranking
    with open('ranking.json') as json_file:
        lista_ranking = json.load(json_file)
        return lista_ranking
    
    
def criar_pergunta ():
    # recebe: nada
    # faz: perguntar ao usuario os dados da pergunta e enviar para salvar em arquivo.
    # retorna: nada
    nivel = int(input("Em qual nivel voce deseja adicionar (Ex: 1, 2 , 3): " ))
    titulo = input("Qual a pergunta que deseja adicionar ou digite n para sair? ")
    alternativa_1 = input("Qual a primeira alternativa que deseja adicionar: ")
    alternativa_2 = input("Qual a segunda alternativa que deseja adicionar: ")
    alternativa_3 = input("Qual a terceira alternativa que deseja adicionar: ")
    alternativa_verdadeira = input("qual a alternativa verdadeira: ").upper()
    if alternativa_verdadeira not in ['A','B','C']:
        print("Error: Alternativa não existente")
        return
    pergunta = {
        "pergunta": titulo,
        "alternativas": [
            {
                "titulo": alternativa_1,
                "verdadeiro": alternativa_verdadeira == "A"
            },
            {
                "titulo": alternativa_2,
                "verdadeiro": alternativa_verdadeira == "B"
            },
            {
                "titulo": alternativa_3,
                "verdadeiro": alternativa_verdadeira == "C"
            }
        ]
    } 
    lista_perguntas = carregar_perguntas(nivel)
    lista_perguntas.append(pergunta)
    salvar_perguntas (nivel, lista_perguntas)
    print("A sua pergunta foi adicionada")
def salvar_perguntas (nivel, lista_perguntas):
    # recebe: um dicionario indicando a pergunta
    # faz: salvar a lista no arquivo.
    # retorna: nada
    if nivel == 1:
        with open('questoes_fáceis.json','w') as json_file:
            json.dump(lista_perguntas, json_file, indent = 4)
    elif nivel == 2:
        with open('questoes_medias.json','w') as json_file:
            json.dump(lista_perguntas, json_file, indent = 4)
    elif nivel == 3:
        with open('questoes_difíceis.json','w') as json_file:
            json.dump(lista_perguntas, json_file, indent = 4)
            
            
def atualizar_ranking(nome, pontos):
    # recebe: uma string indicando o nome do jogador e um inteiro indicando a sua pontuação.
    # faz: buscar a lista, adicionar a nova pontuação na lista, ordenar as pontuações, e enviar para a função salvar_ranking.
    # retorna: nada
    lista_ranking = carregar_ranking()
    novo_ranking = {"nome": nome, "pontos" : pontos}
    lista_ranking.append(novo_ranking)
    salvar_ranking(lista_ranking)


def salvar_ranking(lista_ranking):
    # recebe: uma lista de nomes e pontuações atualizadas.
    # faz: salvar a lista de nomes e potuanções no arquivo.
    # retorna: nada)
    lista_ranking = sorted(lista_ranking, key=lambda d: d['pontos'], reverse=True)
    with open('ranking.json', 'w') as json_file:
        json.dump(lista_ranking, json_file,indent = 4)
        
def visualizar_ranking(top_10 = False):
    # recebe: nada
    # faz: busca o ranking pela função carregar ranking e printa para o usuario 
    # retorna: nada
    lista_ranking = carregar_ranking()
    if top_10 == True:
        print("\nTop 10:")
        if len(lista_ranking) > 10:
            for i in range(0, 10):
                print(f'{i + 1} = {lista_ranking[i]["nome"]} : {lista_ranking[i]["pontos"]}')   
        else:
            for i in range(0, len(lista_ranking)):
                print(f'{i + 1} = {lista_ranking[i]["nome"]} : {lista_ranking[i]["pontos"]}')
    else:
        print("\nRanking:")
        for i in range(0, len(lista_ranking)):
            print(f'{i + 1} = {lista_ranking[i]["nome"]} : {lista_ranking[i]["pontos"]}')
            
def remover_pergunta():
    #recebe: um nivel e uma lista de perguntas
    #faz: remove a pergunta da lista de perguntas
    #retorna: nada
    nivel = int(input("Em qual nivel voce deseja remover (Ex: 1, 2 , 3): " ))
    lista_perguntas = carregar_perguntas(nivel)
    for i in range(0, len(lista_perguntas)):
        print(f'{i} = {lista_perguntas[i]["pergunta"]}')
    codigo_pergunta = int(input("Digite o numero da pergunta que deseja remover: "))
    lista_perguntas.pop(codigo_pergunta)
    salvar_perguntas(nivel, lista_perguntas)
    print("Removido com sucesso")
    
def buscar_pergunta():
    #recebe: um nivel e uma lista de perguntas
    #faz : busca uma lista de perguntas
    #retorna: a lista perguntas
    nivel = int(input("Em qual nivel voce deseja visualizar (Ex: 1, 2 , 3): " ))
    lista_perguntas = carregar_perguntas(nivel)
    for i in range(0, len(lista_perguntas)):
        print(f'{i} = {lista_perguntas[i]["pergunta"]}')
    codigo_pergunta = int(input("Digite o numero da pergunta que deseja visualizar: "))
    print(json.dumps(lista_perguntas[codigo_pergunta], indent = 4))
    
def alterar_pergunta():
    nivel = int(input("Em qual nivel voce deseja alterar (Ex: 1, 2 , 3): " ))
    lista_perguntas = carregar_perguntas(nivel)
    for i in range(0, len(lista_perguntas)):
        print(f'{i} = {lista_perguntas[i]["pergunta"]}')
    codigo_pergunta = int(input("Digite o numero da pergunta que deseja alterar: "))
    titulo = input("Digite o titulo da pergunta: ")
    alternativa_1 = input("Digite  a primeira alternativa: ")
    alternativa_2 = input("Digite a segunda alternativa: ")
    alternativa_3 = input("Digite a terceira alternativa: ")
    alternativa_verdadeira = input("qual a alternativa verdadeira: ").upper()
    if alternativa_verdadeira not in ['A','B','C']:
        print("Error: Alternativa não existente")
        return
    pergunta = {
        "pergunta": titulo,
        "alternativas": [
            {
                "titulo": alternativa_1,
                "verdadeiro": alternativa_verdadeira == "A"
            },
            {
                "titulo": alternativa_2,
                "verdadeiro": alternativa_verdadeira == "B"
            },
            {
                "titulo": alternativa_3,
                "verdadeiro": alternativa_verdadeira == "C"
            }
        ]
    } 
    lista_perguntas[codigo_pergunta] = pergunta
    salvar_perguntas(nivel, lista_perguntas)
    print("Atualizado com sucesso")
while True:
    menu = int(input("Bem vindo, escolha a opção que deseja:\n1 = Jogar Quiz\n2 = Visualizar\n3 = Adicionar Pergunta\n4 = Remover Pergunta\n5 - Buscar Pergunta\n6 = Alterar Pergunta\n7 = Sair "))
    if menu == 1:
        iniciar_jogo()
    elif menu == 2:
        visualizar_ranking()
        break 
    elif menu == 3:
        criar_pergunta()
        break 
    elif menu == 4:
        remover_pergunta()
    elif menu == 5:
        buscar_pergunta()
    elif menu == 6:
        alterar_pergunta()
    elif menu == 7:
        break
        
        
        
        