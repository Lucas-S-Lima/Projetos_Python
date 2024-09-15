import os

lista = []

while True:

    entrada = input('\t[i]- inserir\n\t[l] - listar \n\t[a] - apagar \n'
                    '\nInsira um opção: ')
    
    if entrada not in ('i', 'a', 'l'):
        print('O valor informado é inválido. Tente novamente.')
    
    
    if entrada == 'i':
        os.system('cls')
        
        item = input('Insira o item da lista: ')
        lista.append(item)
        os.system('cls')
        
    elif entrada == 'a':
        os.system('cls')
        
        if len(lista) == 0:
            print('Ainda não há nenhum item na lista.')
        
        else:
            try: 
                excluido = int(input('Insira o índice do item que será excluído: '))
                del lista[excluido]
                print('Item excluído da lista.')

            except ValueError or IndexError:
                print('Verifique se o índice informado existe na lista'
                       'e/ou se o valor inserido se foi um número.')

    elif entrada == 'l':
        os.system('cls')

        if len(lista) == 0:
            print('A lista ainda não possui nenhum item.')

        else:
            os.system('cls')
            for i, valor in enumerate(lista):
                print(i, valor)