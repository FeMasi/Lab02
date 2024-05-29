import dictionary
import re
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
        if traduzione == self.diz.cercaTraduzione(parola_aliena):
            print("Parola già aggiunta con questa traduzione")
        else:
            self.diz.addWord(parola_aliena.lower(), traduzione.lower())

    def handleMultipleAdd(self, entry):
        traduzioni = []
        traduzioni = entry.strip().split()
        parolaAliena= traduzioni[0]
        traduzioni.pop(0)
        trdFinal = ""
        lst = self.diz.multipleTranslate(parolaAliena)

        for parola in traduzioni:
            if parola not in self.diz.cercaTraduzione(parolaAliena):
                trdFinal += parola + " "



        if len(trdFinal) == 0:
            print("traduzioni già aggiunte")
        else:
            self.diz.addWords2(parolaAliena.lower(), trdFinal)



    def handleTranslate(self, query):
        print(self.diz.translate(query))



    def handleWildCard(self,query):
        # query is a string with a ? --> <par?la_aliena>
        #parolaAliena = query.replace("?", ".")

        #x = re.search(parolaAliena, self.diz.dizionario)
        print(self.diz.translateWordWildCard(query))

    def handlePrint(self):
       print(self.diz.__repr__())
