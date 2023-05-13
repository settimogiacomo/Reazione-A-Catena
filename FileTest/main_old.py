#import random, da cancellare??
alfabeto = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
list_par_len = []
list_par_anag = []
parola1 = 'firma'
parola2 = ''
diz = {}

def init():
    f = open('./Parole/parole_difficili.txt')  # dentro ci va il path del file
    linee = f.readlines()  # legge tutte le linee del file e le carica in una lista di linee
    for l in linee:
        l = l.strip()
        diz[l] = len(l)
    print(diz)


def controllo(parola):
    for par in sorted(diz):
        if diz[par] == len(parola) and par != parola:
            list_par_len.append(par)
    print(list_par_len)
    anagramma(parola)



def anagramma(parola):
    for par in list_par_len: #prendo ogni parola della lista
        trovato = False
        for lettera in par: #prendo ogni lettera di ogni parola della lista
            if lettera in parola:
                trovato = True
            else:
                break
        if trovato:
            list_par_anag.append(par)
    print(list_par_anag)






def trova_anagrammi_non_funziona(parola):
    if len(parola) == 1:
        return [parola]

    anagrammi = []
    for lettera in parola:
        restante = [x for x in parola if x != lettera]
        sottoparole = trova_anagrammi(restante)
        for sottoparola in sottoparole:
            par = ''.join(sottoparola)
            print(lettera+par)
            l = ''.join([lettera,par])
            anagrammi.append(lettera+par)

    return anagrammi

anagrammi = []
def trova_anagrammi(parola, prefisso=""):
    if len(parola) <= 1:
        par = prefisso + parola
        if par not in anagrammi and par in diz:
            anagrammi.append(prefisso + parola)
    else:
        for i in range(len(parola)):
            rimanenti = parola[:i] + parola[i+1:]
            trova_anagrammi(rimanenti, prefisso + parola[i])

if __name__ == '__main__':
    init()
    controllo(parola1)
    #parola = input("Inserisci una parola: ")
    parola = parola1
    trova_anagrammi(parola)
    print("Gli anagrammi di", parola, "sono:", anagrammi)
    print(len(anagrammi))
    if parola1 in anagrammi:
        print("Trovato anagramma")

    f = open("./Parole/trovate.txt", "a")
    for par in anagrammi:
        f.write(par + '\n')
    f.close()