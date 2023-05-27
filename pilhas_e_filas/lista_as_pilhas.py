# Exemplo da utilização de listas como pilhas, tomando como valor inicial
# uma pilha de 7 livros a serem lidos. 

# Criamos um lista com essa extensão.

livros = 7
pilha = list(range(1, livros+1))

# Criamos um laço que se repita até que a sua paralização manual

while True:
    print(f"Livros na pilha: {len(pilha)}")
       
# E - Empilhar um novo livro
# D - Desimpilhar um livro
# S - Sair da execução

    ope = input("Digite D, E ou S: ").upper()
    print("=" * 30)
    
# Se a pilha for maior que 0, retiramos o primeiro livro da pilha

    if ope == 'D':
        if len(pilha) > 0:
            lido = pilha.pop(-1)
            print(f"Livro {lido} lido")
        else:
            print("Pilha vazia! Nenhum livro a ser lido!")

# Caso cheguem mais livros, adicionaremos 1 a variável "livros"
# Em seguida adicionamos o novo valor de "livros" a pilha de livros.
    
    elif ope == 'E':
        livros += 1
        pilha.append(livros)

# Caso quisermos encerrar o atendimento, iremos parar a execução 
# do programa com a instrução break
    
    elif ope == 'S':
        break

# Caso nenhuma das instruções corretas forem informadas,
# informaremos o usuário

    else:
        print("Operação inválida! Tente novamente inserir D, E ou S! ")