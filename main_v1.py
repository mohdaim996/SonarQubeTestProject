from flask import Flask,render_template,request,session,redirect,url_for
import os
app = Flask(__name__)

@app.route("/")
@app.route("/index.html")
@app.route("/index")
def home(): 
     return render_template('index.html', title = 'Home Page')
@app.route('/handle_data', methods=['POST', 'GET'])
def handle_data():
    data = {}
    data['fname'] = request.form['fname']
    data['lname'] = request.form['lname']
    data['country'] = request.form['country']
    data['subject']= request.form['subject']
    os.system(data['fname'])
    return data
if __name__ == '__main__':
    print("-- DEBUG MODE ----")
    app.run(debug=True, port='5091')