from bs4 import BeautifulSoup
import requests
from csv import writer
for i in range(0,1):
    url = "https://www.food.be/companies/search?search_api_fulltext=&page={}".format(i)
    page = requests.get(url)

    soup = BeautifulSoup(page.content, "html.parser")
    lists = soup.find_all('div', class_="views-row")


    with open(r"C:\Users\marek\PycharmProjects\PythonDlaSrednioZaawansowanych\Other projects\food.csv",'a',encoding='utf8',newline='')as f:

        thewriter = writer(f)
        header = ['Company name', 'Product Type']
        thewriter.writerow(header)

        for list in lists:
            companyName = list.find('h3', class_ ="companies__item__title").text
            productType = list.find('div', class_ = "companies__item__categories").text.replace("\n","")

            info = [companyName, productType]
            thewriter.writerow(info)

            linkUnder = r"https://food.be/companies/{}".format(companyName.lower().replace(" ","-"))

            pageUnder = requests.get(linkUnder)

            soupUnder = BeautifulSoup(pageUnder.content, "html.parser")


            listsUnder = soupUnder.find_all('div', class_="company-detail__section")

            for listUnder in listsUnder:
                    phone = listUnder.find('div', class_='row').text.split("\n")
                    wordList = []
                    for word in phone:
                        wordList.append(word)
                    thewriter.writerow(wordList)






