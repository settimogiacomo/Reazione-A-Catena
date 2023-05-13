from typing import List, Any

alfabeto = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
parola1 = 'firma'
parola2 = 'servizi'
diz = {}
list_trovate = []

def init():
    f = open('../Parole/parole_difficili.txt')  # dentro ci va il path del file
    linee = f.readlines()  # legge tutte le linee del file e le carica in una lista di linee
    for l in linee:
        l = l.strip()
        diz[l] = len(l)
    #print(diz)

def sostituisci(parola):
    for i in range(len(parola)):
        for l in alfabeto:
            par = list(parola)
            par[i] = l
            par = ''.join(par)
            print(par)

            if par in diz and par not in list_trovate:
                list_trovate.append(par)





if __name__ == '__main__':
    init()
    sostituisci(parola1)
    print(list_trovate)
    f = open("../Parole/trovate.txt", "a")
    for par in list_trovate:
        f.write(par + '\n')
    f.close()



