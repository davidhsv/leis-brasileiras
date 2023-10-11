import markdownify

def striphtml(html):
    return markdownify.markdownify(html)