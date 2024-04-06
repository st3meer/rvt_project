import mechanicalsoup
from bs4 import BeautifulSoup

#  
def parseByFilter(urlInput, priceMin, priceMax, yearMin, yearMax, engOptMin, engOptMax, engType, gbxType, bodyOpt, clrOpt):     
    # 1
    browser = mechanicalsoup.StatefulBrowser()
    url = urlInput + "filter"
    browser.open(url)
    #print(browser.page)
    browser.select_form('form[name="filter_frm"]') # select the form
    # setting the filter options
    if priceMin != None:
        browser["topt[8][min]"] = priceMin # set the minimum price
    if priceMax != None:
        browser["topt[8][max]"] = priceMax # set the maximum price
    if yearMin != None:
        browser["topt[18][min]"] = yearMin # set the minimum year
    if yearMax != None:
        browser["topt[18][max]"] = yearMax # set the maximum year
    if engOptMin != None:
        browser["topt[15][min]"] = engOptMin # set the minimum engine displacement
    if engOptMax != None:
        browser["topt[15][max]"] = engOptMax # set the maximum engine displacement
    if engType != None:
        browser["opt[34]"] = engType # set the engine type
    if gbxType != None:
        browser["opt[35]"] = gbxType # set the gearbox type
    if bodyOpt != None:
        browser["opt[32]"] = bodyOpt # set the body type
    if clrOpt != None:
        browser["opt[17]"] = clrOpt # set the color

    resposne = browser.submit_selected()
    #browser.open(url + "filter/")
    print("url: ", browser.url)
    browser.launch_browser()

    links_got_list = []
    for_count = 0

    soup = BeautifulSoup(resposne.text, 'html.parser')
    form_res = soup.find(id="filter_frm")
    table_res = form_res.find_all('table')[2]
    table_rows = table_res.find_all('tr')
    table_rows.pop(0)
    table_rows.pop(table_rows.__len__() - 1)

    for row in table_rows:
        links_got_list.append([])
        desc = row.find('td', class_='msg2').find('a')
        links_got_list[for_count].append(desc.text)
        price = row.find_all('td', class_='msga2-o pp6')[3]
        links_got_list[for_count].append(price.text)
        link = desc['href'][1:]
        links_got_list[for_count].append(link)
        uid = row['id']
        links_got_list[for_count].append(uid)
        for_count += 1

    return links_got_list
