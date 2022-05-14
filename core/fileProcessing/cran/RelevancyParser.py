
def ParseRelevancyList(text):
    relevancyList = []
    for line in text.split("\n"):
        consult, document, code = line.split()
        if len(relevancyList) < int(consult):
            relevancyList.append([])
        relevancyList[-1].append((int(consult), int(document), int(code)))
    return relevancyList
