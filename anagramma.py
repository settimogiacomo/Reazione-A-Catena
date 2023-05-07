
anagrammi = []
def trova_anagrammi(parola, prefisso=""):
    if len(parola) <= 1:
        par = prefisso + parola
        if par not in anagrammi:
            anagrammi.append(prefisso + parola)
    else:
        for i in range(len(parola)):
            rimanenti = parola[:i] + parola[i+1:]
            trova_anagrammi(rimanenti, prefisso + parola[i])
