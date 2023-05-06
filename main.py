if __name__ == '__main__':
    diz = {}
    f = open('./Parole/parole.txt')  # dentro ci va il path del file
    linee = f.readlines()  # legge tutte le linee del file e le carica in una lista di linee
    for l in linee:
        l= l.strip()
        diz[l] = len(l)

    print(diz)

