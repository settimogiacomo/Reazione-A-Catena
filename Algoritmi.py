from Metodo import Metodo
from Nodo import Nodo
MAX_LIVELLO = 9

class Algoritmi:

    def __init__(self):
        self.alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                    'u', 'v', 'w', 'x', 'y', 'z']
        self.parola1 = ''
        self.parola2 = ''
        self.diz = {}  # tutte le parole
        self.diz_ParMet_trovate = {}  # parole&metodo trovate associate ad una parola
        self.albero: Nodo = None
        self.par2_at_livello = []  # parola 2 si trova al livello numero X
        self.list_per_trov = []  # lista di X percorsi completi con punteggi

    def caricaDizionario(self):
        f = open('./Parole/parole_difficili.txt')  # dentro ci va il path del file
        linee = f.readlines()  # legge tutte le linee del file e le carica in una lista di linee
        for l in linee:
            l = l.strip()
            self.diz[l] = len(l)

# TRASFORMAZIONI PAROLE
    def sostituisci(self, parola):
        for i in range(len(parola)):
            for l in self.alfabeto:
                if l != parola[i]:
                    new_par = list(parola)
                    new_par[i] = l
                    new_par = ''.join(new_par)
                    # print(new_par)

                    if new_par in self.diz and new_par not in self.diz_ParMet_trovate and new_par != parola and new_par != self.parola1:
                        self.diz_ParMet_trovate[new_par] = Metodo.SOSTITUISCI

    def aggiungi(self, parola):
        i_spazio = 1
        parola = ' ' + parola
        for i in range(len(parola)):
            for l in self.alfabeto:
                new_par = parola.replace(' ', l)
                # print(new_par)
                if new_par in self.diz and new_par not in self.diz_ParMet_trovate and new_par != parola and new_par != self.parola1:
                    self.diz_ParMet_trovate[new_par] = Metodo.AGGIUNGI

            parola = self.trasla(i_spazio, parola)
            i_spazio += 1

    def trasla(self, i_spazio, parola):  # aggiungi
        listpar = list(parola)
        listpar.remove(' ')
        listpar.insert(i_spazio, ' ')
        par = ''.join(listpar)
        return par

    def togli(self, parola):
        i_cancella = 0
        # print(parola)
        for i in range(len(parola)):
            new_par = self.rimuovi(i_cancella, parola)
            # print(new_par)
            if new_par in self.diz and new_par not in self.diz_ParMet_trovate and new_par != parola and new_par != self.parola1:
                self.diz_ParMet_trovate[new_par] = Metodo.TOGLI
            i_cancella += 1

    def rimuovi(self, i_spazio, parola):  # togli
        listpar = list(parola)
        listpar.pop(i_spazio)
        par = ''.join(listpar)
        return par

    def anagramma(self, parola, prefisso=""):
        if len(parola) <= 1:
            new_par = prefisso + parola
            if new_par in self.diz and new_par not in self.diz_ParMet_trovate and new_par != self.parola1:
                self.diz_ParMet_trovate[new_par] = Metodo.ANAGRAMMA
        else:
            for i in range(len(parola)):
                rimanenti = parola[:i] + parola[i + 1:]
                self.anagramma(rimanenti, prefisso + parola[i])

# RICHIESTA PAROLE

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


    def controllaParole(self): # feedback visualizzato nella finestra
        ritornoDizionario = ""
        if self.parola1 not in self.diz:
            ritornoDizionario = f"{self.parola1} non è nel dizionario"
        if self.parola2 not in self.diz:
            ritornoDizionario += " e \n" if ritornoDizionario != "" else ""
            ritornoDizionario += f"{self.parola2} non è nel dizionario"
        if self.parola1 == "" or self.parola2 == "":
            ritornoDizionario = "Completa i campi mancanti"
        if ritornoDizionario != "":
            return ritornoDizionario
        if self.parola1 in self.diz and self.parola2 in self.diz:
            return ""


    def calcolaPercorsi(self, node: Nodo):
        self.par2_at_livello = [] # (parola & livello)
        coda = [[node, 0]]
        while coda:
            for i in range(len(coda)):
                nodo, livello = coda.pop(0)
                #print('nodo:',str(nodo))
                if str(nodo) != self.parola2:
                    self.anagramma(str(nodo))
                    self.sostituisci(str(nodo))
                    self.aggiungi(str(nodo))
                    self.togli(str(nodo))
                    if str(nodo) in self.diz_ParMet_trovate: # controllo in più
                        self.diz_ParMet_trovate.pop(str(nodo)) # per togliere i doppioni di anagramma
                    for figlio in self.diz_ParMet_trovate: # figlio è un nodo
                        if str(figlio) not in nodo.genitori: # per non avere ripetizioni di parole nel percorso
                            p = Nodo(figlio, self.diz_ParMet_trovate[figlio])
                            p.genitori = nodo.genitori + [nodo]
                            #print(str(figlio)+'-'+str(nodo.genitori)+'-'+str(nodo)+'-'+str(p.algoritmo)+' -> questo nodo ' + str(p) + ' ha come genitori: ' + str(p.genitori))
                            nodo.add_figlio(p)
                    self.diz_ParMet_trovate = {}
                    if livello < MAX_LIVELLO:
                        for nodoObj in nodo.figli:
                            if str(nodoObj) == self.parola2:
                                self.par2_at_livello.append((nodoObj, livello))  # trovata parola a x livello
                            coda.append((nodoObj, livello + 1))
                    else:
                        break
                else:
                    break
            else:
                continue
            break
        #print('trovata ai livelli: ',self.par2_at_livello)
        #print(self.checkTrovataParola2())

    def checkTrovataParola2(self): # controllo su parola due
        if self.par2_at_livello:
            return 'La parola "' + self.parola2 + '"\nsi trova al livello ' + str(self.par2_at_livello[0][1] + 1)
            # prima parola trovata
            # livello + 1 perchè parte da 0
        else:
            return 'Non è stato possibile arrivare alla\nparola "' + self.parola2 + '" in ' + str(MAX_LIVELLO+1) + ' livelli'

    # ricorsiva
    def printAlbero(self, nodo: Nodo, indentazione=''): # debug stampa su terminale
        indentazione = self.parola1 + ' -> ' if indentazione == '' else indentazione
        if nodo:
            #print(indentazione, nodo.algoritmo)
            for elem in nodo.figli:
                self.printAlbero(elem, indentazione + ' ' + str(elem) + ' -> ')

    # ricorsiva
    def addPerTOLIST(self, nodo : Nodo): #funzione che aggiunge tutti i percorsi completi (parola1->parola2) in una lista
        if nodo:
            if self.parola2 == str(nodo):
                punteggio, percorso_completo = nodo.algoritmo.value, []
                for gen in nodo.genitori:
                    punteggio += gen.algoritmo.value # int enum
                lista_percorso = nodo.genitori + [nodo]
                percorso_completo = [lista_percorso,  punteggio]
                self.list_per_trov.append(percorso_completo) # lista di X percorsi completi con punteggi
            else:
                for elem in nodo.figli:
                    self.addPerTOLIST(elem)
