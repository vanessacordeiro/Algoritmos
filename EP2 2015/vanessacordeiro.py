import urllib.request
import random
k = ""
alfabeto = "abcdefghijklmnopqrstuvxwyz"
letrasE = ["áàãâ","éèê", "íì", "óòõô", "úù", "ç"]
certas = ""
erradas = ""
letras = ""
forca = [
"""
 +-----+
 |     |
 O     |
/|\    |
/ \    |
       |
=========
""",
"""
 +-----+
 |     |
 O     |
/|\    |
/      |
       |
=========
""",
"""
 +-----+
 |     |
 O     |
/|\    |
       |
       |
=========
""",
"""
 +-----+
 |     |
 O     |
/|     |
       |
       |
=========
""",
"""
 +-----+
 |     |
 O     |
 |     |
       |
       |
=========
""",
"""
 +-----+
 |     |
 O     |
       |
       |
       |
=========
""",
"""
 +-----+
 |     |
       |
       |
       |
       |
=========
"""]
temp = urllib.request.urlopen("http://www.ime.usp.br/~pf/dicios/br")
data = temp.read().decode("iso8859").split()
palavra = []
lista= []

           
def sorteio():
    global k
    global sorteada
    for x in data:
        if len(x)>5:
           lista.append(x)
    for x in lista:
        x.lower()
    k = random.choice(lista)
    sorteada = list(k)
    print(sorteada)
    m = 0
    while m<len(k):
        palavra.append("_")
        m = m + 1

def desenho():
    global letras
    global palavra
    if len(erradas)==0:
        print (forca[0])
    elif len(erradas)==1:
        print (forca[1])
    elif len(erradas)==2:
        print(forca[2])
    elif len(erradas)==3:
        print (forca[3])
    elif len(erradas)==4:
        print (forca[4])
    elif len(erradas)==5:
        print (forca[5])
    elif len(erradas)==6:
        print (forca[6])
        print("MORREU!!!")
        a=again()
        if a==True:
            sorteio()
            desenho()
        else:
            exit()
    print(" ".join(palavra))
    print()
    w = win()
    if w==True:
        a = again()
        if a==True:
            sorteio()
            desenho()
        else:
            exit()
    else:
        chute(letras)

def chute(tentativas):
    global certas
    global erradas
    global sorteada
    global letras
    while True:
        y = str(input("Chute uma letra que ainda não tenha chutado: "))
        if y not in tentativas and y in alfabeto:
            l = y
            if y=="a":
                for x in letrasE[0]:
                    if x in k:
                        l = x
            elif y == "e":
                for x in letrasE[1]:
                    if x in k:
                        l = x
            elif y == "i":
                for x in letrasE[2]:
                    if x in k:
                        l = x
            elif y == "o":
                for x in letrasE[3]:
                    if x in k:
                        l = x
            elif y == "u":
                for x in letrasE[4]:
                    if x in k:
                        l = x
            elif y == "c":
                for x in letrasE[5]:
                    if x in k:
                        l = x
            z = 0
            if y in k: 
                m = 0
                while m<len(k):
                    try:
                        z  = sorteada[m:len(k)].index(y)+m
                    except ValueError:
                        break
                    
                    palavra[z] = y
                    certas = certas + y
                    m = z + 1
                if l!= y:
                    m = 0
                    while m<len(k):
                        try:
                            z  = sorteada[m:len(k)].index(l)+m
                        except ValueError:
                            break
                        
                        palavra[z] = l
                        certas = certas + l
                        m = z + 1
            else:
                erradas = erradas + y
            letras = letras + y
            desenho()
            return tentativas
        
def win():
    global k
    global certas
    s = list(k)
    s.sort()
    c = list(certas)
    c.sort()
    if s == c:
        print("VOCÊ VENCEU!!!")
        return True
    else:
        return False
    
def again():
    global certas
    global erradas
    global letras
    global palavra
    global lista
    jogar = str(input ("Deseja jogar denovo (S/N)? "))    
    if jogar == "S" or jogar == "s":
        certas = ""
        erradas = ""
        letras = ""
        palavra.clear()
        lista.clear()
        return True
    elif jogar == "N" or jogar =="n":
        return False
    
sorteio()
desenho()
