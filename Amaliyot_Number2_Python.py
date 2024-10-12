# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 18:45:07 2024

@author: Victus
"""

         # Amaliyot number = 2 
ism = "Sardor"       
kocha = "Bog'bon"
mahalla = "Gulobod"
tuman = "Bodomzor"
viloyat = "Samarqand"


        # birinchi masala
print(kocha, "ko\'chasi", mahalla, "mahallasi", tuman, "tumaani", viloyat, "viloyati")


  #ikkinchi masala 
  
      # fydalanuvchidan so'rash yani input()
kocha = input(" Ko\'changning nomi nima ? :")
print(kocha , " ko'chasiga xush kelibsan!")
mahalla = input("Qaysi mahalla ? :")
print("Mening mahallamning nomi ham " + mahalla)
tuman = input("Qaysi tumandansan ? :")
print("Eng yaxshi tumandan ekansanu a "+ ism)
print(f"{kocha.title()} ko\'chasi , {mahalla.capitalize()}, mahallasi , {tuman.upper()}, tumani , {viloyat.lower()} viloyatdan {ism.title()}")


