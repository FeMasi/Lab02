import dictionary
class Translator:


    def __init__(self):

        pass

    def printMenu(self):
        print("\nMenu:")
        print("1. Aggiungi nuova parola")
        print("2. Cerca traduzione")
        print("3. Traduci con wildcard")
        print("4. Stampa tutto il dizionario")
        print("5. Exit")

    def loadDictionary(self, dict):
        # dict is a string with the filename of the dictionary
        self.diz = dictionary.Dictionary(dict)



    def handleAdd(self, entry):
        parola_aliena, traduzione = entry.strip().split()
        self.diz.addWord(parola_aliena.lower(), traduzione.lower())

    def handleMultipleAdd(self, entry):
        parola_aliena = entry.strip(0).split
        traduzioni = []



    def handleTranslate(self, query):
        print(self.diz.translate(query))



    def handleWildCard(self,query):
        # query is a string with a ? --> <par?la_aliena>
        pass

    def handlePrint(self):
       print(self.diz.__repr__())
