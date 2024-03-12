import translator as tr

t = tr.Translator()
file_path = "dictionary.txt"
t.loadDictionary(file_path)

while(True):

    t.printMenu()

    caratteri = False

    txtIn = input("seleziona un opzione: ")

    # Add input control here!
    if (txtIn.isnumeric()):
        caratteri = True
    else:
        caratteri = False
        print("input non valido")
        continue

    if int(txtIn) == 1:
        print("inserisci la parola da aggiungere nel formato <parola aliena> <traduzione>:")
        query = input()
        if (query.isalpha()):
            caratteri = True
        else:
            caratteri = False
            print("input non valido")
            continue
        t.handleAdd(query)

    if int(txtIn) == 2:
        parola_aliena = input("Inserisci la parola aliena da tradurre: ").lower()
        if (parola_aliena.isalpha()):
            caratteri = True
        else:
            caratteri = False
            print("input non valido")
            continue
        t.handleTranslate(parola_aliena)

    if int(txtIn) == 3:
        pass
    if int(txtIn) == 4:
        print("Il dizionario: ")
        t.handlePrint()
    if int(txtIn) == 5:
        break
