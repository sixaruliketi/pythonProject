from bs4 import BeautifulSoup
import requests as requests
import csv
from neo4j import GraphDatabase

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

# print(page.text)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id="ResultsContainer")

# print(results.prettify())


job_elements = results.find_all("div", class_="card-content")

python_jobs = results.find_all(
    "h2", string=lambda text: "python" in text.lower())

python_job_elements = [
    h2_element.parent.parent.parent for h2_element in python_jobs
]

element_names = ['title', 'link', 'company', 'location']
file = open('jobs4Project.csv', 'a', newline='', encoding='utf-8')
writer = csv.writer(file)
writer.writerow(element_names)
file.close()

for job_element in python_job_elements:
    title = job_element.find("h2", class_="title")
    company = job_element.find("h3", class_="company")
    location = job_element.find("p", class_="location")
    links = job_element.find_all("a")
    for link in links:
        link_url = link["href"]
    title_element = title.text.strip()
    company_element = company.text.strip()
    location_element = location.text.strip()

    file = open('jobs4Project.csv', 'a', newline='', encoding='utf-8')
    writer = csv.writer(file)
    fieldnames = ([title_element, link_url, company_element, location_element])
    writer.writerow(fieldnames)
    file.close()
