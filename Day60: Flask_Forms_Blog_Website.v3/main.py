from flask import Flask, render_template, request
import datetime
import requests
import smtplib
import os

app = Flask(__name__)
date = datetime.datetime.now().strftime("%B %d, %Y")
blog_url = "https://api.npoint.io/5526d00c172f4c1e6d68"
my_email = os.environ['my_email']
password = os.environ['password']


@app.route('/')
def hello():
    blog_posts = requests.get(blog_url).json()
    return render_template("index.html", posts=blog_posts, date=date)


@app.route('/about')
def about_page():
    return render_template("about.html")


@app.route('/contact', methods=["GET", "POST"])
def contact_page():
    if request.method == "POST":
        with smtplib.SMTP("smtp.gmail.com") as connection:
            name = request.form['name']
            email = request.form['email']
            phone = request.form['phone']
            message = request.form['message']
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=email,
                to_addrs=my_email,
                msg=f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
            )
        return f"<h1>Successfully sent your message!</h1>"
    return render_template("contact.html")


@app.route("/post/<int:blog_id>")
def blog_post(blog_id):
    blog_posts = requests.get(blog_url).json()
    return render_template("post.html", posts=blog_posts, blog_id=blog_id, date=date, name="Matt Brescia")


if __name__ == '__main__':
    app.run()
