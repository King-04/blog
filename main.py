from flask import Flask, render_template, request
import requests

posts = requests.get("https://api.npoint.io/b94b5aa04ff6efaf2bd1").json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route('/about')
def get_about():
    return render_template("about.html")


@app.route('/post/<int:index>')
def get_posts(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


@app.route('/contact', methods=["GET", "POST"])
def get_contact():
    if request.method == "POST":
        data = request.form
        print(data["username"])
        print(data["email"])
        print(data["phone_no"])
        print(data["message"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


if __name__ == "__main__":
    app.run(debug=True)
