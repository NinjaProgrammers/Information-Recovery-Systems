from core.basics.Document import Document


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
    content, p = ParseContent(lines, p)
    return Document(id, content), p

def ParseIndex(lines, p):
    str, id = lines[p].split()
    return int(id), p + 1

def ParseContent(lines, p):
    p += 1
    content = ""
    while p < len(lines) and (len(lines[p]) < 2 or lines[p][:2] != '.I'):
        content += lines[p] + '\n'
        p += 1
    return content, p