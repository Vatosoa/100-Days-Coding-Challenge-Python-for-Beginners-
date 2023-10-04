import math

while True:
    print("\nCalculatrice de Logarithmes")
    print("1. Logarithme népérien (ln)")
    print("2. Logarithme en base 10 (log10)")
    print("3. Quitter")

    choix = input("Choisissez une option (1/2/3) : ")

    if choix == "3":
        break

    if choix in ("1", "2"):
        try:
            nombre = float(input("Entrer un nombre positif: "))

            if nombre <= 0:
                print("Erreur : Le nombre doit être positif.")
                continue 

            if choix == "1":
                resultat = math.log(nombre)
                print(f" ln({nombre}) = {resultat}")
            elif choix == "2":
                resultat = math.log10(nombre)
                print(f" ln10({nombre}) = {resultat}")
        except ValueError:
            print("Erreur : Veuillez entrer un nombre positif. ")

    else:
        print("Option non valide. Veuillez choisir une option valide (1/2/3). ")
