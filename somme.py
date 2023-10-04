# Fonction pour calculer la somme des chiffres d'un nombre
def somme(nombre):
    somme = 0
    while nombre > 0:
        #somme += nombre % 10 OU les 2 lignes suivantes
        chiffre = nombre % 10 # Obtenez le chiffre le moins significatif
        somme += chiffre      # Ajoutez le chiffre à la somme
        nombre //= 10         # Supprimez le chiffre que vous venez d'ajouter

    return somme

# Exemple d'utilisation :
nb = int(input("Entrez vos nombres sans espace: ")) #1244
resultat = somme(nb) #1+2+4+4
print(resultat)