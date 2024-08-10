from bs4 import BeautifulSoup
import requests

#Via API We are fetching the website for scraping
response=requests.get("https://appbrewery.github.io/news.ycombinator.com/")
yc_webpage=response.text
soup=BeautifulSoup(yc_webpage,"html.parser")
#print(soup.title) - to get hold of the title tag completely
#print(soup.title.text) - to get hold of the text of the title tag

article_text=[]
article_links=[]
soup_all=soup.find_all(name="a",class_="storylink")
for soup_individual in soup_all:
    only_Name=soup_individual.getText()
    article_text.append(only_Name)
    only_link=soup_individual.get("href")
    article_links.append(only_link)

article_votes=[]
votes_all=soup.find_all(name="span",class_="score")
for vote in votes_all:
    article_votes.append(int(vote.getText().split(" ")[0])) #splitting the string and converting them into an integer itself

print(article_text)
print(article_links)
print(article_votes)

lim=max(article_votes)
max_index=article_votes.index(lim)
print(f"The book which was written by {article_text[max_index]} which is in the link {article_links[max_index]} was highest read with {article_votes[max_index]}")