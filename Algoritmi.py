from Metodo import Metodo
from Nodo import Nodo
MAX_LIVELLO = 4

class Algoritmi:

    def __init__(self):
        self.alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                    'u', 'v', 'w', 'x', 'y', 'z']
        self.parola1 = ''
        self.parola2 = ''
        self.diz = {}
        self.diz_trovate = {}
        self.albero: Nodo = None
        self.conta = 0
        self.diz_livelli = {}

    def caricaDizionario(self):
        f = open('./Parole/parole_difficili.txt')  # dentro ci va il path del file
        linee = f.readlines()  # legge tutte le linee del file e le carica in una lista di linee
        for l in linee:
            l = l.strip()
            self.diz[l] = len(l)

    # solo per terminale
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
            self.albero = Nodo(self.parola1)

    def controllaParole(self):
        ritornoDizionario = ""
        if self.parola1 not in self.diz:
            ritornoDizionario = f"{self.parola1} non è nel dizionario"
        if self.parola2 not in self.diz:
            ritornoDizionario += " e \n" if ritornoDizionario != "" else ""
            ritornoDizionario += f"{self.parola2} non è nel dizionario"
        if ritornoDizionario != "":
            return ritornoDizionario
        if self.parola1 == "" or self.parola2 == "":
            return "Completa i campi mancanti"
        if self.parola1 in self.diz and self.parola2 in self.diz:
            return ""



    def calcolaPercorsi(self, node: Nodo):
        trovata_at_livello = []
        coda = [[node, 0]]
        while coda:
            for i in range(len(coda)):
                nodo, livello = coda.pop(0)
                #print('nodo:',str(nodo))
                if str(nodo) != self.parola2:
                    self.trovaAnagrammi(str(nodo))
                    self.sostituisci(str(nodo))
                    self.aggiungi(str(nodo))
                    self.togli(str(nodo))
                    for figlio in self.diz_trovate:
                        p = Nodo(figlio, self.diz_trovate[figlio])
                        nodo.add_figlio(p)
                    self.diz_trovate = {}
                    if livello < MAX_LIVELLO:
                        for nodoObj in nodo.figli:
                            if str(nodoObj) == self.parola2:
                                trovata_at_livello.append((nodoObj, livello))  # trovata parola a x livello
                            coda.append((nodoObj, livello + 1))
                    else:
                        break
                else:
                    break
            else:
                continue
            break
        print('trovata at livello: ',trovata_at_livello)

    def printAlbero(self, nodo: Nodo, indentazione='eroe -> '):
        if nodo:
            print(indentazione, nodo, nodo.algoritmo)
            for elem in nodo.figli:
                self.printAlbero(elem, indentazione + ' ' + str(elem) + ' -> ')

    def aggiungiTrovate(self):
        # trovare il nodo giusto
        for parola, metodo in self.diz_trovate:
            self.albero.add_figlio(parola, metodo)

# TRASFORMAZIONI PAROLE
    def trovaAnagrammi(self, parola, prefisso=""):
        if len(parola) <= 1:
            new_par = prefisso + parola
            if new_par in self.diz and new_par not in self.diz_trovate and new_par != parola and new_par != self.parola1:
                self.diz_trovate[new_par] = Metodo.ANAGRAMMA
        else:
            for i in range(len(parola)):
                rimanenti = parola[:i] + parola[i + 1:]
                self.trovaAnagrammi(rimanenti, prefisso + parola[i])

    def sostituisci(self, parola):
        for i in range(len(parola)):
            for l in self.alfabeto:
                new_par = list(parola)
                new_par[i] = l
                new_par = ''.join(new_par)
                #print(new_par)

                if new_par in self.diz and new_par not in self.diz_trovate and new_par != parola and new_par != self.parola1:
                    self.diz_trovate[new_par] = Metodo.SOSTITUISCI

    def aggiungi(self, parola):
        i_spazio = 1
        parola = ' ' + parola
        for i in range(len(parola)):
            for l in self.alfabeto:
                new_par = parola.replace(' ', l)
                # print(new_par)
                if new_par in self.diz and new_par not in self.diz_trovate and new_par != parola and new_par != self.parola1:
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
            if new_par in self.diz and new_par not in self.diz_trovate and new_par != parola and new_par != self.parola1:
                self.diz_trovate[new_par] = Metodo.TOGLI
            i_cancella += 1

    def rimuovi(self, i_spazio, parola):
        listpar = list(parola)
        listpar.pop(i_spazio)
        par = ''.join(listpar)
        return par
