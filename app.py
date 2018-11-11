import os
import urllib
from flask import Flask, render_template,request, redirect
from wikiAPI import getContent
from webDetect import runDetector
from jsonmerge import merge
import json
import requests

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

        dictA = json.loads(scrapedJSON, object_hook=_byteify)
        dictB = json.loads(photoJSON, object_hook=_byteify)

        print("\n\ndictB JSON ....................... ",dictB)
        merged_dict = {key: value for (key, value) in (dictA.items() + dictB.items())}
        final = {"jsonip" : merged_dict }
        resultJSONstr = json.dumps(final, separators=(',',':'), ensure_ascii=False)
        resultJSON = json.loads(resultJSONstr)


        #resultJSON = {"content" : scrapedJSON.position , "position" : photoJSON.position}
        print("final JSON ....................... ",final)
    else:
        myFile = None

    #url_for('success',name = user)
    #encodedJSON = urllib.urlencode(resultJSON)
    #print("\n\n encodedJSON ....................... ",encodedJSON)
    #return redirect("https://aiwebsitegen.lib.id/Test@dev/?jsonip="+resultJSON)
    encodedurl =  _byteify(urllib.urlencode(final)) #resultJSON
    #encodedurl = urllib.unquote_plus(encodedurl)
    print("encodedurl JSON ....................... ",encodedurl) 
    urlai = "https://aiwebsitegen.lib.id/Test@0.0.4/?"
    print("\n\n\n"+urlai+encodedurl)
    return redirect(urlai+encodedurl ) #,code=307
    #res = requests.post(urlai, json=resultJSON)
    #print 'response from server:',res.text
    #return requests.post(urlai, data=resultJSON, allow_redirects=True)


def _byteify(data, ignore_dicts = False):
    # if this is a unicode string, return its string representation
    if isinstance(data, unicode):
        return data.encode('utf-8')
    # if this is a list of values, return list of byteified values
    if isinstance(data, list):
        return [ _byteify(item, ignore_dicts=True) for item in data ]
    # if this is a dictionary, return dictionary of byteified keys and values
    # but only if we haven't already byteified it
    if isinstance(data, dict) and not ignore_dicts:
        return {
            _byteify(key, ignore_dicts=True): _byteify(value, ignore_dicts=True)
            for key, value in data.iteritems()
        }
    # if it's anything else, return it in its original form
    return data

def callWebScraper(topic):
	scrapedJSON = getContent(topic)
	return scrapedJSON


def callPhotoDetector(imgPath):
	photoJSON = runDetector(imgPath)
	
	return photoJSON

if __name__ == '__main__' :
    app.run()
                               