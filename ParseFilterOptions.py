import requests
from bs4 import BeautifulSoup

#get lists of possible options for each filter

def parseFilterOptions(urlInput): 
    # Parse the filter options
    # Return a dictionary of filter options
    response = requests.get(urlInput)
    #print(browser.page)
    soup = BeautifulSoup(response.content, 'html.parser')
    soup_form = soup.find('form', attrs={'name': 'filter_frm'})

    #minimum year options
    form_yearMin = soup_form.find('select', attrs={'name': "topt[18][min]"})
    optYearMin = []
    for option in form_yearMin.find_all('option'):
        optYearMin.append(option['value'])

    #maximum year options
    form_yearMax = soup_form.find('select', attrs={'name': "topt[18][max]"})
    optYearMax = []
    for option in form_yearMax.find_all('option'):
        optYearMax.append(option['value'])

    #minimum engine disp options
    form_engDispMin = soup_form.find('select', attrs={'name': "topt[15][min]"})
    optEngDispMin = []
    for option in form_engDispMin.find_all('option'):
        optEngDispMin.append(option['value'])

    #maximum engine disp options
    form_engDispMax = soup_form.find('select', attrs={'name': "topt[15][max]"})
    optEngDispMax = []
    for option in form_engDispMax.find_all('option'):
        optEngDispMax.append(option['value'])

    #engine type options
    form_engType = soup_form.find('select', attrs={'name': "opt[34]"})
    optEngType = {}
    for option in form_engType.find_all('option'):
        optEngType[option.text] = option['value']

    #gearbox type options
    form_gbxType = soup_form.find('select', attrs={'name': "opt[35]"})
    optGbxType = {}
    for option in form_gbxType.find_all('option'):
        optGbxType[option.text] = option['value']

    #body type options
    form_bodyType = soup_form.find('select', attrs={'name': "opt[32]"})
    optBodyType = {}
    for option in form_bodyType.find_all('option'):
        optBodyType[option.text] = option['value']

    #color options
    form_clrType = soup_form.find('select', attrs={'name': "opt[17]"})
    optClrType = {}
    for option in form_clrType.find_all('option'):
        optClrType[option.text] = option['value']

    return_array = [optYearMin, optYearMax, optEngDispMin, optEngDispMax, optEngType, optGbxType, optBodyType, optClrType]
    return return_array