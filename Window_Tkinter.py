import tkinter as tk
from Nodo import Nodo
from Algoritmi import Algoritmi
from Metodo import Metodo

class Window:
    def __init__(self):
        self.algo = Algoritmi()
        self.algo.caricaDizionario()
        self.window = tk.Tk()
        self.window.title("Reazione a Catena")

        tk.Label(self.window, text="Parola 1:").grid(row=0, column=0, pady=5, padx=10)
        tk.Label(self.window, text="Parola 2:").grid(row=1, column=0, pady=5, padx=10)

        self.txtParola1 = tk.Entry(self.window, bd=1, relief='flat',highlightthickness=1,highlightbackground="black", width=30, borderwidth=1)
        self.txtParola1.grid(row=0, column=1, columnspan=5, pady=5, padx=5)

        self.txtParola2 = tk.Entry(self.window, bd=1, relief='flat',highlightthickness=1,highlightbackground="black", width=30, borderwidth=1)
        self.txtParola2.grid(row=1, column=1, columnspan=5, pady=5, padx=5)

        self.btnCerca = tk.Button(self.window, text="Cerca", fg="#000", bg="green3", command=self.cercaPercorso, relief='ridge')
        self.btnCerca.grid(row=2, columnspan=2, column=1)

        self.btnReset = tk.Button(self.window, text="Reset", fg="#000", bg="Red", command=self.reset, relief='ridge')
        self.btnReset.grid(row=2, columnspan=3, column=2)

        self.feedback = tk.StringVar(value='')
        tk.Label(self.window, textvariable=self.feedback, fg='green3').grid(row=3, column=0, columnspan=6)

        self.containerButtons = tk.Text(self.window, width=35, height=15)
        self.containerButtons.grid(row=4, rowspan=2, column=0, columnspan=6)

        self.scroll = tk.Scrollbar(self.window, orient="vertical", command=self.containerButtons.yview)
        self.scroll.grid(row=4, rowspan=2, column=5, sticky=tk.N + tk.E + tk.S)
        self.containerButtons.config(state=tk.NORMAL)
        self.containerButtons.configure(yscrollcommand=self.scroll.set)

        self.lista = tk.Listbox(self.window, width=40, background="#fff")
        self.lista.grid(row=9, column=0, columnspan=6)

    def start(self):
        self.window.mainloop()

    def cercaPercorso(self):  # btn
        self.lista.delete(0,tk.END)
        self.feedback.set('')
        print(self.txtParola1.get(), self.txtParola2.get())
        self.algo.parola1 = self.txtParola1.get().strip().lower()
        self.algo.parola2 = self.txtParola2.get().strip().lower()
        feedbackParole = self.algo.controllaParole()

        if feedbackParole == "":
            nodoInizio = Nodo(self.algo.parola1) # crea il nodo iniziale
            self.algo.calcolaPercorsi(nodoInizio)
            #self.algo.printAlbero(nodoInizio) # debug terminale
            self.algo.addPerTOLIST(nodoInizio)


            self.feedback.set(self.algo.checkTrovataParola2())
            #print(nodoInizio)
            #self.stampaPercorso(nodoInizio) # listbox
            # risultato in stringa di calcolaPercorsi
            self.creaBottoniPercorsi()
        else:
            self.feedback.set(feedbackParole)
        return True

    def reset(self):
        self.txtParola1.delete(0,len(self.txtParola1.get()))
        self.txtParola2.delete(0,len(self.txtParola2.get()))
        self.lista.delete(0,tk.END)
        self.feedback.set('')
        self.containerButtons.delete(1.0,tk.END)
        self.algo = None
        self.algo = Algoritmi()
        self.algo.caricaDizionario()
        return True

    def creaBottoniPercorsi(self):
        self.containerButtons.delete(1.0,tk.END)
        index = 0
        for lista, punteggio in self.algo.list_per_trov:
            bottone = tk.Button(self.containerButtons, text="Percorso con punteggio di: " + str(punteggio), fg="black", bg="cyan", relief='ridge')
            bottone.configure(command=lambda idx=index: self.stampaPercorso(idx))
            self.containerButtons.window_create('end', window=bottone)
            self.containerButtons.insert('end', '\n')
            index += 1

    def stampaPercorso(self, index):
        self.lista.delete(0, tk.END)

        listagenitori = self.algo.list_per_trov[index][0]
        #punteggio = self.algo.list_per_trov[index][1]
        i = 0
        while i < len(listagenitori):
            genitore : Nodo = listagenitori[i]
            self.lista.insert(tk.END, str(genitore) + ' : ' + str(genitore.algoritmo))
            self.lista.itemconfig(tk.END, fg="#000")
            if i != (len(listagenitori)-1):
                self.lista.insert(tk.END, "↓")
            self.lista.itemconfig(tk.END, fg="#000")
            i += 1

