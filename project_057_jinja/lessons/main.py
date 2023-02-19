from flask import Flask, render_template
import random
import requests
import datetime
app = Flask(__name__)


@app.route('/')
def home():
    random_number = random.randint(1, 10)
    current_year = datetime.datetime.now().year
    return render_template(
        "index.html",
        num=random_number,
        year=current_year,
    )

@app.route('/guess/<username>')
def guess_name(username):
    user_age = requests.get(f"https://api.agify.io/?name={username}").json()
    user_gen = requests.get(f"https://api.genderize.io/?name={username}").json()
    return render_template(
        "guess.html",
        name=username,
        gender=user_gen["gender"],
        age=user_age["age"]
    )


@app.route('/blog')
def get_blog():
    blog_api_url = "https://api.npoint.io/e5257578a3cea8ca1fbf"
    all_posts = requests.get(blog_api_url).json()
    return render_template("blog.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)
