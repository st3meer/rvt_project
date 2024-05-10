from PyQt5 import QtWidgets, uic
import ParseFilterOptions, writeToFile

def new_task():
    app = QtWidgets.QApplication([]) #create application
    ui = uic.loadUi('newtask.ui')
    link_error = uic.loadUi('wronglink.ui')
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
        ui.year_min_cbox.addItems(recieved_array[0])
        ui.year_max_cbox.addItems(recieved_array[1])
        ui.eng_min_cbox.addItems(recieved_array[2])
        ui.eng_max_cbox.addItems(recieved_array[3])
        ui.eng_fuel_cbox.addItems(recieved_array[4].keys())
        ui.gear_cbox.addItems(recieved_array[5].keys())
        ui.body_cbox.addItems(recieved_array[6].keys())
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
            link_error.show()
            return
        save_array = []
        save_array.append(ui.name_field.text()) #name
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

        writeToFile.writeConfigFile(save_array[0], save_array[1], save_array[2], save_array[3], save_array[4], save_array[5], save_array[6], save_array[7], save_array[8], save_array[9], save_array[10], save_array[11], save_array[12])

    #connect the buttons to the functions
    ui.send_link_button.clicked.connect(send_link) #send link button - send the link to the parser
    ui.save_button.clicked.connect(save) #save button - save the task to config file
    ui.cancel_button.clicked.connect(app.quit) #cancel button - exit the app
    link_error.ok_button.clicked.connect(link_error.close) #ok button on the link error message - close the message

    #launch the app
    ui.show()
    app.exec()

new_task()