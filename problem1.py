data = {}

# Initialize a variable to keep track of the current key
current_key = None

# Open the text file for reading (use the correct file path)
with open("./5.txt", encoding="utf-8") as f:
    for line in f:
        # Remove leading/trailing whitespaces
        line = line.strip()

        # Check if the line is not empty
        if line:
            # Check if the line ends with a colon to indicate a key
            if line.endswith(":"):
                # Extract the key (remove the colon)
                current_key = line[:-1]
                # Initialize an empty sub-dictionary for the current key
                data[current_key] = {}
            else:
                # Split the line into key and value based on the ":"
                parts = line.split(":")
                if len(parts) == 2:
                    key = parts[0].strip()
                    value = parts[1].strip()
                    # Add the key-value pair to the current sub-dictionary
                    if current_key:
                        data[current_key][key] = value
total_words_before = sum(len(word.split()) for word in data.keys())

# Find and remove entries where English translation ends with "All rights reserved"
words_to_remove = []
for word, translations in data.items():
    english_translation = translations.get('English', '')
    if english_translation.strip().endswith('"All rights reserved"'):
        words_to_remove.append(word)

# Remove entries from the dictionary
for word in words_to_remove:
    del data[word]

# Count words after removal
total_words_after = sum(len(word.split()) for word in data.keys())

# Dump the updated dictionary into the output.txt file
with open('./6.txt', 'w', encoding='utf-8') as output_file:
    for word, translations in data.items():
        output_file.write(f'{word}:\n')
        for language, translation in translations.items():
            output_file.write(f'    {language}: {translation}\n')

# Print the updated dictionary and word counts
print("Updated Dictionary and Word Counts dumped into G17modifieddata1.txt file.")
print("Total words before removal:", total_words_before)
print("Total words after removal:", total_words_after)