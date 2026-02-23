velocidade = str(input('Qual a velocidade do carro?'))
if int(velocidade) > 80:
    print('Voce foi multado por excesso de velocidade!')
    multa = int(velocidade) - 80
    print('Voce deve pagar uma multa de R${:.2f}'.format(multa * 7))
else:
    print('Voce esta dentro do limite de velocidade! Continue assim!')