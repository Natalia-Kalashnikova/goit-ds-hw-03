import json
import requests
from bs4 import BeautifulSoup
from typing import List, Dict, Set, Tuple


def get_soup(url: str, timeout: float = 10) -> BeautifulSoup:
    """Return BeautifulSoup object for the given URL."""
    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()
        return BeautifulSoup(response.text, "html.parser")
    except requests.exceptions.Timeout:
        print(f"Timeout while trying to access {url}")
        raise
    except requests.exceptions.RequestException as e:
        print(f"Error while accessing {url}: {e}")
        raise


def parse_author_details(author_url: str) -> Dict:
    """Parse author details from the author's page."""
    soup = get_soup(author_url)
    fullname = soup.find("h3", class_="author-title").text.strip()
    born_date = soup.find("span", class_="author-born-date").text.strip()
    born_location = soup.find("span", class_="author-born-location").text.strip()
    description = soup.find("div", class_="author-description").text.strip()
    return {
        "fullname": fullname,
        "born_date": born_date,
        "born_location": born_location,
        "description": description,
    }


def scrape_quotes_and_authors(base_url: str) -> Tuple[List[Dict], List[Dict]]:
    """Scrape all quotes and authors from the site."""
    quotes = []
    authors_seen: Set[str] = set()
    authors = []

    page = 1
    while True:
        url = f"{base_url}/page/{page}/"
        soup = get_soup(url)
        quote_blocks = soup.find_all("div", class_="quote")
        if not quote_blocks:
            break
        for block in quote_blocks:
            text = block.find("span", class_="text").text.strip()
            author = block.find("small", class_="author").text.strip()
            tags = [tag.text for tag in block.find_all("a", class_="tag")]
            quotes.append({"tags": tags, "author": author, "quote": text})
            if author not in authors_seen:
                author_link = block.find("a")["href"]
                author_url = f"{base_url}{author_link}"
                author_data = parse_author_details(author_url)
                authors.append(author_data)
                authors_seen.add(author)
        page += 1
    return quotes, authors


def save_json(data: List[Dict], filename: str) -> None:
    """Save data to a JSON file with UTF-8 encoding."""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def main():
    """Main entry point for scraping quotes and authors."""
    base_url = "http://quotes.toscrape.com"
    quotes, authors = scrape_quotes_and_authors(base_url)
    save_json(quotes, "quotes.json")
    save_json(authors, "authors.json")


if __name__ == "__main__":
    main()
