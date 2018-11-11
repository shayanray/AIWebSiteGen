import os
from flask import Flask, render_template,request
from wikiAPI import getContent
from webDetect import runDetector
from jsonmerge import merge
import json

app =  Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    topic = request.form['topic']
    if 'myFile' in request.files:
        imgfile = request.files['myFile']
        imgfile.save(os.path.join('uploaded',imgfile.filename))
        photoJSON  = callPhotoDetector(os.path.join('uploaded',imgfile.filename))
        print("photoJSON >>>>>>>>>>> ",photoJSON)
        #print(" image >>> ",imgfile)

        scrapedJSON = callWebScraper(topic)
        print("scrapedJSON >>> ", scrapedJSON)

        dictA = json.loads(scrapedJSON)
        dictB = json.loads(photoJSON)

        merged_dict = {key: value for (key, value) in (dictA.items() + dictB.items())}
        resultJSON = json.dumps(merged_dict)

        #resultJSON = {"content" : scrapedJSON.position , "position" : photoJSON.position}
        print("merged JSON ....................... ",resultJSON)
    else:
        myFile = None

    #url_for('success',name = user)
    return redirect("https://aiwebsitegen.lib.id/Test@dev/?jsonip=test")


def callWebScraper(topic):
	scrapedJSON = getContent(topic)
	return scrapedJSON


def callPhotoDetector(imgPath):
	photoJSON = runDetector(imgPath)
	
	return photoJSON

if __name__ == '__main__' :
    app.run()
                               