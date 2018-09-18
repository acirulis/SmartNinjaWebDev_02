import datetime

vards = 'Andis'

with open('piemers.html','w+') as file:
    print('Tagad ierakstisim kko failā')
    file.write('<h1>Virsraksts</h1>')
    file.write('<b>Mans vards ir: {}</b> '.format(vards))
    file.write('<ul>')
    for x in range(1,6):
        file.write('<li>kaut kas {}</li>'.format(x))
    file.write('</ul>')
    file.write('<hr />')
    file.write('Uzgenerets: {}'.format(datetime.datetime.now()))





