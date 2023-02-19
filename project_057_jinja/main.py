from flask import Flask, render_template
import requests

app = Flask(__name__)

blog_api_url = "https://api.npoint.io/e5257578a3cea8ca1fbf"
all_posts = requests.get(blog_api_url).json()


@app.route('/')
def home():
    return render_template("index.html", posts=all_posts)


@app.route('/post/<id_post>')
def get_post(id_post):
    id_post = all_posts[int(id_post) - 1]
    return render_template("post.html", post=id_post)


if __name__ == "__main__":
    app.run(debug=True)
