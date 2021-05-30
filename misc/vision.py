import requests
import csv
from bs4 import BeautifulSoup


def grab_from_notesclues():
    page = requests.get("https://www.notesclues.com/upsc-pdf/vision-ias-mains-test-series-pdf/")
    soup = BeautifulSoup(page.content, 'html.parser')

    # document.querySelectorAll("tbody.row-hover>tr")
    tbodies = soup.select('tbody.row-hover>tr')
    header = ['Test No', 'Date', 'Subject', 'Question', 'Answer']

    with open('vision-mains-2020-notesclues.csv', 'w', encoding='UTF8', newline='') as f:
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


def grab_from_upscpdf():
    page_no = 1
    page = requests.get(f"https://upscpdf.com/mains-test-test-series/english-vision-ias-mains-test/page/{page_no}")
    soup = BeautifulSoup(page.content, 'html.parser')

    # document.querySelectorAll("tbody.row-hover>tr")
    post_pages = soup.select('h2.post-box-title a', href=True)
    # header = ['Test No', 'Date', 'Subject', 'Question', 'Answer']

    # with open('vision-mains-2020-upscpdf.csv', 'w', encoding='UTF8', newline='') as f:
    #     writer = csv.writer(f)
    #     writer.writerow(header)

    f = open("vision-2020-mains-upscpdf.txt", "a")

    for post_page in post_pages:
        # post url
        post_url = post_page.get('href')
        # extract test number
        test_no = " ".join(x.capitalize() for x in post_url.split("2020-")[1].split("-with")[0].split('-'))
        # fetch post page
        post = requests.get(post_url)
        # soup
        post_soup = BeautifulSoup(post.content, 'html.parser')

        # case 1: td>h3>a
        case1_links = post_soup.select("td h3 a", href=True)

        if len(case1_links) > 0:
            for link in case1_links:
                if "Click Here To Download" in link.text:
                    f.write(f"{test_no}: {link.get('href')}\n")

        else:
            # case 2 (old): strong>span>span>a
            case2_spans = post_soup.select("ul li strong>span>span", )

            for span in case2_spans:
                if "Question" in span.text:
                    f.write(f"{test_no} (question): {span.find('a', href=True).get('href')}\n")
                else:
                    f.write(f"{test_no} (solution): {span.find('a', href=True).get('href')}\n")

    f.close()
    print("Done!")


if __name__ == "__main__":
    grab_from_notesclues()
    # grab_from_upscpdf()
