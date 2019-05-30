import re

TEXT_ELEMENTS = {"h1", "h2", "h3", "h4", "h5", "h6", "p", "blockquote"}
IMAGE_ELEMENTS = {"img"}
PAGE_ELEMENTS = TEXT_ELEMENTS | IMAGE_ELEMENTS

LINK_RE = re.compile(r"\[(.*)\]\((.*)\)")
STRONG_RE = re.compile(r"([*_]{2})([^\1]+?)\1")
EM_RE = re.compile(r"([*_])([^\1]+?)\1")

def build_page(path):
    """Build an HTML page using our glorious markup
    """

    with open(path, "r") as f:
        lines = [line[:-1] for line in f.readlines()]

    page = ""

    i = 0
    while i < len(lines):
        if lines[i] == "":
            i += 1
            continue

        if lines[i] in TEXT_ELEMENTS:
            start = i + 1
            end = find_end(start, lines)
            page += "<" + lines[i] + ">"
            page += build_text(lines[start:end])
            page += "</" + lines[i] + ">\n"
            i = end
        elif lines[i] in IMAGE_ELEMENTS:
            page += "<" + lines[i]
            page += ' src="' + lines[i+1] + '"'
            page += ' alt="' + lines[i+2] + '">\n'
            i += 3
        else:
            raise Exeption("Error building page")

    return page.strip()

def find_end(start, text):
    """Find end index of the current <tag>
    """
    while start < len(text)\
            and text[start] != ""\
            and (text[start] not in PAGE_ELEMENTS):
        start += 1
    return start

def build_text(lines):
    """Create some text
    Concatenates lines and adds links to text
    """
    text = " ".join(lines)

    # Create links
    match = LINK_RE.search(text)
    while match:
        text = text[:match.start()]\
                + '<a href="' + match.group(2) + '">' + match.group(1) + "</a>"\
                + text[match.end():]
        new_end = match.start() + len(match.group(1)) + len(match.group(2)) + 15
        match = LINK_RE.search(text, new_end)

    # Create strong text
    # NOTE: Has to be done before emphasis because it matches 2 * or _
    match = STRONG_RE.search(text)
    while match:
        text = text[:match.start()]\
                + "<strong>" + match.group(2) + "</strong>"\
                + text[match.end():]
        new_end = match.start() + len(match.group(2)) + 17
        match = STRONG_RE.search(text, new_end)

    # Create emphasized text
    match = EM_RE.search(text)
    while match:
        text = text[:match.start()]\
                + "<em>" + match.group(2) + "</em>"\
                + text[match.end():]
        new_end = match.start() + len(match.group(2)) + 9
        match = EM_RE.search(text, new_end)

    return text
