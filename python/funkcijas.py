def paragrafs(text):
    rezultats = '<span>{}</span>'.format(text)
    return rezultats


zina = ['Pirmais paragrafs', 'Otrais paragrafs', 'Tresais paragrafs']

### PIRMAIS VARIANTS BEZ FUNKCIJAS
print('<H1>Virsraksts</H1>')
print('<p>{}</p>'.format(zina[0]))
print('<p>{}</p>'.format(zina[1]))
print('<p>{}</p>'.format(zina[2]))
print('<p>Nobeiguma teksts</p>')

### OTRAIS VARIANTS AR FUNKCIJU
print('<H1>ALTERNATIVA</H1>')
print(paragrafs(zina[0]))
print(paragrafs(zina[1]))
print(paragrafs(zina[2]))
print(paragrafs('Cits teksts nobeiguma'))


### CITA FUNKCIJA
def summa(a, b):
    rezultats = (a + b) * 2
    return rezultats


skaitlisA = 10
skaitlisB = 20

skaitlisC = summa(skaitlisA, skaitlisB)

print(skaitlisC)
print(summa(4, 5))
