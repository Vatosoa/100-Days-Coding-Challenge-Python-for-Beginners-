while True: 
    print("\nBienvenue sur Notre Calculatrice Préferée.")
    print("1. Addition")
    print("2. Soustraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Quitter")

    choix = input("Choisissez entre 1/2/3/4/5: ")

    if choix == "5":
        break

    if choix in ("1","2","3","4"):
        a = float(input("Entrer un nombre réel: "))
        b = float(input("Entrer un autre nombre réel: "))


        if  choix == "1":
            resultat = a + b
            operation = "Addition"
            operateur = "+"
        elif choix == "2":
            resultat = a - b
            operation = "Soustraction"
            operateur = "-"
        elif choix == "3":
            resultat = a * b
            operation = "Multiplication"
            operateur = "*"
        elif choix == "4":
            if b != 0:
                resultat = a / b
                operation = "Division"
                operateur = "/"                
            else:
                print("Erreur. Division par zéro.")
                continue

        print(f"{choix}.{operation}: {a} {operateur} {b} = {resultat}")

    else: 
        print("Erreur. Option non valide.")