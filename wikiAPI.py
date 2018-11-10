import wikipedia
import json,urllib

print 'Type in article name:'
name = raw_input()

print ("Image Links")
page = wikipedia.page(name)

for x in page.images:
	print(x)

print("\n\n\n\n\n")

title = page.title

url = "https://en.wikipedia.org/w/api.php?action=query&titles=" + title + "&prop=links%7Cextlinks&format=json"
response = urllib.urlopen(url)
data = json.loads(response.read())

for i in data["query"]["pages"]:
	id = i
	break

print("Source links")
for link in data["query"]["pages"][id]["extlinks"]:
	print link
print('\n\n\n\n\n')
print('Summary')
print wikipedia.summary(title)

