print('Analisador de triangulos')

lado1 = float(input('Digite o primeiro lado do triangulo:'))
lado2 = float(input('Digite o segundo lado do triangulo:'))
lado3 = float(input('Digite o terceiro lado do triangulo:'))
if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    print('Os lados formam um triangulo')
else:
    print('Os lados não formam um triangulo')