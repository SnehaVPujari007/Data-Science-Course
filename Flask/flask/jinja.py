### Jinja2 Template Engine
'''
{{}} expressions to print output in html
{%..%} conditions,for loop
{#...#}  comment section
'''
from flask import Flask , render_template,request,redirect,url_for
'''
It creates an instance of the Flask class,
 which will be your WSGI (Web server Gateway Interface) application
'''
###  WSGI application
app = Flask(__name__)
@app.route("/")
def welcome():
    return "<html> <H1>Welcome to the flask course </H1> </html>"
@app.route("/index",methods = ['GET'])
def index():
    return render_template('index.html')
@app.route("/about")
def about():
    return render_template("about.html")
@app.route("/submit", methods= ['GET','POST'])
def submit():
    if request.method=='POST':
        name = request.form['name']
        return f'Hello {name}! '
    return render_template('form.html')
## Variable Rule 
@app.route('/successif/<int:score>')
def successif(score):
    return render_template('result.html',results=score)

@app.route('/fail/<int:score>')
def fail(score):
    return render_template('result.html',results=score)
    
@app.route('/data',methods = ['POST','GET'])
def data():

    total_score = 0
    if request.method == 'POST':
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        c = float(request.form['c'])
        data_science = float(request.form['datascience'])
        total_score = (science+maths+c+data_science)/4
    else:
        return render_template('data.html')
    return redirect(url_for('successif',score = total_score))


   

if __name__== "__main__":
    app.run(debug= True)

