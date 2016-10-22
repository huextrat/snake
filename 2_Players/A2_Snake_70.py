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

###############################################################################################################
def fin():
    can.delete(ALL)
    if manger>manger1:
        end=can.create_text(250,160,font=('Fixedsys',18),text="GAGNANT \nAvec un score de " +str(manger), fill="RED")
        end=can.create_text(950,160,font=('Fixedsys',18),text="PERDANT \nAvec un score de " +str(manger1), fill="RED")
    if manger<manger1:
        end1=can.create_text(250,160,font=('Fixedsys',18),text="PERDANT \nAvec un score de " +str(manger), fill="RED")
        end1=can.create_text(950,160,font=('Fixedsys',18),text="GAGNANT \nAvec un score de " +str(manger1), fill="RED")
    if manger==manger1:
        end2=can.create_text(650,160,font=('Fixedsys',18),text="EGALITE \nAvec un score de " +str(manger), fill="RED")

def changecolor():
    global color_tete, color_corp
    couleur_tete = ['purple','cyan','maroon','green','red','blue','orange', 'yellow']
    color_t = randrange(8)
    color_tete = couleur_tete[color_t]
    couleur_corp = ['purple', 'pink', 'cyan','maroon','green','red','blue','orange', 'yellow']
    color_c = randrange(9)
    color_corp = couleur_corp[color_c]

def changecolor1():
    global color_tete1, color_corp1
    couleur_tete1 = ['purple','cyan','maroon','green','red','blue','orange', 'yellow']
    color_t1 = randrange(8)
    color_tete1 = couleur_tete1[color_t1]
    couleur_corp1 = ['purple', 'pink', 'cyan','maroon','green','red','blue','orange', 'yellow']
    color_c1 = randrange(9)
    color_corp1 = couleur_corp1[color_c1]

###############################################################################################################
def music():
    pygame.mixer.init()
    son = pygame.mixer.Sound('music.ogg')
    son.play(loops=-1, maxtime=0, fade_ms=0)
    
###############################################################################################################

def pose_pomme():
    global coord_pomme,x_pomme,y_pomme,pomme
    x_pomme=randrange(10,610,10)
    y_pomme=randrange(10,440,10)
    pomme=can.create_oval(x_pomme,y_pomme,x_pomme+10,y_pomme+10,fill="Orange")
    coord_pomme=(x_pomme,y_pomme)

def pose_pomme1():
    global coord_pomme1,x_pomme1,y_pomme1,pomme1
    x_pomme1=randrange(630,1250,10)
    y_pomme1=randrange(10,440,10)
    pomme1=can.create_oval(x_pomme1,y_pomme1,x_pomme1+10,y_pomme1+10,fill="Orange")
    coord_pomme1=(x_pomme1,y_pomme1)

###############################################################################################################

#######################################################################
# Fonction principale du jeu ------------------------------------------
#######################################################################
def move():
    global snake,direction,tete_x,tete_y,tete_x2,tete_y2,pomme,coord_pomme, color_tete, color_corp # 2 Lignes de Global
    global x_pomme,y_pomme,corps,pos_x,pos_y,x,y,long,n,manger,delai, delai1, acceleration, acceleration1, Score, jouer, play            

    if temps == 2:
        jouer=can.create_text(630,200,font=('Fixedsys',30),text="Espace pour commencer !", fill="RED")

