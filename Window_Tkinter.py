import tkinter as tk
from Nodo import Nodo
from Algoritmi import Algoritmi
from Metodo import Metodo

class Window:
    def __init__(self):
        self.algo = Algoritmi()
        self.algo.caricaDizionario()
        self.window = tk.Tk()
        tk.Label(self.window, text="Parola 1").grid(row=0,column=0)
        tk.Label(self.window, text="Parola 2").grid(row=1,column=0)
        self.txtParola1 = tk.Entry(self.window, bd=5)
        self.txtParola1.grid(row=0, column=2, columnspan=3)
        self.txtParola2 = tk.Entry(self.window, bd=5)
        self.txtParola2.grid(row=1, column=2, columnspan=3)
        self.btnCerca = tk.Button(self.window, text="Cerca", fg="green3", bg="blue")
        self.btnCerca.configure(command=self.cercaPercorso)
        self.btnCerca.grid(row=4, columnspan=3, column=1)
        self.btnReset = tk.Button(self.window, text="Reset", fg="Red", bg="#000")
        self.btnReset.configure(command=self.reset)
        self.btnReset.grid(row=4, columnspan=3, column=3)
        self.feedback = tk.StringVar(value='')
        tk.Label(self.window, textvariable=self.feedback,fg='green3').grid(row=5,column=0,columnspan=5)

        self.lista = tk.Listbox(self.window, width=40)
        self.lista.grid(row=6, column=0, columnspan=4)



    def start(self):
        self.window.mainloop()

    def cercaPercorso(self):  # btn

        print(self.txtParola1.get(), self.txtParola2.get())
        self.algo.parola1 = self.txtParola1.get()
        self.algo.parola2 = self.txtParola2.get()
        feedbackParole = self.algo.controllaParole()
        if feedbackParole == "":
            nodoInizio = Nodo(self.algo.parola1)
            self.algo.calcolaPercorsi(nodoInizio)
            self.algo.printAlbero(nodoInizio)

            self.feedback.set(self.algo.checkTrovataParola2())
            print(nodoInizio)
            self.stampaPercorso(nodoInizio)
            # risultato in stringa di calcolaPercorsi
        else:
            self.feedback.set(feedbackParole)
        return True

    def reset(self):
        self.txtParola1.delete(0,len(self.txtParola1.get()))
        self.txtParola2.delete(0,len(self.txtParola2.get()))
        self.algo.albero = None
        self.algo.parola1 = ''
        self.algo.parola2 = ''
        return True

    def stampaPercorso(self, nodo:Nodo):
        print(str(nodo), '=',self.algo.parola2)
        if str(nodo) == self.algo.parola2 and self.lista.size() == 0:
            print(str(nodo)+'+'+str(nodo.algoritmo))
            i = 0
            while i < len(nodo.genitori):
                genitore:Nodo = nodo.genitori[i]
                self.lista.insert(tk.END, str(genitore) + ' : ' + str(genitore.algoritmo))
                colore = self.scegliColore(genitore.algoritmo)
                self.lista.itemconfig(tk.END, fg="#fff", bg=colore, selectbackground=colore, selectforeground="white")
                if i != (len(nodo.genitori)):
                    self.lista.insert(tk.END, "↓")
                i += 1
            self.lista.insert(tk.END, str(nodo) + ' : ' + str(nodo.algoritmo))
            colore = self.scegliColore(nodo.algoritmo)
            self.lista.itemconfig(tk.END, fg="#fff", bg=colore, selectbackground=colore, selectforeground="white")

        else:
            if nodo:
                for elem in nodo.figli:
                    self.stampaPercorso(elem)

    def scegliColore(self, metodo:Metodo):
        match metodo:
            case 0:
                return '#fff'
            case 1:
                return 'DarkOrchid1'
            case 2:
                return 'yellow'
            case 3:
                return 'cyan2'
            case 4:
                return 'red3'