import spacy

# Load the English language model
nlp = spacy.load('en_core_web_sm')

# Input and output file paths
input_file_path = './2.txt'
output_file_path = './3.txt'

# Read the input file
with open(input_file_path, 'r', encoding='utf-8') as file:
    text = file.read()

# Process the text using spaCy
doc = nlp(text)

# Lemmatize each token in the processed document
lemmatized_tokens = [token.lemma_ for token in doc]

# Join the lemmatized tokens to form a text
lemmatized_text = ' '.join(lemmatized_tokens)

# Write the lemmatized text to the output file
with open(output_file_path, 'a', encoding='utf-8') as file:
    file.write(lemmatized_text)

print(f'Lemmatization complete. Output saved to {output_file_path}')



