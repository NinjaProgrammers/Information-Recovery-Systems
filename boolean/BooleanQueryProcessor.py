from basics.BasicQueryProcessor import BasicQueryProcessor


class BooleanQueryProcessor(BasicQueryProcessor):
    def __init__(self, terms):
        super().__init__(terms)

    # TODO: Process the query so it gets the user input and returns the corresponding Dijuntive Normal Form
    def ProcessQuery(self, query):
        return query