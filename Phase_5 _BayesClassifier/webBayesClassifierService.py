import bayesClassifier
"""
Bayes Classifier WebService Connector script
Mainly, it has 2 functions
->receives as input a comment
->returns the label for the input
"""
def WebServiceBayes(comment):
    labelForInputComment = bayesClassifier.getLabel(comment)
    return labelForInputComment
