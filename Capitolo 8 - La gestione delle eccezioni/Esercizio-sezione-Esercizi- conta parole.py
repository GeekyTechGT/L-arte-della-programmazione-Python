def conta_parole(nome_file):
    """
    Conta il numero di parole presenti nel file specificato.
    Solleva FileNotFoundError se il file non viene trovato.
    Solleva IOError se si verifica un errore di lettura del file.
    """

    try:
        with open(nome_file, 'r') as file:
            contenuto = file.read()
            parole = contenuto.split()
            numero_parole = len(parole)
            return numero_parole

    except FileNotFoundError:
        raise FileNotFoundError("Errore: File non trovato!")
    except IOError:
        raise IOError("Errore: Si è verificato un errore di lettura del file!")
    except Exception as e:
        raise Exception("Errore imprevisto durante l'elaborazione del file:", str(e))


# Test del programma
try:
    nome_file = input("Inserisci il nome del file: ")
    numero_parole = conta_parole(nome_file)
    print("Il numero di parole nel file è:", numero_parole)

except FileNotFoundError as e:
    print(e)
except IOError as e:
    print(e)
except Exception as e:
    print(e)
