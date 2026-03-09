# 🎬 JustWatch Movie Data Scraper

## 📌 Project Overview
This project scrapes movie data from **JustWatch** using Python.  
The scraper collects movie information such as title, genre, runtime, IMDb rating, number of reviews, director, main actor, and production country.

The goal of this project is to build a **clean movie dataset for data analysis and visualization**.

---

## ⚙️ Tools & Technologies
- Python
- Selenium
- BeautifulSoup
- Pandas
- WebDriver Manager

---

## 🗂 Dataset Information

The dataset contains information for **800+ movies** scraped from JustWatch.

### Columns

| Column | Description |
|------|------|
| title | Movie title |
| year | Release year |
| genre | Primary genre |
| runtime_in_min | Runtime in minutes |
| imdb_rating | IMDb rating |
| no_of_reviews | Number of IMDb reviews |
| director | Movie director |
| actor | Main actor |
| country | Production country |
| url | Movie page URL |

---

## 🔎 Scraping Workflow

1. Open JustWatch movie listing page
2. Scroll the page to load all movies
3. Extract movie URLs
4. Visit each movie page
5. Save HTML pages
6. Parse HTML using BeautifulSoup
7. Clean and structure the data
8. Create a final dataset using Pandas

Pipeline:

Website → Selenium Scraping → HTML Storage → BeautifulSoup Parsing → Clean Dataset

---

## 📂 Project Structure

movie-data-scrapping-justwatch
├── demo-selenium-yutube-video
│
│── justwatchscraper.py
│
├ notebooks
│ └── data_processing.ipynb
│
├── data
│ └── movies_dataset.csv
│
└── README.md


---

## 📊 Example Dataset

| title | year | genre | runtime_in_min | imdb_rating |
|------|------|------|------|------|
| Baahubali | 2015 | Action & Adventure | 159 | 8.0 |
| Inception | 2010 | Sci-Fi | 148 | 8.8 |

---

## 🚀 Future Improvements

- Add more movies to the dataset
- Perform exploratory data analysis (EDA)
- Build movie recommendation system
- Create a dashboard using Streamlit

---

## 📜 Disclaimer
This project is created for **educational and data analysis purposes only**.

---

## 👤 Author
**Mohd Iqbal**

GitHub:  
https://github.com/iqbal188
