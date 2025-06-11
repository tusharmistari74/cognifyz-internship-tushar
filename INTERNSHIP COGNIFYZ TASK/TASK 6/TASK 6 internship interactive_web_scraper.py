import requests
from bs4 import BeautifulSoup
import random


visited_quotes = set()


def scrape_quotes():
    url = "http://quotes.toscrape.com/page/{}/"
    all_quotes = []

    for page in range(1, 6):
        response = requests.get(url.format(page))
        soup = BeautifulSoup(response.text, 'html.parser')
        quotes = soup.find_all("span", class_="text")
        authors = soup.find_all("small", class_="author")
        for quote, author in zip(quotes, authors):
            full_quote = f"\"{quote.text}\" — {author.text}"
            all_quotes.append(full_quote)

    print("\n💬 Quotes (Random & Unique):")
    shown = 0
    while shown < 5 and len(visited_quotes) < len(all_quotes):
        selected = random.choice(all_quotes)
        if selected not in visited_quotes:
            visited_quotes.add(selected)
            print(f"👉 {selected}")
            shown += 1
    if shown == 0:
        print("✅ All quotes have been shown.")

def scrape_hackernews():
    url = "https://news.ycombinator.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    titles = soup.select('.titleline > a')

    print("\n📰 Top Hacker News Headlines:")
    for i, title in enumerate(titles[:10], start=1):
        print(f"{i}. {title.text}")

def scrape_python_news():
    url = "https://hackertab.dev/topics/python"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    titles = soup.select('.blog-widget .menu li')

    print("\n🐍 Latest Python.org Blog Posts:")
    for i, post in enumerate(titles[:5], start=1):
        print(f"{i}. {post.text.strip()}")

def scrape_books():
    url = "http://books.toscrape.com/catalogue/category/books_1/index.html"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    books = soup.select('h3 a')

    print("\n📚 Featured Books:")
    for i, book in enumerate(books[:5], start=1):
        print(f"{i}. {book['title']}")

def scrape_motivation():
    url = "https://www.keepinspiring.me/famous-quotes/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    quotes = soup.find_all("blockquote")

    print("\n🌟 Famous Motivational Quotes:")
    for i, block in enumerate(quotes[:5], start=1):
        print(f"{i}. {block.get_text(strip=True)}")

def main():
    while True:
        print("\n🌐 INTERACTIVE WEB SCRAPER")
        print("1. Scrape Random Non-Repeating Quotes")
        print("2. Scrape Hacker News Headlines")
        print("3. Scrape Python.org Blog Titles")
        print("4. Scrape Book Titles (Books to Scrape)")
        print("5. Scrape Famous Motivational Quotes")
        print("6. Exit")

        choice = input("Choose an option (1–6): ").strip()
        if choice == '1':
            scrape_quotes()
        elif choice == '2':
            scrape_hackernews()
        elif choice == '3':
            scrape_python_news()
        elif choice == '4':
            scrape_books()
        elif choice == '5':
            scrape_motivation()
        elif choice == '6':
            print("👋 Exiting. Thank you for scraping!")
            break
        else:
            print("❌ Invalid input. Please choose a number from 1 to 6.")

if __name__ == "__main__":
    main()