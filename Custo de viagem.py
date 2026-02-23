distancia = float(input('Qual a distancia da viagem em km?'))
if distancia <= 200:
    print('O custo da viagem é de R${:.2f}'.format(distancia * 0.50))
else:
    print('O custo da viagem é de R${:.2f}'.format(distancia * 0.45))