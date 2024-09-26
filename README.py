from random import *

lm_inf=int(input("limite infÃ©rieur ?"))
lm_supp=(int(input("limite suppÃ©rieur ?")))
nb_essaie_max=int(input("essaie max ?"))
nb_essaie=0
a=randrange(lm_inf,lm_supp+1)
historique=[]

jeu = True

while jeu :
    b=int(input("nb= ?"))
    nb_essaie =nb_essaie+1
    historique.append(b)
    
    difference=abs(b-a)

    if difference<=0.1*lm_supp:
        print("trÃ©s proche")
    elif difference<=0.30*lm_supp:
        print("proche")
    else:
        print("loin")
    
    if nb_essaie==nb_essaie_max:
        print(f"c'est perdu ! le nombre Ã©tait {a}")
        jeu = False
    
    elif a == b:
        print("c'est gagnÃ© !")
        jeu = False
    
    elif b<a:
        print("plus grand")
        
    elif b>a:
       print("plus petit")
    
   
print(nb_essaie,"try",historique)
