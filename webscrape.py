from bs4 import BeautifulSoup
import requests
import os.path

def webscrape(folder_path, startChapter, endChapter, websiteURL):
    index = websiteURL.rfind("-")
    websiteURL = websiteURL[:index]
    websiteURL += "-"
    for i in range(startChapter, endChapter):
        url = websiteURL + str(i)
        response = requests.get(url = url, headers = {"User-Agent": "Mozilla/5.0"})
        html_content = response.content
        soup = BeautifulSoup(html_content, "html.parser")

        paragraphs = soup.find_all("p")
        text = []
        for paragraph in paragraphs:
            text.append(paragraph.text.strip())

        with open(os.path.join(folder_path, f"Chapter {i}.txt"), "w") as file:
            for line in text:
                file.write(f"{line}\n")
                file.write("\n")
        file.close()