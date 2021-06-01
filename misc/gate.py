import json

import requests
from bs4 import BeautifulSoup


def grab_gate_prev_papers():
    page = requests.get("https://www.geeksforgeeks.org/original-gate-previous-year-question-papers-cse-and-it-gq/")
    soup = BeautifulSoup(page.content, 'html.parser')

    # grab all links
    all_links = soup.select('td a', href=True)

    results = []
    temp = {}
    year = "2021"

    for link in all_links:
        text = link.text.lower().strip()
        y = text.split(" ")[0]

        if year in text:
            temp[text] = link.get("href")
        else:
            if temp:
                results.append(temp)
            temp = {text: link.get("href")}
            year = y

    f = open("links.json", "w")
    f.write(json.dumps(results))


if __name__ == "__main__":
    grab_gate_prev_papers()
