import requests

from bs4 import BeautifulSoup
import csv


class News:
    def __init__(self, title: str, url: str, script: str):
        self.title = title
        self.url = url
        self.script = script

    def __str__(self):
        return f'{self.title} {self.url} {self.script}'


class ParsedNews:

    def __init__(self, max_pages):
        self.data = self.get_data_news(max_pages)

    def save_data_to_csv(self, csv_file_name: str):
        with open(csv_file_name, 'w+', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=['title', 'url', 'script'])
            writer.writeheader()
            for news in self.data:
                writer.writerow({'title': news.title, 'url': news.url, 'script': news.script})

    def get_data_news(self, max_pages=2):
        res = []
        for index in range(1, max_pages + 1):
            url = f'https://krasnodarmedia.su/news/?page={index}'
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            }
            response = requests.get(url, headers=headers)
            data = response.text
            soup = BeautifulSoup(data, 'lxml')
            news = soup.find_all('a', attrs={'class': 'news-for-copy'})
            for n in news:
                news_title = n.text
                news_url = n['href']
                news_script = self.get_text_news(news_url)
                news_item = News(news_title, news_url, news_script)
                res.append(news_item)
        return res

    def get_text_news(self, url):

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        data = response.text
        soup = BeautifulSoup(data, 'lxml')
        n = soup.find_all(class_='page-content io-article-body d-block')
        full_text = ' '.join([p.get_text(strip=True) for p in n])
        return full_text


parser = ParsedNews(max_pages=1)
parser.save_data_to_csv('news8562.csv')