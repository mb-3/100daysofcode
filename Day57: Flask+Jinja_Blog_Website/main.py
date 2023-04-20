from flask import Flask, render_template
import requests
import datetime

year = datetime.datetime.now().year
blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
app = Flask(__name__)


@app.route('/')
def home():
    blog_posts = requests.get(blog_url).json()
    return render_template("index.html", posts=blog_posts, year=year, name="Matt Brescia")


@app.route("/post/<int:blog_id>")
def blog_post(blog_id):
    blog_posts = requests.get(blog_url).json()
    return render_template("post.html", posts=blog_posts, blog_id=blog_id, year=year, name="Matt Brescia")


if __name__ == "__main__":
    app.run()
