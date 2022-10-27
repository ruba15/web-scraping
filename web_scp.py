import requests
from bs4 import BeautifulSoup

url = 'https://in.indeed.com/jobs?q=data%20analyst%20&l=Chennai%2C%20Tamil%20Nadu&vjk=07233c22eddb367e'

page = requests.get(url)

from csv import writer

soup = BeautifulSoup(page.content, 'html.parser')
jobs = soup.find_all('table', class_='jobCard_mainContent big6_visualChanges')

salary =''
with open('indeed.csv', 'w', newline='', encoding = 'utf8') as f:
    thewriter = writer(f)
    header = ['Title', 'Company', 'Location', 'Salary']
    thewriter.writerow(header)
    
    
    for job in jobs:
        title = job.find('a', class_="jcs-JobTitle").text
        company = job.find('span', class_="companyName").text
        Location = job.find('div', class_="companyLocation").text
        salary1 = job.find('span', class_="icl-u-xs-mr--xs attribute_snippet")
        if salary1:
            salary = salary1.text 
        else:
            salary = "Not Mentioned"
            
        details = [title, company, Location, salary]
        thewriter.writerow(details) 
