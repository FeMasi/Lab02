class Dictionary:
    def __init__(self, file_path):
        self.file_path = file_path
        self.dizionario = self.leggi_dizionario()


    def leggi_dizionario(self):
        """
        Legge un dizionario iniziale da un file di testo.
        Restituisce un dizionario Python con le parole aliene e le relative traduzioni.
        """
        dizionario = {}
        try:
            with (open(self.file_path, 'r') as file):
                for line in file:
                    parola_aliena, traduzione = line.strip().split()
                    dizionario[parola_aliena.lower()] = traduzione.lower()
            return dizionario
        except FileNotFoundError:
            print("Il file 'dictionary.txt' non è stato trovato.")
            return {}

    def addWord(self, parola_aliena, traduzione):
        self.dizionario[parola_aliena.lower()] = traduzione.lower()
        print(f"Parola '{parola_aliena}' aggiunta al dizionario.")


    def translate(self, parola_aliena):
        if parola_aliena.lower() in self.dizionario:
            return "la traduzione è: " + self.dizionario[parola_aliena.lower()]
        else:
            return "parola non trovata"


    def translateWordWildCard(self):
        pass


    def __repr__(self):
        return repr(self.dizionario)


