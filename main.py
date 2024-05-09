from parseByFilter import parseByFilter
from ParseFilterOptions import parseFilterOptions
from writeToFile import writeToFileCSV

logo = '''                
                                  
    ssssssssss       ssssssssss   
  ss::::::::::s    ss::::::::::s  
ss:::::::::::::s ss:::::::::::::s 
s::::::ssss:::::ss::::::ssss:::::s
 s:::::s  ssssss  s:::::s  ssssss 
   s::::::s         s::::::s      
      s::::::s         s::::::s   
ssssss   s:::::s ssssss   s:::::s 
s:::::ssss::::::ss:::::ssss::::::s
s::::::::::::::s s::::::::::::::s 
 s:::::::::::ss   s:::::::::::ss  
  sssssssssss      sssssssssss    
                                                         
  ___  ___ _ __ __ _ _ __   ___ _ __ 
 / __|/ __| '__/ _` | '_ \ / _ \ '__|
 \__ \ (__| | | (_| | |_) |  __/ |   
 |___/\___|_|  \__,_| .__/ \___|_|   
                    | |              
                    |_|  

'''
print(logo)
print("WELCOME TO SScraper")
print("please enter valid SS.LV car search URL:")
print("example: https://www.ss.com/lv/transport/cars/bmw/")
#url = input()
url = 'https://www.ss.lv/lv/transport/cars/bmw/5-series/'
filename = 'linksList'
writeToFileCSV(filename, parseByFilter(url, 500, 3500, None, None, None, None, None, None, None, None))
#parseFilterOptions(url) #for testing purposes
