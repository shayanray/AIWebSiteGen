from flask import Flask, render_template,request
app =  Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    topic = request.form['topic']
    if 'myFile' in request.files:
        print("File is in there! yo..")
        myFile = request.files['myFile']

    else:
        myFile = None

    return topic

if __name__ == '__main__' :
    app.run()
                               