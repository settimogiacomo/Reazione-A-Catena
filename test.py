from  Nodo import Nodo
from Metodo import Metodo

x = Nodo('firma', Metodo.NESSUNO)
trovate = ['firmai',
'firma',
'ferma',
'forma',
'firme',
'firmi',
'firmo',
'farmi']

for parola in trovate:
    p = Nodo(parola, Metodo.AGGIUNGI)
    x.add_figlio(p)

print(x.stampa())
