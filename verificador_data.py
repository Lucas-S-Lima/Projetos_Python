import sys

data = input('Insira uma data (dd/mm/aaaa): ')

dia = int(data[:2])
mes = int(data[3:5])
ano = int(data[6:10])

bissexto_algarismos = int(data[8:10]) # 2 ultimos algarismos para verificar se o ano é bissexto

bissexto = bissexto_algarismos % 4

lista_meses = [1,2,3,4,5,6,7,8,9,10,11,12]

# Verificando se é bissexto

if bissexto == 0:
    bissexto = True
else:
    bissexto = False

# Verificando se o ano é válido

if ano < 0:
    print('O ano inserido é inválido.')
    sys.exit()
else:
    pass

# Verificando se o mês é válido

if mes in lista_meses:
    pass
else:
    print('O mês inserido é inválido.')
    sys.exit()

# Verificando fevereiro 

if mes == 2 and (bissexto == True):

    if dia > 29:
        print('O dia informado é inválido.')
        sys.exit()
    else:
        pass

if mes == 2 and (bissexto == False):
   
    if dia > 28:
        print('O dia informado é inválido.')
        sys.exit()
    else: 
        pass

# Verificando se o dia é válido

if dia < 1 or dia > 31:
    print('O dia informado é inválida.')
    sys.exit()

else:
    pass

    print('A data informada é valida.')




    