class Singleton:
    __instance = None

    @staticmethod
    def get_instance():
        if Singleton.__instance is None:
            Singleton()
        return Singleton.__instance

    def __init__(self):
        if Singleton.__instance is not None:
            raise Exception('Questo è un Singleton! Usa il metodo \
            get_instance() per ottenerne l\'istanza.')
        else:
            Singleton.__instance = self

# Utilizzo del Singleton
singleton_instance1 = Singleton.get_instance()
singleton_instance2 = Singleton.get_instance()

# Verifica se le due istanze sono identiche
print(singleton_instance1 is singleton_instance2)  # Output: True
