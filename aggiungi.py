alfabeto = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
parola1 = 'sembrerai'
parola2 = 'smembrerai'
diz = {}
list_trovate = []

def init():
    f = open('./Parole/parole_facili.txt')  # dentro ci va il path del file
    linee = f.readlines()  # legge tutte le linee del file e le carica in una lista di linee
    for l in linee:
        l = l.strip()
        diz[l] = len(l)
    #print(diz)

def aggiungi(parola):
    i_spazio = 1
    parola = ' ' + parola
    for i in range(len(parola)):
        for l in alfabeto:
            new_par = parola.replace(' ', l)
            #print(new_par)
            if new_par in diz:
                list_trovate.append(new_par)

        parola = trasla(i_spazio, parola)
        i_spazio += 1

def trasla(i_spazio, parola):
    listpar = list(parola)
    listpar.remove(' ')
    listpar.insert(i_spazio, ' ')
    par = ''.join(listpar)
    return par



if __name__ == '__main__':
    init()
    aggiungi(parola1)
    print(list_trovate)

