m_peixe = float(input("Digite a massa de peixes: "))
excesso = (m_peixe - 50) 
multa = excesso * 4


if m_peixe <= 50:
  print("A quantidade pescada está dentro do regulamento. Não há multa.")
else:
  print("A multa a ser paga é de R$ %.2f" % multa)