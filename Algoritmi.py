import random
from Metodo import Metodo
from Nodo import Nodo
class Algoritmi:

    def __init__(self):
        self.anagrammi = []
        self.alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                    'u', 'v', 'w', 'x', 'y', 'z']
        self.parola1 = 'firma'
        self.parola2 = 'smembrerai'
        self.diz = {}
        self.list_trovate = []

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
        print(self.parola1, self.parola2)

    def trova_anagrammi(self,parola, prefisso=""):
        if len(parola) <= 1:
            par = prefisso + parola
            if par in self.diz and par not in self.list_trovate:
                self.list_trovate.append(prefisso + parola)
            else:
                for i in range(len(parola)):
                    rimanenti = parola[:i] + parola[i + 1:]
                    self.trova_anagrammi(rimanenti, prefisso + parola[i])

    def sostituisci(self,parola):
        for i in range(len(parola)):
            for l in self.alfabeto:
                par = list(parola)
                par[i] = l
                par = ''.join(par)
                print(par)

                if par in self.diz and par not in self.list_trovate:
                    self.list_trovate.append(par)

    def aggiungi(self,parola):
        i_spazio = 1
        parola = ' ' + parola
        for i in range(len(parola)):
            for l in self.alfabeto:
                new_par = parola.replace(' ', l)
                # print(new_par)
                if new_par in self.diz and new_par not in self.list_trovate:
                    self.list_trovate.append(new_par)

            parola = self.trasla(i_spazio, parola)
            i_spazio += 1

    def trasla(i_spazio, parola):
        listpar = list(parola)
        listpar.remove(' ')
        listpar.insert(i_spazio, ' ')
        par = ''.join(listpar)
        return par

    def togli(self,parola):
        i_cancella = 0
        print(parola)
        for i in range(len(parola)):
            new_par = self.rimuovi(i_cancella, parola)
            print(new_par)
            if new_par in self.diz and new_par not in self.list_trovate:
                self.list_trovate.append(new_par)
            i_cancella += 1

    def rimuovi(i_spazio, parola):
        listpar = list(parola)
        listpar.pop(i_spazio)
        par = ''.join(listpar)
        return par
