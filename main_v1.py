from flask import Flask,render_template,request,session,redirect,url_for
import os

app = Flask(__name__)
username='admin'
password='admin'
def readData():
    with open('review.json') as json_file:
        return json.load(json_file)       
def storeData(name, review): 
    data = {"name":name,"review":review}
    with open('review.json', 'w') as outfile:
        json.dump(data, outfile)
@app.route("/")
def home(): 
    url = request.args.get('page')
    if url != None:
        return redirect(url)
    return render_template('index.html', title = 'Home Page')
@app.route("/admin")
def admin():
    return render_template('admin.html', title = 'Home Page')
@app.route('/post_review',methods=['POST', 'GET'])
def post_review():
    name = request.form['name']
    review = request.form['review']
    storeData(name,review)
    return render_template('review.html', title = 'Home Page')
@app.route('/handle_data', methods=['POST', 'GET'])
def handle_data():
    data = {}
    data['fname'] = request.form['fname']
    data['lname'] = request.form['lname']
    data['country'] = request.form['country']
    data['subject']= request.form['subject']
    return os.popen(f' type {data["subject"]} >> log.txt').read()
     #text & type main_v1.py & echo text
if __name__ == '__main__':
    print("-- DEBUG MODE ----")
    app.run(debug=True, port='3000')
