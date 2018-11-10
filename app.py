from flask import Flask, render_template,request
app =  Flask(_name_)
@app.route('/hello/')
@app.route('/hello/<name>')
def pajamas(name=None):
    return render_template('hello.html',name=name)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if _name_ == '_main_' :
    app.run()
