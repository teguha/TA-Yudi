from multiprocessing.dummy import active_children
from flask import Flask , render_template, url_for , request ,redirect , session, flash, jsonify
# import pymysql
import uuid
import re
import time
import os 
import bcrypt
import hashlib

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html',title="wakanda report")
    # return "Hello, World!"


@app.route("/login" , methods=['GET' , 'POST'])
def login():
    error = None
    if request.method =='POST':
        username = request.form['username']
        passw = request.form['password'].encode('utf-8')
        md5 = hashlib.md5()
        md5.update(passw)
        psw = md5.hexdigest()
        # hash_password = bcrypt.hashpw(passw, bcrypt.gensalt())
        # query = "SELECT * FROM admin WHERE username= %s and passwd=%s"
        # values = (username,psw)
        # mycursor = mydb.cursor()
        # mycursor.execute(query,values)
        # datas = mycursor.fetchone()
        # print(values)
        #print(bcrypt.hashpw(passw,salt))
        #print(hash_password)
    
        # if datas is not None and len(datas) > 0:
        #     session['id'] = datas[0]
        #     print("succes")
        #     return redirect(url_for('dsh'))
        # else :
        #     error ="Gagal Username dan Password salah !"
        #     return render_template('login.html',title='login', error=error)
    else :
        return render_template('login.html' , title='login' , error = error)


@app.route("/dsh" ,  methods=['GET' , 'POST'])
def dsh():    
    return render_template('dsh.html', title="dashbord")

@app.route("/pageDsh" ,  methods=['GET' , 'POST'])
def pageDsh():    
    return render_template('menu/dashbord.html')

@app.route("/pageTable" ,  methods=['GET' , 'POST'])
def pageTable():    
    return render_template('menu/table.html')

@app.route('/chart-data')
def chart_data():
    data = {
        '2024': [50, 60, 70, 65, 80, 75, 85, 90, 95, 100, 110, 120],
        '2025': [60, 65, 75, 70, 85, 80, 85, 90, 95, 100, 110, 120],
        '2026': [80, 70, 80, 75, 90, 85, 85, 90, 95, 100, 110, 120]
    }
    return jsonify(data)

@app.route('/data')
def data():
    data = [
        {"name": "Tiger Nixon", "position": "System Architect", "office": "Edinburgh", "age": 61, "start_date": "2011/04/25", "salary": "$320,800"},
        {"name": "Garrett Winters", "position": "Accountant", "office": "Tokyo", "age": 63, "start_date": "2011/07/25", "salary": "$170,750"}
    ]
    
    return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=255555, debug=True)