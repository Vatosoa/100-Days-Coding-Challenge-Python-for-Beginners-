def factorielle(n):
    if n == 0:
        return 1
    else:
        return n * factorielle(n-1)
    
# Exemple d'utilisation : 
nb = int(input("Entrez un nombre: "))
resultat = factorielle(nb)
print(resultat)