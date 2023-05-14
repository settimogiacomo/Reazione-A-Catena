import random
from Metodo import Metodo
from Nodo import Nodo
class Algoritmi:

    def __init__(self):
        self.alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                    'u', 'v', 'w', 'x', 'y', 'z']
        self.parola1 = ''
        self.parola2 = ''
        self.diz = {}
        self.diz_trovate = {}
        self.albero : Nodo = None

    def caricaDizionario(self):
        f = open('./Parole/parole_difficili.txt')  # dentro ci va il path del file
        linee = f.readlines()  # legge tutte le linee del file e le carica in una lista di linee
        for l in linee:
            l = l.strip()
            self.diz[l] = len(l)

    def chiediParole(self):
        print("Scrivi le parole di cui vuoi conoscere il percorso:")
        self.parola1 = input()
        self.parola2 = input()
        trovate = False
        while not trovate:
            if self.parola1 not in self.diz:
                print(self.parola1, 'non esiste nel dizionario, riprova')
                self.parola1 = input()
            if self.parola2 not in self.diz:
                print(self.parola2, 'non esiste nel dizionario, riprova')
                self.parola2 = input()
            if self.parola1 in self.diz and self.parola2 in self.diz:
                trovate = True
        if trovate:
            print(self.parola1, self.parola2)
            self.albero = Nodo(self.parola1, Metodo.NESSUNO)

    def calcolaPercorsi(self, nodo : Nodo):
        if str(nodo) != '' and str(nodo) != self.parola2:
            self.trova_anagrammi(str(nodo))
            self.sostituisci(str(nodo))
            self.aggiungi(str(nodo))
            self.togli(str(nodo))
            #print(self.diz_trovate)
            for figlio in sorted(self.diz_trovate):
                p = Nodo(figlio,self.diz_trovate[figlio])
                nodo.add_figlio(p)
            self.diz_trovate = {}
            for nodoObj in nodo.figli:
                self.calcolaPercorsi(nodoObj)
        else:
            print('trovato percorso', self.parola2)


    def aggiungiTrovate(self):
        # trovare il nodo giusto
        for parola, metodo in self.diz_trovate:
            self.albero.add_figlio(parola, metodo)

    def trova_anagrammi(self,parola, prefisso=""):
        if len(parola) <= 1:
            par = prefisso + parola
            if par in self.diz and par not in self.diz_trovate:
                self.diz_trovate[prefisso + parola] = Metodo.ANAGRAMMA
            else:
                for i in range(len(parola)):
                    rimanenti = parola[:i] + parola[i + 1:]
                    self.trova_anagrammi(rimanenti, prefisso + parola[i])

    def sostituisci(self, parola):
        for i in range(len(parola)):
            for l in self.alfabeto:
                par = list(parola)
                par[i] = l
                par = ''.join(par)
                #print(par)

                if par in self.diz and par not in self.diz_trovate:
                    self.diz_trovate[par] = Metodo.SOSTITUISCI

    def aggiungi(self, parola):
        i_spazio = 1
        parola = ' ' + parola
        for i in range(len(parola)):
            for l in self.alfabeto:
                new_par = parola.replace(' ', l)
                # print(new_par)
                if new_par in self.diz and new_par not in self.diz_trovate:
                    self.diz_trovate[new_par] = Metodo.AGGIUNGI

            parola = self.trasla(i_spazio, parola)
            i_spazio += 1

    def trasla(self, i_spazio, parola):
        listpar = list(parola)
        listpar.remove(' ')
        listpar.insert(i_spazio, ' ')
        par = ''.join(listpar)
        return par

    def togli(self, parola):
        i_cancella = 0
        #print(parola)
        for i in range(len(parola)):
            new_par = self.rimuovi(i_cancella, parola)
            #print(new_par)
            if new_par in self.diz and new_par not in self.diz_trovate:
                self.diz_trovate[new_par] = Metodo.TOGLI
            i_cancella += 1

    def rimuovi(self, i_spazio, parola):
        listpar = list(parola)
        listpar.pop(i_spazio)
        par = ''.join(listpar)
        return par
