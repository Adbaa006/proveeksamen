from flask import Flask, render_template, url_for, request, redirect, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re


app = Flask(__name__)

app.secret_key = 'adcæøå'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'user-system'

mysql = MySQL(app)

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/kontakt")
def kontakt():
    return render_template('kontakt.html')

@app.route("/innlogging")
def innlogging():
    return render_template('innlogging.html')

@app.route("/produkter/<type>")
def produkter(type):
    return render_template('produkter.html', type=type)

@app.route("/kategori/<navn>")
def kategori(navn):
    return render_template('kategori.html', kategori=navn)

@app.route("/favoritter")
def favoritter():
    return render_template('favoritter.html')

@app.route("/handlekurv")
def handlekurv():
    return render_template('handlekurv.html')

@app.route("/footer")
def footer():
    return render_template('footer.html')

if __name__ == "__main__":
    app.run(debug=True)

