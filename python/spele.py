from random import randint

secret = randint(0, 100)
minejums = -1 #kaut kas tāds, kas nav iespejams kā secret


while minejums != secret:
    minejums = int(input("Ludzu miniet skaitli: "))

    if secret > minejums:
        print("Istais skaitlis ir lielaks")
    elif secret < minejums:
        print("Istais skaitlis ir mazaks")
    else:
        print("Apsveicu, skaitlis ir pareizs!")



