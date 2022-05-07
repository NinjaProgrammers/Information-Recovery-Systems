from basics.Document import Document


def ParseDocuments(text):
    lines = text.split('\n')

    documentsList = []
    p = 0
    while p < len(lines):
        document, p = ParseDocument(lines, p)
        documentsList.append(document)

    return documentsList

def ParseDocument(lines, p):
    id, p = ParseIndex(lines, p)
    title, p = ParseTitle(lines, p)
    author, p = ParseAuthor(lines, p)
    bibliography, p = ParseBibliography(lines, p)
    content, p = ParseContent(lines, p)
    return Document(id, title, author, bibliography, content), p

def ParseIndex(lines, p):
    str, id = lines[p].split()
    return int(id), p + 1

def ParseTitle(lines, p):
    p += 1
    title = ""
    while p < len(lines) and lines[p] != '.A':
        title += lines[p] + '\n'
        p += 1
    return title, p

def ParseAuthor(lines, p):
    p += 1
    author = ""
    while p < len(lines) and lines[p] != '.B':
        author += lines[p] + '\n'
        p += 1
    return author, p

def ParseBibliography(lines, p):
    p += 1
    bibliography = ""
    while p < len(lines) and lines[p] != '.W':
        bibliography += lines[p] + '\n'
        p += 1
    return bibliography, p

def ParseContent(lines, p):
    p += 1
    content = ""
    while p < len(lines) and (len(lines[p]) < 2 or lines[p][:2] != '.I'):
        content += lines[p] + '\n'
        p += 1
    return content, p