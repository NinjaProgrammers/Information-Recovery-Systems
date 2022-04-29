

def readDocument(address):
    f = open(address, "r")
    content = f.read()
    f.close()
    return content

