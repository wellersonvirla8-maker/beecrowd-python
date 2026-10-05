numero_funcionario = int(input("Digite o valor do seu salario: "))
horas_trabalhadas = int(input("Quantas horas você trabalhou: "))
valor_por_hora = float(input("Digite o valor que você recebe por hora: "))

# Cálculo do salário
salario = horas_trabalhadas * valor_por_hora

# Exibição do resultado formatado
print(f"NUMBER = {numero_funcionario}")
print(f"SALARY = U$ {salario:.2f}")