#importando o arquivo txt
with open("vendasloja.txt", "r") as relatorio:
    valor_total_vendas = 0

#Armazenando o relatorio em uma variável
    relatorio_analise = relatorio.read()

#Criando uma lista com relatorio
    lista = relatorio_analise.split('\n')

#Retirando o primeiro item da lista
    lista = lista[1:]

#Encontrando a posição do ; com a estrutura for
    for item in lista:
        posição_caracter = item.find(";")

#Soma dos valores das vendas
        valor_soma = (item[posição_caracter + 1:])

#Não podemos esquecer que valor_soma é uma string até o momento        
        valor_soma = float(item[posição_caracter + 1:])

#Estabelecendo a soma do valor_soma
        valor_total_vendas += valor_soma

print(f'O valor total de vendas é de: R$ {valor_total_vendas:.2f}')
        
       
        
    