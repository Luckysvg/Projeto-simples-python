import random
numero = random.randint(1, 100)
chute = int(input("Tente adivinhar o numero de 1 a 100"))
tentativas = 0

while True:
    chute = int(input("Digite seu chute: "))
    tentativas += 1
    if chute < numero:
        print("Muito baixo")

    elif chute > numero:
        print("Muito alto")

    else:
        print(f"Parabens, Voce acertou em {tentativas} tentativas")
        break
    




            

   

    
    
    
      
     

       







