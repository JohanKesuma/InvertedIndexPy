from model.document import Document


class Term(object):
    def __init__(self, term = "", document=Document()):
        self.document = document
        self.term = term

    def __str__(self):
        termStr = self.term.lower() + " --> " + self.document.docId

        return termStr
