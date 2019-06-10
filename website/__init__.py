import markdown2

from flask import Flask, render_template, redirect

app = Flask(__name__, static_folder='static')

navigation = [
        ("Start", ""),
        ("Posts", "/posts"),
        ("Contact", "/contact"),
        ("About us", "/about_us")]

def paragraph(text):
    return dict(is_image=False,
            text=text)

def image(src, alt):
    return dict(is_image=True,
            src=src,
            alt=alt)

def post(src, alt, text):
    return dict(src=src, alt=alt, text=text)

def render_page(path, nav_index, swedish):
    return render_template("page.html",
            html=markdown2.markdown_path(path),
            navigation=navigation,
            selected=nav_index,
            path=navigation[nav_index][1],
            swedish=swedish)

@app.route("/")
def index():
    return redirect("/se", code=302)

@app.route("/se")
def index_se():
    return render_page("website/pages/index_se.md", 0, True)

@app.route("/contact/se")
def contact_se():
    return render_page("website/pages/contact_se.md", 2, True)

@app.route("/contact/en")
def contact_en():
    return render_page("website/pages/contact_en.md", 2, False)

