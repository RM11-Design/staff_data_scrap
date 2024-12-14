from bs4 import BeautifulSoup
import requests
import csv

page = requests.get('https://www.cubsucc.com/faculty-directory/')

soup = BeautifulSoup(page.text, 'html.parser')

names = soup.findAll("span", attrs={"class":"name"})         
titles = soup.findAll("span",attrs={"class":"jobTitle"})
departments = soup.findAll("span",attrs={"class":"department"})

with open("UCC_name_department.csv","w",newline="") as f:
    write = csv.writer(f)

    write.writerow(["NAME","TITLE","DEPARTMENT"])

    for name,title,department in zip(names,titles,departments):
        
        # Extracts name text
        name_text = name.a.contents[0].strip()
        # Extract title text
        title_text = title.text.strip()
        # Extract department text
        department_text = department.text.strip()
        
        print(name_text + " - " + title_text + " - " + department_text)

        write.writerow([name_text,title_text,department_text])

