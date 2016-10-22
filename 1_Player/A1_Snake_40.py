#######################
###### Python 3. ######
######## Snake ########
##### Hugo EXTRAT #####
#######################

from tkinter import*
from tkinter.colorchooser import *
from random import randrange
import os
import time
import pygame

'########################################################################'
'#----------------------------------------------------------------------#'
'#                                Fonctions                             #'
'#----------------------------------------------------------------------#'
'########################################################################'

#######################################################################
# Fonction pour l'écran de fin ----------------------------------------
#######################################################################
def fin():
    can.delete(ALL) ## On supprime tous les objets du Canvas (can)
    end=can.create_text(350,160,font=('Fixedsys',24),text="Vous êtes mort! \nVotre score est de :" +str(manger), fill="RED") ## On crée un Texte avec le Score final

#######################################################################
# Les couleurs de la tete et du corp sont aléatoires ------------------
#######################################################################
def changecolor():
    global color_tete, color_corp
    couleur_tete = ['purple','cyan','maroon','green','red','blue','orange', 'yellow'] ## Couleur de la tête aléatoire
    color_t = randrange(8)
    color_tete = couleur_tete[color_t]
    
    couleur_corp = ['purple', 'pink', 'cyan','maroon','green','red','blue','orange', 'yellow'] ## Couleur du corp aléatoire
    color_c = randrange(9)
    color_corp = couleur_corp[color_c]

def tp():
    global coord_portail, coord_portail3,x_tp,y_tp,x_tp1,y_tp1
    x_tp=randrange(60,340,10)
    y_tp=randrange(60,300,10)
    portail=can.create_rectangle(x_tp,y_tp,x_tp+10,y_tp+10)
    portail1=can.create_rectangle(x_tp-5,y_tp-5,x_tp+15,y_tp+15)  
    coord_portail=(x_tp,y_tp)
    
    x_tp1=randrange(350,630,10)
    y_tp1=randrange(60,300,10)
    portail3=can.create_rectangle(x_tp1,y_tp1,x_tp1+10,y_tp1+10)
    portail4=can.create_rectangle(x_tp1-5,y_tp1-5,x_tp1+15,y_tp1+15)
    coord_portail3=(x_tp1,y_tp1)
#######################################################################
# La musique en jeu ( Utilisation de PyGame ) -------------------------
#######################################################################    
def music():
    pygame.mixer.init()
    son = pygame.mixer.Sound('music.ogg') ## On récupère la musique dans le dossier principal
    son.play(loops=-1, maxtime=0, fade_ms=0) ## Quand la musique se termine on la relance avec loops=-1
    
#######################################################################
# Fonction pour l'apparition aléatoire des pommes ---------------------
#######################################################################
def pose_pomme():
    global coord_pomme,x_pomme,y_pomme,pomme
    x_pomme=randrange(10,680,10) ## Coordonnées aléatoires X et Y des pommes
    y_pomme=randrange(10,360,10)
    pomme=can.create_oval(x_pomme,y_pomme,x_pomme+10,y_pomme+10,fill="Orange") ## Création d'une pomme dans le Canvas au coordonnées ci-dessus
    coord_pomme=(x_pomme,y_pomme) ## Coordonnées de la pomme

#######################################################################
# Fonction principale du jeu ------------------------------------------
#######################################################################
def move():
    global snake,direction,tete_x,tete_y,tete_x2,tete_y2,pomme,coord_pomme, color_tete, color_corp, coord_portail, coord_portail3 ## 2 Lignes de Global
    global x_pomme,y_pomme,corps,pos_x,pos_y,x,y,long,n,manger, temps, temps1,delai, acceleration, acceleration1, Score, jouer, play, manger            

    if temps == 2:
        jouer=can.create_text(350,200,font=('Fixedsys',18),text="Espace pour commencer !", fill="RED")
        