#######################################################################
# Boucles permettant le déplacement du serpent
    # Mouvement à gauche
    if direction==2:
        x=-10
        y=0

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
    long=len(snake) # <--------- Longeur du Serpent
    long=long-1 ## Dans une liste on part de 0 et la longueur donne le nombre d'éléments
                ## Il faut donc enlever 1
    
    #######################################################################
    # Boucles permettant au serpent de grandir
    while long !=0: 

        pos_x[long]=pos_x[long-1]
        pos_y[long]=pos_y[long-1]
        long+=-1
    
    pos_x[0]+=x
    pos_y[0]+=y
    long=0
    
    while long!=len(snake):
        can.coords(snake[long],pos_x[long],pos_y[long],pos_x[long]+10,pos_y[long]+10)
        long+=1
    long=1

    coord_tete=pos_x[long],pos_y[long]
    
    if pos_y[long] > 440 or pos_y[long] < 10:
        fin()
    if pos_x[long] == 620 or pos_x[long] == 0:
        fin()

   
    #######################################################################
    # Boucles pour la rencontre entre la tete et la pomme
    
    if coord_tete==coord_pomme:
        can.delete(pomme)
        pose_pomme()
        
        if pos_x[0]==x_pomme and pos_y[0]==y_pomme:
            can.delete(pomme)
            pose_pomme()
        if pos_x[long]==x_pomme and pos_y[long]==y_pomme:
            can.delete(pomme)
            pose_pomme()
            
        manger+=10
        Score.config(text="Score : "+str(manger))
        
        if manger == 100:
            delai1 -= 5
            acceleration=can.create_text(310,440,font=('Fixedsys',16),text="Accélération du serpent adverse !!", fill="RED")
        if manger == 200:
            delai1 -= 5
            acceleration1=can.create_text(310,440,font=('Fixedsys',16),text="Bravo, votre adversaire va voir son serpent accélérer !!", fill="RED")

        
        
        
        corps=can.create_rectangle(1000,1000,1010,1010,fill=color_corp)# <-- On crée le carré en dehors du Canvas
        snake.append(corps)# <---------- On accroche ensuite le nouveau carré

        pos_x.append (pos_x[n]+10+x)
        pos_y.append (pos_y[n]+10+y)     

        n=n+1
        
    while long!=len(snake):
        if pos_x[long]==pos_x[0] and pos_y[long]==pos_y[0]:
            fin()
        long+=1
        
    if manger > 100:
        can.delete(acceleration)
    if manger > 200:
        can.delete(acceleration1)   

    if temps == 0: 
        can.after(delai,move)

########## ############ ############## ############# ########## ############# ############## ############### #############
def move1():
    global snake1,direction1,tete_x1,tete_y1,tete_x4,tete_y4,pomme1,coord_pomme1, color_tete1, color_corp1 # 2 Lignes de Global
    global x_pomme1,y_pomme1,corps1,pos_x1,pos_y1,x1,y1,long_1,n1,manger1, delai1, delai, acceleration2, acceleration3, Score1, jouer, play            

#######################################################################
# Boucles permettant le déplacement du serpent
    # Mouvement à gauche
    if direction1==2:
        x1=-10
        y1=0

    # Mouvement à droite
    elif direction1==1:
        x1=10
        y1=0

    # Mouvement en bas      
    elif direction1==0:
        y1=-10
        x1=0
        
    # Mouvement en haut     
    elif direction1==3:
        y1=10
        x1=0

    long_1=len(snake1) # <--------- Longeur du Serpent
    long_1=long_1-1 ## Dans une liste on part de 0 et la longueur donne le nombre d'éléments
                ## Il faut donc enlever 1
    
    #######################################################################
    # Boucles permettant au serpent de grandir
    
    while long_1 != 0: 

        pos_x1[long_1]=pos_x1[long_1-1]
        pos_y1[long_1]=pos_y1[long_1-1]
        long_1+=-1
    
    pos_x1[0]+=x1
    pos_y1[0]+=y1
    long_1=0
    
    while long_1!=len(snake1):
        can.coords(snake1[long_1],pos_x1[long_1],pos_y1[long_1],pos_x1[long_1]+10,pos_y1[long_1]+10)
        long_1+=1
    long_1=1

    coord_tete1=pos_x1[long_1],pos_y1[long_1]
    
    if pos_y1[long_1] > 440 or pos_y1[long_1] < 10:
        fin()

    if pos_x1[long_1] > 1240 or pos_x1[long_1] < 630:
        fin()


    #######################################################################
    # Boucles pour la rencontre entre la tete et la pomme
    
    if coord_tete1==coord_pomme1:
        can.delete(pomme1)
        pose_pomme1()
        
        if pos_x1[0]==x_pomme1 and pos_y1[0]==y_pomme1:
            can.delete(pomme1)
            pose_pomme1()
        if pos_x1[long_1]==x_pomme1 and pos_y1[long_1]==y_pomme1:
            can.delete(pomme1)
            pose_pomme1()
            
        manger1+=10
        Score1.config(text="Score : "+str(manger1))
        
        if manger1 == 100:
            delai -= 5
            acceleration2=can.create_text(930,440,font=('Fixedsys',16),text="Accélération du serpent adverse !!", fill="RED")
        if manger1 == 200:
            delai -= 5
            acceleration3=can.create_text(930,440,font=('Fixedsys',16),text="Bravo, votre adversaire va voir son serpent accélérer !!", fill="RED")
            
        
        
        
        corps1=can.create_rectangle(1000,1000,1010,1010,fill=color_corp1)# <-- On crée le carré en dehors du Canvas
        snake1.append(corps1)# <---------- On accroche ensuite le nouveau carré

        pos_x1.append (pos_x1[n1]+10+x1)
        pos_y1.append (pos_y1[n1]+10+y1)     

        n1=n1+1
        
    while long_1!=len(snake1):
        if pos_x1[long_1]==pos_x1[0] and pos_y1[long_1]==pos_y1[0]:
            fin()
           
        long_1+=1
        
    if manger1 > 100:
        can.delete(acceleration2)
    if manger1 > 200:
        can.delete(acceleration3)


    if temps == 0: 
        can.after(delai1,move1)

        
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


        
def up1(event):
    global direction1
    if direction1 !=3:
        direction1 = 0
        
