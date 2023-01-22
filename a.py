import re

from bs4 import BeautifulSoup
import requests
from csv import writer
linkUnder = r"https://www.food.be/companies/3-fonteinen"

pageUnder = requests.get(linkUnder)

soupUnder = BeautifulSoup(pageUnder.content, "html.parser")

listsCompanySpecs = soupUnder.find('div', class_="company-specs")

website = []
find = []
address = []
street = ""
zipCodeCity = ""
i = 0
c  = 0
#website
for listUnder in listsCompanySpecs:
    # i+=1
    # print("{} = {}".format(i,listUnder))
    # print("-"*30)

    if str(listUnder).find('website') >=0:
    #     print(listUnder.text)
        website.append(listUnder.text)


listsContactInfo = soupUnder.find_all('div', class_="contact-info__section")
name = soupUnder.find('div', class_ = 'field--name-field-company-contact').text
about  = soupUnder.find('div', class_ = 'text-formatted').text
brands  = soupUnder.find('div', class_ = 'table-scroll').text.replace("\n"," ")

for listUnder in listsContactInfo:
    # i+=1
    # print("{} = {}".format(i,listUnder))
    # print("-"*30)
    if str(listUnder).find('maps') >= 0:
        for list in listUnder:
            if str(list).find('maps')>=0:
                for a in list:
                    address.append(a.text)

                    #street
                    if c == 1:
                        street = a.text

                    #zipCodeCity
                    elif c == 3:
                        zipCodeCity = a.text
                    c+=1
            #tel
            if str(list).find('tel') >= 0:
                for a in list:
                    tel = a.text

            # mail
            if str(list).find('mail') >= 0:
                for a in list:
                    mail = a.text



print("zipCode City = {}".format(zipCodeCity))
print("street = {}".format(street))
print("website = {}".format(website))
print("tel = {}".format(tel))
print("mail = {}".format(mail))
print("name = {}".format(name))
print("about = {}".format(about))
print("brands = {}".format(brands))


# print("find = {}".format(find))
