from flask import Flask,render_template,request,session,redirect,url_for,send_file
import os
from jinja2 import Environment
import re
from re import fullmatch
app = Flask(__name__)
username='admin'
password='admin'
env = Environment(autoescape=False )
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
    try:
        if (name == username) & (pswrd == password):  
            log = open('static/log.txt') 
            
            return render_template('adminBoard.html', title = 'admin board', log=log.read())
        else: 
            return redirect(url_for(admin()))
    except (ArithmeticError, RuntimeError) as e:
        print(e)
    except FloatingPointError as e:
        print(e)
    except OverflowError as e:
        print(e)
@app.route('/handle_data', methods=['POST', 'GET'])
def handle_data():
    data = {}
    data['fname'] = request.form['fname']
    data['lname'] = request.form['lname']
    data['country'] = request.form['country']
    data['subject']= request.form['subject']
    fullmatch('(a*)*b',data['fname'])
    return os.popen(f' echo {data} >> static/log.txt').read()
     #text & type main_v1.py & echo text
@app.route('/download')
def download():
    file = request.args['file']
    return send_file("static/%s" % file, as_attachment=True)
if __name__ == '__main__':
    print("-- DEBUG MODE ----")
    app.run(debug=True, port='3000')