#######################################################################
# Boucles permettant le déplacement du serpent
    # Mouvement à gauche
    if direction==2:
        x=-10 ## Correspond à la valeur du déplacement en X
        y=0 ## De même mais en Y

    # Mouvement à droite
    elif direction==1:
        x=10
        y=0

    # Mouvement en bas      
    elif direction==0:
        y=-10
        x=0
        
    # Mouvement en haut     
    elif direction==3:
        y=10
        x=0

    #######################################################################
    long=len(snake) ##  Longeur du Serpent
    long=long-1 ## Dans une liste on part de 0 et que la longueur donne le nombre d'éléments
                ## Il faut enlever 1
    
    #######################################################################
    # Boucles permettant au serpent de grandir
    while long !=0: 
        ## On déplace d'abord les coordonnées des éléments, le corp du Serpent doit suivre la tête
        ## Le corp qui suit la tête ne doit jamais la dépasser, ainsi tous les carré vont se suivre
        pos_x[long]=pos_x[long-1] 
        pos_y[long]=pos_y[long-1]
        long+=-1
    
    pos_x[0]+=x
    pos_y[0]+=y
    long=0

    
    while long!=len(snake):
        can.coords(snake[long],pos_x[long],pos_y[long],pos_x[long]+10,pos_y[long]+10) ## Ce qui était valable pour les positions le devient pour le déplacement.
        long+=1
    long=1


    coord_tete=pos_x[long],pos_y[long] ## Coordonnées de la tête

    ## Si on touche un mur on affiche la fonction fin()
    if pos_y[long] > 350 or pos_y[long] < 10:
        temps=1
        fin()
        pseudo1()

    if pos_x[long] > 680 or pos_x[long] < 10:
        temps=1
        fin()
        pseudo1()

   
    #######################################################################
    # Boucle pour la rencontre entre la tete et la pomme
    
    if coord_tete==coord_pomme: ## Si les coordonnées de la tête et de la pomme sont les mêmes on fait la boucle
        can.delete(pomme) ## On supprime la pomme
        pose_pomme() ## On crée une pomme à un endroit aléatoire

        ## La pomme ne doit pas être sur le Serpent
        if pos_x[0]==x_pomme and pos_y[0]==y_pomme:
            can.delete(pomme)
            pose_pomme()
        if pos_x[long]==x_pomme and pos_y[long]==y_pomme:
            can.delete(pomme)
            pose_pomme()
            
        manger+=10 ## Chaque pomme mangé le score augmente de 10
        Score.config(text="Score : "+str(manger)) ## On affiche le score

        ## Options du jeu
        if manger >= 100:
            can.configure(bg="white") ## Si manger >=100 le fond devient Blanc
        if manger >= 200:
            can.configure(bg="grey") ## Si manger >=100 le fond devient Gris
        if manger == 100:
            delai -= 5 ## Quand manger == 100 la vitesse du Serpent augmente
            acceleration=can.create_text(350,350,font=('Fixedsys',16),text="Attention ! Petite accélération du serpent.", fill="RED") ## Texte pour anoncer l'accélération du Serpent
        if manger == 200:
            delai -= 5 ## Quand manger == 200 la vitesse du Serpent augmente
            acceleration1=can.create_text(350,350,font=('Fixedsys',16),text="Vous êtes très fort, la difficulté augmente.", fill="WHITE") ## Texte pour anoncer l'accélération du Serpent
        if manger > 100:
            can.delete(acceleration)
        if manger > 200:
            can.delete(acceleration1)
        if manger==200:
            tp()
            
        corps=can.create_rectangle(1000,1000,1010,1010,fill=color_corp)## On crée le carré en dehors du Canvas pour ne pas l'afficher à l'écran
        snake.append(corps)## On accroche ensuite le nouveau carré
        ## Et hop le serpent se crée au fil du jeu
        pos_x.append (pos_x[n]+10+x)
        pos_y.append (pos_y[n]+10+y)     

        n=n+1
        
    if manger>=200:
        if coord_tete==coord_portail:
            pos_x[0]=x_tp1+10
            pos_y[0]=y_tp1+10
        if coord_tete==coord_portail3:
            pos_x[0]=x_tp+10
            pos_y[0]=y_tp+10
            
    while long!=len(snake):
        if pos_x[long]==pos_x[0] and pos_y[long]==pos_y[0]:## Si le serpent se rentre dedans, l'écran de fin s'affiche
            temps=1
            fin()
            pseudo1()
        long+=1
        

    if temps == 0:    
        can.after(delai,move) ## On relance la fonction avec un temps défini
    
