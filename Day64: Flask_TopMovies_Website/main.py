from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
import os

db = SQLAlchemy()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///my_top_movies.db"
app.config['SECRET_KEY'] = os.environ['API_SECRET']
db.init_app(app)
Bootstrap5(app)

headers = {
    "accept": "application/json",
    "Authorization": os.environ['API_TOKEN']
}

class Movies(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(250), nullable=True)
    img_url = db.Column(db.String(250), nullable=False)

class RateMovieForm(FlaskForm):
    rating = StringField(u'Rating', validators=[DataRequired()])
    review = StringField(u'Review', validators=[DataRequired()])
    submit = SubmitField('Done', validators=None)

class AddMovieForm(FlaskForm):
    title = StringField(u'Movie Title', validators=[DataRequired()])
    submit = SubmitField('Add Movie', validators=None)

@app.route("/")
def home():
    movie_list = db.session.execute(db.select(Movies).order_by(Movies.rating).limit(10)).scalars()
    starting_rank = 10
    for i in movie_list:
        i.ranking = starting_rank
        starting_rank -= 1
        db.session.commit()
    top_10_movies = db.session.execute(db.select(Movies).order_by(Movies.rating).limit(10)).scalars()
    return render_template("index.html", movies=top_10_movies)

@app.route("/edit", methods=["GET", "POST"])
def edit():
    form = RateMovieForm()
    movie_id = request.args.get('id')
    movie_select = db.get_or_404(Movies, movie_id)
    if form.validate_on_submit():
        movie_select.rating = request.form['rating']
        movie_select.review = request.form['review']
        db.session.add(movie_select)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit.html", movie=movie_select, form=form)


@app.route("/add", methods=["GET", "POST"])
def add_movie():
    form = AddMovieForm()
    if form.validate_on_submit():
        url = "https://api.themoviedb.org/3/search/movie"
        params = {
            "query": request.form['title']
        }
        response = requests.get(url, headers=headers, params=params)
        data = response.json()['results']
        return render_template("select.html", data=data)
    return render_template("add.html", form=form)


@app.route("/select", methods=["GET", "POST"])
def select():
    form = RateMovieForm()
    url = f"https://api.themoviedb.org/3/movie/{request.args.get('id')}"
    response = requests.get(url, headers=headers)
    data = response.json()
    print(data)
    entry = Movies(
        title=data['original_title'],
        year=data['release_date'][0:4],
        img_url="https://image.tmdb.org/t/p/w500" + data['poster_path'],
        description=data['overview']
    )
    if form.validate_on_submit():
        entry.rating = request.form['rating']
        entry.review = request.form['review']
        db.session.add(entry)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit.html", movie=entry, form=form)


@app.route("/delete")
def delete():
    movie_id = request.args.get('id')
    movie_to_delete = db.get_or_404(Movies, movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for("home"))


if __name__ == '__main__':
    app.run(debug=True)
