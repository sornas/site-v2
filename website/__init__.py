"""
TODO: Better way of redirecting to other sites from a link.
"""

import markdown2

from flask import Flask, render_template, redirect

app = Flask(__name__, static_folder='static')

GITHUB_LINK = "https://github.com/lithekod"
BYLAWS_LINK = "https://github.com/lithekod/bylaws/blob/master/stadgar.pdf"
PROTOCOLS_LINK = "https://github.com/lithekod/protocols"

# Elements used to create Navigation bar
# ((Name_se, Name_en), Url, Internal?)
navigation = [
        (("Start", "Start"),            "/",              True),
        (("Inlägg", "Posts"),           "/posts/",        True),
        (("Kontakt", "Contact us"),     "/contact/",      True),
        (("AoC", "AoC"),                "/aoc/",          True),
        (("Tävlingar", "Competitions"), "/competitions/", True),
        (("Fusk", "Cheats"),            "/cheats/",       True),
        (("Vår Github", "Our Github"),  GITHUB_LINK,     False),
        (("Stadgar", "By-laws"),        BYLAWS_LINK,     False),
        (("Protokoll", "Protocols"),    PROTOCOLS_LINK,  False)]

def render_page(path, url, nav_index, swedish):
    """Render a Markdown file into a page on the website

    Arguments:
    path - Path to a markdown file.
    url - The url to the page.
    nav_index - Index of page in navigation list.
    swedish - Whether the page is in swedish or not (english).
    """
    return render_template("page.html",
            html=markdown2.markdown_path(path),
            url=url,
            navigation=navigation,
            selected=nav_index,
            swedish=swedish)


"""Redirects
The default page when accessing a link will be in swedish.
"""

@app.route("/")
def index_redir(): return redirect("/se/", code=302)

@app.route("/posts/")
def posts_redir(): return redirect("/posts/se/", code=302)

@app.route("/contact/")
def contact_redir(): return redirect("/contact/se/", code=302)

@app.route("/aoc/")
def aoc_redir(): return redirect("/aoc/se/", code=302)

@app.route("/competitions/")
def competitions_redir(): return redirect("/competitions/se/", code=302)

@app.route("/cheats/")
def cheats_redir(): return redirect("/cheats/se/", code=302)

@app.route("/ncpc/")
def ncpc_redir(): return redirect("/ncpc/se/", code=302)

@app.route("/impa/")
def impa_redir(): return redirect("/impa/se/", code=302)

# Temporary
@app.route("/opera/")
def opera_redir():
    return render_template("redirect.html", url="https://forms.gle/4dcwCGrvcWP7qo6R8")

"""Pages on sidebar
These pages are shown on and can be accessed from the sidebar.
The render_page is given an index to indicate which link
from the sidebar to highlight.
"""

@app.route("/se/")
def index_se():
    """ Swedish Index page """
    return render_page("website/pages/index_se.md", "/", 0, True)

@app.route("/en/")
def index_en():
    """ English Index page """
    return render_page("website/pages/index_en.md", "/", 0, False)

@app.route("/posts/se/")
def posts_se():
    """ Swedish Posts page """
    return render_page("website/pages/posts_se.md", "/posts/", 1, True)

@app.route("/posts/en/")
def posts_en():
    """ English Posts page """
    return render_page("website/pages/posts_en.md", "/posts/", 1, False)

@app.route("/contact/se/")
def contact_se():
    """ Swedish Contact page """
    return render_page("website/pages/contact_se.md", "/contact/", 2, True)

@app.route("/contact/en/")
def contact_en():
    """ English Contact page """
    return render_page("website/pages/contact_en.md", "/contact/", 2, False)

@app.route("/aoc/se/")
def aoc_se():
    """ Swedish Advent of Code page """
    return render_page("website/pages/aoc_se.md", "/aoc/", 3, True)

@app.route("/aoc/en/")
def aoc_en():
    """ English Advent of Code page """
    return render_page("website/pages/aoc_en.md", "/aoc/", 3, False)

@app.route("/competitions/se/")
def competitions_se():
    """ Swedish Competitons page """
    return render_page("website/pages/competitions_se.md", "/competitions/", 4, True)

@app.route("/competitions/en/")
def competitions_en():
    """ English Competitons page """
    return render_page("website/pages/competitions_en.md", "/competitions/", 4, False)

@app.route("/cheats/se/")
def cheats_se():
    """ Swedish Cheats page """
    return render_page("website/pages/cheats_se.md", "/cheats/", 5, True)

@app.route("/cheats/en/")
def cheats_en():
    """ English Cheats page """
    return render_page("website/pages/cheats_en.md", "/cheats/", 5, False)


"""Other pages
These pages can be accessed from a direct link. They do not show up
on the sidebar. render_page is therefore given the index -1 to highlight
which results in no page being highlighted.
"""

@app.route("/ncpc/se/")
def ncpc_se():
    """ Swedish NCPC page """
    return render_page("website/pages/ncpc_se.md", "/ncpc/", -1, True)

@app.route("/ncpc/en/")
def ncpc_en():
    """ English NCPC page """
    return render_page("website/pages/ncpc_en.md", "/ncpc/", -1, False)

@app.route("/impa/se/")
def impa_se():
    """ Swedish IMPA page """
    return render_page("website/pages/impa_se.md", "/impa/", -1, True)

@app.route("/impa/en/")
def impa_en():
    """ English IMPA page """
    return render_page("website/pages/impa_en.md", "/impa/", -1, False)


"""Errorhandlers
For now we only handle pages that are not found.
"""

@app.errorhandler(404)
def not_found(e):
    """ 404 Page """
    return render_page("website/pages/404.md", "/404/", -1, False), 404
