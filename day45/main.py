from bs4 import BeautifulSoup

with open("website.html") as file:
    contents=file.read()
soup=BeautifulSoup(contents,"html.parser")
# print(soup.title.name) #gives the name of tag i.e. title
# print(soup.prettify()) # its print all the data i html file  by prettyfying

#for printing all the tags----
# all_anchor_tags=soup.find_all(name="a")
# print(all_anchor_tags)
# for tag in all_anchor_tags:
#     print(tag.get("href")) #printing the anchor tags and links


