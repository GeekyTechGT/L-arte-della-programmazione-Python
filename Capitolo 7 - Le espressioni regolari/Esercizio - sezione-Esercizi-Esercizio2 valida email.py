import re

def valida_indirizzo_email(email):
    """
    Verifica se un indirizzo email è valido secondo gli standard.
    
    Argomenti:
    - email: L'indirizzo email da verificare.
    
    Restituisce:
    - True se l'indirizzo email è valido, False altrimenti.
    """
    
    # Creazione del pattern per l'indirizzo email
    pattern = re.compile(r"""
        ^                    # Ancoraggio all'inizio della stringa
        [\w\.-]+             # Nome utente: caratteri alfanumerici, punto, trattino
        @                    # Simbolo '@'
        ([\w-]+\.)+          # Dominio: caratteri alfanumerici, trattino, punto (ripetuti almeno una volta)
        [a-zA-Z]{2,}         # Dominio di primo livello: almeno due lettere
        $                    # Ancoraggio alla fine della stringa
        """, re.VERBOSE)
    
    # Verifica della corrispondenza con il pattern
    corrispondenza = pattern.search(email)
    
    # Restituzione del risultato
    if corrispondenza:
        return True
    else:
        return False


# Esempi di utilizzo
email1 = "example@example.com"         # Email valida
email2 = "example@123.456.789"         # Email non valida

print(valida_indirizzo_email(email1))  # Output: True
print(valida_indirizzo_email(email2))  # Output: False
