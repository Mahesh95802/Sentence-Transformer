import nltk
from textblob import TextBlob
from styleformer import Styleformer

nltk.download('punkt')

def casualToFormal(text):
    CTF = Styleformer(style=0)
    blob = TextBlob(text)
    result = []
    for i in blob.sentences:
        temp_result = CTF.transfer(i.string)
        result.append(temp_result)
    return " ".join(result)