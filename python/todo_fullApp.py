import os

# funkcija, kas tikai izdrukā uz ekrāna sākumskatu ar iespējamajām darbībām
def print_menu():
    print("\n\n")
    print("TODO APPLICATION\n")
    print('[1] - List current tasks')
    print('[2] - Add new task')
    print('[3] - Delete all tasks')
    print('[4] - Quit (and write to file)')
    return True # nav obligāti atgriezt True, bet tā ir laba prakse

# nolasam tasku saturu no faila
def read_from_file(filename):
    try:
        tasks = []
        file_handle = open(filename, "r", encoding="utf-8") # fails atvērts lasīšanai ar utf8 kodējumu
        lines = file_handle.read().splitlines() #nolasam failu un sadalam rindiņās
        for line in lines: #katra rindiņa ir viens tasks formātā Task::Status
            task_data = line.split("::") #sadalam taska aprakstu un statusu
            task = {}
            task['title'] = task_data[0]
            task['status'] = (task_data[1] == "True") # teksta falā ierakstīts string "True" vai "False"
            tasks.append(task)
        file_handle.close()
        return tasks
    except IOError: #Exceptions, gadījumā ja fails neeksistē, vai to nevar nolasīt
        return []

#ierakstam failā savus taskus
def write_to_file(filename, tasks):
    if len(tasks) > 0:
        file_handle = open(filename, "w+", encoding="utf-8") #atveram rakstīšanai vai papildināšanai
        for task in tasks:
            task_line = "%s::%s\n" % (task['title'], task['status']) #noformatējam datus pašizdomātā formātā
            file_handle.write(task_line)
        file_handle.close()
    return True

#jauna taska pievienošana globālajam mainīgajam
def add_new_task(tasks, task_title, task_status):
    task = {}
    task['title'] = task_title
    task['status'] = (task_status == 'd')
    tasks.append(task)

#visu tasku saraksta izvadīšana uz ekrāna
def list_all_tasks(tasks):
    for task in tasks:
        print('\nTASK')
        print('Title: %s ' % task['title'])
        print('Status: %s ' % task['status'])
    return True

#nodzēšam visus taskus izdzēšot failu un atgriežot tukšu tasku sarakstu, kas vēlāk tiek piešķirts tasks mainīgajam.
def remove_all_tasks(filename):
    os.remove(filename)
    return []

# MAIN PROGRAM STARTS HERE
# Visa aplikācija ir sadalīta vairākās funkcijās (metodēs), lai nodrošinātu ērtāku pārskatāmību
# un zemāk esošajā while ciklā var ērti izsekot līdzi iespējām, ko piedāvā programma.
# Tāpat, piemēram, ērti pārslēgties uz citu datu glabāšanas veidu (datu bāzi), izmanot tikai
# attiecīgās funkcijas.

# faila vārdu saglabājam mainīgajā, lai tas nebūtu jāatkārto vairākas reizes
FILE_NAME = 'todo.dat'
tasks = read_from_file(FILE_NAME)

# while cikls kontrolē galveno darbības loģiku, saņem lietotāja ievaddatus
# un izsauc attiecīgo funkciju.
while True:
    print_menu()
    action = input('Your choice: ....')
    if action == '4':
        write_to_file(FILE_NAME, tasks)
        break
    if action == '1':
        list_all_tasks(tasks)
    if action == '2':
        task_title = input('Enter task name: .. ')
        task_status = input('Enter [d], if done: .. ')
        add_new_task(tasks, task_title, task_status.lower()) #nododam kā parametru statusu, vienlaicīgi to uztaisot par mazo burtu.
    if action == '3':
        tasks = remove_all_tasks(FILE_NAME)

print('\nGood bye!')