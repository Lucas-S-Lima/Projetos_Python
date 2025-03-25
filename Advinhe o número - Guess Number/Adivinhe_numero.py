import random  #importando a biblioteca random

#criando a função que irá gerar e armazenar o valor a ser adivinhado

def adivinhe(n):
# random.randint(x,y) gera valores aleatórios e inteiros entre os intervalos definidos
    numero_gerado = random.randint(1, n) 
   
    numero_inserido = 0

#Laço de repetição que irá imprimir a mensagem para o usuário de acordo com o palpite. Enquanto numero_inserido for diferente do numero_gerado aleatoriamente, o programa pedirá valores ao usuários e retornará as mensagens de orientação.

    while numero_inserido != numero_gerado:
        numero_inserido = int(input("Digite um número: "))
        if numero_inserido > numero_gerado:
            print("Você está perto, mas foi alto demais! Tente denovo")
        elif numero_inserido < numero_gerado:
            print("Você está perto, mas foi baixo demais! Tente denovo")  
        else:
            print("Parabéns! Bem na mosca! O número correto é {}".format(numero_gerado))     

adivinhe(50)
    