def right1(event):
    global direction1
    if direction1 !=2:
        direction1 = 1

def left1(event):
    global direction1
    if direction1 !=1:
        direction1 = 2

def down1(event):
    global direction1
    if direction1 !=0:
        direction1 = 3

#######################################################################
# Fonctions pour lancer une nouvelle partie ---------------------------
#######################################################################

def new_game():
    global snake,direction,pomme,coord_pomme, coord_tete, color_tete, color_corp, snake1,direction1,pomme1,coord_pomme1, color_tete1, color_corp1
    global x_pomme,y_pomme,corps,pos_x,pos_y,x,y,long,n, temps, temps1, manger, Score, x_pomme1,y_pomme1,corps1,pos_x1,pos_y1,x1,y1,long_1,n1,manger1, temps, temps1, delai, delai1, acceleration, acceleration1, Score, jouer, play

    score=0
    score1=0
    
    can.delete(ALL)

    can.configure(bg="grey")
    
    changecolor()
    changecolor1()
    
    snake=[]
    snake1=[]
    
    tete=can.create_rectangle(80,80,90,90,fill=color_tete)
    corps=can.create_rectangle(70,80,80,90,fill=color_corp)

    tete1=can.create_rectangle(700,80,710,90,fill=color_tete1)
    corps1=can.create_rectangle(690,80,700,90,fill=color_corp1)
    
    snake.append(tete)
    snake.append(corps)

    snake1.append(tete1)
    snake1.append(corps1)

    pos_x=[]
    pos_y=[]

    pos_x1=[]
    pos_y1=[]

    pos_x.append (can.coords(tete)[0])
    pos_y.append (can.coords(tete)[1])
    pos_x.append (can.coords(corps)[2])
    pos_y.append (can.coords(corps)[3])

    pos_x1.append (can.coords(tete1)[0])
    pos_y1.append (can.coords(tete1)[1])
    pos_x1.append (can.coords(corps1)[2])
    pos_y1.append (can.coords(corps1)[3])
    
    can.create_rectangle(0,0,10,500,fill="black")
    can.create_rectangle(0,0,1260,10,fill="black")
    can.create_rectangle(620,0,630,500,fill="black")
    can.create_rectangle(0,450,1260,500,fill="black")
    can.create_rectangle(1250,0,1260,500,fill="black")

    long==0
    n=1
    manger = 0
    temps = 2
    temps1 = 1
    temps2 = 0
    
    direction = 1
    delai=70

    long_1==0
    n1=1
    manger1 = 0
    direction1 = 1
    delai1=70
    
    Score.config(text="Score : " +str(manger))
    Score1.config(text="Score : " +str(manger1))
    
    pose_pomme()
    pose_pomme1()
    
    if manger!=0:
        manger=0

    if manger1!=0:
        manger1=0

    
#######################################################################
# Fonctions pour la Pause et la Fermeture -----------------------------
#######################################################################
def pause(event):
    global temps, pause, temps1, temps2
    temps = 1
    temps1 = 1
    if temps == 1:
        if temps2 == 1:
            pause=can.create_text(630,250,font=('Fixedsys',50),text="PAUSE", fill="RED")
            temps2 = 0
            
def play(event):
    global temps, pause, temps1, jouer, temps2
    temps=0
    if temps1 == 1:
        if temps == 0:
            can.delete(pause)
            can.delete(jouer)
            temps1 = 0
            temps2 = 1
            move()
            move1()

