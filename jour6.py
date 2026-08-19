con=open("jour6.pdf","ab")
texte="salut, comment cv. Je vais bien  ALLKHAMDOULILLAH"
con.write(texte.encode())
f=open("jour6.pdf","rb")
file=f.read()
print(file)

# with open("jour6.pdf","rb") as f:
#     p=f.read()
#     print(p)

import os
if os.path.exists("jour5.txt"):
    os.remove("jour5.txt")
else:
    print("le fichier n'est pas")