import os
path = "saveddata/" #path to save folder
def writeToFileCSV(filename, links_got_list): #create a csv file for internal use
    file1 = path + filename + ".csv"
    file2 = path + filename + "Old.csv"

    if os.path.exists(file2):
        os.remove(file2)
    if os.path.exists(file1):
        os.rename(file1, file2)    
    with open(file1, 'w', encoding="utf-16") as f:
        for item in links_got_list:
            for i in item:
                i = i.replace('\n', " ")
                i = i.replace('\r', " ")
                f.write(i + ';')
            f.write('\n')

def writeToFileTXT(links_got_list): #create a user readable result list
    with open('linksListUser.txt', 'w', encoding="utf-16") as f:
        f.write("in development")

def writeConfigFile(isActive, name, url, upd_period, priceMin, priceMax, yearMin, yearMax, engOptMin, engOptMax, engType, gbxType, bodyOpt, clrOpt):
    with open(path + name + ".config", 'w', encoding="utf-16") as f:
        f.write(str(isActive) + "\n")
        f.write(str(name) + "\n")
        f.write(str(url + '\n'))
        f.write(str(upd_period) + '\n')
        f.write(str(priceMin) + '\n')
        f.write(str(priceMax) + '\n')
        f.write(str(yearMin) + '\n')
        f.write(str(yearMax) + '\n')
        f.write(str(engOptMin) + '\n')
        f.write(str(engOptMax) + '\n')
        f.write(str(engType) + '\n')
        f.write(str(gbxType) + '\n')
        f.write(str(bodyOpt) + '\n')
        f.write(str(clrOpt) + '\n')

def addTask(taskname):
    configfile = open(path + "general.config", "r")
    config_contents = configfile.readlines()
    configfile.close()
    if taskname not in config_contents:
        config_contents.append(taskname)
        configfile = open(path + "general.config", "w")
        configfile.writelines(config_contents)
        configfile.write("\n")
        configfile.close()
        return True
    else:
        return False
