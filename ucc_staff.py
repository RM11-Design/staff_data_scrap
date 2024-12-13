from bs4 import BeautifulSoup
import requests
import csv

page = requests.get('https://www.cubsucc.com/faculty-directory/')

soup = BeautifulSoup(page.text, 'html.parser')

names = soup.findAll("span", attrs={"class":"name"})
departments = soup.findAll("span",attrs={"class":"department"})

with open("UCC_name_department.csv","w",newline="") as f:
    write = csv.writer(f)

    write.writerow(["NAME","DEPARTMENT"])

    for name,department in zip(names,departments):
        
        name_text = name.find("a").text.strip() if name.find("a") else name.text.strip()
        # Extract department text
        department_text = department.text.strip()
        
        print(name_text + " - " + department_text)

        write.writerow([name_text,department_text])

