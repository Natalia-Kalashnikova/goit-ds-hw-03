# 1.🐱 MongoDB Cats CRUD

This Python module provides basic **CRUD operations** for managing cat documents in a MongoDB collection.

---

## 🚀 Features

- Create a new cat document.
- Read (get) all cats or get a cat by name
- Update a cat's age
- Add a feature to a cat
- Delete a cat by name
- Delete all cats

---

## 📦 Tech Stack

- Python 3.13+
- pymongo
- python-dotenv
- MongoDB Atlas

---

# 2.📝 Quotes Scraper

A Python script to scrape [quotes.toscrape.com](http://quotes.toscrape.com) and import data into MongoDB.

---

## 📦 Tech Stack

- Python 3.13 + Poetry
- Requests + BeautifulSoup
- MongoDB Atlas
- dotenv

---

## Setup Instructions

1. Clone the repository or copy the script to your project.

2. Install dependencies with Poetry:

```bash
poetry install
```

3. Install dependencies with Poetry:

```bash
poetry add requests pymongo python-dotenv beautifulsoup4
```

4. Set up environment variables

Copy `.env.example` to `.env` and fill in your MongoDB Atlas URI:

5. Populate the database with sample data:

```bash
poetry python main.py
```

6. Import data into MongoDB:

```bash
poetry python mongo_import.py
```

---
