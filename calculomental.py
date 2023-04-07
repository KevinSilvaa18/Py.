import os
import random

def str():
    os.system('clear')
    dif = int(input('de 0 a:'))
    num0 = random.randint(0, dif)
    num1 = random.randint(0, dif)
    sinal = random.choice(['+', '-'])
    if sinal == '+':
        resp = num0+num1
    if sinal == '-':
        resp = num0-num1
    if sinal == '-' and num0<num1:
        num0 = num0+num1
        resp = num0-num1

    estrutura = (f"{num0}{sinal}{num1}")
    pergunta = int(input(f"{estrutura}:"))
    if pergunta == resp:
        i = 0
        while i == 0:
            num1 = random.randint(0, dif)
            sinal = random.choice(['+', '-'])
            if sinal == '+':
                total = resp+num1
            if sinal == '-':
                total = resp-num1
            if sinal == '-' and num1>resp:
                num1 = random.randint(0, resp)
                total = resp-num1
            
            estrutura = (f"{resp}{sinal}{num1}")
            pergunta = int(input(f"{estrutura}:"))
            if pergunta != total:
                print ('errou')
                print ("a resposta seria", total)
                tryagain = input('tentar novamente?s/n:')
                if tryagain == 's':
                    str()
                else:
                    quit()
            resp = total
            os.system('clear')
    
    else:
        print('errado')
        print ("a resposta seria", resp)
        tryagain = input('tentar novamente?s/n:')
        if tryagain == 's':
            str()
        else:
            quit()
str()