import spacy
# import nltk
# nltk.download('wordnet')
# from nltk.stem import WordNetLemmatizer
# lemmatizer = WordNetLemmatizer()
# words = ["Lookup for hospital", "Searching for hospital to transfer patient", "I want to search hospital data", "Hospital lookup for patient", "Looking up hospital details" ]
# ignore_words = ['?','!']
# words = [lemitizer.lemmatize(w.lower())for w in words if w not in ignore_words]
# print(words)

# Load the spaCy English model
# nlp = spacy.load('en_core_web_sm')
# words = [' '.join([token.lemma_ for token in nlp(w)]) for w in words]
# print(words)

# Load the spaCy English model
nlp = spacy.load('en_core_web_sm')
 
# Define a sample text
text = "The quick brown foxes are jumping over the lazy dogs."
 
# Process the text using spaCy
doc = nlp(text)
 
# Extract lemmatized tokens
lemmatized_tokens = [token.lemma_ for token in doc]
 
# Join the lemmatized tokens into a sentence
lemmatized_text = ' '.join(lemmatized_tokens)
 
# Print the original and lemmatized text
print("Original Text:", text)
print("Lemmatized Text:", lemmatized_text)