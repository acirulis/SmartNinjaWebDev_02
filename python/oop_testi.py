class Persona:
    def __init__(self, vards, uzvards, telefons, dzims_gads, epasts):
        self.vards = vards
        self.uzvards = uzvards
        self.telefons = telefons
        self.dzims_gads = dzims_gads
        self.epasts = epasts
    def pilns_vards(self):
        s = self.vards + " " + self.uzvards
        return s
    def vecums(self):
        v = 2018 - self.dzims_gads
        return v


anna = Persona(vards="Anna", uzvards="Berzina", telefons="222222", dzims_gads=1990, epasts="anna@anna.lv")
peteris = Persona("Peteris", "Kalnins", "333333", 1980, "peteris@gmail.com")
juris = Persona("Juris", "Liepins", "4444444", 2000, "juris@inbox.lv")

klasesbiedri = [anna, peteris, juris]

for cilveks in klasesbiedri:
    print("Vards: ", cilveks.pilns_vards())
    print("Vecums: ", cilveks.vecums())


















