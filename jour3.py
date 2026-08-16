a=int(input("donner un entier\n"))
if a>0:
    print("j'ai " + str(a) + " ans ")
else:
    print("a est negatif")    

for i in range(6):
    print(i)
    if i==4:
        break

for i in range(6):
    if i==4:
        continue
    print(i)