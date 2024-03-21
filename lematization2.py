import re

def custom_lemmatize(word):
    # Define a dictionary of custom lemmatization rules
    lemmatization_rules = {
           "పిల్లలను" : "పిల్ల",
            "కనక": "కనకం",
            "కనాలా": "కను",
            "ప్రణాళులు": "ప్రణామం",
            'తీసుకొనే': 'తీసుకో',
            'వస్తే': 'వచ్చు',
            'తీసుకోవాలా': 'తీసుకో',
            'వద్దా': 'వద్దు',
            'సింహాలు': 'సింహం',
            'అనేది': 'అను',
            "పుస్తకాలు": "పుస్తకం",
            "ప్రయాణాలు": "ప్రయాణం",
            'విద్యలు': 'విద్య',
            'పారిశ్రామికాలు': 'పారిశ్రామిక',
            'విద్యార్థులు': 'విద్యార్థి',
            "వ్యాఖ్యానాలు": "వ్యాఖ్యానం",
            'వాణిజ్యాలు': 'వాణిజ్యం',
            'బాలలు': 'బాల',
            'అమ్మలు': 'అమ్మ',
            'నిర్దిష్టమైన' : 'నిర్దిష్టం',
            'నిర్దుష్ట' : 'నిర్దుష్టం',
            'నిర్దేశించబడనప్పుడు' : 'నిర్దేశించు',
            'నిర్దేశించేది' : 'నిర్దేశించు',
            'నిర్దేశించేదీ' : 'నిర్దేశించు',
            'వాటాకి' : 'వాటా',
            'అభిప్రాయము':'అభిప్రాయం'
        }
    return lemmatization_rules.get(word, word)

def convert_plural_to_singular(word):
    # Define the regular expression pattern
    pattern = r'(.+?)(లు|ళ్ళు|ల|ళ్ళ|ళ్ళను|లనులు|ళ్ళనులు|లులు|ళ్ళులు)$'
    # Use regex substitution to convert plural to singular
    singular_word = re.sub(pattern, r'\1', word)
    return singular_word

# Read data from input file
with open('./1.txt', 'r', encoding='utf-8') as input_file:
    input_data = input_file.read()

# Tokenize the input data into words
words = input_data.split()

# Apply lemmatization and plural to singular conversion to each word
processed_words = []
for word in words:
    lemmatized_word = custom_lemmatize(word)
    singular_word = convert_plural_to_singular(lemmatized_word)
    processed_words.append(singular_word)

# Join the processed words with newline character between them
output_data = '\n'.join(processed_words)

# Write the processed data to output file
with open('./2.txt', 'w', encoding='utf-8') as output_file:
    output_file.write(output_data)

print("Lemmatization and Plural to Singular conversion completed. Check G17afterLemmatization1.txt for the result.")