import re
import fnmatch


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
                    traduzioni = []
                    traduzioni = line.strip().split()
                    parolaAliena = traduzioni[0]
                    traduzioni.pop(0)
                    trd = ""
                    for parola in traduzioni:
                        trd += parola + " "
                    #parola_aliena, traduzione = line.strip().split()
                    dizionario[parolaAliena.lower()] = trd.lower()
            return dizionario
        except FileNotFoundError:
            print("Il file 'dictionary.txt' non è stato trovato.")
            return {}

    def addWord(self, parola_aliena, traduzione):
        trdprecedente = self.cercaTraduzione(parola_aliena)
        trdprecedente += traduzione + " "
        self.dizionario[parola_aliena.lower()] = trdprecedente.lower()
        print(f"Parola '{parola_aliena}' aggiunta al dizionario.")
        self.scriviDizionario()
        #try:
        #    with (open(self.file_path, 'a') as file):
        #        file.write("\n" + parola_aliena.lower() + " " + traduzione.lower())
        #
        #except FileNotFoundError:
        #   print("File non trovato")

    def addWords2(self, parola_aliena, traduzioni):
        trdprecedente = self.cercaTraduzione(parola_aliena)
        trdprecedente += traduzioni
        print(trdprecedente)

        self.dizionario[parola_aliena.lower()] = trdprecedente.lower()

        print(f"Parola '{parola_aliena}' aggiunta al dizionario con nuova traduzione.")
        self.scriviDizionario()

    def scriviDizionario(self):
        try:
            with (open(self.file_path, 'w', encoding='utf-8') as file):
                file.write("")
        except FileNotFoundError:
            print("File non trovato")
        for key in self.dizionario:
            try:
                with (open(self.file_path, 'a') as file):
                    file.write(key.lower() + " " + self.dizionario[key.lower()] + "\n")
            except FileNotFoundError:
                print("File non trovato")

    def addWords(self, parola_aliena, traduzioni):
        for parola in traduzioni:

            self.dizionario[parola_aliena.lower()] = parola.lower()
            print(f"Parola '{parola_aliena}' aggiunta al dizionario con nuova traduzione.")
            try:
                with (open(self.file_path, 'a') as file):
                    file.write("\n" + parola_aliena.lower() + " " + parola.lower())

            except FileNotFoundError:
                print("File non trovato")

    def translate(self, parola_aliena):
        if parola_aliena.lower() in self.dizionario:
            return "la traduzione è: " + self.dizionario[parola_aliena.lower()]
        else:
            return "parola non trovata"

    def multipleTranslate(self, parola_aliena):
        lst =[]
        for x in self.dizionario:
            if x == parola_aliena.lower():
                lst.append(self.dizionario[x])

        #print("***********************************")
        #print(lst)
        return lst

    def cercaTraduzione(self, parola_aliena):
        if parola_aliena.lower() in self.dizionario:
            return self.dizionario[parola_aliena.lower()]
        else:
            return ""
    def translateWordWildCard(self, parola_aliena):
        print("******************")
        print(parola_aliena)
        filtered = fnmatch.filter(self.dizionario.keys(), parola_aliena)
        print(filtered)
        return "Possibile traduzione di " + parola_aliena + ": " + self.dizionario[filtered[0]]
        #x = re.search(parola_aliena, self.dizionario.keys())
        #for key in self.dizionario:
        #    x= re.search(parola_aliena, key)
        #    if x != None:
        #        return "Possibile traduzione di " + parola_aliena + ": " + self.dizionario[key]


    def __repr__(self):
        return repr(self.dizionario)


