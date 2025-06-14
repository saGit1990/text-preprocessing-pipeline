import nltk
import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer, PorterStemmer

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('punkt_tab')

class DataCleaner:
  def __init__(self, text: str):
    self.name = "DataCleaner"
    self.text = text
    self.token = []

  def remove_punctuations(self) -> str:
    self.text = re.sub(r'[^a-zA-Z0-9\s]','', self.text.lower())
    return self.text

  def tokenizer(self, text: str) -> list[str]:
    self.token = nltk.word_tokenize(text)
    return self.token

  def remove_stopwords(self, tokens: list[str])-> list[str]:
    self.token=  [t for t in tokens if t not in stopwords.words()]
    return self.token

  def stemming(self, tokens: list[str]) -> list[str]:
    stemmer = PorterStemmer()
    self.token = [stemmer.stem(t) for t in tokens]
    return self.token

  def lemmatizer(self, tokens: list[str])-> list[str]:
    lemma = WordNetLemmatizer()
    self.token = [lemma.lemmatize(t) for t in tokens]
    return self.token

  def cleaned_text(self) -> str:
    self.text = self.remove_punctuations()
    self.token = self.tokenizer(self.text)
    self.token = self.remove_stopwords(self.token)
    self.token = self.stemming(self.token)
    self.token = self.lemmatizer(self.token)

    return " ".join(self.token)