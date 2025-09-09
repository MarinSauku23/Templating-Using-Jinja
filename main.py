from flask import Flask, render_template
import requests


app = Flask(__name__)


blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
blog_response = requests.get(url=blog_url)
blog_posts = blog_response.json()


@app.route('/')
def home():
    return render_template("index.html", posts=blog_posts)


@app.route("/post/<int:blog_id>")
def get_blog(blog_id):
    requested_blog = None
    for blog in blog_posts:
        if blog["id"] == blog_id:
            requested_blog = blog["id"]
    return render_template("post.html", posts=blog_posts, blog_id=requested_blog)


if __name__ == "__main__":
    app.run(debug=True)
