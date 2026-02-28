salario_aumento = float(input('Qual seu salario?'))
if salario_aumento <= 1250:
    aumento = salario_aumento * 0.15
    print('O aumento do salario é de R${:.2f}'.format(aumento))
else:
    print('O aumento do salario é de R${:.2f}'.format(salario_aumento * 0.10))