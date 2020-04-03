import random
Fichas=100
while Fichas>0:
    print("Você tem",Fichas,"fichas")
    p1=input("Quer apostar?(s/n)")
    if p1=='n':
        print("Você saiu do jogo")
        break
    elif p1=='s':
        print("Você esta na fase 'Come out'")
        p2=input("Qual aposta você gostaria de fazer? (Você pode escolher entre 'Pass Line Bet', 'Field', 'Any Craps', 'Twelve')")
        if p2=="Pass Line Bet":
            aposta=int(input("Quanto você quer apostar?"))
            dado1=random.randint(1,6)
            dado2=random.randint(1,6)
            soma1=dado1+dado2
            print('essa foi a soma dos dados',soma1)
            if soma1==7 or soma1==11:
                print("Você venceu!")
                Fichas+=aposta
            elif soma1==2 or soma1==3 or soma1==12:
                print("Você perdeu!")
                Fichas-=aposta
            else:
                print("Você está na fase 'Point'")
                p3=input("Qual aposta você quer fazer? (Você pode escolher entre 'Field', 'Any Craps', 'Twelve','continuar no Pass Line Bet')")
                if p3=="Field":
                    dado1=random.randint(1,6)
                    dado2=random.randint(1,6)
                    soma2=dado1+dado2
                    print('essa foi a soma dos dados',soma2)
                    if soma2==5 or soma2==6 or soma2==7 or soma2==8:
                        print("Você perdeu!")
                        Fichas-=aposta
                    elif soma2==3 or soma2==4 or soma2==9 or soma2==10 or soma2==11:
                        print("Você venceu!")
                        Fichas+=aposta
                    elif soma2==2:
                        print("Você venceu!")
                        Fichas+=2*aposta
                    else:
                        Fichas+=3*aposta       
                if p3=="continuar no Pass Line Bet":
                    dado1=random.randint(1,6)
                    dado2=random.randint(1,6)
                    soma3=dado1+dado2
                    print('essa foi a soma dos dados',soma3)
                    while soma3!=soma1 and soma3!=7:
                        print("Rodando novamente")
                        dado1=random.randint(1,6)
                        dado2=random.randint(1,6)
                        soma3=dado1+dado2
                        print('essa foi a soma dos dados',soma3)
                    if soma3==soma1:
                        print("Você venceu!")
                        Fichas+=aposta
                    elif soma3==7:
                        print("Você perdeu!")
                        Fichas-=aposta


                if p3=="Any Craps":
                    dado1=random.randint(1,6)
                    dado2=random.randint(1,6)
                    soma4=dado1+dado2
                    print('essa foi a soma dos dados',soma4)
                    if soma4==2 or soma4==3 or soma4==12:
                        print("Você venceu!")
                        Fichas+=7*aposta
                    else:
                        print("Você perdeu!")
                        Fichas-=aposta
                elif p3=="Twelve":
                    dado1=random.randint(1,6)
                    dado2=random.randint(1,6)
                    soma5=dado1+dado2
                    print('essa foi a soma dos dados',soma5)
                    if soma5== 12:
                        print("Você venceu!")
                        Fichas+=30*aposta
                    else:
                        print("Você perdeu!")
                        Fichas-=aposta
        elif p2=="Field":
            aposta=int(input("Quanto você quer apostar?"))
            dado1=random.randint(1,6)
            dado2=random.randint(1,6)
            soma6=dado1+dado2
            print('essa foi a soma dos dados',soma6)
            if soma6==5 or soma6==6 or soma6==7 or soma6==8:
                print("Você perdeu!")
                Fichas-=aposta
            elif soma6==3 or soma6==4 or soma6==9 or soma6==10 or soma6==11:
                print("Você venceu!")
                Fichas+=aposta
            elif soma6==2:
                print("Você venceu!")
                Fichas+=2*aposta
            else:
                Fichas+=3*aposta
        elif p2=="Any Craps":
            aposta=int(input("Quanto você quer apostar?"))
            dado1=random.randint(1,6)
            dado2=random.randint(1,6)
            soma7=dado1+dado2
            print('essa foi a soma dos dados',soma7)
            if soma7==2 or soma7==3 or soma7==12:
                 print("Você venceu!")
                 Fichas+=7*aposta
            else:
                print("Você perdeu!")
                Fichas-=aposta
        elif p2=="Twelve":
            aposta=int(input("Quanto você quer apostar?"))
            dado1=random.randint(1,6)
            dado2=random.randint(1,6)
            soma8=dado1+dado2
            print('essa foi a soma dos dados',soma8)
            if soma8== 12:
                print("Você venceu!")
                Fichas+=30*aposta
            else:
                print("Você perdeu!")
                Fichas-=aposta
