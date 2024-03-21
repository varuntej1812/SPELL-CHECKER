# Sample list of Telugu words
telugu_words = ["పఅరిశ్రామ", "అఅచుకుని", "అఅర్థం", "అక్క", "ఇఅల్లు", "ఇల్లు"]

# List of Telugu vowels (achulu)
achulu = ["అ", "ఆ", "ఇ", "ఈ", "ఉ", "ఊ", "ఋ", "ౠ", "ఎ", "ఏ", "ఐ", "ఒ", "ఓ", "ఔ"]

# Function to check if a word has achulu from the second character to last character
def has_achulu(word):
    return any(char in achulu for char in word[1:])

# Find and print words with achulu from the second char to last char
matching_words = [word for word in telugu_words if has_achulu(word)]
print("Words with achulu from the second char to last char:", matching_words)