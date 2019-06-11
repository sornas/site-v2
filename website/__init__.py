import markdown2

from flask import Flask, render_template, redirect

app = Flask(__name__, static_folder='static')

# Elements used to create Navigation bar
# (Name, Url, Multi-Language?)
navigation = [
        ("Start", "", True),
        ("Posts", "/posts", True),
        ("Contact", "/contact", True),
        ("About us", "/about_us", True),
        ("Our Github", "https://github.com/lithekod", False),
        ("By-laws", "https://github.com/lithekod/bylaws/blob/master/stadgar.pdf", False),
        ("Protocols", "https://github.com/lithekod/protocols", False)]

#def paragraph(text):
#    return dict(is_image=False,
#            text=text)
#
#def image(src, alt):
#    return dict(is_image=True,
#            src=src,
#            alt=alt)
#
#def post(src, alt, text):
#    return dict(src=src, alt=alt, text=text)

def render_page(path, nav_index, swedish):
    """Render a Markdown file into a page on the website

    Arguments:
    path ------- Path to a markdown file (or not.. idk)
    nav_index -- Index of page in navigation list
    swedish ---- Whether the page is in swedish or not (english)
    """
    return render_template("page.html",
            html=markdown2.markdown_path(path),
            navigation=navigation,
            selected=nav_index,
            page_url=navigation[nav_index][1],
            swedish=swedish)

@app.route("/")
def index():
    """ Redirect the index page to the swedish version of the index page """
    return redirect("/se", code=302)

@app.route("/se")
def index_se():
    """ Swedish Index page """
    return render_page("website/pages/index_se.md", 0, True)

@app.route("/en")
def index_en():
    """ English Index page """
    return render_page("website/pages/index_en.md", 0, True)

@app.route("/contact/se")
def contact_se():
    """ Swedish Contact page """
    return render_page("website/pages/contact_se.md", 2, True)

@app.route("/contact/en")
def contact_en():
    """ English Contact page """
    return render_page("website/pages/contact_en.md", 2, False)

