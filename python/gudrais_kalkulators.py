print("Gudrais kalkulators")

darbiba = input("Lūdzu ievadiet vēlamo darbību(+ - * /): ")
a = int(input("Lūdzu ievadiet pirmo skatli: "))
b = int(input("Lūdzu ievadiet otro skaitli: "))

if darbiba == "+":
    rez = a + b
elif darbiba == "-":
    rez = a - b
elif darbiba == "*":
    rez = a * b
elif darbiba == "/":
    rez = a / b
else:
    print("Šāda darbība nav atpazīta")

print("Rezultāts {} {} {} = {}".format(a, darbiba, b, rez))
