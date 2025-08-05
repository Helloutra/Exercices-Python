moyenne = 0
somme = 0
nb_notes = 0
while True:
    note = input("Entrez une note sur 20 (ou 'q' pour quitter) : ")
    if note.lower() == 'q':
        break
    try:
        note = float(note)
        if 0 <= note <= 20:
            somme += note
            nb_notes += 1
        else:
            print("La note doit être entre 0 et 20.")
    except ValueError:
        print("Veuillez entrer un nombre valide.")
if nb_notes > 0:
    moyenne = somme / nb_notes
    print(f"La moyenne des notes est : {moyenne:.2f}")