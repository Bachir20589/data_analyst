import csv
with open("etudiant.csv","rt") as f:
    l=csv.DictReader(f)
    for li in l:
        print(li)
dict={"nom":"Modou","age":20}
print(dict)