import streamlit as st
from nlp_toolkit import (
    preprocess_text,
    named_entity_recognition,
    sentiment_analysis,
    text_summarization,
    topic_modeling,
    language_detection,
    text_translation
)

st.title('Advanced NLP Toolkit')

# Input text
user_input = st.text_area('Enter Text')

if st.button('Process Text'):
    if user_input:
        st.subheader('Preprocessed Text')
        preprocessed_text = preprocess_text(user_input)
        st.write(preprocessed_text)

        st.subheader('Named Entity Recognition')
        entities = named_entity_recognition(user_input)
        st.write(entities)

        st.subheader('Sentiment Analysis')
        sentiment = sentiment_analysis(user_input)
        st.write(sentiment)

        st.subheader('Text Summarization')
        try:
            summary = text_summarization(user_input)
            st.write(summary)
        except Exception as e:
            st.write(f"Error in summarization: {e}")

        st.subheader('Topic Modeling')
        topics = topic_modeling([user_input])
        for idx, topic_terms in topics:
            st.write(f"Topic {idx + 1}: {', '.join(topic_terms)}")

        st.subheader('Language Detection')
        language = language_detection(user_input)
        st.write(language)

        st.subheader('Text Translation')
        target_language = st.selectbox('Select Target Language', ['fr', 'es', 'de', 'zh', 'ja'])
        translation = text_translation(user_input, target_language)
        st.write(translation)

    else:
        st.write('Please enter some text to process.')
