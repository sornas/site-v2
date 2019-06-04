from flask import Flask, render_template
from markdown2 import Markdown

app = Flask(__name__, static_folder='static')

navigation = [
        ("Start", "index"),
        ("Posts", "posts"),
        ("About us", "about_us")]

md_converter = Markdown()

def read_text(path):
    with open(path, "r") as f:
        return f.read()

def paragraph(text):
    return dict(is_image=False,
            text=text)

def image(src, alt):
    return dict(is_image=True,
            src=src,
            alt=alt)

def post(src, alt, text):
    return dict(src=src, alt=alt, text=text)

@app.route("/")
def index():
    return render_template("page.html",
            html=md_converter.convert(read_text("website/pages/index.md")),
            navigation=navigation,
            selected=1)

@app.route("/page")
def page():
    return render_template("page.html",
            html=md_converter.convert(read_text("website/pages/example.md")),
            navigation=navigation)

@app.route("/posts")
def posts():
    posts = [
            post(
                "http://images4.fanpop.com/image/photos/16100000/Cute-Kitten-kittens-16122946-1280-800.jpg",
                "A kitty! :D",
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."),
            post(
                "http://images4.fanpop.com/image/photos/16100000/Cute-Kitten-kittens-16122946-1280-800.jpg",
                "A kitty! :D",
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."),
            post(
                "http://images4.fanpop.com/image/photos/16100000/Cute-Kitten-kittens-16122946-1280-800.jpg",
                "A kitty! :D",
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")]
    return render_template('posts.html',
            title="Posts",
            posts=posts,
            navigation=navigation,
            selected=2)

@app.route("/index")
def start():
    all_content = [
            image("https://lokeshdhakar.com/projects/lightbox2/images/image-3.jpg", "A nice bridge"),
            paragraph("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")]
    return render_template('index.html',
            title="Hello World",
            all_content=all_content,
            navigation=navigation,
            selected=1)
