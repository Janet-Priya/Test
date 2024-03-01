
import requests
from bs4 import BeautifulSoup

def scrape_news():
    url = "https://timesofindia.indiatimes.com/home/headlines"
    response = requests.get(url)
    if response.status_code == 200:
        page_content = response.text
        soup = BeautifulSoup(page_content, "html.parser")
        articles = soup.find_all("tr", class_="athing")
        
        for index, article in enumerate(articles, start=1):
            title = article.text
            article_url = article # Use a different variable name for the URL attribute
            print(f"Article {index}: {title}\nURL: {article_url}\n")  # Use the new variable name here
    else:
        print(f"Failed to fetch content from {url}")

if __name__ == "__main__":
    scrape_news()


