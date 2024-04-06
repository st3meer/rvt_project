import mechanicalsoup
from bs4 import BeautifulSoup


#  , priceMin, priceMax, yearMin, yearMax, engOptMin, engOptMax, engType, gbxType, bodyOpt, clrOpt
def parseByFilter(urlInput):     
    # 1
    browser = mechanicalsoup.StatefulBrowser()
    url = urlInput + "filter"
    browser.open(url)
    #print(browser.page)
    browser.select_form('form[name="filter_frm"]')

    browser["topt[8][min]"] = 500
    browser["topt[8][max]"] = 2000
    browser["topt[18][min]"] = "1999"
    browser["topt[18][max]"] = "2013"
    #browser["topt[15][min]"] = 1.0
    #browser["topt[15][max]"] = 3.0
    #browser["opt[34]"] = eng_options[2]
    #browser["opt[35]"] = gbx_options[1]
    #browser["opt[32]"] = body_options[9]
    #browser["opt[17]"] = clr_options[3]

    resposne = browser.submit_selected()
    #browser.open(url + "filter/")
    print("url: ", browser.url)
    #browser.launch_browser()


    soup = BeautifulSoup(resposne.text, 'html.parser')
    form_res = soup.find(id="filter_frm")
    table_res = form_res.find_all('table')[2]
    table_rows = table_res.find_all('tr')
    table_rows.pop(0)
    table_rows.pop(table_rows.__len__() - 1)
    for row in table_rows:
        #print(row.prettify())
        print("-------------------------------------------------")
        desc = row.find('td', class_='msg2').find('a')
        print("---desc-start--------------------------------------------")
        print(desc.text)
        print("---desc-end--------------------------------------------")
        price = row.find_all('td', class_='msga2-o pp6')[2]
        print("price: ", price.text)
        link = desc['href'][1:]
        print("link: ", browser.url + link)
    return 0
        