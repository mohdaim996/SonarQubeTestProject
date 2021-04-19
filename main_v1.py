from flask import Flask,render_template,request,session,redirect,url_for
import os

app = Flask(__name__)
username='admin'
password='admin'

@app.route("/")
def home(): 
    url = request.args.get('page')
    if url != None:
        return redirect(url)
    return render_template('index.html', title = 'Home Page')
@app.route("/admin")
def admin():
    return render_template('admin.html', title = 'admin login')
@app.route('/admin_check',methods=['POST', 'GET'])
def admin_check():
    name = request.form['name']
    pswrd = request.form['password']
    if (name == username) & (pswrd == password):  
        log = open('log.txt') 
           
        return render_template('adminBoard.html', title = 'admin board', log=log.read())
    else: 
        return redirect(url_for(admin()))
@app.route('/handle_data', methods=['POST', 'GET'])
def handle_data():
    data = {}
    data['fname'] = request.form['fname']
    data['lname'] = request.form['lname']
    data['country'] = request.form['country']
    data['subject']= request.form['subject']
    return os.popen(f' echo {data} >> log.txt').read()
     #text & type main_v1.py & echo text
if __name__ == '__main__':
    print("-- DEBUG MODE ----")
    app.run(debug=True, port='3000')
