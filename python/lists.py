print("Musu TODO aplikācija")

todo_list = {}


while True:
    task = input("Ludzu ievadiet darāmo darbu: ")
    status = input("Vai darbs ir izdarits? (j/n): ")
    if status.lower() == 'j':
        todo_list[task] = True
    else:
        todo_list[task] = False
    new = input("Vai pievienot vēl jaunu? (j/n) ")
    if new.lower() == "n":
        break

fails = open('todo.txt','w+')
print('Visi pievienotie darbi:')
skaititajs = 1
for task in todo_list:
    if todo_list[task]:
        statuss = 'IR'
    else:
        statuss = 'NAV'
    print('{} - {} Izdarits: {}'.format(skaititajs, task, statuss))
    fails.write('{} - {} Izdarits: {}\n'.format(skaititajs, task, statuss))
    skaititajs = skaititajs + 1
fails.close()

