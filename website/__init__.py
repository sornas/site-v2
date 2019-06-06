import markdown2

from flask import Flask, render_template

app = Flask(__name__, static_folder='static')

navigation = [
        ("Start", ""),
        ("Posts", "posts"),
        ("Contact", "contact"),
        ("About us", "about_us")]

def paragraph(text):
    return dict(is_image=False,
            text=text)

def image(src, alt):
    return dict(is_image=True,
            src=src,
            alt=alt)

def post(src, alt, text):
    return dict(src=src, alt=alt, text=text)

def render_page(path, nav_index):
    return render_template("page.html",
            html=markdown2.markdown_path(path),
            navigation=navigation,
            selected=nav_index)

@app.route("/")
def index():
    return render_page("website/pages/index_se.md", 1)

# @app.route("/contact/se")
# def contact_se():
#     return render_page("website/pages/contact_se.md", 3)
# 
# @app.route("/contact/en")
# def contact_en():
#     return render_page("website/pages/contact_en.md", 3)

