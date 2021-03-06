from sklearn_crfsuite import CRF
from seqeval.metrics import classification_report
from util import *


class CRFModel(object):
    def __init__(self,
                 algorithm='lbfgs',
                 c1=0.1,
                 c2=0.1,
                 max_iterations=100,
                 all_possible_transitions=False
                 ):

        self.model = CRF(algorithm=algorithm,
                         c1=c1,
                         c2=c2,
                         max_iterations=max_iterations,
                         all_possible_transitions=all_possible_transitions)

    def train(self, sentences, tag_lists):
        features = [sent2features(s) for s in sentences]
        self.model.fit(features, tag_lists)

    def test(self, testWordLists, testTagLists, wordDict, tagDict):
        features = [sent2features(s) for s in testWordLists]
        tagPres = self.model.predict(features)
        print(classification_report(testTagLists, tagPres, digits=6))

    def predict(self, sentences):
        features = [sent2features(sentences)]
        tagPres = self.model.predict(features)
        return tagPres


