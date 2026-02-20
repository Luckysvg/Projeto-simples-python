cidade = input('Em que cidade voce nasceu?')
if cidade.find('Santo') >= 0:
    print('Voce nasceu em uma cidade que tem Santo no nome {}'.format(cidade.find('Santo')))
else:
    print('Voce nasceu em uma cidade que nao tem Santo no nome {}'.format(cidade.find('Santo')))
    