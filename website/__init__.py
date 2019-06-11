import markdown2

from flask import Flask, render_template

app = Flask(__name__, static_folder='static')

navigation = [
        ("Start", ""),
        ("Info", "posts"),
        ("Kontakt", "contact"),
        ("Om oss", "about_us")]

def paragraph(text):
    return dict(is_image=False,
            text=text)

def image(src, alt):
    return dict(is_image=True,
            src=src,
            alt=alt)

def post(src, alt, text):
    return dict(src=src, alt=alt, text=text)

def render_page(page, lang, theme, nav_index):
    actual_path = "website/pages/" + page + "_" + lang + ".md"
    return render_template("page.html",
            html=markdown2.markdown_path(actual_path),
            navigation=navigation,
            selected=nav_index,
            theme=theme)

@app.route("/<lang>/<theme>")
def index(lang, theme):
    print(lang, theme)
    assert(theme in ["light", "dark"])
    assert(lang in ["sv", "en"])
    return render_page("index", lang, theme, 1)

# @app.route("/contact/se")
# def contact_se():
#     return render_page("website/pages/contact_se.md", 3)
# 
# @app.route("/contact/en")
# def contact_en():
#     return render_page("website/pages/contact_en.md", 3)

