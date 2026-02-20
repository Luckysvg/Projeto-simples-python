frase = input('Digite uma frase:').strip().upper()
print('A letra A aparece {} vezes na frase'.format(frase.count('A')))
print('A letra A aparece pela primeira vez na posiçao {}'.format(frase.find('A')+1))
print('A letra A aparece pela ultima vez na posiçao {}'.format(frase.rfind('A')+1)) 