def quitter():
    Fenetre.destroy()



#######################################################################
# Création de la Fenetre avec le Canvas -------------------------------
#######################################################################
Fenetre = Tk()
menubar = Menu(Fenetre)
Fenetre.title("Best Snake")
Fenetre.resizable(width=False,height=False)
can=Canvas(Fenetre, width=1260, height=500, bg="grey")
can.pack()

can.create_rectangle(0,0,10,500,fill="black")
can.create_rectangle(0,0,1260,10,fill="black")
can.create_rectangle(620,0,630,500,fill="black")
can.create_rectangle(0,450,1260,500,fill="black")
can.create_rectangle(1250,0,1260,500,fill="black")

Bouton_new=Button(Fenetre, text="Nouvelle Partie", command=new_game)
Bouton_new.place(x=20, y=465, width=100, height=30)

Bouton_quit=Button(Fenetre, text="Quitter", command=quitter)
Bouton_quit.place(x=150, y=465, width=100, height=30)

space = Label(can, font=('Fixedsys',15), text="-Espace pour commencer !", fg='red', bg='black')
space.place(x=600, y=455)

label_pause = Label(can, font=('Fixedsys',10), text="-P pour pause !", fg='red', bg='black')
label_pause.place(x=600, y=475)
#######################################################################
# Création d'un Menu --------------------------------------------------
#######################################################################
fichier_menu = Menu(menubar)
fichier_menu.add_command(label="Nouvelle Partie", command=new_game)
fichier_menu.add_command(label="Quitter", command=quitter)

menubar.add_cascade(label="Fichier", menu=fichier_menu)



Fenetre.config(menu=menubar)

########################################################################
#----------------------------------------------------------------------#
#                                Variables                             #
#----------------------------------------------------------------------#
########################################################################

#######################################################################
# Ce que devient le serpent -------------------------------------------
#######################################################################
snake=[]
snake1=[]
#######################################################################
# Direction du serpent au début ( Droite ) ----------------------------
#######################################################################
direction=1
direction1=1
#######################################################################
# Première pomme pour le jardin d'Éden --------------------------------
#######################################################################
pose_pomme()
changecolor()
pose_pomme1()
changecolor1()
#######################################################################
# Création du serpent -------------------------------------------------
#######################################################################
tete=can.create_rectangle(80,100,90,110,fill=color_tete)
corps=can.create_rectangle(70,100,80,110,fill=color_corp)


# Problème ICI ################################################################################

tete1=can.create_rectangle(700,100,710,110,fill=color_tete1)
corps1=can.create_rectangle(70,200,80,210,fill=color_corp1)

################################################
snake.append(tete)
snake.append(corps)

snake1.append(tete1)
snake1.append(corps1)

pos_x=[]
pos_y=[]

pos_x1=[]
pos_y1=[]

pos_x.append (can.coords(tete)[0])
pos_y.append (can.coords(tete)[1])
pos_x.append (can.coords(corps)[2])
pos_y.append (can.coords(corps)[3])

pos_x1.append (can.coords(tete1)[0])
pos_y1.append (can.coords(tete1)[1])
pos_x1.append (can.coords(corps1)[2])
pos_y1.append (can.coords(corps1)[3])
#######################################################################
# Définition des variables --------------------------------------------
#######################################################################
long=0
n=1
manger = 0

long_1=0
n1=1
manger1 = 0

temps = 2
temps1 = 1
temps2 = 0

delai = 70
delai1 = 70

Score = Label(can, font=('Fixedsys',10), text="Score : " + str(manger), fg='red', bg='black')
Score.place(x=300, y=465)

Score1 = Label(can, font=('Fixedsys',10), text="Score : " + str(manger1), fg='red', bg='black')
Score1.place(x=1000, y=465)
#######################################################################
# Lancement de l'animation --------------------------------------------
#######################################################################
move()
move1()
music()
#######################################################################
# Assignation des touches aux fonctions -------------------------------
#######################################################################
Fenetre.bind('<Up>', up1)
Fenetre.bind('<Right>', right1)
Fenetre.bind('<Left>', left1)
Fenetre.bind('<Down>', down1)

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

Fenetre.bind('<KeyPress-n>', lambda event : new_game())
Fenetre.bind('<KeyPress-N>', lambda event : new_game())

Fenetre.mainloop()

