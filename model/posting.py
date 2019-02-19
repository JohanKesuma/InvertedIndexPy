from model.document import Document

class Posting:

    def __init__(self, term, document):
        self.document = document
        self.term = term

    def __str__(self):
        return self.term + ' -> ' + self.document.docId



class PostingList:
    def __init__(self):
        self.postingList = []

    def __str__(self):
        string = ''

        for doc in self.postingList:

            string += doc.document.docId + ", "

        return string
