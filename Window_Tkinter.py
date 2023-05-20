import tkinter
import tkinter as tk
from Algoritmi import Algoritmi

class Window:
    def __init__(self):
        self.algo = Algoritmi()
        self.algo.caricaDizionario()
        #self.algo.chiediParole()
        self.window = tk.Tk()
        tk.Label(self.window, text="Parola 1").grid(row=0,column=0)
        tk.Label(self.window, text="Parola 2").grid(row=1,column=0)
        self.txtParola1 = tk.Entry(self.window, bd=5).grid(row=0, column=2, columnspan=3)
        self.txtParola2 = tk.Entry(self.window, bd=5).grid(row=1, column=2, columnspan=3)
        self.btnCerca = tk.Button(self.window, text="Cerca", fg="yellow", bg="blue")
        self.btnCerca.configure(command=self.cercaPercorso)
        self.btnCerca.grid(row=4, columnspan=3, column=1)
        self.btnReset = tk.Button(self.window, text="Reset", fg="Red", bg="#000")
        self.btnReset.configure(command=self.reset)
        self.btnReset.grid(row=4, columnspan=3, column=3)
        self.feedback = tk.StringVar(value='')
        tk.Label(self.window, textvariable=self.feedback,fg='#000').grid(row=5,column=2,columnspan=5)



    def start(self):
        self.window.mainloop()

    def cercaPercorso(self):

        print(self.txtParola1.get(), self.txtParola2.get())
        self.algo.parola1 = self.txtParola1.get()
        self.algo.parola2 = self.txtParola2.get()
        nasino = self.algo.controllaParole()
        if nasino == "":
            print("crea il nodo")
            #self.algo.calcolaPercorsi()
        else:
            self.feedback.set(nasino)




        return True

    def reset(self):
        print(self.txtParola1.get())
        self.txtParola1.delete(0,len(self.txtParola1.get()))
        self.txtParola2.delete(0,len(self.txtParola2.get()))
        return True