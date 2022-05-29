from core.basics.Document import Document


def ParseIMDB(text: str):
    return [Document(id + 1, content) for id, content in enumerate(text.split('\n'))]
