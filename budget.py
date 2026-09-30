
import json


#======= Charger dépense ==============
def charger_depense():
    try: 
         with open("depense.json", "r", encoding="utf-8") as fichier_depense:
              return json.load(fichier_depense)
    except FileNotFoundError:
         return []
          

#============== ajouter dépense ========================
def ajouter_depense(liste):
    titre = input("Description de la depense : ").strip()

    if not titre:
        print("La description ne peut pas être vide.")
        return

    montant = input("Le montant ").strip()
    if not montant:
        print("Pas de montant ")
        return

    try :
        montant = float(montant)
    except ValueError:
        print("Erreur : saisis un nombre valide ")
        return

    categorie = input("Categorie ").strip()
    if not categorie:
            print("Pas de categorie ")
            return

    liste.append({"titre": titre, "montant": montant, "categorie": categorie})
    print("Dépense ajoutée !")

    
#============== Afficher depense ========================

def afficher_depenses(liste):
      if not liste:
            print("Pas de Dépense ")
            return

      for i, depense in enumerate(liste, start=1):
           print(f"{i}. {depense['titre']} - {depense['montant']: .2f}  €  [{depense['categorie']}]")


#============== Calculer Total Dépense depense ========================
def calculer_total(liste):
     if not liste:
        print("Pas de Dépense ")  
        return

     somme = 0

     for depense in liste:
          somme += depense["montant"]
     print(f"Total des dépenses : {somme:.2f} €")

#============== Supprimer depense ========================
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
    
#==================== Sauvegarder_depenses(liste) ===============     
def sauvegarder_depenses(liste):
     with open("depense.json", "w", encoding="utf-8") as fichier_depense:
          json.dump(liste, fichier_depense, indent=4)
          
     


     
#========= Menu ================
# 
def menu():

    depenses = charger_depense()

    while True:
        print("\n--- GESTIONNAIRE DE BUDGET ---")

        print("1. Ajouter une dépense")
        print("2. Afficher les dépenses")
        print("3. Calculer le total")
        print("4. Supprimer une dépense")
        print("5. Quitter")

        choix_utilisateur = input("Choisie une option de 1 a 5 : ").strip()


        if choix_utilisateur == "1":
            ajouter_depense(depenses)

        elif choix_utilisateur == "2" : 
            afficher_depenses(depenses)

        elif choix_utilisateur == "3" :
            calculer_total(depenses)

        elif choix_utilisateur == "4" :
            supprimer_depense(depenses)

        elif choix_utilisateur == "5" :
            sauvegarder_depenses(depenses)
            print("Dépenses sauvegardées ! Au revoir !")

            return

        else :

           print("Option invalide, saisis un chiffre entre 1 et 5.")
        

if __name__ == "__main__":
    menu()        


       
            

             

             

             

        
             
               