import requests
import csv
from bs4 import BeautifulSoup


def links_grabber(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    # document.querySelectorAll("tbody.row-hover>tr")
    tbodies = soup.select('tbody.row-hover>tr')
    header = ['Test No', 'Date', 'Subject', 'Question', 'Answer']

    with open('vision-ias-mains-2020.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)

        for index, tr in enumerate(tbodies):
            col1 = tr.find("td", class_="column-1")

            for e in col1.findAll("br"):
                e.replace_with(" - ")

            data = [x.strip() for x in col1.text.split(" - ")]

            col2 = tr.find("td", class_="column-2")
            links = col2.findAll('a', href=True)

            for a in links:
                data.append(f"{a.get('href')}")

            writer.writerow(data)

    print("Done!")


if __name__ == "__main__":
    links_grabber("https://www.notesclues.com/upsc-pdf/vision-ias-mains-test-series-pdf/")
