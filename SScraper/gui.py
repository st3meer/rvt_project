from PyQt5 import QtWidgets, uic
from parseByFilter import parseByFilter
import ParseFilterOptions, writeToFile, readfiles

ui_folder = 'ui/'

app = QtWidgets.QApplication([]) #create application
main_ui = uic.loadUi(ui_folder + 'mainwindow.ui')
main_ui.setWindowTitle('SScraper')

def new_task():
    #app = QtWidgets.QApplication([]) #create application
    ui = uic.loadUi(ui_folder + 'newtask1.ui')
    link_error = uic.loadUi(ui_folder + 'wronglink.ui')
    ui.setWindowTitle('New Task')

    upd_options = { #update time options and their values
        "5 min": "300",
        "10 min": "600",
        "20 min": "1200",
        "30 min": "1800",
        "1 hour": "3600",
    }

    ui.update_time_cbox.addItems(upd_options.keys()) #add update time options to the combobox
    ui.filter_box.setEnabled(False) #disable the filter options comboboxes while no link is provided

    def call_error_message(text): #call the error message
        link_error.err_text.setText(text)
        link_error.show()

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
            add_filters(recieved_filter_options)
            ui.filter_box.setEnabled(True) #enable the filter options comboboxes
        else:
            print("Invalid link")
            call_error_message("Wrong link. Note: the link should start with https://www.ss.com/en/transport/cars/")


    def save():
        if ui.filter_box.isEnabled() == False:
            print("Link not provided")
            call_error_message("no link provided")
            return
        save_array = []
        save_array.append(ui.name_field.text())  #name
        save_array.append(ui.link_field.text()) #link
        save_array.append(upd_options[ui.update_time_cbox.currentText()]) #update time
        save_array.append(ui.price_min_field.text()) #min price
        save_array.append(ui.price_max_field.text()) #max price
        save_array.append(ui.year_min_cbox.currentText()) #min year
        save_array.append(ui.year_max_cbox.currentText()) #max year
        save_array.append(ui.eng_min_cbox.currentText()) #min engine displacement
        save_array.append(ui.eng_max_cbox.currentText()) #max engine displacement
        save_array.append(recieved_filter_options[4][ui.eng_fuel_cbox.currentText()]) #engine type
        save_array.append(recieved_filter_options[5][ui.gear_cbox.currentText()]) #gearbox type
        save_array.append(recieved_filter_options[6][ui.body_cbox.currentText()]) #body type
        save_array.append(recieved_filter_options[7][ui.color_cbox.currentText()]) #color
        if writeToFile.addTask(save_array[0]) == True:
            writeToFile.writeConfigFile(True, save_array[0], save_array[1], save_array[2], save_array[3], save_array[4], save_array[5], save_array[6], save_array[7], save_array[8], save_array[9], save_array[10], save_array[11], save_array[12])
            print("HIIII")
            update_task_list()
            ui.close()
        else:
            call_error_message("task with this name already exists")

    #connect the buttons to the functions
    ui.send_link_button.clicked.connect(send_link) #send link button - send the link to the parser
    ui.save_button.clicked.connect(save) #save button - save the task to config file
    ui.cancel_button.clicked.connect(ui.close) #cancel button - exit the app
    link_error.ok_button.clicked.connect(link_error.close) #ok button on the link error message - close the message
    ui.show() #show the window

def add_new_task(): #add new task button
    new_task()
main_ui.new_task_button.clicked.connect(add_new_task) #connect the button to the function

def update_task_list(): #update the task list, reading the tasks from the config file
    tasks = readfiles.get_task_list()
    main_ui.task_list.clear()
    main_ui.task_list.addItems(tasks)

def select_item():
    selected_item = main_ui.task_list.currentItem()
    if selected_item != None:
        taskname = selected_item.text() #get the selected task name
        taskname = taskname.replace('\n', '')
        print(taskname)
        update(taskname)

def update(taskname):
    print("update")
    config = readfiles.get_task_config(taskname)
    for i in range(0, config.__len__()):
        config[i] = config[i].replace('\n', '')
    writeToFile.writeToFileCSV(taskname, parseByFilter(config[2], config[4], config[5], config[6], config[7], config[8], config[9], config[10], config[11], config[12], config[13]))


main_ui.task_list.itemDoubleClicked.connect(select_item)

update_task_list()
main_ui.show()
app.exec()
