from model.document import Document
from model.term import Term
from operator import attrgetter


class InvertedIndex(object):

    def __init__(self):
        self.termList = []

    @staticmethod
    def toInvertedIndex(document):
        iIndex = InvertedIndex()
        
        # isi list term
        tempTerms = []
        for doc in document:
            docTerm = doc.content.split(" ")
            for t in docTerm:
                term = Term(t, doc)
                tempTerms.append(term)
                iIndex.termList.append(term)
        # end

        iIndex.termList.sort(key = attrgetter('term'))

        return iIndex
        

    def __str__(self):
        string = ''
        for x in self.termList:
            string += x.__str__()
            string += '\n'

        return string
