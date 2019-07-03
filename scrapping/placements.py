import requests
from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options



options = Options()

#options.add_argument("--headless")

# Add path of Geckodriver.exe in executable_path below
driver = webdriver.Firefox(firefox_options=options,executable_path="C:/Users/Gupta Niwas/Downloads/PBL SEM 4/geckodriver-v0.20.0-win64/geckodriver.exe")
print("Firefox Headless Browser Invoked")
curl="https://www.shiksha.com/medicine-health-sciences/dietics-nutrition/course/b-sc-in-nutrition-and-dietetics-quantum-school-of-health-sciences-admission-office-dehradun-298754"
driver.get(curl)
placement=[]
places=driver.find_elements_by_class_name("comp-nm")
print(places)
j=0
for i in places:
    if j==0:
        print(i.text)
        place=i.text
        j=1
    else:
        place=place+" , "
        place=place+i.text
    print(place)
    placement.append(place)
    print(placement)


'''
def placements(curl):
        place="-"
        p=requests.get(curl)
        ps=BeautifulSoup(p.content,"lxml")
        places=ps.find_all("div",{"id":"placements"})
        print(places)
        placess=places[0].find_all("span",{"class":"comp-nm"})
        j=0
        for i in placess:
            if j==0:
                print(i.text)
                place=i.text
                j=1
            else:
                place=place+" , "
                place=place+i.text
        print(place)
        placement.append(place)
        print(placement)
placements(curl)
'''