#######################################################################
# Fonctions définissant le mouvement avec les touches -----------------
#######################################################################
def up(event):
    global direction
    if direction !=3:
        direction = 0
        
def right(event):
    global direction
    if direction !=2:
        direction = 1

def left(event):
    global direction
    if direction !=1:
        direction = 2

def down(event):
    global direction
    if direction !=0:
        direction = 3

#######################################################################
# Fonctions pour lancer une nouvelle partie ---------------------------
#######################################################################


def new_game():
    global snake,direction,tete_x,tete_y,tete_x2,tete_y2,pomme,coord_pomme, coord_tete, color_tete, color_corp
    global x_pomme,y_pomme,corps,pos_x,pos_y,x,y,long,n, temps, temps1, manger, Score, top

    score=0
    can.delete(ALL)

    if temps == 1:
        top.destroy()

    can.configure(bg="grey")

    
    changecolor()
    
    snake=[]
    
    tete=can.create_rectangle(100,100,110,110,fill=color_tete)
    corps=can.create_rectangle(90,100,100,110,fill=color_corp)
    
    snake.append(tete)
    snake.append(corps)

    pos_x=[]
    pos_y=[]

    pos_x.append (can.coords(tete)[0])
    pos_y.append (can.coords(tete)[1])
    pos_x.append (can.coords(corps)[2])
    pos_y.append (can.coords(corps)[3])
    
    can.create_rectangle(0,0,10,400,fill="black")
    can.create_rectangle(0,0,700,10,fill="black")
    can.create_rectangle(690,0,700,400,fill="black")
    can.create_rectangle(0,400,700,360,fill="black")

    long==0
    n=1
    manger = 0
    temps = 2
    temps1 = 1
    direction = 1
    delai=40

    Score.config(text="Score : " +str(manger))
    
    pose_pomme()
    
    if manger!=0:
        manger=0



#######################################################################
# Fonctions pour la Pause et la Fermeture -----------------------------
#######################################################################
def pause(event):
    global temps, pause, temps1, temps2
    temps = 1 ## Variable temps permettant de savoir quand le jeu est en cours ou quand celui-ci est en pause
    temps1 = 1
    if temps == 1:
        if temps2 == 1: ## Temps2 nous permet d'afficher qu'une fois le texte PAUSE
            pause=can.create_text(350,200,font=('Fixedsys',18),text="PAUSE", fill="RED") ## Voici l'affichage du texte PAUSE
            temps2 = 0

def play(event):
    global temps, pause, temps1, jouer, temps2
    temps=0
    if temps1 == 1: ## Nous permet de relancer le jeu en appuyant sur Espace si celui-ci était en pause
        if temps == 0:
            can.delete(pause)
            can.delete(jouer)
            temps1 = 0
            temps2 = 1
            move()

def quitter():
    Fenetre.destroy() ## Pour fermer le jeu

#######################################################################
# Fonctions pour enregistrer le score ---------------------------------
#######################################################################
def score_text():
    global temps, temps1, pause
    os.popen("scores_40.txt")
    temps1 = 1
    temps = 1
