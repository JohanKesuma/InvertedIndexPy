from operator import attrgetter

from model.document import Document
from model.term import *
from model.posting import *
import copy


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
                posting = Posting(doc)
                term = TempTerm(t.lower(), posting)
                tempTerms.append(term)
        # end
        tempTerms.sort(key = attrgetter('term')) # sort tempTerm

        # menampilkan ordered tempTerm dengan dokumennya
        for x in tempTerms: 
            print(x)
        #end

        print()

        # membuat inverted index
        
        term1 = Term()
        for i in range(len(tempTerms)):

            term1.term = tempTerms[i].term
            
            if i > 0:
                if tempTerms[i].term == tempTerms[i - 1].term:
                    if tempTerms[i].posting.document.docId != tempTerms[i - 1].posting.document.docId:
                        posting = Posting(tempTerms[i].posting.document)
                        term1.postingList.postingList.append(posting)
                else:
                    posting = Posting(tempTerms[i].posting.document)
                    term1.postingList.postingList.append(posting)
            else:
                posting = Posting(tempTerms[i].posting.document)
                term1.postingList.postingList.append(posting)
            if i < (len(tempTerms) - 1):
                if tempTerms[i].term != tempTerms[i + 1].term:
                    iIndex.termList.append(copy.deepcopy(term1))
                    term1.postingList.postingList.clear()
            else:
                iIndex.termList.append(copy.deepcopy(term1))
        #end
        return iIndex

    def __str__(self):
        string = ''
        for x in self.termList:
            string += x.__str__()
            string += '\n'

        return string
