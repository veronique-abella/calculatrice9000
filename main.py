def addition(a, b):
    return a + b

def soustraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Erreur : Division par zéro impossible"
    return a / b

def calculatrice():
    operations = {
        '+': addition,
        '-': soustraction,
        '*': multiplication,
        '/': division
    }

    print("Bienvenue dans la calculatrice !")
    while True:
        try:
            nombre1 = float(input("Entrez le premier nombre : "))
            nombre2 = float(input("Entrez le deuxième nombre : "))
            operation = input("Entrez l'opération (+, -, *, /) : ")

            if operation not in operations:
                print("Erreur : Opération non valide.")
                continue

            resultat = operations[operation](nombre1, nombre2)
            print(f"Le résultat de {nombre1} {operation} {nombre2} est égal à : {resultat}")
        except ValueError:
            print("Erreur : Veuillez entrer des nombres valides.")
        except Exception as e:
            print(f"Erreur : {e}")

        continuer = input("Voulez-vous continuer ? (Oui/Non) : ")
        if continuer.lower() != 'oui':
            break

calculatrice()