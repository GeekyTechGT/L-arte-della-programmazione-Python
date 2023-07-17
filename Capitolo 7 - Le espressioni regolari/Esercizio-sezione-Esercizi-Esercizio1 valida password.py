import re

def valida_password(password):
    """
    Verifica se una password è valida secondo determinati criteri.
    
    Argomenti:
    - password: La password da verificare.
    
    Restituisce:
    - True se la password è valida, False altrimenti.
    """
    
    # Creazione del pattern per la password
    pattern = re.compile(r"""
        ^                 # Ancoraggio all'inizio della stringa
        (?=.*[A-Z])       # Almeno una lettera maiuscola
        (?=.*[a-z])       # Almeno una lettera minuscola
        (?=.*\d)          # Almeno una cifra
        (?=.*[@#$%^&+=])  # Almeno un carattere speciale tra @#$%^&+=
        (?=\S+$)          # Nessuno spazio bianco consentito
        .{8,16}           # Lunghezza della password tra 8 e 16 caratteri
        $                 # Ancoraggio alla fine della stringa
        """, re.VERBOSE)
    
    # Verifica della corrispondenza con il pattern
    corrispondenza = pattern.search(password)
    
    # Restituzione del risultato
    if corrispondenza:
        return True
    else:
        return False


# Esempi di utilizzo
password1 = "Password1@"  # Password valida
password2 = "abc123"      # Password non valida

print(valida_password(password1))  # Output: True
print(valida_password(password2))  # Output: False