import mechanicalsoup
from bs4 import BeautifulSoup
#import requests
from time import sleep

#  
def parseByFilter(urlInput, priceMin, priceMax, yearMin, yearMax, engOptMin, engOptMax, engType, gbxType, bodyOpt, clrOpt):     
    # 1
    try:
        links_got_list = []
        for_count = 0
        pages = 0
        #page_counter = 1
        if not urlInput.endswith("/"): # check if the url ends with a slash
            urlInput += "/" # add a slash to the end of the url
        url = urlInput + "filter/" # add the filter to the url
        print("iurl: ", url)
        browser = mechanicalsoup.StatefulBrowser()
        browser.open(url)
    except Exception as e:
        print("Failed to open the page")
        print(e)
        return 0


        #print(browser.page)
    try:
        browser.select_form('form[name="filter_frm"]') # select the form
        # setting the filter options
        if priceMin != '':
            browser["topt[8][min]"] = priceMin # set the minimum price
        if priceMax != '':
            browser["topt[8][max]"] = priceMax # set the maximum price
        if yearMin != '':
            browser["topt[18][min]"] = yearMin # set the minimum year
        if yearMax != '':
            browser["topt[18][max]"] = yearMax # set the maximum year
        if engOptMin != '':
            browser["topt[15][min]"] = engOptMin # set the minimum engine displacement
        if engOptMax != '':
            browser["topt[15][max]"] = engOptMax # set the maximum engine displacement
        if engType != '':
            browser["opt[34]"] = engType # set the engine type
        if gbxType != '':
            browser["opt[35]"] = gbxType # set the gearbox type
        if bodyOpt != '':
            browser["opt[32]"] = bodyOpt # set the body type
        if clrOpt != '':
            browser["opt[17]"] = clrOpt # set the color 
    except Exception as e:
        print("Failed to set the filter options")
        print(e)
        return 0

    try:
        resposne = browser.submit_selected() # submit the form
        while True:
            print("burl: ", browser.url)

            burl = str(browser.url)
            if pages != 0 and burl == url: # if the page is the same as the previous one, break the loop
                break

            #select the table with the links from the page elements
            soup = BeautifulSoup(resposne.text, 'html.parser')
            form_res = soup.find(id="filter_frm")
            table_res = form_res.find_all('table')[2]
            table_rows = table_res.find_all('tr')
            table_rows.pop(0)
            table_rows.pop(table_rows.__len__() - 1) #remove the first and last rows 
            #first and last table rows dont contain the links
            if table_rows.__len__() <= 1: # if there are no links, break the loop
                return 1
            for row in table_rows: # get the list of links from the table
                links_got_list.append([])
                desc = row.find('td', class_='msg2').find('a') # get the description
                desc1 = desc.text
                desc_fl_index = desc1.find('\n') #check if the description contains a new line and its index
                if desc_fl_index != -1: #if it does, get only the first line of the description
                    desc1 = desc1[:desc_fl_index] #get only the first line of the description
                links_got_list[for_count].append(desc1)
                pp6 = row.find_all('td', class_='msga2-o pp6') # get the list of data about the post
                price = pp6[pp6.__len__() - 1] # get the price (always the last element in the list)
                links_got_list[for_count].append(price.text) 
                link = desc['href'][1:] # get the link
                link = link.split('/')
                link1 = urlInput + link[5] + link[6] # get the full link
                links_got_list[for_count].append(link1) 
                uid = row['id'] # get the unique id
                links_got_list[for_count].append(uid)
                for_count += 1
            print("found ", for_count, " links.") # print the number of links found
            pages += 1 # increment the number of pages (debug)
            sleep(1)
            #to avoid anti DDOS protection and other bugs, sleep for 1 second before the next request

            #page switching
            form_res = soup.find(id="filter_frm")
            page_selector = form_res.find('div', class_='td2')
            if page_selector == None: # if there is no page selector, break the loop
                break
            page_selector_buttons = page_selector.find_all('a')
            next_button = page_selector_buttons[page_selector_buttons.__len__()  - 1] # get the next page button
            resposne = browser.follow_link(next_button) # follow the link to the next page
            #browser.open(url + "filter/")
            print(pages) # print the number of pages (debug)
    except Exception as e:
        print("Failed to get the links")
        print(e)
        return 0
    print("found ", pages, " pages.") 
    return links_got_list # return the list of links
