from flask import Flask, render_template,request
from wikiAPI import getContent
from webDetect import runDetector

app =  Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    topic = request.form['topic']
    if 'myFile' in request.files:
        myFile = request.files['myFile']
        print("image ",myFile)

    else:
        myFile = None

    return topic


def callWebScraper(topic):
	scrapedJSON = getContent(topic)
	print(scrapedJSON)


def callPhotoDetector(imgPath):
	photoJSON = runDetector(imgPath)
	print(photoJSON)

if __name__ == '__main__' :
    app.run()
                               