import os
def writeToFileCSV(filename, links_got_list): #create a csv file for internal use
    file1 = filename + ".csv"
    file2 = filename + "Old.csv"

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

def writeConfigFile(url, priceMin, priceMax, yearMin, yearMax, engOptMin, engOptMax, engType, gbxType, bodyOpt, clrOpt):
    with open('config.txt', 'w', encoding="utf-16") as f:
        f.write("url: " + url + '\n')
        f.write("priceMin: " + str(priceMin) + '\n')
        f.write("priceMax: " + str(priceMax) + '\n')
        f.write("yearMin: " + str(yearMin) + '\n')
        f.write("yearMax: " + str(yearMax) + '\n')
        f.write("engOptMin: " + str(engOptMin) + '\n')
        f.write("engOptMax: " + str(engOptMax) + '\n')
        f.write("engType: " + str(engType) + '\n')
        f.write("gbxType: " + str(gbxType) + '\n')
        f.write("bodyOpt: " + str(bodyOpt) + '\n')
        f.write("clrOpt: " + str(clrOpt) + '\n')

