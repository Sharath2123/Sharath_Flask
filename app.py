from flask import Flask, render_template, request,redirect
from flask_bcrypt import Bcrypt
import mysql.connector

app = Flask(__name__)
app.secret_key = "Sharath@FLASK@2025"
bcrypt = Bcrypt(app)
# Jobs = [
#     {
#         'id':'1',
#         'title':'(Data) Analyst',
#         'location':'Bangaluru,India',
#         'salary':'Rs.10,00,000'
#     },
#     {
#         'id':'2',
#         'title':'ML Engineer',
#         'location':'Delhi,India'
#     },
#     {
#         'id':'3',
#         'title':'Frontend Engineer',
#         'location':'Remote',
#         'salary':'Rs.6,00,000'
#     },
#     {
#         'id':'4',
#         'title':'Backend Engineer',
#         'location':'San Francisco, USA',
#         'salary':'$120,000'
#     }
# ]

db = mysql.connector.connect(
    host="sql12.freesqldatabase.com",
    user="sql12791871",
    password="4VzUEm7rb8",
    database="sql12791871"
)


@app.route('/home')
def hello():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM JOBS")
    Jobs = cursor.fetchall()
    return render_template('home.html',jobs=Jobs)

@app.route('/about')
def call():
    return render_template('about.html')

@app.route('/', methods=['GET','POST'])
def reg():
    if request.method=="POST":
        email = request.form['email']
        password = bcrypt.generate_password_hash(request.form['password']).decode('utf-8')

        cursor = db.cursor()
        cursor.execute("INSERT INTO USER (email,password) values (%s,%s)",(email,password))
        db.commit()
        return redirect("/login")
    return render_template('register.html')

@app.route("/login",methods=["GET","POST"])
def logg():
    if request.method=="POST":
        email = request.form['email']
        password_input = request.form['password']

        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM USER WHERE email = %s",(email,))
        user = cursor.fetchone()

        if user and bcrypt.check_password_hash(user['password'],password_input):
            return redirect("/home")
        else:
            return "Invalid credentials"
    return render_template('login.html')
        
    



if __name__=='__main__':
    app.run(host='0.0.0.0',debug=True)