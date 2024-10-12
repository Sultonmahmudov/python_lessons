# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 14:16:55 2024

@author: Victus
"""

#Foydalanuvchudan juf son kiritishini so'rang. Agar foydalanuvchi juft son kiritsa, "rahmat", Agar foydalanuvuvchi toq son kiritsa"Bu son juft emas" Degan xabar bering.

#number = float(input("Musbat son kiriting :"))
#if number > 0:
 #   print("Rahmat")
#elif number == 0:
 #   print(f"{number} , musbat ham manfiy ham emas !")
#elif number < 0:
 #   print("Musbat son kiriting !")
#else:
 #   print("Error !")


#Foydalanuvchi yoshini so'rang va muzeyga kirish uchun chipta narxini quyidagicha chiqaring.
#age = int(input("Marhamat, Foydananuvchi yoshinggizni kiriting :"))
#if (age < 4 or age > 60):
#    print("Hurmatli mijoz bizning hizmatimizdan foydalanish siz uchun bepul , Rahmat !")
#elif age < 18:
#    print("10 000 so'm to'lo'v qiling hurmatli mijoz !")
#elif age >= 18 :
#    print("20 000 so'm to'lo'v qiling hurmatli mijoz !")
#else :
 #   print("Eror !")



#Foydalanuvchidan uchta son kiritishni so'rang va ularning katta kichikligi haqida malunot bering.
#n1 = float(input("Birinchi raqamni kiriting :>>>"))
#n2 = float(input("ikkinchi raqamni kiriting :>>>"))
#n3 = float(input("Uchinchi sonni kiriting :>>>"))

#if n1 > n2 and n1>n3:
 #   print(f"The biggest numner is {n1} ")
#elif n1<n2 and n2>n3:
 #   print(f"The giggest number is {n2}")
#elif n1<n3 and n2<n3:
 #   print(f"The biggest number is {n3}")
#elif n1==n2==n3:
 #   print("All number is equal !")
#else:
 #   print("Error!")
    


products = ['ruchka', 'daftar', 'o\'chirg\'ich', 'chizg\'ich', 'qalam', 'jazval', 'kitob', 'jild', 'komiks']
#basket= []
#for n in range(5):
 #   basket.append(input(f"{n+1} - mahsulotni kiriting : "))
  #  print(basket)
    
#for product in basket:
 #   if product.lower() in products:
  #      print(f"Bu {product} bizning magazinimizda bor")
   # else:
    #    print(f"{product} mahsuloti bizning magazinimizda yo'q")
           

items =[]
for n in range(5):
    items.append(input(f"{n+1} -  mahsulotini kirgizing :"))
    print(items)
bor_mahsulotlar=[]
mavjud_emas =[]    
if products:
    for product in items:
        if product in products:
            bor_mahsulotlar.append(product)
            print("bor")
            print(bor_mahsulotlar)
        else :
            print("mavjud emas")
            print(mavjud_emas)
            mavjud_emas.append(product)
            
            
        
else:
    print("Savatcha bo'm bo'sh")




