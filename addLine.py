def inserisci_riga(file_path, riga_da_inserire, posizione):
    with open(file_path, 'r') as file:
        righe = file.readlines()

    # Inserisci la nuova riga nella posizione desiderata
    righe.insert(posizione, riga_da_inserire)

    with open(file_path, 'w') as file:
        file.writelines(righe)

# Esempio di utilizzo
file_path = 'nome_file.txt'
riga_da_inserire = "Nuova riga da inserire."
posizione_desiderata = 2  # Indice della posizione in cui inserire la riga

inserisci_riga(file_path, riga_da_inserire, posizione_desiderata)



with open('nome_file.txt', 'r+') as file:
    posizione_desiderata = 10  # Posizione in cui inserire la riga
    file.seek(posizione_desiderata)
    file.write("Nuova riga da inserire.")
