# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 22:22:39 2024

@author: Victus
"""

            #Amaliyot number= 3
    # !- masala
ismlar= ["Soatbek", "Jo\'rabek", "Humoyun"]
     # 2- masala
print(ismlar[0].title(), "ishlaring o\'qishlaring yaxshi bo\'lyaptimi ?")
print(ismlar[1].capitalize(), 'and' , ismlar[2].lower(), 'qadirdon do\'stlardan !')
print(ismlar[2], "juda tirishqoq va mehnatni qadirlatdigan insonlar sirasiga kiradi !")


     # 3- masala 
sonlar= [43, 25, -24, 61, 0.5, -61]
print(sonlar[2] + sonlar[1])
print(sonlar[5] * sonlar[0])
sonlar[3]= 0.005
print(sonlar[0]% sonlar[4]*5)
print(sonlar)
sonlar.append(21)
print(sonlar)
sonlar.insert(0, 0)
del sonlar[5]
del sonlar[6]
print(sonlar)
sonlar.remove(-61)
sonlar.remove(-24)
print(sonlar)

     # 4- masala 
t_shaxslar = ['Ibn Sino', 'Al Xorazmiy' , 'Imom Buxoriy', 'At Termiziy']
z_shaxslar = ['mark zucherberk' , 'Iion Mask' , ' Dr.Danish', 'alisher aka']
shaxs = t_shaxslar.pop(1)
print('men tarixiy shaxslar haqida gapirganimda birinchi navbatda ', shaxs,'\n'
      'zamonaviy shaxslardan esa ' , z_shaxslar.pop(0),'\n'
      'takidlab o\'taman')


      # 5- masala 
friends= []
friends.append('Layloxon')
friends.append('Shahloxon')
friends.append('Zulfizarxon')
friends.insert(3, 'Dilro\'zaxon')
print(friends)
friends.remove('Layloxon')

print(friends)
friends.insert(0, 'Shezodbek')
friends.insert(2, 'Oybekjon')
friends.insert(4, 'Shag\'zodbek')
print(friends)

guest= []
guest.append(friends.pop(0))
guest.append(friends.pop(3))
print(guest)
