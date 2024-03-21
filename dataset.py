from googletrans import Translator
i=0
# Initialize translator
translator = Translator()

# Read input lines from the file
with open('./4.txt', 'r', encoding='utf-8') as file:
    input_lines = file.readlines()

# Open output file in append mode
with open('./5.txt', 'a', encoding='utf-8') as file:
    # Iterate through each line and translate
    for line in input_lines:
        # Translate text into English, Hindi, Tamil, and Kannada
        english_translation = translator.translate(line.strip(), src='te', dest='en').text
        hindi_translation = translator.translate(line.strip(), src='te', dest='hi').text
        tamil_translation = translator.translate(line.strip(), src='te', dest='ta').text
        kannada_translation = translator.translate(line.strip(), src='te', dest='kn').text

        # Append translations to output file
        file.write(f'{line.strip()}:\n')
        file.write(f'    English: "{line.strip()}" in English is "{english_translation}" \n')
        file.write(f'    Hindi: "{line.strip()}" in Hindi is "{hindi_translation}" \n')
        file.write(f'    Tamil: "In Tamil, "{line.strip()}" is "{tamil_translation}" \n')
        file.write(f'    Kannada: "In Kannada, "{line.strip()}" is "{kannada_translation}"\n\n')
        i=i+1
        print(i)

# Print success message
print('Translations appended to output.txt file.')
