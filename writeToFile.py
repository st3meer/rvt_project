import os
def writeToFileCSV(links_got_list): #create a csv file for internal use
    if os.path.exists("linkListOld.csv"):
        os.remove("linkListOld.csv")
    if os.path.exists("linksList.csv"):
        os.rename("linksList.csv", "linkListOld.csv")    
    with open('linksList.csv', 'w', encoding="utf-16") as f:
        for item in links_got_list:
            for i in item:
                f.write(i.replace('U+000A', " ") + ';')
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