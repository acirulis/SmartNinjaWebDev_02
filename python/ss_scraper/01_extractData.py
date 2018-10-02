from bs4 import BeautifulSoup
import pandas as pd
import sys

def process_file(fname):
    with open(fname,'rb')as file_:
        html = file_.read()
    soup = BeautifulSoup(html,'html.parser')

    table = soup.find("table", attrs={"align":"center", "cellpadding": "2", "border": "0"})
    # headings = [th.get_text() for th in table.find("tr").find_all("th")]
    return table


# align=center cellpadding=2 cellspacing=0 border=0 width="100%"

datasets = []

for n in range(1,4):
    file_ = 'data/ss_0{}.html'.format(n)
    table = process_file(file_)
    # print(table)
    # sys.exit()
    print('Headings...')
    headings = [tr.get_text() for tr in table.find('tr').find_all('td')]
    headings[0] = 'Ievads'

    # print(headings)
    # sys.exit()

    print('Data...')
    for row in table.find_all("tr")[1:-1]: # skip first & last rows
        row = [td.get_text() for td in row.find_all('td')][2:]
        #print(row)
        datarow = zip(headings, row)
        datasets.append(dict(datarow))


#sys.exit()

data = pd.DataFrame(datasets)
print(data.info())
print(data['Ievads'])

# some cleaning
data['Ievads'] = data['Ievads'].apply(lambda x: x.replace('\n','').replace('\r','').strip())
#
data.to_csv('data/ss_out.csv',index=False, encoding='utf-8')
#
