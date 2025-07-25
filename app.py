from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

# Jobs = [
#     {
#         'id':'1',
#         'title':'Data Analyst',
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


@app.route('/')
def hello():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM JOBS")
    Jobs = cursor.fetchall()
    return render_template('home.html',jobs=Jobs)

@app.route('/about')
def call():
    return render_template('about.html')


if __name__=='__main__':
    app.run(host='0.0.0.0',debug=True)