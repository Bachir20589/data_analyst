con=open("jour5.txt","rt")
print(con.read())

f=open("jour5.txt","at")
f.write("how are you")

conp=open("jour5.txt","rt")
print(conp.read())

with open("jour5.txt", "rt") as fichier:
    ligne1 = fichier.readline()
    print(ligne1)   
    ligne2 = fichier.readline()
    print(ligne2) 
    ligne3=fichier.readline()
    print(ligne3)  


import os
if os.path.exists("jour5.txt"):
    os.remove("jour5.txt")
else:
    print("le fichier existait\n")

# with open("jour5.txt", "rt") as fichier:
#     contenu = fichier.read()
#     print(contenu)