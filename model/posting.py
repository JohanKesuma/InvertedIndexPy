from model.document import Document

class Posting:

    def __init__(self, document):
        self.document = document


class PostingList:
    def __init__(self):
        self.postingList = []

    def __str__(self):
        string = ''

        for doc in self.postingList:

            string += doc.document.docId + ", "

        return string
