
def apresenteSe ():
    print('+-------------------------------------------------------------+')
    print('|                                                             |')
    print('| AGENDA PESSOAL DE ANIVERSÁRIOS E FORMAS DE CONTATAR PESSOAS |')
    print('|                                                             |')
    print('| Discentes:Enzzo                                             |')
    print('|                                                             |')
    print('|                                                             |')
    print('|                                                             |')
    print('+-------------------------------------------------------------+')
    
    

def umTexto (solicitacao, mensagem, valido):
    digitouDireito=False
    while not digitouDireito:
        txt=input(solicitacao)

        if txt not in valido:
            print(mensagem,'- Favor redigitar...')
        else:
            digitouDireito=True

    return txt

def opcaoEscolhida (mnu):
    print()

    opcoesValidas=[]
    posicao=0
    while posicao<len(mnu):
        print (posicao+1,') ',mnu[posicao],sep='')
        opcoesValidas.append(str(posicao+1))
        posicao+=1

    print()
    return umTexto('Qual é a sua opção? ', 'Opção inválida', opcoesValidas)


def ondeEsta (nom,agd):
    inicio=0
    final =len(agd)-1
    
    while inicio<=final:
        meio=(inicio+final)//2
        
        if nom.upper()==agd[meio][0].upper():
            return [True,meio]
        elif nom.upper()<agd[meio][0].upper():
            final=meio-1
        else: # nom.upper()>agd[meio][0].upper()
            inicio=meio+1
            
    return [False,inicio]

def cadastrar (agd):
    digitouDireito=False
    while not digitouDireito:
        nome=verificarNome('\nNome.......: ')

        resposta=ondeEsta(nome,agd)
        achou   = resposta[0]
        posicao = resposta[1]

        if achou:
            print ('Pessoa já existente - Favor redigitar...')
        else:
            digitouDireito=True
            
    aniversario = verificarAniversario('Aniversário: ')
    endereco   =verificarEndereco('Endereço...: ')
    telefone   =verificarNumero('Telefone...: ', 10)
    celular    =verificarNumero('Celular....: ', 11)
    email      =verificarEmail('e-mail.....: ')
    
    contato=[nome,aniversario,endereco,telefone,celular,email]
    
    agd.insert(posicao,contato)
    print('Cadastro realizado com sucesso!')

def procurar (agd):
    print("\nProcurando contato...")

    while True:
        nome = verificarNome("Digite o nome do contato: ")

        resposta = ondeEsta(nome, agd)
        achou = resposta[0]
        posicao = resposta[1]

        if achou:
            print("\nDados do contato:")
            print("Nome.......:", agd[posicao][0])
            print("Aniversário:", agd[posicao][1])
            print("Endereço...:", agd[posicao][2])
            print("Telefone...:", agd[posicao][3])
            print("Celular....:", agd[posicao][4])
            print("E-mail.....:", agd[posicao][5])
            break  # Sai do loop, pois encontrou o contato
        else:
            print("Nome não encontrado. Tente novamente.")


def atualizar (agd):
    digitouDireito = False
    while not digitouDireito:
        nome = verificarNome("Nome da pessoa para atualizar: ")

        resposta = ondeEsta(nome, agd)
        achou = resposta[0]
        posicao = resposta[1]

        if not achou:
            print("Pessoa não encontrada - Favor redigitar...")
        else:
            digitouDireito = True

            menu_atualizacao = ["Aniversário", "Endereço", "Telefone", "Celular", "E-mail", "Finalizar atualizações"]

    while True:
        opcao = int(opcaoEscolhida(menu_atualizacao))

        if opcao == 1:
            agd[posicao][1] = verificarAniversario("Novo aniversário: ")
        elif opcao == 2:
            agd[posicao][2] = verificarEndereco("Novo endereço: ")
        elif opcao == 3:
            agd[posicao][3] = verificarNumero("Novo telefone: ", 10)
        elif opcao == 4:
            agd[posicao][4] = verificarNumero("Novo celular: ", 11)
        elif opcao == 5:
            agd[posicao][5] = verificarEmail("Novo e-mail: ", "@gmail.com")
        else:
            print("Atualizações finalizadas!")
            break

def listar (agd):
    if len(agd)==0:
        print('Ainda não há contatos cadastrados')
    else:
        print('\n Lista de contatos')
        print()
        posicao=0
        while posicao < len(agd):
            print(agd[posicao][0])
            print(agd[posicao][1])
            print(agd[posicao][2])
            print(agd[posicao][3])
            print(agd[posicao][4])
            print(agd[posicao][5])
            print()
            posicao+=1
   
