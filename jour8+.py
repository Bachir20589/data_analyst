import csv

with open("etudiant.csv","rt") as a:
    f=csv.DictReader(a)
    for i in f:
        print(i["nom"])