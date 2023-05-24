valor_h = float(input("Digite o valor da hora de trabalho: "))
q_horas = float(input("Digite a quantidade de horas trabalhadas: "))
salario_b = (valor_h) * (q_horas) 
inss = (salario_b) * 0.08
sindicato = (salario_b) * 0.05
ir = (salario_b) * 0.11
descontos = (ir + sindicato + inss)
salario_l = (salario_b) - (descontos)

print(f"Salário Bruto é de {salario_b:.2f}")
print(f"O valor pago de INSS é de {inss:.2f}")
print(f"O valor pago de sindicato é de {sindicato:.2f}")
print(f"O Salário Líquido é de {salario_l:.2f}")