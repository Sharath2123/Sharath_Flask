from flask import Flask, render_template, jsonify

app = Flask(__name__)

Jobs = [
    {
        'id':'1',
        'title':'Data Analyst',
        'location':'Bangaluru,India',
        'salary':'Rs.10,00,000'
    },
    {
        'id':'2',
        'title':'ML Engineer',
        'location':'Delhi,India'
    },
    {
        'id':'3',
        'title':'Frontend Engineer',
        'location':'Remote',
        'salary':'Rs.6,00,000'
    },
    {
        'id':'4',
        'title':'Backend Engineer',
        'location':'San Francisco, USA',
        'salary':'$120,000'
    }
]

@app.route('/')
def hello():
    return render_template('home.html',jobs=Jobs)


@app.route('/jobs')
def list_jobs():
    return jsonify(Jobs)

if __name__=='__main__':
    app.run(host='0.0.0.0',debug=True)