def score():
    global pseudo, temps, pause, temps1, manger, top
    score = open("scores_40.txt", "a")
    score.write("\nLe score de " + pseudo.get() +
                " est de " + str(manger))
    temps1 = 1
    temps = 1
    top.destroy()
def pseudo1():
    
    global pseudo, top
    top = Toplevel(Fenetre)
    top.resizable(width=False,height=False)
    Label_pseudo = Label(top, text='Votre Pseudo : ')
    Label_pseudo.pack(side=LEFT, padx=5, pady=5)

    pseudo=StringVar()
    pseudo.set('')
    pseudo = Entry(top, textvariable = pseudo)
    pseudo.insert(0, "Player 1")
    pseudo.focus_set()
    pseudo.pack(side = LEFT)

    
    Bouton_pseudo = Button(top, text='Valider', command=score)
    Bouton_pseudo.pack(side = LEFT)

#######################################################################
# Fonctions pour le Menu ----------------------------------------------
#######################################################################
def Docs():
    global temps, temps1, pause
    filewin = Toplevel(Fenetre) ## Nous permet d'afficher une nouvelle fenetre au dessus de la première
    Label4=Label(filewin,text="Snake 1 Joueur :\n\n -Pour le déplacement du serpent vous pouvez utiliser les touches ZQSD ou les flèches du clavier.\n" +
                 "-Vous pouvez mettre en pause le jeu avec la touche P et relancer le jeu avec la touche ESPACE.\n" +
                 "-Pour lancer une nouvelle partie vous avez la touche N ou le bouton Nouvelle Partie.\n\n" +
                 " Nous vous souhaitons bonne chance et bon jeu") ## Texte dans la fenetre
    Label4.place(x=10,y=10)
    filewin.geometry('500x150')
    filewin.resizable(width=False,height=False) ## On ne peut pas l'agrandir manuellement
    temps1 = 1 ## On met en pause le jeu quand on ouvre une fenetre
    temps = 1

def En_Savoir_Plus():
    global temps, temps1, pause
    filewin2 = Toplevel(Fenetre) ## Nous permet d'afficher une nouvelle fenetre au dessus de la première
    Label5=Label(filewin2,text="Jeu réalisé par Aloïs et Hugo pour notre projet en ISN 2015.\n\n Lycée du Forez\n\n" +
                " Contact : jununelol@gmail.com") ## Texte dans la fenetre
    Label5.place(x=10,y=10)
    filewin2.geometry('310x60')
    filewin2.resizable(width=False,height=False) ## On ne peut pas l'agrandir manuellement
    temps1 = 1 ## On met en pause le jeu quand on ouvre une fenetre
    temps = 1





'########################################################################'
'#----------------------------------------------------------------------#'
'#                          Fenêtre et menu                             #'
'#----------------------------------------------------------------------#'
'########################################################################'

#######################################################################
# Création de la Fenetre avec le Canvas -------------------------------
#######################################################################
Fenetre = Tk()
menubar = Menu(Fenetre)
Fenetre.title("Best Snake") ## Titre de la fenetre
Fenetre.resizable(width=False,height=False) ## On ne peut pas agrandir la fenetre manuellement
can=Canvas(Fenetre, width=700, height=400, bg="grey") ## Couleur du fond
can.pack()

can.create_rectangle(0,0,10,400,fill="black") ## Ici les bordures avec leurs coordonnées
can.create_rectangle(0,0,700,10,fill="black")
can.create_rectangle(690,0,700,400,fill="black")
can.create_rectangle(0,400,700,360,fill="black")

Bouton_new=Button(Fenetre, text="Nouvelle Partie", command=new_game) ## Les boutons situés en bas de la fenetre
Bouton_new.place(x=20, y=365, width=100, height=30)

Bouton_quit=Button(Fenetre, text="Quitter", command=quitter)
Bouton_quit.place(x=150, y=365, width=100, height=30)

Bouton_score=Button(Fenetre, text="Scores", command=score_text)
Bouton_score.place(x=620, y=365, width=70, height=30)

