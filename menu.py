#######################
###### Python 3. ######
######## Snake ########
##### Hugo EXTRAT #####
#######################

from tkinter import *
import os
import pygame

#----------------------------------------------------------------------------------------------------
# Fonction pour quitter le launcher
def quitter():
    Fenetre.destroy()

#----------------------------------------------------------------------------------------------------
# Fonction ajouter une valeur à une variable quand on clique sur le bouton radio
def jouer():
    global var_jouer
    var_jouer += 1

#----------------------------------------------------------------------------------------------------
# Bouton pour lancer le jeu correspondant au nombres de joueurs
def start():
    if var_joueur.get()==1 and var_jouer!=0 and var_vitesse.get()==1:
        os.popen("1_Player\A1_Snake_70.py")

    elif var_joueur.get()==1 and var_jouer!=0 and var_vitesse.get()==2:
        os.popen("1_Player\A1_Snake_50.py")

    elif var_joueur.get()==1 and var_jouer!=0 and var_vitesse.get()==3:
        os.popen("1_Player\A1_Snake_40.py")

    elif var_joueur.get()==1 and var_jouer!=0 and var_vitesse.get()==4:
        os.popen("1_Player\A1_Snake_30.py")


    
        
    elif var_joueur.get()==2 and var_jouer!=0 and var_vitesse.get()==1:
        os.popen("2_Players\A2_Snake_70.py")

    elif var_joueur.get()==2 and var_jouer!=0 and var_vitesse.get()==2:
        os.popen("2_Players\A2_Snake_50.py")

    elif var_joueur.get()==2 and var_jouer!=0 and var_vitesse.get()==3:
        os.popen("2_Players\A2_Snake_40.py")

    elif var_joueur.get()==2 and var_jouer!=0 and var_vitesse.get()==4:
        os.popen("2_Players\A2_Snake_30.py")



    elif var_jouer==0:
        filewin4=Toplevel(Fenetre)
        Label7=Label(filewin4,text="Veuillez sélectionner le nombre de joueur.")
        Label7.place(x=20,y=10)
        filewin4.geometry('250x50')
        filewin4.title('Attention !')
        
    elif var_jouer==1:
        filewin4=Toplevel(Fenetre)
        Label7=Label(filewin4,text="Veuillez sélectionner un mode de jeu.")
        Label7.place(x=20,y=10)
        filewin4.geometry('250x50')
        filewin4.title('Attention !')
#---------------------------------------------------------------------------------------------------
#Fonction pour le menu ( Work in progress )
def Docs():
   filewin = Toplevel(Fenetre)
   Label4=Label(filewin,text="-Pour lancer une partie veuillez sélectionner le nombres de joueurs et la vitesse de votre serpent.\n" +
                "-Une fois cette démarche réalisé appuyé sur le bouton Jouer.\n")
   Label4.place(x=10,y=10)
   filewin.geometry('540x200')
   filewin.resizable(width=False,height=False)
   

def En_Savoir_Plus():
   filewin2 = Toplevel(Fenetre)
   Label5=Label(filewin2,text="Projet ISN 2015\n\n Lycée du Forez\n\n" +
                " Contact : extrat.h@gmail.com")
   Label5.place(x=10,y=10)
   filewin2.geometry('190x120')
   filewin2.resizable(width=False,height=False)

def tuto():
    filewin3 = Toplevel(Fenetre)
    Label6=Label(filewin3,text="Snake 1 Joueur :\n\n -Pour le déplacement du serpent vous pouvez utiliser les touches ZQSD ou les flèches du clavier.\n" +
                 "-Vous pouvez mettre en pause le jeu avec la touche P et relancer le jeu avec la touche ESPACE.\n\n" +
                 "Snake 2 Joueurs :\n\n -Le premier joueur va jouer avec les touches ZQSD et l'autre joueur avec les flèches du clavier.\n" +
                 "-Vous pouvez mettre en pause le jeu avec la touche P et relancer le jeu avec la touche ESPACE.\n" +
                 "-Pour lancer une nouvelle partie vous avez la touche N ou le bouton Nouvelle Partie.\n" +
                 "-Si l'un des joueurs fait mourir son serpent il perd la partie.\n\n" +
                 " Nous vous souhaitons bonne chance et bon jeu")
    Label6.place(x=10,y=10)
    filewin3.geometry('540x250')
    filewin3.resizable(width=False,height=False)

    
