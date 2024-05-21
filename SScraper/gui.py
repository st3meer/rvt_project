from PyQt5 import QtWidgets, uic
from parseByFilter import parseByFilter
import ParseFilterOptions, writeToFile, readfiles
import os, errno

ui_folder = 'ui/'
selected_item = None

app = QtWidgets.QApplication([]) #create application
main_ui = uic.loadUi(ui_folder + 'mainwindow.ui') #load the main window
main_ui.setWindowTitle('SScraper')

def silentremove(filename): #remove the file without throwing an exception if the file does not exist
    try:
        os.remove(filename)
    except OSError as e: 
        if e.errno != errno.ENOENT: # errno.ENOENT = no such file or directory
            raise # re-raise exception if a different error occurred

def call_error_message(text): #call the error message
    link_error.err_text.setText(text)
    link_error.show()


def new_task(): #create a new task window
    #app = QtWidgets.QApplication([]) #create application
    ui = uic.loadUi(ui_folder + 'newtask1.ui')
    ui.setWindowTitle('New Task')

    ui.filter_box.setEnabled(False) #disable the filter options comboboxes while no link is provided

    def add_filters(recieved_array): #add receved filter options to the comboboxes
        ui.year_min_cbox.clear()
        ui.year_min_cbox.addItems(recieved_array[0])
        ui.year_max_cbox.clear()
        ui.year_max_cbox.addItems(recieved_array[1])
        ui.eng_min_cbox.clear()
        ui.eng_min_cbox.addItems(recieved_array[2])
        ui.eng_max_cbox.clear()
        ui.eng_max_cbox.addItems(recieved_array[3])
        ui.eng_fuel_cbox.clear()
        ui.eng_fuel_cbox.addItems(recieved_array[4].keys())
        ui.gear_cbox.clear()
        ui.gear_cbox.addItems(recieved_array[5].keys())
        ui.body_cbox.clear()
        ui.body_cbox.addItems(recieved_array[6].keys())
        ui.color_cbox.clear()
        ui.color_cbox.addItems(recieved_array[7].keys())


    def send_link():  #send the link to the parser
        link = ui.link_field.text()
        print(link)
        if link.startswith("https://www.ss.com/en/transport/cars/"): #check if the link is valid
            global recieved_filter_options
            recieved_filter_options = ParseFilterOptions.parseFilterOptions(link)
            if recieved_filter_options == 0:
                print("Failed to get the filter options")
                call_error_message("Failed to get the filter options")
                return
            add_filters(recieved_filter_options)
            ui.filter_box.setEnabled(True) #enable the filter options comboboxes
        else:
            print("Invalid link")
            call_error_message("Wrong link. Note: the link should start with https://www.ss.com/en/transport/cars/")


    def save():
        password = '0'
        min_price = ui.price_min_field.text()
        max_price = ui.price_max_field.text()
        try:
            float(min_price)
            float(max_price)
        except:
            print("Price not provided")
            call_error_message("price not provided. Price can only be a number")
            return
        if ui.use_pass_button.isChecked() == True:
            if ui.passwordfield.text() == '':
                print("Password not provided")
                call_error_message("password not provided")
            else:
                password = ui.passwordfield.text()
            writeToFile.addTask(ui.name_field.text(), ui.passwordfield.text())
        if ui.filter_box.isEnabled() == False:
            print("Link not provided")
            call_error_message("no link provided")
            return
        save_array = []
        save_array.append(ui.name_field.text())  #name
        save_array.append(ui.link_field.text()) #link
        save_array.append(0) #unused field (for next versions)
        save_array.append(min_price) #min price
        save_array.append(max_price) #max price
        save_array.append(ui.year_min_cbox.currentText()) #min year
        save_array.append(ui.year_max_cbox.currentText()) #max year
        save_array.append(ui.eng_min_cbox.currentText()) #min engine displacement
        save_array.append(ui.eng_max_cbox.currentText()) #max engine displacement
        save_array.append(recieved_filter_options[4][ui.eng_fuel_cbox.currentText()]) #engine type
        save_array.append(recieved_filter_options[5][ui.gear_cbox.currentText()]) #gearbox type
        save_array.append(recieved_filter_options[6][ui.body_cbox.currentText()]) #body type
        save_array.append(recieved_filter_options[7][ui.color_cbox.currentText()]) #color
        if writeToFile.addTask(save_array[0], password) == True:
            writeToFile.writeConfigFile(True, save_array[0], save_array[1], save_array[2], save_array[3], save_array[4], save_array[5], save_array[6], save_array[7], save_array[8], save_array[9], save_array[10], save_array[11], save_array[12])
            update_task_list()
            ui.close()
        else:
            call_error_message("task with this name already exists")

    #connect the buttons to the functions
    ui.send_link_button.clicked.connect(send_link) #send link button - send the link to the parser
    ui.save_button.clicked.connect(save) #save button - save the task to config file
    ui.cancel_button.clicked.connect(ui.close) #cancel button - exit the app
    ui.show() #show the window

