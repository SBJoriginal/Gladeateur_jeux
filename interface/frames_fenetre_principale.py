"""
Module contenant des frames utilitaires présents dans la fenêtre principale.
"""

from tkinter import Frame, Label, Button, Scale, VERTICAL, IntVar

#import self as self

# from interface import fenetre_introduction

from interface.fenetre_introduction import FenetreIntroduction
from interface.joueur_ordinateur import JoueurOrdinateur
#from gestionnaire_io_interface import GestionnaireIOInterface

class FrameDescription(Frame):
    def __init__(self, master):
        """
        Constructeur de la classe FrameDescription. Affiche un descriptif
        de ce qui se passe dans le jeu.

        Args:
            master (Tk): La fenêtre dans laquelle ce frame s'insert.
        """
        super().__init__(master)
        self.label_description = Label(self, text="")
        self.label_description.grid(row=0, column=0)

    def populer(self, texte, temps_attente, suite):
        """
        Cette méthode affiche les informations sur le jeu.

        Args:
            texte (str): Le message à afficher
            temps_attente (int): Temps en millisecondes avant d'exécuter la suite
            suite (fonction): La fonction à exécuter après
        """
        self.label_description['text'] = texte
        self.after(temps_attente, suite)

    def vider(self):
        """
        Cette méthode enlève l'affichage.
        """
        self.label_description['text'] = ""


class FrameJoueurActif(Frame):
    def __init__(self, master):
        """
        Constructeur de la classe FrameJoueurActif. Affiche les informations relatives au
        joueur dont c'est le tour.

        Args:
            master (Tk): La fenêtre dans laquelle ce frame s'insert.
        """
        super().__init__(master)

        self.label_nom_joueur = Label(self, text="")
        self.label_nombre_des = Label(self, text="")

        self.label_nom_joueur.grid(row=0, column=0)
        self.label_nombre_des.grid(row=1, column=0)

        self.clic_bouton = lambda: None
        self.bouton_terminer_tour = Button(self, text="Terminer le tour", command=self.appui_bouton)
        self.bouton_terminer_tour.grid(row=1, column=1)
        self.bouton_terminer_tour["state"] = "disabled"

        self.couleurs = [
            'blue', 'green', 'red', 'orange', 'purple'
        ]

    def populer(self, joueur):
        """
        Ajoute les informations d'un joueur dans le frame.

        Args:
            joueur (Joueur): le joueur dont c'est le tour
        """
        self.label_nom_joueur["text"] = f"Joueur # {joueur.numero_joueur}"
        self.label_nombre_des["text"] = f"{len(joueur.des)} dés"
        self.label_nom_joueur["fg"] = self.couleurs[joueur.numero_joueur - 1]
        self.label_nombre_des["fg"] = self.couleurs[joueur.numero_joueur - 1]

    def activer_bouton(self, fonction):
        """
        Permet de cliquer sur le bouton fin du tour, et associe la fonction au clic.

        Args:
            fonction (fonction): La fonction à exécuter suite au clic de bouton
        """
        self.bouton_terminer_tour["state"] = "normal"
        self.clic_bouton = fonction

    def appui_bouton(self):
        """
        Effectue la fonction à exécuter suite au clic de bouton, et grise le bouton.
        """
        self.bouton_terminer_tour["state"] = "disabled"
        self.clic_bouton()


class FrameTableauJoueurs(Frame):
    def __init__(self, master):
        super().__init__(master)

        #### DÉBUT DÉFI TABLEAU DES JOUEURS ####
        # Une partie du code pour ce défi se trouve dans le constructeur,
        # le reste dans la méthode mise_a_jour
        #
        # self.liste_de_joueurs = []
        #
        # for i in range(len(self.master.joueurs)):
        #     self.liste_de_joueurs.append(Label(self, text=self.master.joueurs[i], fg=self.master.frame_joueur.couleurs[i]))
        #     self.liste_de_joueurs[i].grid(row=i, column=0)

        self.master = master
        self.frame_joueur = FrameJoueurActif(self.master)
        self.arene, self.joueurs = FenetreIntroduction.obtenir_donnees(self.master)

    def mise_a_jour(self):

        i = 0
        for joueur in self.joueurs:
            joueur_encors = Label(self, text="")
            if len(joueur.des) != 0:
                joueur_encors["text"] = f"Joueur {str(joueur.numero_joueur)} : {str(len(joueur.des))} dés."
                joueur_encors["text"] = self.master.frame_joueur.couleurs[joueur.numero_joueur - 1]
            else:
                joueur_encors["text"] = f"Joueur {str(joueur.numero_joueur)} : {str(len(joueur.des))} dés. ÉLIMINÉ !"
                joueur_encors["fg"] = self.master.frame_joueur.couleurs[joueur.numero_joueur - 1]

            joueur_encors.grid(row=i, column=10)
            i += 1


#### FIN DÉFI TABLEAU DES JOUEURS ####


class FrameTempsAttente(Frame):
    def __init__(self, master):
        super().__init__(master)

        #### DÉBUT DÉFI TEMPS ATTENTE ####

        def nouvelle_fonction():
            nouveau_temps_attente = scale_temps_attente.get()
            print(nouveau_temps_attente)
            return nouveau_temps_attente

        scale_temps_attente = Scale(master, from_=10, to=500, command=nouvelle_fonction)
        scale_temps_attente.grid(row=1, column=1, padx=10, pady=10)

        self.master.gestionnaire_io.temps_attente = nouvelle_fonction

        #### FIN DÉFI TEMPS ATTENTE ####
