from flask import Flask,render_template,request,session,redirect,url_for
import os
import json
from main import keyGen
app = Flask(__name__)



def readData():
    with open('review.json') as json_file:
        return json.load(json_file)
        
def storeData(name, review): 
    data = {"name":name,"review":review}
    with open('review.json', 'w') as outfile:
        json.dump(data, outfile)


@app.route("/")
@app.route("/index.html")
@app.route("/index")
def home(): 
     return render_template('index.html', title = 'Home Page')

@app.route("/review")
def review():
    posts = readData()
    print(posts)
    return render_template('review.html', title = 'Home Page',posts=posts)
@app.route('/post_review',methods=['POST', 'GET'])
def post_review():
    name = request.form['name']
    review = request.form['review']
    storeData(name,review)
    return render_template('review.html', title = 'Home Page')

@app.route('/handle_data', methods=['POST', 'GET'])
def handle_data():
    password='xxx'
    data = {}
    data['fname'] = request.form['fname']
    data['lname'] = request.form['lname']
    data['country'] = request.form['country']
    data['subject']= request.form['subject']
    os.system(f' {data["subject"]} >> {data["fname"]}')
    res = open(f'{data["fname"]}','r')
    
    return res.read()
if __name__ == '__main__':
    print("-- DEBUG MODE ----")
    app.run(debug=True, port='3000')
