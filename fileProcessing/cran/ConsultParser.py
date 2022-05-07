from basics.Consult import Consult


def ParseConsults(text):
    lines = text.split("\n")
    consultList = []

    p = 0
    while p < len(lines):
        consult, p = ParseConsult(lines, p)
        consultList.append(consult)

    return consultList

def ParseConsult(lines, p):
    id, p = ParseIndex(lines, p)
    content, p = ParseContent(lines, p)
    return Consult(id, content), p

def ParseIndex(lines, p):
    str, id = lines[p].split()
    return int(id), p + 1

def ParseContent(lines, p):
    p += 1
    content = ""
    while p < len(lines) and (len(lines[p]) < 2 or lines[p][:2] != ".I"):
        content += lines[p] + '\n'
        p += 1
    return content, p


