print("Kalkulators 1.0")

x = input("Lūdzu ievadiet X: ")
y = input("Lūdzu ievadiet Y: ")

rez = int(x) + int(y)
print("Rezultāts: ", x, "  + ", y, " = ", rez)
if rez > 50:
    print("Rezultāts ir lielāks par 50")
elif rez == 50:
    print("Rezultāts ir 50")
else:
    print("Rezultāts ir mazāks par 50")

# ALTERNATĪVS VARIANTS AR TADU PAŠU REZULTĀTU
# if rez > 50:
#     print("Rezultāts ir lielāks par 50")
# elif rez < 50:
#     print("Rezultāts ir mazāks par 50")
# else:
#     print("Rezultāts ir 50")
