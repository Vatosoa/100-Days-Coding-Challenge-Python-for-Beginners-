while True:
    print("Calculatrice de Vecteurs")
    print("1. Addition de Vecteurs")
    print("2. Soustraction de Vecteurs")
    print("3. Produit Scalaire de Vecteurs")
    print("4. Quitter")
    
    choix = input("Choisissez une option (1/2/3/4) : ")
    
    if choix == '4':
        break
    
    if choix in ('1', '2', '3'):
        try:
            taille = int(input("Entrez la taille des vecteurs : "))
            vecteur1 = [float(input(f"Entrez l'élément {i + 1} du premier vecteur : ")) for i in range(taille)]
            vecteur2 = [float(input(f"Entrez l'élément {i + 1} du deuxième vecteur : ")) for i in range(taille)]
            
            if choix == '1':
                resultat = [x + y for x, y in zip(vecteur1, vecteur2)]
                print("Résultat de l'addition : ", resultat)
            elif choix == '2':
                resultat = [x - y for x, y in zip(vecteur1, vecteur2)]
                print("Résultat de la soustraction : ", resultat)
            elif choix == '3':
                resultat = sum(x * y for x, y in zip(vecteur1, vecteur2))
                print("Résultat du produit scalaire : ", resultat)
        
        except ValueError:
            print("Erreur : Veuillez entrer des valeurs numériques.")
    else:
        print("Option non valide. Veuillez choisir une option valide (1/2/3/4).")
