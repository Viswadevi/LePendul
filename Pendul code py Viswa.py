# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 14:59:47 2023

@author: ViswadeviNARAYANASSA
"""


import random
bibliothèque = ["pomme", "betterave","carotte"]
mot_a_deviner = random.choice(bibliothèque)
mot_cache = "-" * len(mot_a_deviner)
print(mot_cache)


nb_erreurs = 11
lettres_proposees = []

while nb_erreurs > 0 and "-" in mot_cache:
    lettre = input("Proposez une lettre : ")
    
    if lettre in lettres_proposees:
        print("Vous avez déjà proposé cette lettre.")
        continue
        
    lettres_proposees.append(lettre)
    
   
    if lettre in mot_a_deviner:
       
        for i in range(len(mot_a_deviner)):
            if mot_a_deviner[i] == lettre:
                mot_cache = mot_cache[:i] + lettre + mot_cache[i+1:]
        print(mot_cache)
    else:
        nb_erreurs -= 1
        print("La lettre", lettre," n'est pas dans le mot. Il vous reste", nb_erreurs,"essais.")
        

if "-" not in mot_cache:
    print("Vous avez gagné !")
else:
    print("Vous avez perdu... Le mot était:" ,mot_a_deviner)