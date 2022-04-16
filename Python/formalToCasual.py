import nltk
from textblob import TextBlob
from styleformer import Styleformer
nltk.download('punkt')

def formalToCasual(text):
    FTC = Styleformer(style=1)
    blob = TextBlob(text)
    result = []
    for i in blob.sentences:
        temp_result = FTC.transfer(i.string)
        result.append(temp_result)
    return " ".join(result)