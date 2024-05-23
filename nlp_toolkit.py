import spacy
import nltk
from transformers import pipeline
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from gensim.summarization import summarize
from langdetect import detect
from googletrans import Translator

# Load SpaCy model for NER
nlp_spacy = spacy.load('en_core_web_sm')

# Load transformers pipeline for sentiment analysis
sentiment_pipeline = pipeline('sentiment-analysis')

# Load transformers pipeline for summarization
summarization_pipeline = pipeline('summarization')

# Load transformers pipeline for translation
translation_pipeline = pipeline('translation_en_to_fr')

# Download NLTK stopwords
nltk.download('stopwords')
nltk.download('punkt')
stop_words = set(stopwords.words('english'))

def preprocess_text(text):
    # Tokenization and stopword removal
    tokens = word_tokenize(text)
    filtered_tokens = [word for word in tokens if word.lower() not in stop_words]
    return ' '.join(filtered_tokens)

def named_entity_recognition(text):
    doc = nlp_spacy(text)
    entities = [(entity.text, entity.label_) for entity in doc.ents]
    return entities

def sentiment_analysis(text):
    return sentiment_pipeline(text)

def text_summarization(text):
    return summarization_pipeline(text)[0]['summary_text']

def topic_modeling(texts):
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.decomposition import LatentDirichletAllocation

    vectorizer = TfidfVectorizer(stop_words='english')
    X = vectorizer.fit_transform(texts)
    lda = LatentDirichletAllocation(n_components=5, random_state=0)
    lda.fit(X)

    topics = []
    for idx, topic in enumerate(lda.components_):
        topic_terms = [vectorizer.get_feature_names_out()[i] for i in topic.argsort()[:-11:-1]]
        topics.append((idx, topic_terms))
    return topics

def language_detection(text):
    return detect(text)

def text_translation(text, target_language='fr'):
    translator = Translator()
    translation = translator.translate(text, dest=target_language)
    return translation.text
