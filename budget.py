

def ajouter_depense(liste):
    titre = input("Description de la depense: ").strip()

    if not titre:
        print("La description ne peut pas être vide.")
        return

    montant = input("Le montant").strip()
    if not montant:
        print("Pas de mantant ")
        return

    try :
        montant = float(montant)
    except ValueError:
        print("Erreur : saisis un nombre valide")

    categorie = input("Categorie").strip()
    if not categorie:
            print("Pas de categorie ")
            return

    liste.append({"titre": titre, "montant": montant, "categorie": categorie})
    print("Dépense ajoutée !")

    


def afficher_depenses(liste):
      if not liste:
            print("Pas de Dépense ")
            return

      for i, depense in enumerate(liste, start=1):
           print(f"{i}. {depense['title']} - {depense['montant']: .2f}  €  [{depense['categorie']}]")



def calculer_total(liste):
     if not liste:
        print("Pas de Dépense ")  
        return

     somme = 0

     for depense in liste:
          somme += depense["montant"]

          
     print(f"Total des dépenses : {somme:.2f} €")


def supprimer_depense(liste):
    if not liste:
        print("Pas de dépense.")
        return

    afficher_depenses(liste)

    choix = input("Numéro de la dépense à supprimer : ").strip()

    try:
        index = int(choix) - 1
    except ValueError:
        print("Erreur : saisis un numéro valide.")
        return

    if 0 <= index < len(liste):
        element_supprime = liste.pop(index)
        print(f"Dépense « {element_supprime['titre']} » supprimée !")
    else:
        print("Numéro introuvable.")
    
     



     
     