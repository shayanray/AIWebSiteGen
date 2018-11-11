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
		id0 = i
		break
	
	whole = page.content
	whole = whole.encode('ascii','ignore') 
	startIndex = whole.index("External links") + 18

	urlList = []
	for link in data["query"]["pages"][id0]["extlinks"]:
		print("startIndex >> ", startIndex)
		try:
			endIndex = whole.index("\n", startIndex)
		except:
			continue
		if endIndex:
			temp = whole[startIndex: endIndex]
			temp = temp.replace("'", "")
			temp = temp.replace("\"", "")
			keyvalue = {}
			if len(temp) > 40:
				keyvalue["title"] = temp[0:40] + "..."
			else:
				keyvalue["title"] = temp
			keyvalue["url"] = "http:" + str(link)[9:len(str(link))-2]
			urlList.append(keyvalue)
			startIndex = endIndex + 1
		
	
	shareList= ["http://chittagongit.com//images/facebook-share-icon-png/facebook-share-icon-png-9.jpg", "https://www.green-marine.org/wp-content/uploads/2015/08/Twitter_logo-325x325.png"]
	output["refurls"] = urlList
	output["share"] = shareList
	output["footer"] = "All Rights Reserved."
	
	scraper["content"] = output	

	scraperJson = json.dumps(scraper)

	return scraperJson
	
	
