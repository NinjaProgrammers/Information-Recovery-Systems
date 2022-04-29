from fileProcessing.cran.Document import Document


def parseDocuments(text):
    lines = text.split('\n')

    documentsList = []
    p = 0
    while p < len(lines):
        document, p = parseDocument(lines, p)
        documentsList.append(document)

    return documentsList

def parseDocument(lines, p):
    id, p = parseIndex(lines, p)
    title, p = parseTitle(lines, p)
    author, p = parseAuthor(lines, p)
    bibliography, p = parseBibliography(lines, p)
    content, p = parseContent(lines, p)
    return Document(id, title, author, bibliography, content), p

def parseIndex(lines, p):
    str, id = lines[p].split()
    return id, p + 1

def parseTitle(lines, p):
    p += 1
    title = ""
    while p < len(lines) and lines[p] != '.A':
        title += lines[p] + '\n'
        p += 1
    return title, p

def parseAuthor(lines, p):
    p += 1
    author = ""
    while p < len(lines) and lines[p] != '.B':
        author += lines[p] + '\n'
        p += 1
    return author, p

def parseBibliography(lines, p):
    p += 1
    bibliography = ""
    while p < len(lines) and lines[p] != '.W':
        bibliography += lines[p] + '\n'
        p += 1
    return bibliography, p

def parseContent(lines, p):
    p += 1
    content = ""
    while p < len(lines) and (len(lines[p]) < 2 or lines[p][:2] != '.I'):
        content += lines[p] + '\n'
        p += 1
    return content, p