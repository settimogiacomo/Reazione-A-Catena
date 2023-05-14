from Algoritmi import Algoritmi

if __name__ == '__main__':
    foo = Algoritmi()
    foo.caricaDizionario()
    foo.chiediParole()
    if foo.parola1 != '' and foo.parola2 != '':
        print('foo.calcolaPercorsi()')
        foo.calcolaPercorsi(foo.albero)
        foo.vediAlbero(foo.albero)
