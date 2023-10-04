import tkinter as tk

# Fonctions pour les opérations de base
def addition(a, b):
    return a + b

def soustraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Erreur : Division par zéro"
    return a / b

# Fonctions pour les opérations sur les vecteurs
def addition_vecteurs(vecteur1, vecteur2):
    return [x + y for x, y in zip(vecteur1, vecteur2)]

def soustraction_vecteurs(vecteur1, vecteur2):
    return [x - y for x, y in zip(vecteur1, vecteur2)]

def produit_scalaire(vecteur1, vecteur2):
    return sum(x * y for x, y in zip(vecteur1, vecteur2))

# Fonction pour afficher le résultat dans l'interface
def afficher_resultat(resultat):
    resultat_label.config(text=f"Résultat : {resultat}")

# Fonctions pour les boutons d'opérations de base
def calculer_operation(operation):
    try:
        valeur1 = float(valeur1_entry.get())
        valeur2 = float(valeur2_entry.get())
        if operation == "addition":
            resultat = addition(valeur1, valeur2)
        elif operation == "soustraction":
            resultat = soustraction(valeur1, valeur2)
        elif operation == "multiplication":
            resultat = multiplication(valeur1, valeur2)
        elif operation == "division":
            resultat = division(valeur1, valeur2)
        afficher_resultat(resultat)
    except ValueError:
        afficher_resultat("Erreur : Veuillez entrer des valeurs numériques.")
    except ZeroDivisionError:
        afficher_resultat("Erreur : Division par zéro.")

# Fonctions pour les boutons d'opérations sur les vecteurs
def calculer_operation_vecteur(operation):
    try:
        vecteur1 = [float(x) for x in vecteur1_entry.get().split()]
        vecteur2 = [float(x) for x in vecteur2_entry.get().split()]
        if operation == "addition_vecteurs":
            resultat = addition_vecteurs(vecteur1, vecteur2)
        elif operation == "soustraction_vecteurs":
            resultat = soustraction_vecteurs(vecteur1, vecteur2)
        elif operation == "produit_scalaire":
            resultat = produit_scalaire(vecteur1, vecteur2)
        afficher_resultat(resultat)
    except ValueError:
        afficher_resultat("Erreur : Veuillez entrer des valeurs numériques.")

# Configuration de la fenêtre Tkinter
window = tk.Tk()
window.title("Calculatrice")

# Cadre pour les opérations de base
operation_base_frame = tk.Frame(window)
operation_base_frame.pack(pady=10)

valeur1_label = tk.Label(operation_base_frame, text="Valeur 1:")
valeur1_label.pack(side="left")

valeur1_entry = tk.Entry(operation_base_frame)
valeur1_entry.pack(side="left")

valeur2_label = tk.Label(operation_base_frame, text="Valeur 2:")
valeur2_label.pack(side="left")

valeur2_entry = tk.Entry(operation_base_frame)
valeur2_entry.pack(side="left")

addition_button = tk.Button(operation_base_frame, text="Addition", command=lambda: calculer_operation("addition"))
addition_button.pack(side="left")

soustraction_button = tk.Button(operation_base_frame, text="Soustraction", command=lambda: calculer_operation("soustraction"))
soustraction_button.pack(side="left")

multiplication_button = tk.Button(operation_base_frame, text="Multiplication", command=lambda: calculer_operation("multiplication"))
multiplication_button.pack(side="left")

division_button = tk.Button(operation_base_frame, text="Division", command=lambda: calculer_operation("division"))
division_button.pack(side="left")

# Cadre pour les opérations sur les vecteurs
operation_vecteur_frame = tk.Frame(window)
operation_vecteur_frame.pack(pady=10)

vecteur1_label = tk.Label(operation_vecteur_frame, text="Vecteur 1 (séparé par des espaces):")
vecteur1_label.pack(side="left")

vecteur1_entry = tk.Entry(operation_vecteur_frame)
vecteur1_entry.pack(side="left")

vecteur2_label = tk.Label(operation_vecteur_frame, text="Vecteur 2 (séparé par des espaces):")
vecteur2_label.pack(side="left")

vecteur2_entry = tk.Entry(operation_vecteur_frame)
vecteur2_entry.pack(side="left")

addition_vecteurs_button = tk.Button(operation_vecteur_frame, text="Addition de Vecteurs", command=lambda: calculer_operation_vecteur("addition_vecteurs"))
addition_vecteurs_button.pack(side="left")

soustraction_vecteurs_button = tk.Button(operation_vecteur_frame, text="Soustraction de Vecteurs", command=lambda: calculer_operation_vecteur("soustraction_vecteurs"))
soustraction_vecteurs_button.pack(side="left")

produit_scalaire_button = tk.Button(operation_vecteur_frame, text="Produit Scalaire", command=lambda: calculer_operation_vecteur("produit_scalaire"))
produit_scalaire_button.pack(side="left")

# Affichage du résultat
resultat_label = tk.Label(window, text="")
resultat_label.pack()

window.mainloop()
