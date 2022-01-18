from flask import Flask, redirect, url_for, render_template, request,session, flash
from flask_mysqldb import MySQL
from datetime import timedelta
from bs4 import BeautifulSoup
import requests


app = Flask(__name__)
mysql= MySQL(app)
app.secret_key="scraping"

app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = ""
app.config['MYSQL_DB'] = "scraping"

@app.route("/")
def home():
    mycursor = mysql.connection.cursor()
    mycursor.execute("SELECT * FROM buku")
    myresult  = mycursor.fetchall()
    mycursor.close()
    return render_template("index.html", scrape = myresult )

@app.route("/admin", methods = ["POST", "GET"])
def scrap():
    if request.method == "POST":
        proses = request.form["pcr"]
        scraping(proses)
        flash("berhasil")
        return render_template("admin.html")
    else :
        flash("gagal")
        return render_template("admin.html")
        
@app.route("/buku")
def data():
    mycursor = mysql.connection.cursor()
    mycursor.execute("SELECT * FROM buku")
    myresult = mycursor.fetchall()
    mycursor.close()
    return render_template("buku.html",scrape = myresult)

@app.route("/login")
def login():
    return render_template("login.html")


def scraping(url):
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")
    
    judul = soup.find('h1', attrs={"itemprop":"name"}).get_text()

    deskripsi = soup.find('div', attrs={"itemprop":"description"}).get_text()

    pengarang = soup.find('div', class_='WRRASc').get_text()
    
    penerbit = soup.find('span', class_='htlgb').get_text()

    mycursor  = mysql.connection.cursor()
    sql = "INSERT INTO buku (judul,deskripsi,pengarang,penerbit) VALUES (%s,%s,%s,%s)"
    val = (judul,deskripsi,pengarang,penerbit)
    mycursor.execute(sql, val)
    mysql.connection.commit()
    mycursor.close()
    return "sukses"

if __name__ == "__main__":
    app.run(debug=True)