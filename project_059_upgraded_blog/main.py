from flask import Flask, render_template
import requests

app = Flask(__name__)

blog_api_url = "https://api.npoint.io/f6d7e2050b0fdfb807d0"
all_posts = requests.get(blog_api_url).json()


@app.route('/')
@app.route('/index.html')
def index():
    return render_template("index.html", posts=all_posts)


@app.route('/about.html')
def about():
    return render_template("about.html")


@app.route('/contact.html')
def contact():
    return render_template("contact.html")

@app.route('/post/<id_post>')
def get_post(id_post):
    id_post = all_posts[int(id_post) - 1]
    return render_template("post.html", post=id_post)


if __name__ == "__main__":
    app.run(debug=True)
