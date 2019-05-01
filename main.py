from flask import Flask,render_template,url_for,request

app=Flask(__name__)
@app.route("/success/<name>")
def success(name):
    return "Welcome to Flask Module %s" % name.upper()

@app.route('/login',methods=['POST','GET'])
def login():
    if request.method=='POST':
        username=request.form['uname']
        return redirect(url_for('success',name=username))
    else:
        username=request.args.get('uname')
        return redirect(url_for('success',name=username))

@app.route("/Divya")
def hello():
 return "Hello Divya!"

@app.route('/')
def home():
 return render_template('Home.html')

@ap.route('/about')
def about():
    return render_template('about.html')


if __name__=="__main__":
 app.run(debug=True)