def add_new_task(): #add new task button
    new_task()
main_ui.new_task_button.clicked.connect(add_new_task) #connect the button to the function

def update_task_list(): #update the task list, reading the tasks from the config file
    tasks = readfiles.get_task_list()
    tasknames = tasks.keys()
    main_ui.task_list.clear() #clear the interface list
    for i in tasknames:
        main_ui.task_list.addItem(i + '\n') #add the tasks to the list

def update_link_list(): #update the link list, reading the links from the csv file
    taskname = select_item()
    if taskname == 'wp':
        print("Wrong password")
        call_error_message("Wrong password")
        main_ui.all_links_table.clear()
        return
    links_array = readfiles.get_link_list(taskname) #get the links
    if links_array == 0:
        print("Failed to get the links")
        call_error_message("Failed to read file")
        return
    main_ui.all_links_table.clear()
    main_ui.all_links_table.setColumnCount(4)
    main_ui.all_links_table.setRowCount(links_array.__len__()) #set the table size
    for i in range(0, links_array.__len__()):
        for j in range(0, links_array[i].__len__()):
            main_ui.all_links_table.setItem(i, j, QtWidgets.QTableWidgetItem(links_array[i][j])) #add the text to the table

def update_new_link_list(): #update the link list, reading the links from the csv file
    taskname = select_item()
    if taskname == 'wp':
        print("Wrong password")
        call_error_message("Wrong password")
        main_ui.new_links_table.clear()
        return
    links_array = readfiles.compareCSV(taskname) #get the links
    main_ui.new_links_table.clear()
    main_ui.new_links_table.setColumnCount(4)
    main_ui.new_links_table.setRowCount(links_array.__len__()) #set the table size
    for i in range(0, links_array.__len__()):
        for j in range(0, links_array[i].__len__()):
            main_ui.new_links_table.setItem(i, j, QtWidgets.QTableWidgetItem(links_array[i][j])) #add the text to the table


def select_item():
    tasks = readfiles.get_task_list()
    selected_item = main_ui.task_list.currentItem() #get the selected item
    if selected_item != None: #check if the item is selected
        selected_item = selected_item.text().replace('\n', '') #get the selected task name
        if tasks[selected_item] != '0': #if the task has a password
            entered_password = main_ui.password.text() #check if the entered password is correct
            print('de', entered_password)
            if entered_password != tasks[selected_item]:
                return 'wp'
            else:
                print(selected_item)
                return selected_item
        else: #if the task does not have a password
            print(selected_item)
            return selected_item

def update(): #update the task
    print("update")
    taskname = select_item()
    if taskname == 'wp':
        print("Wrong password")
        call_error_message("Wrong password")
        return
    config = readfiles.get_task_config(taskname)
    if config == 0: #check for exceptions
        print("Failed to get the config")
        call_error_message("Failed to read config file of this task")
        return
    for i in range(0, config.__len__()): #remove the new line characters 
        config[i] = config[i].replace('\n', '')
    #parse the page
    new_links = parseByFilter(config[2], config[4], config[5], config[6], config[7], config[8], config[9], config[10], config[11], config[12], config[13]) 
    if new_links == 0: #check for exceptions
        print("Failed to get the links")
        call_error_message("Failed to get the links")
        return
    elif new_links == 1:
        print("No links found")
        call_error_message("No links found, please check your filters")
        return
    else:
        writeToFile.writeToFileCSV(taskname, new_links) #write the links to the csv file
        update_link_list()

def delete_task():
    taskname = select_item()
    silentremove("saveddata/" + taskname + ".config")
    silentremove("saveddata/" + taskname + ".csv")
    silentremove("saveddata/" + taskname + "Old.csv")
    writeToFile.removeTask(taskname)
    update_task_list()

#main_ui.task_list.itemDoubleClicked.connect(update)
link_error = uic.loadUi(ui_folder + 'wronglink.ui') #load the error window
link_error.ok_button.clicked.connect(link_error.close) #ok button on the link error message - close the message
password_window = uic.loadUi(ui_folder + 'password.ui') #load the password window

main_ui.task_list.itemClicked.connect(update_link_list)
main_ui.update_button.clicked.connect(update)
main_ui.all_links_table.setSortingEnabled(True)
main_ui.delete_task_button.clicked.connect(delete_task)

update_task_list()
main_ui.show()
app.exec()
