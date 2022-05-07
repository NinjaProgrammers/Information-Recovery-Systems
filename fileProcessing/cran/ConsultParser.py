from fileProcessing.cran.Consult import Consult


def parseConsults(text):
    lines = text.split("\n")
    consultList = []

    p = 0
    while p < len(lines):
        consult, p = parseConsult(text, p)
        consultList.append(consult)

    return consultList

def parseConsult(text, p):
    id, p = parseIndex(text, p)
    content, p = parseContent(text, p)
    return Consult(id, content), p

def parseIndex(text, p):
    str, id = text[p].split()
    return int(id), p + 1

def parseContent(text, p):
    content = ""
    while p < len(text) and (len(text[p]) < 2 or text[p][:2] != ".I"):
        content += text[p]
        p += 1
    return content, p


