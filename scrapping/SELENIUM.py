from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options



options = Options()

# Below line stops from opening browser
# Comment it if you want to see the browser opening and auto click working
options.add_argument("--headless")

# Add path of Geckodriver.exe in executable_path below
driver = webdriver.Firefox(firefox_options=options,executable_path="C:/Users/Gupta Niwas/Downloads/PBL SEM 4/geckodriver-v0.20.0-win64/geckodriver.exe")
print("Firefox Headless Browser Invoked")


driver.get('https://www.shiksha.com/b-tech/colleges/b-tech-colleges-mumbai-all')
#_css_selector(".class_name tag")
csss=driver.find_elements_by_css_selector(".outerframe a")
print(len(csss))
while(len(csss)):
    b=0
    for i in csss:
        print(i.text)
        if len(i.text)>=1:
            if i.text[0]=="+":
                b=1
                break
    if b==0:
        break
    for i in csss:
        #print(i.text)
        try:
            i.click()
            driver.implicitly_wait(100)
        except:
            pass
    csss=driver.find_elements_by_css_selector(".outerframe a")
    print(len(csss))


sleep(5)
# Getting the page surce containing JavaScript Data
src=driver.page_source
#src = driver.find_element_by_tag_name('html').get_attribute('innerHTML')
#src = driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
print(src)
soup = BeautifulSoup(src,"lxml")
#tp = soup.find_all("div",{"class":"clg-tpl-parent"})
tpm = soup.find("section",{"class":"tpl-curse-dtls more_46905_0"})
print("length tpm -->>",len(tpm))
'''
college_names = []
course_names = []
fee_details=[]
exam_details=[]
affiliation = []
facilities_individual=[]
facilities=[]
# FOR COLLEGE ID
college_id=[]
slc = "instituteContainer_"
len_slc=len(slc)
# Done for college id
for x in tp:
    college_names.append((x.find_all("h2",{"class":"tuple-clg-heading"})[0].contents[0].text))
    course_names.append((x.find_all("h5",{"class":"tpl-course-name"})[0].contents[0].text))
    fee_details.append((x.find_all("div",{"class":"tuple-fee-col"})[0].contents[3].text))
    try:
        exam_details.append(x.find_all("div",{"class":"tuple-exam-dtls"})[0].contents[3].text)
    except:
        pass
    affiliation.append((x.find_all("div",{"class":"tuple-alum-col"})[0].contents[3].text))
    for i in range(1,len(x.find_all("ul",{"class":"facility-icons"})[0].contents),2):
        facilities_individual.append(x.find_all("ul",{"class":"facility-icons"})[0].contents[i].text)
    facilities.append(facilities_individual)
    college_id.append(x.find_all("div",{"class":"clg-tpl"})[0]['id'][len(slc):])

import pandas as pd
data =pd.DataFrame(list(zip(college_names,college_id,course_names,fee_details,exam_details,affiliation,facilities)),columns=['Name','Shiksha_ID','Course', 'Fees','Exam','Affiliation','Facilities'])
print(data)
input("prompt ->>")
'''

'''
js=driver.find_elements_by_partial_link_text("+ ")#+" More courses")
print(len(js))
#for i in range(len(js)):
while(len(js)):
    for i in js:
        try:
            i.click()
            driver.implicitly_wait(100)
        except: #try removing except
            pass
        #finally:
    js=driver.find_elements_by_partial_link_text("+ ")
'''

'''
js=driver.find_elements_by_tag_name("a")
while(len(js)):
    for i in js:
        if(i.get_attribute("href") is not None and "javascript:void(0);" in i.get_attribute("href")):
            try:
                i.click()
                driver.implicitly_wait(100)
            except:
                pass
        #finally:
    js=driver.find_elements_by_tag_name("a")
'''

'''
#aElements = driver.find_elements_by_tag_name("a")
aElements = driver.find_elements_by_partial_link_text("+ ")

for name in aElements:
    if(name.get_attribute("href") is not None and "javascript:void(0);" in name.get_attribute("href")):
        print("IM IN HUR")
        name.click()
        #break
#driver.quit()
'''