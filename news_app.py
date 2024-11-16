# if you want scrap a website
#install requests
#install bs4 as beautifulsoup
#install pandas as pd
#install streamlit as st
#install html5lib

# news scrap
import requests
from bs4 import BeautifulSoup
import pandas as pd
import streamlit as st
from datetime import datetime
st.title("News Dashboard")
# category_filter = st.selectbox("Select Category", CATEGORIES)
date_filter = st.date_input("Select Date")
# news_df = pd.concat([scrape_news(category) for category in CATEGORIES])

# filtered_df = news_df[(news_df['Category'] == category_filter) &
# (news_df['Date'].str.contains(str(date_filter).split(' ')[0]))]
# st.write(filtered_df)
if st.button("View Article Summaries"):
# for index, row in filtered_df.iterrows():
# st.subheader(row['Title'])
#st.write(row['Summary'])

# News website URL
# URL= "https://edition.cnn.com"

#Categories to scrape
 CATEGORIES = ["world", "politics", "business", "tech"]
 print(CATEGORIES)
def scrape_news_articles(category):
    articles = []
    response = requests.get(f"{"URL"}/{category}")
    soup = BeautifulSoup(response.content, 'html.parser')
    print(response)
    print(soup)

    # Extract article titles, publication dates, and short summaries
    article_elements = soup.find_all('article')
    for article in article_elements:
        title = article.find('h3').text.strip()
        date = article.find('span', class_='meta').text.strip()
        summary = article.find('p').text.strip()
        articles.append({
            'Title': title,
            'Date': date,
            'Summary': summary,
            'Category': category
        })
    
    return pd.DataFrame(articles)

# Scrape news articles
news_df = pd.concat([scrape_news_articles(category) for category in CATEGORIES])

# Streamlit App
st.title("News Dashboard")

# Category filter
category_filter = st.selectbox("Select Category", CATEGORIES)
print(category_filter)

# Date filter
date_filter = st.date_input("Select Date")
print(date_filter)

# Display news articles
filtered_df = news_df[(news_df['Category'] == category_filter) & 
                     (news_df['Date'].str.contains(str(date_filter).split(' ')[0]))]
st.write(filtered_df)
print(filtered_df)

# Display article summaries
if st.button("View Article Summaries"):
    for index, row in filtered_df.iterrows():
        st.subheader(row['Title'])
        st.write(row['Summary'])