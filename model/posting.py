class Posting:

    def __init__(self, document=None):
        if document == None:
            self.document = []
        else:
            self.document = document


class PostingList:
    def __init__(self):
        self.postingList = []
