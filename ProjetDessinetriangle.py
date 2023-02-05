# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 20:57:38 2021

@author: MONSEF
"""

from turtle import *
import random




def trapez(a):
    """Cette fronction prend en argument un entier a et dessine un trapez en fonction de a.
    La tortue à la fin est à la position de départ dans la même orientation.
                                     longeur a                                                    
          ____________________________________________________                                                                             
         /                                                    \
        /                                                      \                     
       /                                                        \     
      /                                                          \
    >/____________________________________________________________\
    """
    #couleur donne 3 nombres au hasard entre 0 et 1  qu'on va utiliser pour définir nos couleurs.
    couleur = (random.random(),random.random(),random.random())
    #la couleur est totalement au hasard grâce à couleur
    fillcolor(couleur)
    #on commence le remplissage du trapèze par la couleur
    begin_fill()
    #dessin du trapèze
    forward(a*2)
    left(120)
    forward(a)
    left(60)
    forward(a)
    left(60)
    forward(a)
    left(120)
    #Fin du remplissage.
    end_fill()
    
    



    
def dessine_solution(n):
    """dessine_solution est une fonction récrusive qui prendre un argument n et 
    qui trouve une solution pour dessiner un grand triangle en fonction de n
    On découpe le triangle en 4 petits triangles et la fonction nous propose une solution à chacun de ces triangles en
    supposant qu'elle sait tracer cette solution pour n-1 (Il y a donc 4 appels récursifs)
    Notre stratégie est de revenir au point de départ après chaque appel récrusif pour se replacer au bon endroit
    et au bon angle plus facilement."""
    #on sauvegarde les coordonnées de la tortue. Cela nous servira à revenir au point de départ après chaque appel récursif.
    x,y = pos()
    #On sauvegarde pour la même raison l'orientation de la tortue au départ.
    p = heading()
    #a est par convention la longeur d'un côté du petit triangle de base.
    a=20
    #Cas de base: Celui-ci va nous dessiner un petit trapèze à l'endroit voulu.
    # On aura aura implicitement le "petit triangle noir(de base)" + le trapèze
    if n == 1:
        up()
        forward(a*2)
        left(120)
        down()
        #appel de la fonction trapèze afin qu'elle dessine un trapèz en fonction de notre a (variable définie plus haut.)
        trapez(a)
        up()
        #on lève le turtle et on retourne au point de départ grâce à nos sauvegardes plus haut.
        goto(x,y)
        seth(p)
        
    else:
        #cas récursif : on découpe notre triangle en 4 petits triangles de côté 2**(n-1)
        #triangle Triforce ;) 
        
        #premier appel recursif sur n-1.
        # on rappel la fonction sur n-1 , la solution du premier petit triange va être dessiner
        dessine_solution(n-1)
        #A la fin du premier appel recursif, la tortue est placé au point de départ.
        #Il suffit alors de lever la tortue pour se placer au bon endroit pour le deuxième appel recursif.
        up()
        #On avance de a*(2**(n-1)) , soit la longueur du côte de notre premier triangle
        forward(a*(2**(n-1)))
        #On tourne d'un angle de 60 degré 
        left(60)
        #On avance de a*(2**(n-1)) , soit la longueur du côte de notre premier triangle multiplié par la longeur d'un trapèze
        forward(a*(2**(n-1)))
        #la tortue tourne d'un angle de 60 degré afin de dessiner dans la bonne position la solution du prochain triangle.
        left(60)
        down()
        #Deuxième appel récursif dessinant la solution sur n-1 pour le deuxième petit triangle.
        dessine_solution(n-1)
        
        #retour au point de départ pour dessiner la solution du troisième petit triangle
        up()
        goto(x,y)
        seth(p)
        #même principe que pour l'appel récursif précédent
        forward(a*(2**(n-1)))
        left(60)
        forward(a*(2**(n-1)))
        #on tourne cette fois-ci d'un angle de 120 degré afin de ne pas repasser sur le même petit triangle
        left(120)
        down()
        #On pose le turtle , on rappel la fonction sur n-1 afin de dessiner la solution du troisième petit triangle
        #(celui du "milieu" dans le grand triange)
        dessine_solution(n-1)
        
        #Le turtle se lève et retourne au point de départ.
        up()
        goto(x,y)
        seth(p)
        #même principe que pour les appels récursifs précédent.
        forward(a*(2**(n-1)))
        left(60)
        forward(a*(2**(n-1)))
        #cette fois-ci on fait un demi-tour afin que la tortue dessine correctement la solution.
        right(180)
        #On pose la tortue afin de déssiner la solution sur n-1
        down()
        #on rappel la fonction pour que la tortue dessine la solution sur n-1 (magie de la récrusivité)
        dessine_solution(n-1)
        
        #On retourne au point de départ et on va constater quelque chose
        up()
        goto(x,y)
        seth(p)
        #On constate que nos 4 triangles ont chacun un petit trou manquant
        #Ce petit trou manquant forme la forme d'un trapèze.
        #Il faut donc dessiner un trepèze au bon endroit.
        #Logiquement, cette emplacement est le même que celui où on se déplace pour nos appels récursifs
        #Mais on va y accéder d'un manière différente pour nous faciliter la tâche.
        
        forward(a*(2**(n-1)))
        forward(a*(2**(n-1)))
        left(120)
        #la tortue avance en fonction de la longeur du petit triangle.
        #Cepandant , on va soutraire a car a est justement la longeur du trapez
        #à placer à cette endroit. Si on ne soustrait pas a , le trapèze va 
        # finir par en écraser un autre.
        forward(a*(2**(n-1))-a)
        down()
        #petit trapèze manquant afin de "fermer la solution".Appel de la fonction trapèze bien sûr...
        trapez(a)
        #retour au point de départ selon notre stratégie initiale.
        up()
        goto(x,y)
        seth(p)

dessine_solution(3)
speed(0)