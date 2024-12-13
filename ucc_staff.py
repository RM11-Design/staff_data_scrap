from bs4 import BeautifulSoup
import requests
import csv

page = requests.get('https://www.cubsucc.com/faculty-directory/')

soup = BeautifulSoup(page.text, 'html.parser')

names = soup.findAll("span", attrs={"class":"name"})
departments = soup.findAll("span",attrs={"class":"department"})

file = open("UCC_name_department.csv","w")
write = csv.writer(file)

write.writerow(["NAME","DEPARTMENT"])

for name,department in zip(names,departments):
    print(name.text + " - " + department.text)
    write.writerow([name.text,department.text])
file.close()
