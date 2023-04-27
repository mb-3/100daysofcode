from flask import Flask, render_template
import datetime
import requests

app = Flask(__name__)
date = datetime.datetime.now().strftime("%B %d, %Y")
blog_url = "https://api.npoint.io/5526d00c172f4c1e6d68"


@app.route('/')
def hello():
    blog_posts = requests.get(blog_url).json()
    return render_template("index.html", posts=blog_posts, date=date)


@app.route('/about.html')
def about_page():
    return render_template("about.html")


@app.route('/contact.html')
def contact_page():
    return render_template("contact.html")


@app.route("/post/<int:blog_id>")
def blog_post(blog_id):
    blog_posts = requests.get(blog_url).json()
    return render_template("post.html", posts=blog_posts, blog_id=blog_id, date=date, name="Matt Brescia")


if __name__ == '__main__':
    app.run(debug=True)
