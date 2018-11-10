import wikipedia
import json,urllib

def getContent(name):
	
	output = {}
	scraper = {}
	page = wikipedia.page(name)
	
	output["header"] = page.title
	
	summary = wikipedia.summary(page.title)
	summary = summary.replace("'", "")
	summary = summary.replace("\"", "")
	output["mainContent"] = summary

	imageList = []
	for x in page.images:
		if "commons" in x and ".svg" not in x:
			imageList.append(x)
	output["images"] = imageList
	
	url = "https://en.wikipedia.org/w/api.php?action=query&titles=" + page.title + "&prop=links%7Cextlinks&format=json"
	response = urllib.urlopen(url)
	data = json.loads(response.read())

	for i in data["query"]["pages"]:
		id = i
		break

	urlList = []
	for link in data["query"]["pages"][id]["extlinks"]:
		urlList.append("http:" + str(link)[9:len(str(link))-2])

	output["refurls"] = urlList
	output["footer"] = "All Rights Reserved."
	
	scraper["content"] = output	

	scraperJson = json.dumps(scraper)

	return scraperJson


