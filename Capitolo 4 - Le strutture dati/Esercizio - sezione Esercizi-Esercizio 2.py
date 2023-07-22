def genera_dizionario_studenti(lista_studenti):
    """
    Genera un dizionario degli studenti a partire da una lista di studenti.
    
    Args:
        lista_studenti (list): Lista degli studenti.
    
    Returns:
        dict: Dizionario degli studenti con i rispettivi voti inizializzati a 0.
    """
    dizionario_studenti = {}
    for studente in lista_studenti:
        dizionario_studenti[studente] = 0
    return dizionario_studenti

def registra_voto(dizionario_studenti, studente, voto):
    """
    Registra il voto di uno studente nel dizionario degli studenti.
    
    Args:
        dizionario_studenti (dict): Dizionario degli studenti con i rispettivi voti.
        studente (str): Nome dello studente.
        voto (int): Voto dello studente.
    """
    dizionario_studenti[studente] = voto

def calcola_media_voti(dizionario_studenti):
    """
    Calcola la media dei voti degli studenti nel dizionario degli studenti.
    
    Args:
        dizionario_studenti (dict): Dizionario degli studenti con i rispettivi voti.
    
    Returns:
        float: La media dei voti degli studenti.
    """
    voti = list(dizionario_studenti.values())
    media = sum(voti) / len(voti)
    return media

def trova_studenti_con_voto_alto(dizionario_studenti, soglia):
    """
    Trova gli studenti con un voto superiore alla soglia specificata.
    
    Args:
        dizionario_studenti (dict): Dizionario degli studenti con i rispettivi voti.
        soglia (int): Soglia del voto.
    
    Returns:
        set: Insieme degli studenti con un voto superiore alla soglia.
    """
    studenti_con_voto_alto = set()
    for studente, voto in dizionario_studenti.items():
        if voto > soglia:
            studenti_con_voto_alto.add(studente)
    return studenti_con_voto_alto

def conta_studenti_per_voto(dizionario_studenti):
    """
    Conta il numero di studenti per ogni voto nel dizionario degli studenti.
    
    Args:
        dizionario_studenti (dict): Dizionario degli studenti con i rispettivi voti.
    
    Returns:
        dict: Dizionario con il conteggio degli studenti per ogni voto.
    """
    conteggio_studenti_per_voto = {}
    for voto in dizionario_studenti.values():
        if voto in conteggio_studenti_per_voto:
            conteggio_studenti_per_voto[voto] += 1
        else:
            conteggio_studenti_per_voto[voto] = 1
    return conteggio_studenti_per_voto

# Esempio di utilizzo delle funzioni

# Task 1: Generare un dizionario degli studenti
lista_studenti = ["Alice", "Bob", "Charlie"]
dizionario_studenti = genera_dizionario_studenti(lista_studenti)
print("Dizionario degli studenti:", dizionario_studenti)
print()

# Task 2: Registare i voti degli studenti
registra_voto(dizionario_studenti, "Alice", 85)
registra_voto(dizionario_studenti, "Bob", 92)
registra_voto(dizionario_studenti, "Charlie", 78)
print("Dizionario degli studenti dopo aver registrato i voti:", dizionario_studenti)
print()

# Task 3: Calcolare la media dei voti degli studenti
media_voti = calcola_media_voti(dizionario_studenti)
print("Media dei voti degli studenti:", media_voti)
print()

# Task 4: Trovare gli studenti con un voto alto
soglia_voto_alto = 80
studenti_voto_alto = trova_studenti_con_voto_alto(dizionario_studenti, soglia_voto_alto)
print(f"Gli studenti con un voto superiore a {soglia_voto_alto} sono:", studenti_voto_alto)
print()

# Task 5: Contare gli studenti per ogni voto
conteggio_studenti_per_voto = conta_studenti_per_voto(dizionario_studenti)
print("Conteggio degli studenti per ogni voto:")
for voto, conteggio in conteggio_studenti_per_voto.items():
    print(f"Voto: {voto}, Numero di studenti: {conteggio}")