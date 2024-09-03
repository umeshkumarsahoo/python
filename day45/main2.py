import requests as req
from bs4 import BeautifulSoup

# Send a GET request to the Hacker News homepage
response = req.get(url="https://news.ycombinator.com/")
response.raise_for_status()

# Parse the HTML content of the page
yc_web = response.text
soup = BeautifulSoup(yc_web, "html.parser")

# Find all the span tags with the class "titleline"
article_tags = soup.find_all(name="span", class_="titleline")

article_text = []  # List to store article titles
article_link = []  # List to store article links

# Extract the title and link from each article tag
for article_tag in article_tags:
    a_tag = article_tag.find("a")  # Find the <a> tag within the <span>
    link = a_tag.get("href")  # Correctly extract the href attribute
    text = a_tag.getText()  # Extract the text of the <a> tag (title)
    article_text.append(text)
    article_link.append(link)

# Find the upvote counts
article_up_votes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

# Find the index of the article with the highest number of upvotes
max_vote_index = article_up_votes.index(max(article_up_votes))

# Print the title, upvotes, and link of the highest-voted article
print(f"Max vote article is '{article_text[max_vote_index]}' :: votes {article_up_votes[max_vote_index]} :: link is {article_link[max_vote_index]}")
