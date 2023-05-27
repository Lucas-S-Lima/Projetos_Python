# Exemplo da utilização de listas como filas, tomando como valor inicial
# uma fila de 10 pessoas a serem atendidas. 

# Criamos um lista com essa extensão.

ultimo = 10
fila = list(range(1, ultimo+1))

# Criamos um laço que se repita até que a sua paralização manual

while True:
    print(f"Pessoas na fila: {len(fila)}")
       
# F - Adicionar um cliente na fila
# A - Realizar o atendimento
# S - Sair da fila

    ope = input("Digite A, S ou F: ").upper()
    print("=" * 30)
    
# Se a fila for maior que 0, atenderemos o primeiro cliente
# e em seguida o tiraremos da fila, e por fim exibimos qual 
# cliente foi atendido

    if ope == 'A':
        if len(fila) > 0:
            atendido = fila.pop(0)
            print(f"Cliente {atendido} atendido")
        else:
            print("Fila vazia! Ninguém a ser atendido!")

# Caso cheguem mais clientes, adicionaremos 1 a variável "ultimo"
# Em seguida adicionamos o novo valor de "ultimo" a fila.
    
    elif ope == 'F':
        ultimo += 1
        fila.append(ultimo)

# Caso quisermos encerrar o atendimento, iremos parar a execução 
# do programa com a instrução break
    
    elif ope == 'S':
        break

# Caso nenhuma das instruções corretas forem informadas,
# informaremos o usuário

    else:
        print("Operação inválida! Tente novamente inserir A, S ou F! ")