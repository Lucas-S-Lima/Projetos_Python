import requests 

# Criando uma inicialização do programa

print('*' * 18 + ' ' "Consulta - CEP" ' ' + '*' * 18)
print()

cep_informado = input("Insira o CEP: ")

while True:
    if len(cep_informado) > 8:
        print("O CEP possui mais de 8 caracteres, tente novamente")
        cep_informado = input("Insira o CEP: ")
    elif len(cep_informado) < 8:
        print("O CEP informado possui mais de 8 caracteres, tente novamente.")
        cep_informado = input("Insira o CEP: ")    
    else:
        break

r = requests.get(f"https://viacep.com.br/ws/{cep_informado}/json/")
info = r.json()

while True: 
    if 'erro' in info:
        print("CEP inexistente!")
        cep_informado = input("Insira o CEP: ")
    else:
        break

print()
print("=" * 16 + ' ' + "Resultados da busca" + ' ' + "=" * 16)
print()

print(f"Cep: {info['cep']}\nLogradouro: {info['logradouro']}\nBairro: {info['bairro']}\nCidade: {info['localidade']}\nUF: {info['uf']}")






