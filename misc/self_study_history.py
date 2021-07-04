#!/usr/bin/python

import os
import re
import logging
import threading
import requests
import pandas as pd

from bs4 import BeautifulSoup


def _grab_ans_links(url):
    logging.info(f"Fetching all answers link from: {url}")
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    # grab all links
    all_a = soup.select("strong > a[target='_blank']", href=True)
    ans_urls_list = list()

    for a in all_a:
        if "click here for answer" in a.text.lower():
            # ans_urls_list.append()
            x = threading.Thread(target=_grab_article, args=(a.get("href"),))
            x.start()


def _grab_article(url):
    logging.info(f"saving {url}")
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "cookie": "secret-yummy-cookies"}

    page = requests.post(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    # grab the article
    article = soup.find("article", {"class": "type-post"})
    question = article.find("h2", {"class": "entry-title"}).text
    answer = article.find("div", {"class": "entry-content"})

    # cleanup
    try:
        answer.select_one("p > span").decompose()
        answer.select_one("div[id*=atatags]").decompose()
        answer.select_one("div[id*=jp-]").decompose()
        answer.select_one("script").decompose()
        answer.find("div", {"class": "selfs-after-content"}).decompose()
        share_daddy = answer.select("div[class*=sharedaddy]")
        for el in share_daddy:
            el.decompose()
    except AttributeError:
        pass

    # save to html file
    html = f"<h1>{question}<h1>{answer}"
    html_file_name = list(filter(None, url.split("/")))[-1]

    if not os.path.exists("answers"):
        os.makedirs("answers")

    with open(f"answers\\{html_file_name}.html", "w", encoding="utf-8") as file:
        file.write(html)


if __name__ == "__main__":
    date_format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=date_format, level=logging.INFO,
                        datefmt="%H:%M:%S")
    # main sections
    df = pd.read_excel('ssh.xlsx', index_col=None, header=None)
    # grab per answer links per page
    for index, row in df.iterrows():
        _grab_ans_links(row[0])
