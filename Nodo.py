from Metodo import Metodo
class Nodo:
    def __init__(self, radice, algoritmo: Metodo = Metodo.NESSUNO):
        self.radice = radice # stringa parola
        self.algoritmo = algoritmo #algoritmo usato per generare la parola, enum
        self.figli = []
        self.genitori = []

    def __str__(self):
        return self.radice

    def stampa(self):
        listaStampata = ''
        if self.figli:
            for nodoObj in self.figli:
                listaStampata += str(nodoObj) + ' --> '
        return self.radice, listaStampata

    def add_figlio(self, nodoObj):
        self.figli.append(nodoObj) #oggetto nodo