space = Label(can, font=('Fixedsys',10), text="-Espace pour commencer !", fg='red', bg='black')
space.place(x=280, y=360)

label_pause = Label(can, font=('Fixedsys',10), text="-P pour pause !", fg='red', bg='black')
label_pause.place(x=280, y=380)
#######################################################################
# Création d'un Menu --------------------------------------------------
#######################################################################
fichier_menu = Menu(menubar)
fichier_menu.add_command(label="Nouvelle Partie", command=new_game)
fichier_menu.add_command(label="Quitter", command=quitter)

menubar.add_cascade(label="Fichier", menu=fichier_menu)

aide_menu = Menu(menubar)
aide_menu.add_command(label="Docs", command=Docs)
aide_menu.add_command(label="En savoir plus", command=En_Savoir_Plus)

menubar.add_cascade(label="Aide", menu=aide_menu)

score_menu = Menu(menubar)
score_menu.add_command(label="Scores", command=score_text)

menubar.add_cascade(label="Score", menu=score_menu)

Fenetre.config(menu=menubar)


'########################################################################'
'#----------------------------------------------------------------------#'
'#                                Variables                             #'
'#----------------------------------------------------------------------#'
'########################################################################'
#######################################################################
# Liste pour le serpent qui va s'agrandir -----------------------------
#######################################################################
snake=[]

#######################################################################
# Direction du serpent au début (Droite) ------------------------------
#######################################################################
direction=1

#######################################################################
# Première pomme pour le jeu ------------------------------------------
#######################################################################
pose_pomme()
changecolor()

#######################################################################
# Création du serpent -------------------------------------------------
#######################################################################
tete=can.create_rectangle(100,100,110,110,fill=color_tete) ## On crée la tête au début avec des coordonnées précis
corps=can.create_rectangle(90,100,100,110,fill=color_corp) ## On crée le corp au début avec des coordonnées précis

snake.append(tete) ## On met les parties du serpent dans la liste Snake
snake.append(corps)

pos_x=[] ## Position de X et de Y
pos_y=[]

pos_x.append (can.coords(tete)[0])
pos_y.append (can.coords(tete)[1])
pos_x.append (can.coords(corps)[2])
pos_y.append (can.coords(corps)[3])

#######################################################################
# Définition des variables --------------------------------------------
#######################################################################
long=0
n=1
manger = 0

temps = 2
temps1 = 1
temps2 = 0

delai = 40 ## Delai == vitesse du Serpent

Score = Label(can, font=('Fixedsys',10), text="Score : " + str(manger), fg='red', bg='black') ## Affichage du Score
Score.place(x=500, y=365)
#######################################################################
# Lancement de l'animation --------------------------------------------
#######################################################################
move()
music()

#######################################################################
# Assignation des touches aux fonctions -------------------------------
#######################################################################
Fenetre.bind('<Up>', up)
Fenetre.bind('<Right>', right)
Fenetre.bind('<Left>', left)
Fenetre.bind('<Down>', down)

Fenetre.bind('<KeyPress-z>', up)
Fenetre.bind('<KeyPress-d>', right)
Fenetre.bind('<KeyPress-q>', left)
Fenetre.bind('<KeyPress-s>', down)
Fenetre.bind('<KeyPress-p>', pause)
Fenetre.bind('<space>', play)

Fenetre.bind('<KeyPress-Z>', up)
Fenetre.bind('<KeyPress-D>', right)
Fenetre.bind('<KeyPress-Q>', left)
Fenetre.bind('<KeyPress-S>', down)
Fenetre.bind('<KeyPress-P>', pause)

Fenetre.bind('<KeyPress-n>', lambda event : new_game()) ## Permet de mettre la fonction new_game en mode event quand on appuye sur N
Fenetre.bind('<KeyPress-N>', lambda event : new_game())

Fenetre.mainloop()
