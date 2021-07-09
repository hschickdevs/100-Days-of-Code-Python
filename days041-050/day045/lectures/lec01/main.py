from bs4 import BeautifulSoup

with open('website.html') as file:
    contents = file.read()

soup = BeautifulSoup(contents, 'html.parser')
print(soup.title)
print(soup.title.name)
print(soup.title.string)
print()

print(soup.prettify())
print()

print(soup.a)
print(soup.li)
print(soup.p)
print()

anchor_tags = soup.find_all(name='a')
print(anchor_tags)
print()

for tag in anchor_tags:
    print(tag.getText(), tag.get("href"))
print()

heading = soup.find(name="h1", id="name")
print(heading)
print(heading.getText())
print()

section_heading = soup.find(name="h3", class_="heading")
print(section_heading)
print(section_heading.getText())
print(section_heading.name)
print(section_heading.get("class"))
print()

company_url = soup.select_one(selector="p a")
print(company_url)

name = soup.select_one(selector="#name")
print(name)

headings = soup.select(selector='.heading')
print(headings)
