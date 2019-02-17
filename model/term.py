from model.document import Document
from model.posting import Posting
from model.posting import PostingList


class Term(object):
    def __init__(self, term = "", postingList = PostingList()):
        self.postingList = postingList
        self.term = term

    def __str__(self):
        termStr = self.term + " --> " + self.postingList.__str__()

        return termStr

class TempTerm(object):
    def __init__(self, term = "", posting = Posting(Document())):
        self.posting = posting
        self.term = term

    def __str__(self):
        termStr = self.term.lower() + " --> " + self.posting.document.docId

        return termStr
