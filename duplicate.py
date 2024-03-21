input_file_path = './3.txt'
output_file_path = './4.txt'

# Use a dictionary to store word frequencies before removing duplicates
word_frequencies_before = {}

# Read words from input file and count frequencies
with open(input_file_path, 'r', encoding='utf-8') as input_file:
    for line in input_file:
        cleaned_word = line.strip()
        word_frequencies_before[cleaned_word] = word_frequencies_before.get(cleaned_word, 0) + 1

# Count the total number of words before removing duplicates
total_words_before = sum(word_frequencies_before.values())

# Use a set to store unique words
unique_words = set()

# Read words from input file and remove duplicates
with open(input_file_path, 'r', encoding='utf-8') as input_file:
    for line in input_file:
        cleaned_word = line.strip()
        unique_words.add(cleaned_word)

# Count the total number of unique words after removing duplicates
total_unique_words = len(unique_words)

# Write unique words back to the file
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    for word in sorted(unique_words):
        output_file.write(word + '\n')

# Print counts before and after removing duplicates
print(f"Total words before removing duplicates: {total_words_before}")
print(f"Total unique words after removing duplicates: {total_unique_words}")
print("Duplicates removed and unique words written to G17afterNoDuplicates.txt.")