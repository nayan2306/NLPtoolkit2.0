# Advanced NLP Toolkit

This project is an advanced NLP (Natural Language Processing) toolkit built using Streamlit. It offers a wide range of NLP functionalities including text preprocessing, named entity recognition, sentiment analysis, text summarization, topic modeling, language detection, and text translation.

## Features

- **Text Preprocessing:** Tokenization and stopword removal.
- **Named Entity Recognition (NER):** Identifies entities in the text using SpaCy.
- **Sentiment Analysis:** Analyzes the sentiment of the text using Hugging Face transformers.
- **Text Summarization:** Summarizes the input text using Hugging Face transformers.
- **Topic Modeling:** Identifies topics within the text using LDA.
- **Language Detection:** Detects the language of the input text.
- **Text Translation:** Translates the input text into multiple languages using Google Translate.

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/nlp-toolkit.git
    cd nlp-toolkit
    ```

2. Create a virtual environment and activate it:

    ```sh
    python -m venv venv
    source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required packages:

    ```sh
    pip install -r requirements.txt
    ```

4. Download necessary NLTK data:

    ```sh
    python -c "import nltk; nltk.download('stopwords'); nltk.download('punkt')"
    ```

5. Download SpaCy model:

    ```sh
    python -m spacy download en_core_web_sm
    ```

## Usage

1. Run the Streamlit app:

    ```sh
    streamlit run app.py
    ```

2. Open your web browser and go to `http://localhost:8501`.

3. Enter text in the provided text area and click "Process Text" to see the results of various NLP operations.

## File Structure

- `app.py`: The Streamlit application.
- `nlp_toolkit.py`: Contains the core NLP functionalities.
- `requirements.txt`: Lists the required Python packages.
- `README.md`: Project documentation.

## Dependencies

- `streamlit`: For building the web application.
- `spacy`: For named entity recognition.
- `nltk`: For text preprocessing.
- `transformers`: For sentiment analysis and text summarization.
- `gensim`: For topic modeling.
- `langdetect`: For language detection.
- `googletrans`: For text translation.

## Examples

1. **Preprocessed Text:** Removes stopwords and tokenizes the input text.
2. **Named Entity Recognition:** Identifies entities such as people, organizations, and locations in the text.
3. **Sentiment Analysis:** Provides sentiment scores (positive/negative) for the text.
4. **Text Summarization:** Generates a concise summary of the text.
5. **Topic Modeling:** Extracts topics and associated keywords from the text.
6. **Language Detection:** Detects the language in which the text is written.
7. **Text Translation:** Translates the text into the selected target language.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