#----------------------------------------------------------------------------------------------------
# Fenetre tkinter avec des variables
Fenetre=Tk()
menubar = Menu(Fenetre)
Fenetre.title('Snake')
Fenetre.geometry('400x500')
Fenetre.config(bg='gray51')
Fenetre.resizable(width=False,height=False)

#----------------------------------------------------------------------------------------------------
#Création d'un menu

fichier_menu = Menu(menubar)

fichier_menu.add_command(label="Comment jouer ?", command=tuto)
fichier_menu.add_command(label="Quitter", command=quitter)
menubar.add_cascade(label="Fichier", menu=fichier_menu)


aide_menu = Menu(menubar)

aide_menu.add_command(label="Docs", command=Docs)
aide_menu.add_command(label="En savoir plus", command=En_Savoir_Plus)
menubar.add_cascade(label="Aide", menu=aide_menu)

Fenetre.config(menu=menubar)

#---------------------------------------------------------------------------------------------------
#Variables

var_jouer = 0
var_joueur = IntVar()
var_vitesse = IntVar()



#----------------------------------------------------------------------------------------------------
# Bouton pour lancer le jeu
bouton_jouer=Button(Fenetre, text='Jouer', command=start)
bouton_jouer.place(x=20,y=110,width=360,height=80)
bouton_jouer.config(font=('courrier',30,'bold'),bg='black',fg='white')

#----------------------------------------------------------------------------------------------------
# Bouton pour quitter le launcher
bouton_quitter=Button(Fenetre,text='Quitter',command=quitter)
bouton_quitter.place(x=20,y=440,width=360,height=50)
bouton_quitter.config(font=('courrier',30,'bold'),bg='black',fg='white')

#----------------------------------------------------------------------------------------------------
# Bouton radios permettant le choix du nombre de joueurs
bouton_joueur_un=Radiobutton(Fenetre, text='Un Joueur', value=1, variable=var_joueur, command=jouer)
bouton_joueur_un.place(x=20,y=210,width=130,height=50)
bouton_joueur_un.config(font=('courrier',16,'bold'),bg='gray51',fg='black')

bouton_joueur_deux=Radiobutton(Fenetre,text='Deux Joueurs', value=2, variable=var_joueur, command=jouer)
bouton_joueur_deux.place(x=180,y=210,width=170,height=50)
bouton_joueur_deux.config(font=('courrier',16,'bold'),bg='gray51',fg='black')

#-----------------------------------------------------------------------------------------------------
# Bouton radios permettant le choix de la vitesse
bouton_vitesseun=Radiobutton(Fenetre,text='Lente', value=1, variable=var_vitesse)
bouton_vitesseun.place(x=20,y=310,width=170,height=50)
bouton_vitesseun.config(font=('courrier',16,'bold'),bg='gray51',fg='black')

bouton_vitessedeux=Radiobutton(Fenetre,text='Normale', value=2, variable=var_vitesse)
bouton_vitessedeux.place(x=180,y=310,width=170,height=50)
bouton_vitessedeux.config(font=('courrier',16,'bold'),bg='gray51',fg='black')

bouton_vitessetrois=Radiobutton(Fenetre,text='Rapide', value=3, variable=var_vitesse)
bouton_vitessetrois.place(x=22,y=370,width=170,height=50)
bouton_vitessetrois.config(font=('courrier',16,'bold'),bg='gray51',fg='black')

bouton_vitessequatre=Radiobutton(Fenetre,text='Hardcore', value=4, variable=var_vitesse)
bouton_vitessequatre.place(x=180,y=370,width=170,height=50)
bouton_vitessequatre.config(font=('courrier',16,'bold'),bg='gray51',fg='black')

#------------------------------------------------------------------------------------------------------
# Affichage de la vitesse en Ms
vitesse=Label(Fenetre,text='Vitesse :')
vitesse.place(x=125,y=260,width=150,height=50)
vitesse.config(font=('courrier',20,'bold'),bg='gray51',fg='black')

#------------------------------------------------------------------------------------------------------
# Titre du jeu
titre=Label(Fenetre, text='SNAKE')
titre.place(x=20,y=0,width=360,height=100)
titre.config(font=('courrier',70,'bold'),bg='gray51',fg='black')


Fenetre.mainloop()
