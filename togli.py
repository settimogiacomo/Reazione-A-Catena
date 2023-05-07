parola1 = 'smembrerai'
parola2 = 'sembrerai'
diz = {}
list_trovate = []


def init():
    f = open('./Parole/parole_facili.txt')  # dentro ci va il path del file
    linee = f.readlines()  # legge tutte le linee del file e le carica in una lista di linee
    for l in linee:
        l = l.strip()
        diz[l] = len(l)


# print(diz)


def togli(parola):
    i_cancella = 0
    print(parola)
    for i in range(len(parola)):
        new_par = rimuovi(i_cancella, parola)
        print(new_par)
        if new_par in diz:
            list_trovate.append(new_par)
        i_cancella += 1


def rimuovi(i_spazio, parola):
    listpar = list(parola)
    listpar.pop(i_spazio)
    par = ''.join(listpar)
    return par


if __name__ == '__main__':
    init()
    togli(parola1)
    print(list_trovate)
