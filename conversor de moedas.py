real = float(input("Quanto de dinheiro voce tem na sua carteira? R$"))
dolar = real / 3.27
print("Com R${:.2f} voce pode comprar UR${:.2f}".format(real, dolar))