def excluir (agd):
    print()
    
    digitouDireito=False
    while not digitouDireito:
        nome=verificarNome('Nome.......: ')
        
        resposta=ondeEsta(nome,agd)
        achou   = resposta[0]
        posicao = resposta[1]
        
        if not achou:
            print ('Pessoa inexistente - Favor redigitar...')
        else:
            digitouDireito=True
    
    print('Aniversario:',agd[posicao][1])
    print('Endereco...:',agd[posicao][2])
    print('Telefone...:',agd[posicao][3])
    print('Celular....:',agd[posicao][4])
    print('e-mail.....:',agd[posicao][5])

    resposta=umTexto('Deseja realmente excluir? ','Você deve digitar S ou N',['s','S','n','N'])
    
    if resposta in ['s','S']:
        del agd[posicao]
        print('Remoção realizada com sucesso!')
    else:
        print('Remoção não realizada!')

def verificarNumero(mensagem, qtdDigitosAceita):
    digitouDireito=False
    while not digitouDireito:
        try:
            numeroTelefone=int(input(mensagem))
            qtdDigitos= len(str(numeroTelefone))
            if qtdDigitos != qtdDigitosAceita:
                print('O número deve ter', qtdDigitosAceita,  'dígitos; tente novamente!')
            else:
                digitouDireito=True
        except ValueError:
            print('Você só deve inserir números; tente novamente!')
    return numeroTelefone

def verificarEmail (mensagem, obrigatorio=["@gmail.com", "@ymail.com", '@hotmail.com']):
    digitouDireito=False
    while not digitouDireito:
        email=input(mensagem)
        if obrigatorio[0] in email or obrigatorio[1] in email or obrigatorio[2] in email:
            digitouDireito=True
        else: 
            print('Você deve adicionar o final', obrigatorio)
    return email

def verificarEndereco(solicitacao):
    enderecoValido=False
    while not enderecoValido:
        endereco = input(solicitacao)
        if len(endereco)<2:
            print('Endereço inválido; tente novamente!')
        else:
            enderecoValido=True
    return endereco

def verificarNome(solicitacao, invalido=['0','1','2','3','4','5','6','7','8','9','*','?', '/', ':', '+','-','!','@','#','$','%']):
    digitouDireito = False  
    while not digitouDireito:
        nome = input(solicitacao)  
        if any(caractere in invalido for caractere in nome):
            print("O nome só deve ter letras! Tente novamente.")
        elif len(nome) <=1:
            print('O nome deve conter, no mínimo, duas letras; tente novamente!')
        else:
            digitouDireito = True  
            return nome

def verificarAniversario(solicitacao):
    aniversario_valido = False
    while not aniversario_valido:
        aniversario = input("Aniversário (DD/MM/AAAA): ")
        partes = aniversario.split("/")
    
        if len(partes) == 3 and len(partes[0]) == 2 and len(partes[1])==2 and len(partes[2])==4:
                dia = int(partes[0])
                mes = int(partes[1])
                ano = int(partes[2])
                
                if dia == 29 and mes == 2 and ano % 4 == 0 and ano<=2025: 
                    aniversario_valido=True
                elif mes in [4, 6, 9, 11] and 1<= dia <=30 and ano<=2025:
                    aniversario_valido=True
                elif mes in [1,3,5,7,8,10,12] and 1<= dia <=31 and ano<=2025:
                    aniversario_valido=True
                elif mes ==2 and 1<= dia <=28 and ano<=2025:
                    aniversario_valido=True
                
                
        if aniversario_valido:
            return aniversario
        else:
            print('Data inválida; tente novamente!')


apresenteSe()

agenda=[]

menu=['Cadastrar Contato',\
      'Procurar Contato',\
      'Atualizar Contato',\
      'Listar Contatos',\
      'Excluir Contato',\
      'Sair do Programa']

deseja_terminar_o_programa=False
while not deseja_terminar_o_programa:
    opcao = int(opcaoEscolhida(menu))

    if opcao==1:
        cadastrar(agenda)
    elif opcao==2:
        procurar(agenda)
    elif opcao==3:
        atualizar(agenda)
    elif opcao==4:
        listar(agenda)
    elif opcao==5:
        excluir(agenda)
    else: # opcao==6
        deseja_terminar_o_programa=True
        
print('PROGRAMA ENCERRADO COM SUCESSO!')
