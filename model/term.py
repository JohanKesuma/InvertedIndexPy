from model.document import Document
from model.posting import Posting
from model.posting import PostingList


class Term(object):
    def __init__(self, term = "", postingList = PostingList()):
        self.postingList = postingList # list of PostingList()
        self.term = term

    def __str__(self):
        termStr = self.term + " --> " + self.postingList.__str__()

        return termStr
