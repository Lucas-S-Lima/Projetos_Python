altura = float(input("Insira sua altura: "))
sexo = str(input("Insira seu sexo: "))
m_mulher = (62.1 * altura) - 44.7
m_homem = (72.7 * altura) - 58

if sexo == 'masculino':
  print(f"Seu peso ideal seria de {m_homem:.2f} kg")
else:
  print(f"Seu peso ideal seria de {m_mulher:.2f} kg") 