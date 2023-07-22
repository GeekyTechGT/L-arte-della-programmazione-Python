def calcola_media(lista_numeri):
    """
    Calcola la media dei numeri nella lista.
    
    Args:
        lista_numeri (list): Lista di numeri.
    
    Returns:
        float: La media dei numeri nella lista.
    """
    somma = sum(lista_numeri)
    media = somma / len(lista_numeri)
    return media

def trova_parole_comuni(testo1, testo2):
    """
    Trova le parole comuni tra due testi.
    
    Args:
        testo1 (str): Primo testo.
        testo2 (str): Secondo testo.
    
    Returns:
        set: Insieme delle parole comuni tra i due testi.
    """
    parole1 = set(testo1.split())
    parole2 = set(testo2.split())
    parole_comuni = parole1.intersection(parole2)
    return parole_comuni

# Esempio di utilizzo delle funzioni

# Task 1: Calcolare la media di una lista di numeri
lista_numeri = [10, 20, 30, 40, 50]
media = calcola_media(lista_numeri)
print(f"La media dei numeri nella lista {lista_numeri} è: {media}")

# Task 2: Trovare le parole comuni tra due testi
testo1 = "Questo è un esempio di testo."
testo2 = "Questo è un altro esempio di testo."
parole_comuni = trova_parole_comuni(testo1, testo2)
print(f"Le parole comuni tra i due testi sono: {parole_comuni}")