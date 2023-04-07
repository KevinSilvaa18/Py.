import os
keyPass = 1203
def start():
    arqoupal = input ("1-arquivos 2-palavras:")
    if arqoupal == '1':
        def ENCDESCARQUIVOS():
            escolha = input("1-encryptar 2-descryptar:")
            if escolha == '1':
                os.system("dir -p")
                nomeArq = input("nome do arquivo:")
                with open(nomeArq, 'r') as arquivo:
                    conteudo = arquivo.read()
                    mapa_caracteres = {
                    
                        "@":  "1",
                        "#":  "2", 
                        "$":  "3",
                        "%":  "4",
                        "¨":  "5",
                        "&":  "6",
                        "*":  "7",
                        "(":  "8",
                        ")":  "9",
                        "/": " ", 
                        "0": "a",
                        "1": "b",
                        "2": "c",
                        "3": "d",
                        "4": "e",
                        "5": "f",
                        "6": "g",
                        "7": "h",
                        "8": "i",
                        "9": "j",
                        "O0": "k",
                        "O1": "l",
                        "O2": "m",
                        "O3": "n",
                        "O4": "o",
                        "O5": "p",
                        "O6": "q",
                        "O7": "r",
                        "O8": "s",
                        "O9": "t",
                        "T0": "u",
                        "T1": "v",
                        "T2": "w",
                        "T3": "x",
                        "T4": "y",
                        "T5": "z",
                    }

                    # Solicita a entrada do usuário
                    palavra = conteudo

                    # Aplica o mapeamento de caracteres
                    for chave, valor in mapa_caracteres.items():
                        if chave.startswith("O"):
                            chave = chave.replace("O", "")
                            chave = int(chave)
                            chave = chave+keyPass
                            chave = (f"O{chave}")
                            chave = str(chave)
                        if chave.startswith("T"):
                            chave = chave.replace("T", "")
                            chave = int(chave)
                            chave = chave+keyPass
                            chave = (f"T{chave}")
                            chave = str(chave)
                        if chave.isdigit():
                            chave = int(chave)
                            chave = chave+keyPass
                            #chave = chave
                        chave = str(chave)
                        palavra = palavra.replace(valor, chave)
                        palavra = palavra.replace(" ", "X")
                    
                    # Imprime a palavra resultante
                    print(palavra)
                    save = input("salvar?s/n:")
                    if save == "s":
                        novoNome = input("digite um nome para salvar:")
                        with open(novoNome, "w") as arquivo:
                            arquivo.write(palavra)
                            #start()
                    else:
                        start()  
            if escolha == '2':
                os.system("dir -p")
                nomeArq = input("nome do arquivo:")
                with open(nomeArq, 'r') as arquivo:
                    conteudo = arquivo.read()
                    mapa_caracteres = {
                    "X": " ",
                    "/": " ", 
                    "0": "a",
                    "1": "b",
                    "2": "c",
                    "3": "d",
                    "4": "e",
                    "5": "f",
                    "6": "g",
                    "7": "h",
                    "8": "i",
                    "9": "j",
                    "Oa": "k",
                    "Ob": "l",
                    "Oc": "m",
                    "Od": "n",
                    "Oe": "o",
                    "Of": "p",
                    "Og": "q",
                    "Oh": "r",
                    "Oi": "s",
                    "Oj": "t",
                    "Ta": "u",
                    "Tb": "v",
                    "Tc": "w",
                    "Td": "x",
                    "Te": "y",
                    "Tf": "z",
                    "@":  "1",
                    "#":  "2", 
                    "$":  "3",
                    "%":  "4",
                    "¨":  "5",
                    "&":  "6",
                    "*":  "7",
                    "(":  "8",
                    ")":  "9",
                }

                # Solicita a entrada do usuário
                palavra = conteudo
                
                # Aplica o mapeamento de caracteres
                for chave, valor in mapa_caracteres.items():
                    if chave.isdigit():
                        chave = int(chave)
                        chave = chave+keyPass
                    chave = str(chave)
                    palavra = palavra.replace(chave, valor)

                print(palavra)
                save = input("salvar?s/n:")
                if save == "s":
                    novoNome = input("digite um nome para salvar:")
                    with open(novoNome, "w") as arquivo:
                        arquivo.write(palavra)
                        
                else:
                    start()
        ENCDESCARQUIVOS()

    if arqoupal == '2':
        def ENCDESCPALAVRAS():
            global keyPass
            escolha = input("1-encryptar 2-descryptar:")
            if escolha == '1':

                mapa_caracteres = {
                
                    "@":  "1",
                    "#":  "2", 
                    "$":  "3",
                    "%":  "4",
                    "¨":  "5",
                    "&":  "6",
                    "*":  "7",
                    "(":  "8",
                    ")":  "9",
                    "/": " ", 
                    "0": "a",
                    "1": "b",
                    "2": "c",
                    "3": "d",
                    "4": "e",
                    "5": "f",
                    "6": "g",
                    "7": "h",
                    "8": "i",
                    "9": "j",
                    "O0": "k",
                    "O1": "l",
                    "O2": "m",
                    "O3": "n",
                    "O4": "o",
                    "O5": "p",
                    "O6": "q",
                    "O7": "r",
                    "O8": "s",
                    "O9": "t",
                    "T0": "u",
                    "T1": "v",
                    "T2": "w",
                    "T3": "x",
                    "T4": "y",
                    "T5": "z",
                }

                # Solicita a entrada do usuário
                palavra = input("Digite a palavra: ")

                # Aplica o mapeamento de caracteres
                for chave, valor in mapa_caracteres.items():
                    if chave.startswith("O"):
                        chave = chave.replace("O", "")
                        chave = int(chave)
                        chave = chave+keyPass
                        chave = (f"O{chave}")
                        chave = str(chave)
                    if chave.startswith("T"):
                        chave = chave.replace("T", "")
                        chave = int(chave)
                        chave = chave+keyPass
                        chave = (f"T{chave}")
                        chave = str(chave)
                    if chave.isdigit():
                        chave = int(chave)
                        chave = chave+keyPass
                        #chave = chave
                    chave = str(chave)
                    palavra = palavra.replace(valor, chave)
                    palavra = palavra.replace(" ", "X")
                
                # Imprime a palavra resultante
                print(palavra)
                ENCDESCPALAVRAS()
            
            if escolha == '2':

                mapa_caracteres = {
                    "X": " ",
                    "/": " ", 
                    "0": "a",
                    "1": "b",
                    "2": "c",
                    "3": "d",
                    "4": "e",
                    "5": "f",
                    "6": "g",
                    "7": "h",
                    "8": "i",
                    "9": "j",
                    "Oa": "k",
                    "Ob": "l",
                    "Oc": "m",
                    "Od": "n",
                    "Oe": "o",
                    "Of": "p",
                    "Og": "q",
                    "Oh": "r",
                    "Oi": "s",
                    "Oj": "t",
                    "Ta": "u",
                    "Tb": "v",
                    "Tc": "w",
                    "Td": "x",
                    "Te": "y",
                    "Tf": "z",
                    "@":  "1",
                    "#":  "2", 
                    "$":  "3",
                    "%":  "4",
                    "¨":  "5",
                    "&":  "6",
                    "*":  "7",
                    "(":  "8",
                    ")":  "9",
                }

                # Solicita a entrada do usuário
                palavra = input("Digite a palavra: ")
                
                # Aplica o mapeamento de caracteres
                for chave, valor in mapa_caracteres.items():
                    if chave.isdigit():
                        chave = int(chave)
                        chave = chave+keyPass
                    chave = str(chave)
                    palavra = palavra.replace(chave, valor)

                # Imprime a palavra resultante
                print(palavra)
                ENCDESCPALAVRAS()
        ENCDESCPALAVRAS()
start()